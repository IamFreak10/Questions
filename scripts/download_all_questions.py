#!/usr/bin/env python3
"""
Onebyzero Edu 6th Semester Question Downloader & Structurer
Downloads all question papers, PDFs, scans, and typed questions with structured organization.
"""

import os
import sys
import json
import re
import io
import time
import urllib.request
import urllib.parse
from PIL import Image

BASE_URL = "https://www.onebyzeroedu.com"
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
COOKIE_FILE = os.path.join(WORKSPACE_DIR, "www.onebyzeroedu.com_json_1793625040572.json")

# 6th Semester Courses
COURSES = [
    {"id": 49, "code": "CSE-3201", "name": "Mathematical Analysis for Computer Science", "credits": 3.0, "dir": "01_CSE-3201_Mathematical_Analysis_for_Computer_Science"},
    {"id": 50, "code": "CSE-3203", "name": "Theory of Computation", "credits": 3.0, "dir": "02_CSE-3203_Theory_of_Computation"},
    {"id": 51, "code": "CSE-3205", "name": "Artificial Intelligence", "credits": 3.0, "dir": "03_CSE-3205_Artificial_Intelligence"},
    {"id": 52, "code": "CSE-3206", "name": "Artificial Intelligence Lab", "credits": 1.5, "dir": "04_CSE-3206_Artificial_Intelligence_Lab"},
    {"id": 53, "code": "CSE-3207", "name": "Peripherals and Interfacing", "credits": 3.0, "dir": "05_CSE-3207_Peripherals_and_Interfacing"},
    {"id": 54, "code": "CSE-3208", "name": "Peripherals and Interfacing Lab", "credits": 1.5, "dir": "06_CSE-3208_Peripherals_and_Interfacing_Lab"},
    {"id": 55, "code": "CSE-3209", "name": "Simulation and Modeling", "credits": 3.0, "dir": "07_CSE-3209_Simulation_and_Modeling"},
    {"id": 56, "code": "CSE-3210", "name": "Simulation and Modeling Lab", "credits": 0.75, "dir": "08_CSE-3210_Simulation_and_Modeling_Lab"},
    {"id": 57, "code": "CSE-3212", "name": "Mobile Application Development Lab", "credits": 1.5, "dir": "09_CSE-3212_Mobile_Application_Development_Lab"},
]

def load_cookies():
    cookie_str = ""
    if os.path.exists(COOKIE_FILE):
        with open(COOKIE_FILE, "r", encoding="utf-8") as f:
            cookies = json.load(f)
            pairs = [f"{c['name']}={c['value']}" for c in cookies if 'name' in c and 'value' in c]
            cookie_str = "; ".join(pairs)
    else:
        # Fallback to hardcoded known values
        cookie_str = "sessionid=szn9kyhp7rfcik752au4b33feg0gqpws; csrftoken=j91P6QeEKv3k8eS7mzJ4ZMCRHShkwb5B"
    return cookie_str

COOKIES = load_cookies()

def make_request(url, headers_extra=None, retries=3):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": COOKIES,
        "Accept": "*/*"
    }
    if headers_extra:
        headers.update(headers_extra)
    
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req, timeout=30)
            return resp
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2)
            else:
                raise e

def sanitize_filename(name):
    clean = re.sub(r'[\/\\:\*\?\"<>\|]', '_', name)
    clean = re.sub(r'\s+', '_', clean.strip())
    clean = re.sub(r'_+', '_', clean)
    return clean

def determine_category(title):
    t = title.lower()
    if "final" in t and "lab" not in t:
        return "Final"
    elif "mid" in t:
        return "Midterm"
    elif "lab" in t:
        return "Lab_Exam"
    elif "class test" in t or "ct" in t or "quiz" in t:
        return "Class_Test"
    else:
        return "General"

def parse_course_questions(course_id):
    url = f"{BASE_URL}/university/view_questions/{course_id}/"
    resp = make_request(url)
    html = resp.read().decode("utf-8", errors="replace")
    
    # Split by cards or search matches
    matches = list(re.finditer(r'href=[\"\']/university/resource/question/(\d+)/[\"\']', html))
    questions = []
    seen = set()
    
    for m in matches:
        qid = m.group(1)
        if qid in seen:
            continue
        seen.add(qid)
        
        start_pos = max(0, m.start() - 2500)
        card_text = html[start_pos:m.start() + 500]
        
        # Title
        h6_matches = list(re.finditer(r'<h6>(.*?)</h6>', card_text))
        title = h6_matches[-1].group(1).strip() if h6_matches else f"Question {qid}"
        
        # Teacher
        meta_matches = list(re.finditer(r'class=\"obz-question-meta\">(.*?)</p>', card_text, re.DOTALL))
        teacher = ' '.join(re.sub(r'<[^>]+>', ' ', meta_matches[-1].group(1)).split()) if meta_matches else ""
        
        # Date
        date_matches = list(re.finditer(r'class=\"obz-exam-date\".*?<span>(.*?)</span>', card_text, re.DOTALL))
        exam_date = date_matches[-1].group(1).strip() if date_matches else ""
        
        # Thumbnail
        thumb_matches = list(re.finditer(r'class=\"popup-thumbnail\"\s+src=[\"\']([^\"\']+)[\"\']', card_text))
        thumb_url = thumb_matches[-1].group(1) if thumb_matches else f"/media/university/resources/questions/thumbnails/{qid}_thumbnail.jpg"
        if not thumb_url.startswith("http"):
            thumb_url = f"{BASE_URL}{thumb_url}"
            
        questions.append({
            "id": qid,
            "title": title,
            "teacher": teacher,
            "exam_date": exam_date,
            "thumbnail_url": thumb_url
        })
        
    return questions

def extract_drive_preview_image(drive_id):
    preview_url = f"https://drive.google.com/file/d/{drive_id}/preview"
    try:
        req = urllib.request.Request(preview_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            html = resp.read().decode("utf-8", errors="replace")
            
        img_urls = re.findall(r'https://drive\.google\.com/drive-viewer/[^\s\"\'<>]+', html)
        if img_urls:
            best_url = list(set(img_urls))[0]
            best_url = best_url.replace(r'\u003d', '=').replace(r'\u0026', '&')
            # Increase quality from s1600 to s2400 or s0
            high_res_url = re.sub(r'=s\d+', '=s2400', best_url)
            
            img_req = urllib.request.Request(high_res_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(img_req, timeout=30) as img_resp:
                img_data = img_resp.read()
                return img_data
    except Exception as e:
        print(f"    [Drive Error {drive_id}]: {e}")
    return None

def parse_typed_questions(html, assets_dir, base_rel_assets):
    """
    Extracts structured question paper data from obz-question-paper-hero & container.
    """
    data = {
        "university": "University of Barishal",
        "department": "Department of Computer Science and Engineering",
        "exam_title": "",
        "course_title": "",
        "semester": "6th",
        "session": "",
        "time": "",
        "marks": "",
        "teacher": "",
        "instructions": "",
        "questions": []
    }
    
    # Extract metadata fields
    exam_m = re.search(r'class=\"[^\"]*obz-exam-title[^\"]*\">\s*(.*?)\s*</p>', html, re.DOTALL)
    if exam_m:
        data["exam_title"] = ' '.join(re.sub(r'<[^>]+>', ' ', exam_m.group(1)).split())
        
    course_m = re.search(r'class=\"[^\"]*obz-course-title-line[^\"]*\">\s*(.*?)\s*</p>', html, re.DOTALL)
    if course_m:
        data["course_title"] = ' '.join(re.sub(r'<[^>]+>', ' ', course_m.group(1)).split())
        
    session_m = re.search(r'Session:</strong>\s*(.*?)\s*</p>', html, re.DOTALL)
    if session_m:
        data["session"] = ' '.join(re.sub(r'<[^>]+>', ' ', session_m.group(1)).split())
        
    tm_m = re.search(r'class=\"[^\"]*obz-time-marks-line[^\"]*\">\s*(.*?)\s*</p>', html, re.DOTALL)
    if tm_m:
        tm_text = ' '.join(re.sub(r'<[^>]+>', ' ', tm_m.group(1)).split())
        data["time_marks"] = tm_text
        if "Time:" in tm_text:
            parts = tm_text.split("|")
            data["time"] = parts[0].replace("Time:", "").strip()
            if len(parts) > 1:
                data["marks"] = parts[1].replace("Marks:", "").strip()
                
    teacher_m = re.search(r'class=\"[^\"]*obz-teacher-line[^\"]*\">\s*(.*?)\s*</p>', html, re.DOTALL)
    if teacher_m:
        data["teacher"] = ' '.join(re.sub(r'<[^>]+>', ' ', teacher_m.group(1)).split()).replace("Course Teacher:", "").strip()
        
    instr_m = re.search(r'class=\"[^\"]*obz-additional-text-box[^\"]*\">\s*(.*?)\s*</div>', html, re.DOTALL)
    if instr_m:
        data["instructions"] = ' '.join(re.sub(r'<[^>]+>', ' ', instr_m.group(1)).split())

    # Extract creative questions (cq-card)
    cq_cards = html.split('obz-cq-card')
    for card_str in cq_cards[1:]:
        cq_data = {"number": "", "text": "", "subquestions": []}
        
        num_m = re.search(r'class=\"[^\"]*obz-cq-serial[^\"]*\">\s*(.*?)\s*</h5>', card_str, re.DOTALL)
        if num_m:
            cq_data["number"] = re.sub(r'<[^>]+>', '', num_m.group(1)).strip()
            
        cq_text_m = re.search(r'class=\"[^\"]*obz-cq-question-text[^\"]*\">\s*(.*?)\s*</p>', card_str, re.DOTALL)
        if cq_text_m:
            cq_data["text"] = ' '.join(re.sub(r'<[^>]+>', ' ', cq_text_m.group(1)).split()).strip()
            
        # Sub questions (obz-sq-card)
        sq_cards = card_str.split('obz-sq-card')
        for sq_str in sq_cards[1:]:
            sq_item = {"label": "", "text": "", "topics": [], "images": []}
            
            sq_text_m = re.search(r'class=\"[^\"]*obz-sq-text[^\"]*\">\s*(.*?)\s*</div>', sq_str, re.DOTALL)
            if sq_text_m:
                raw_sq = sq_text_m.group(1)
                label_m = re.search(r'<span><strong>(.*?)</strong></span>', raw_sq)
                if label_m:
                    sq_item["label"] = label_m.group(1).strip()
                # Clean text
                clean_sq = re.sub(r'<img[^>]+>', '', raw_sq)
                sq_item["text"] = ' '.join(re.sub(r'<[^>]+>', ' ', clean_sq).split())
                if sq_item["label"] and sq_item["text"].startswith(sq_item["label"]):
                    sq_item["text"] = sq_item["text"][len(sq_item["label"]):].strip()
                    
            # Check for embedded images in sq
            img_srcs = re.findall(r'<img\s+[^>]*src=[\"\']([^\"\']+)[\"\']', sq_str)
            for src in img_srcs:
                if "media/single_questions" in src or "media/" in src:
                    img_url = f"{BASE_URL}{src}" if not src.startswith("http") else src
                    img_filename = os.path.basename(src.split("?")[0])
                    local_img_path = os.path.join(assets_dir, img_filename)
                    rel_img_path = f"{base_rel_assets}/{img_filename}"
                    if not os.path.exists(local_img_path):
                        try:
                            iresp = make_request(img_url)
                            with open(local_img_path, "wb") as f_img:
                                f_img.write(iresp.read())
                        except Exception as e:
                            print(f"      [Failed to download image {src}]: {e}")
                    sq_item["images"].append(rel_img_path)
                    
            # Topics
            topic_m = re.findall(r'single_topic_wise_questions/\d+/[^>]*>(.*?)</a>', sq_str)
            sq_item["topics"] = [t.strip() for t in topic_m if t.strip()]
            
            cq_data["subquestions"].append(sq_item)
            
        data["questions"].append(cq_data)
        
    return data

def render_question_paper_html(data):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data.get('course_title', 'Course')} - {data.get('exam_title', 'Exam')}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #222;
            max-width: 850px;
            margin: 40px auto;
            padding: 30px;
            background: #fdfdfd;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border-radius: 8px;
        }}
        .header {{
            text-align: center;
            border-bottom: 2px solid #333;
            padding-bottom: 15px;
            margin-bottom: 20px;
        }}
        .header h2 {{ margin: 0 0 5px; font-size: 24px; color: #1a1a1a; }}
        .header h3 {{ margin: 0 0 8px; font-size: 18px; color: #333; }}
        .header h4 {{ margin: 0 0 10px; font-size: 16px; color: #4e38aa; }}
        .meta-table {{
            width: 100%;
            margin-top: 10px;
            font-size: 14px;
        }}
        .meta-table td {{ padding: 2px 8px; }}
        .instructions {{
            background: #f4f4f8;
            border-left: 4px solid #4e38aa;
            padding: 10px 15px;
            margin: 15px 0 25px;
            font-style: italic;
            font-size: 13.5px;
        }}
        .question-block {{
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 1px dashed #ccc;
        }}
        .q-number {{
            font-weight: bold;
            font-size: 16px;
            color: #2c3e50;
            margin-bottom: 8px;
        }}
        .sub-q {{
            display: flex;
            align-items: baseline;
            margin-bottom: 10px;
            padding-left: 15px;
        }}
        .sub-label {{
            font-weight: bold;
            min-width: 28px;
            color: #333;
        }}
        .sub-text {{
            flex: 1;
        }}
        .topics {{
            font-size: 11px;
            color: #666;
            margin-left: 10px;
            background: #eef2f7;
            padding: 2px 6px;
            border-radius: 4px;
        }}
        .q-img {{
            display: block;
            max-width: 90%;
            margin: 10px auto;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }}
        @media print {{
            body {{
                box-shadow: none;
                margin: 0;
                padding: 0;
                max-width: 100%;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h2>{data.get('university', 'University of Barishal')}</h2>
        <h3>{data.get('department', 'Department of Computer Science and Engineering')}</h3>
        <h4>{data.get('exam_title', 'Exam')} - Semester: {data.get('semester', '6th')}</h4>
        <table class="meta-table">
            <tr>
                <td style="text-align: left;"><strong>Course:</strong> {data.get('course_title', '')}</td>
                <td style="text-align: right;"><strong>Session:</strong> {data.get('session', '')}</td>
            </tr>
            <tr>
                <td style="text-align: left;"><strong>Time:</strong> {data.get('time', 'N/A')} | <strong>Marks:</strong> {data.get('marks', 'N/A')}</td>
                <td style="text-align: right;"><strong>Teacher:</strong> {data.get('teacher', 'N/A')}</td>
            </tr>
        </table>
    </div>
"""
    if data.get("instructions"):
        html += f'    <div class="instructions">{data["instructions"]}</div>\n'
        
    for q in data.get("questions", []):
        html += '    <div class="question-block">\n'
        if q.get("number"):
            html += f'        <div class="q-number">{q["number"]} {q.get("text", "")}</div>\n'
        for sq in q.get("subquestions", []):
            html += '        <div class="sub-q">\n'
            if sq.get("label"):
                html += f'            <div class="sub-label">{sq["label"]}</div>\n'
            html += f'            <div class="sub-text">{sq.get("text", "")}\n'
            if sq.get("topics"):
                topics_str = ", ".join(sq["topics"])
                html += f'                <span class="topics">Topics: {topics_str}</span>\n'
            for img_rel in sq.get("images", []):
                html += f'                <br><img class="q-img" src="{img_rel}" alt="Question Diagram">\n'
            html += '            </div>\n'
            html += '        </div>\n'
        html += '    </div>\n'
        
    html += """</body>
</html>
"""
    return html

def render_question_paper_md(data):
    md = f"""# {data.get('university', 'University of Barishal')}
### {data.get('department', 'Department of Computer Science and Engineering')}
**{data.get('exam_title', 'Exam')} | Semester: {data.get('semester', '6th')}**

- **Course:** {data.get('course_title', '')}
- **Session:** {data.get('session', '')}
- **Time:** {data.get('time', 'N/A')} | **Full Marks:** {data.get('marks', 'N/A')}
- **Course Teacher:** {data.get('teacher', 'N/A')}

---
"""
    if data.get("instructions"):
        md += f"> *{data['instructions']}*\n\n"
        
    for q in data.get("questions", []):
        if q.get("number"):
            md += f"### {q['number']} {q.get('text', '')}\n\n"
        for sq in q.get("subquestions", []):
            lbl = f"**{sq['label']}** " if sq.get("label") else "- "
            md += f"{lbl}{sq.get('text', '')}"
            if sq.get("topics"):
                md += f" *(Topics: {', '.join(sq['topics'])})*"
            md += "\n\n"
            for img_rel in sq.get("images", []):
                md += f"![Question Diagram]({img_rel})\n\n"
        md += "---\n\n"
        
    return md

def process_question(course, q_meta):
    qid = q_meta["id"]
    title = q_meta["title"]
    teacher = q_meta["teacher"]
    exam_date = q_meta["exam_date"]
    
    category = determine_category(title)
    course_dir = os.path.join(WORKSPACE_DIR, course["dir"])
    cat_dir = os.path.join(course_dir, category)
    assets_dir = os.path.join(course_dir, "assets")
    os.makedirs(cat_dir, exist_ok=True)
    os.makedirs(assets_dir, exist_ok=True)
    
    base_prefix = sanitize_filename(f"{title}_{teacher}_{qid}" if teacher else f"{title}_{qid}")
    
    print(f"  [{category}] QID {qid}: {title} (Teacher: {teacher or 'N/A'})")
    
    result = {
        "id": qid,
        "title": title,
        "teacher": teacher,
        "category": category,
        "exam_date": exam_date,
        "files": []
    }

    # Check if already downloaded
    if os.path.exists(cat_dir):
        existing = [f for f in os.listdir(cat_dir) if f.startswith(base_prefix)]
        if existing:
            result["files"] = [os.path.relpath(os.path.join(cat_dir, f), course_dir) for f in existing]
            print(f"    -> Already downloaded ({len(existing)} file(s)), skipping network.")
            return result
    
    q_url = f"{BASE_URL}/university/resource/question/{qid}/"
    
    try:
        resp = make_request(q_url)
        ct = resp.headers.get("Content-Type", "")
        cd = resp.headers.get("Content-Disposition", "")
        body = resp.read()
        
        # Case 1: Direct PDF
        if "application/pdf" in ct or (cd and ".pdf" in cd):
            pdf_path = os.path.join(cat_dir, f"{base_prefix}.pdf")
            with open(pdf_path, "wb") as f:
                f.write(body)
            result["files"].append(os.path.relpath(pdf_path, course_dir))
            print(f"    -> Downloaded direct PDF: {os.path.basename(pdf_path)}")
            return result
            
        # Case 2: Direct Image
        if "image/" in ct:
            ext = ".png" if "png" in ct else ".jpg"
            img_path = os.path.join(cat_dir, f"{base_prefix}{ext}")
            with open(img_path, "wb") as f:
                f.write(body)
            result["files"].append(os.path.relpath(img_path, course_dir))
            # Also generate a PDF version for convenience
            pdf_path = os.path.join(cat_dir, f"{base_prefix}.pdf")
            try:
                img = Image.open(io.BytesIO(body))
                img.convert("RGB").save(pdf_path, "PDF")
                result["files"].append(os.path.relpath(pdf_path, course_dir))
                print(f"    -> Downloaded direct image & generated PDF: {os.path.basename(pdf_path)}")
            except Exception:
                pass
            return result
            
        # Case 3: HTML content (Typed paper or Drive embedded)
        html = body.decode("utf-8", errors="replace")
        
        # Check for Google Drive links on page or via /iframe/
        drive_ids = re.findall(r'drive\.google\.com/file/d/([a-zA-Z0-9_-]+)', html)
        if not drive_ids:
            try:
                if_url = f"{q_url}iframe/"
                if_resp = make_request(if_url)
                if_html = if_resp.read().decode("utf-8", errors="replace")
                drive_ids = re.findall(r'drive\.google\.com/file/d/([a-zA-Z0-9_-]+)', if_html)
            except Exception:
                pass
                
        # If Drive link found, fetch high-res scan image
        drive_downloaded = False
        if drive_ids:
            drive_id = drive_ids[0]
            drive_img_data = extract_drive_preview_image(drive_id)
            if drive_img_data:
                scan_img_path = os.path.join(cat_dir, f"{base_prefix}_Scan.webp")
                scan_pdf_path = os.path.join(cat_dir, f"{base_prefix}_Scan.pdf")
                with open(scan_img_path, "wb") as f:
                    f.write(drive_img_data)
                result["files"].append(os.path.relpath(scan_img_path, course_dir))
                try:
                    img = Image.open(io.BytesIO(drive_img_data))
                    img.convert("RGB").save(scan_pdf_path, "PDF")
                    result["files"].append(os.path.relpath(scan_pdf_path, course_dir))
                    print(f"    -> Downloaded Drive Scan & generated PDF: {os.path.basename(scan_pdf_path)}")
                    drive_downloaded = True
                except Exception as e:
                    print(f"    -> Drive image saved: {os.path.basename(scan_img_path)}")
                    drive_downloaded = True
            else:
                result["drive_link"] = f"https://drive.google.com/file/d/{drive_id}/view"
                
        # Check if typed question paper exists
        if "obz-question-paper-hero" in html or "obz-cq-card" in html:
            base_rel_assets = "../assets"
            paper_data = parse_typed_questions(html, assets_dir, base_rel_assets)
            
            # Save HTML
            html_content = render_question_paper_html(paper_data)
            html_path = os.path.join(cat_dir, f"{base_prefix}_Question_Paper.html")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            result["files"].append(os.path.relpath(html_path, course_dir))
            
            # Save Markdown
            md_content = render_question_paper_md(paper_data)
            md_path = os.path.join(cat_dir, f"{base_prefix}_Question_Paper.md")
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md_content)
            result["files"].append(os.path.relpath(md_path, course_dir))
            print(f"    -> Generated Structured Question Paper: {os.path.basename(html_path)} & .md")
            
        # Fallback if no drive image was downloaded: download thumbnail
        if not drive_downloaded and not result["files"]:
            thumb_url = q_meta.get("thumbnail_url")
            if thumb_url:
                try:
                    t_resp = make_request(thumb_url)
                    t_data = t_resp.read()
                    t_path = os.path.join(cat_dir, f"{base_prefix}_Thumbnail.jpg")
                    with open(t_path, "wb") as f:
                        f.write(t_data)
                    result["files"].append(os.path.relpath(t_path, course_dir))
                    print(f"    -> Saved Thumbnail fallback: {os.path.basename(t_path)}")
                except Exception:
                    pass
                    
    except Exception as e:
        print(f"    [Error processing QID {qid}]: {e}")
        result["error"] = str(e)
        
    return result

def generate_course_readme(course, results):
    course_dir = os.path.join(WORKSPACE_DIR, course["dir"])
    os.makedirs(course_dir, exist_ok=True)
    readme_path = os.path.join(course_dir, "README.md")
    
    total_q = len(results)
    categories = {}
    for r in results:
        cat = r["category"]
        categories.setdefault(cat, []).append(r)
        
    md = f"""# {course['code']} - {course['name']}
**Semester:** 6th Semester  
**Credits:** {course['credits']}  
**Total Questions:** {total_q}

---

## Question Catalog

"""
    if total_q == 0:
        md += "*No exam questions currently uploaded for this course on Onebyzero Edu.*\n"
    else:
        for cat in ["Final", "Midterm", "Lab_Exam", "Class_Test", "General"]:
            if cat in categories:
                md += f"### {cat.replace('_', ' ')} Questions ({len(categories[cat])})\n\n"
                md += "| Title | Teacher | Exam Date | Available Files |\n"
                md += "| :--- | :--- | :--- | :--- |\n"
                for q in categories[cat]:
                    files_links = []
                    for fpath in q["files"]:
                        fname = os.path.basename(fpath)
                        ext = fname.split(".")[-1].upper()
                        if "_Question_Paper.html" in fname:
                            files_links.append(f"[{ext} Paper]({fpath})")
                        elif "_Scan.pdf" in fname:
                            files_links.append(f"[Scan PDF]({fpath})")
                        elif "_Scan." in fname:
                            files_links.append(f"[Scan Img]({fpath})")
                        else:
                            files_links.append(f"[{ext}]({fpath})")
                    if "drive_link" in q:
                        files_links.append(f"[Google Drive]({q['drive_link']})")
                    files_str = " &bull; ".join(files_links) if files_links else "No files"
                    md += f"| **{q['title']}** | {q['teacher'] or '-'} | {q['exam_date'] or '-'} | {files_str} |\n"
                md += "\n"
            
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(md)

def generate_master_readme(all_course_data):
    master_path = os.path.join(WORKSPACE_DIR, "README.md")
    total_questions = sum(len(c["questions"]) for c in all_course_data)
    
    md = f"""# 📚 6th Semester Questions Archive
Comprehensive repository of all previous years' exam questions for the 6th Semester, Department of Computer Science and Engineering, University of Barishal. Downloaded directly from [Onebyzero Edu](https://www.onebyzeroedu.com/university/show_department/1/#sem6).

**Total Courses:** {len(all_course_data)}  
**Total Exam Questions:** {total_questions}  
**Last Updated:** {time.strftime('%Y-%m-%d %H:%M:%S')}

---

## 🗂️ Courses Overview

| # | Course Code | Course Name | Credits | Questions Count | Directory |
| :-: | :--- | :--- | :-: | :-: | :--- |
"""
    for idx, c in enumerate(all_course_data, 1):
        q_count = len(c["questions"])
        md += f"| {idx} | **{c['code']}** | [{c['name']}]({c['dir']}/README.md) | {c['credits']} | {q_count} | [`{c['dir']}/`]({c['dir']}/) |\n"
        
    md += """
---

## 📁 Directory & Organization Structure
Each course is systematically arranged by exam type with all original scans, typed papers, and PDFs:

```
Questions/
├── 01_CSE-3201_Mathematical_Analysis_for_Computer_Science/
│   ├── Final/               # Semester final exam papers
│   ├── Midterm/             # 1st Mid & 2nd Mid exam papers
│   ├── assets/              # Diagram figures and question graphics
│   └── README.md            # Course-specific question catalog
├── 02_CSE-3203_Theory_of_Computation/
│   ├── Final/
│   ├── Midterm/
│   ├── assets/
│   └── README.md
├── 03_CSE-3205_Artificial_Intelligence/
├── 04_CSE-3206_Artificial_Intelligence_Lab/
├── 05_CSE-3207_Peripherals_and_Interfacing/
├── 06_CSE-3208_Peripherals_and_Interfacing_Lab/
├── 07_CSE-3209_Simulation_and_Modeling/
├── 08_CSE-3210_Simulation_and_Modeling_Lab/
├── 09_CSE-3212_Mobile_Application_Development_Lab/
├── README.md                # Master semester catalog
└── metadata.json            # Machine-readable archive metadata
```

## 📄 File Types Included
- **Original PDFs (`.pdf`)**: Official high-quality PDF files downloaded from the server.
- **Scans (`_Scan.pdf` / `_Scan.webp` / `.jpg`)**: High-resolution digitized question paper scans.
- **Interactive Question Papers (`_Question_Paper.html`)**: Beautiful, self-contained, offline-ready printable HTML question papers with embedded diagrams.
- **Markdown Question Papers (`_Question_Paper.md`)**: Fully transcribed questions with topics and formulas.
"""
    with open(master_path, "w", encoding="utf-8") as f:
        f.write(md)

def main():
    print("=" * 60)
    print("Onebyzero Edu 6th Semester Question Downloader & Structurer")
    print("=" * 60)
    
    all_course_data = []
    
    for c in COURSES:
        cid = c["id"]
        code = c["code"]
        name = c["name"]
        print(f"\nFetching questions for [{code}] {name} (ID {cid})...")
        
        q_list = parse_course_questions(cid)
        print(f"  Found {len(q_list)} question(s).")
        
        course_results = []
        for q_meta in q_list:
            res = process_question(c, q_meta)
            course_results.append(res)
            
        generate_course_readme(c, course_results)
        all_course_data.append({
            "id": cid,
            "code": code,
            "name": name,
            "credits": c["credits"],
            "dir": c["dir"],
            "questions": course_results
        })
        
    generate_master_readme(all_course_data)
    
    # Write metadata.json
    meta_path = os.path.join(WORKSPACE_DIR, "metadata.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(all_course_data, f, indent=2)
        
    print("\n" + "=" * 60)
    print(f"All downloads complete! Processed {sum(len(c['questions']) for c in all_course_data)} questions.")
    print(f"Master README: {os.path.join(WORKSPACE_DIR, 'README.md')}")
    print(f"Metadata file: {meta_path}")
    print("=" * 60)

if __name__ == "__main__":
    main()

