#!/usr/bin/env python3
"""
Repository Structurer & Cleaner for 6th Semester Questions
Cleans non-essential duplicate files (.webp, .html, redundant images, cookies)
and structures only essential files (.pdf, .md, assets, READMEs) for GitHub.
"""

import os
import shutil
import re
import json

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

# Course definition
COURSES = [
    {"code": "CSE-3201", "name": "Mathematical Analysis for Computer Science", "dir": "01_CSE-3201_Mathematical_Analysis_for_Computer_Science"},
    {"code": "CSE-3203", "name": "Theory of Computation", "dir": "02_CSE-3203_Theory_of_Computation"},
    {"code": "CSE-3205", "name": "Artificial Intelligence", "dir": "03_CSE-3205_Artificial_Intelligence"},
    {"code": "CSE-3206", "name": "Artificial Intelligence Lab", "dir": "04_CSE-3206_Artificial_Intelligence_Lab"},
    {"code": "CSE-3207", "name": "Peripherals and Interfacing", "dir": "05_CSE-3207_Peripherals_and_Interfacing"},
    {"code": "CSE-3208", "name": "Peripherals and Interfacing Lab", "dir": "06_CSE-3208_Peripherals_and_Interfacing_Lab"},
    {"code": "CSE-3209", "name": "Simulation and Modeling", "dir": "07_CSE-3209_Simulation_and_Modeling"},
    {"code": "CSE-3210", "name": "Simulation and Modeling Lab", "dir": "08_CSE-3210_Simulation_and_Modeling_Lab"},
    {"code": "CSE-3212", "name": "Mobile Application Development Lab", "dir": "09_CSE-3212_Mobile_Application_Development_Lab"},
]

def clean_teacher_name(raw_teacher):
    if not raw_teacher or raw_teacher.lower() in ["n/a", "none"]:
        return ""
    t = re.sub(r'Dr\.\s*', 'Dr_', raw_teacher)
    t = re.sub(r'Md\.\s*', 'Md_', t)
    t = re.sub(r'[^\w\s]', '', t)
    t = re.sub(r'\s+', '_', t.strip())
    t = re.sub(r'_+', '_', t)
    return t.strip('_')

def get_canonical_name(qid, title, teacher, course_code):
    # Special cases for collisions
    if qid == "261":
        return "2017-2018_1st_Mid_SetA"
    if qid == "262":
        return "2017-2018_1st_Mid_SetB"
    if qid == "815":
        return "Undated_Artificial_Intelligence_Q815"
    if qid == "763":
        return "Undated_Artificial_Intelligence_Q763"
        
    # Extract session: e.g. (21-22) -> 2021-2022
    sess_m = re.search(r'\((\d{2})-(\d{2})\)', title)
    if sess_m:
        session = f"20{sess_m.group(1)}-20{sess_m.group(2)}"
    else:
        session = "Undated"
        
    # Extract exam type
    clean_title = re.sub(r'\s*\(\d{2}-\d{2}\)', '', title).strip()
    clean_title = re.sub(r'\(.*?\)', '', clean_title).strip()
    clean_type = re.sub(r'[^\w\s]', '', clean_title)
    clean_type = re.sub(r'\s+', '_', clean_type)
    
    if not clean_type or clean_type.lower() == "none":
        clean_type = "Question"
        
    t_clean = clean_teacher_name(teacher)
    
    parts = [session, clean_type]
    if t_clean:
        parts.append(t_clean)
        
    return "_".join(parts)

def restructure():
    print("=" * 60)
    print("Restructuring Repository to Essential Files Only")
    print("=" * 60)
    
    with open(os.path.join(WORKSPACE, "metadata.json"), "r", encoding="utf-8") as f:
        meta_data = json.load(f)
        
    clean_metadata = []
    total_pdfs = 0
    total_mds = 0
    
    for course_info in meta_data:
        ccode = course_info["code"]
        cname = course_info["name"]
        cdir = os.path.join(WORKSPACE, course_info["dir"])
        print(f"\nProcessing [{ccode}] {cname}...")
        
        course_clean_questions = []
        
        for q in course_info["questions"]:
            qid = q["id"]
            title = q["title"]
            teacher = q["teacher"]
            category = q["category"]
            exam_date = q.get("exam_date", "")
            
            cat_dir = os.path.join(cdir, category)
            if not os.path.exists(cat_dir):
                continue
                
            canonical_base = get_canonical_name(qid, title, teacher, ccode)
            
            # Find all files belonging to this question in cat_dir
            q_files = [f for f in os.listdir(cat_dir) if f"_{qid}" in f or f"_{qid}." in f or f"_{qid}_" in f]
            
            # Identify PDF
            pdf_src = None
            # Priority: Direct PDF > Scan PDF > Question Paper PDF > any PDF
            for f in q_files:
                if f.endswith(".pdf") and "_Scan.pdf" not in f and "_Question_Paper.pdf" not in f:
                    pdf_src = f
                    break
            if not pdf_src:
                for f in q_files:
                    if f.endswith("_Scan.pdf"):
                        pdf_src = f
                        break
            if not pdf_src:
                for f in q_files:
                    if f.endswith(".pdf"):
                        pdf_src = f
                        break
                        
            # Identify Markdown
            md_src = None
            for f in q_files:
                if f.endswith(".md"):
                    md_src = f
                    break
                    
            final_files = []
            
            # 1. Handle PDF
            if pdf_src:
                src_path = os.path.join(cat_dir, pdf_src)
                dst_pdf_name = f"{canonical_base}.pdf"
                dst_path = os.path.join(cat_dir, dst_pdf_name)
                if src_path != dst_path:
                    shutil.move(src_path, dst_path)
                final_files.append(f"{category}/{dst_pdf_name}")
                total_pdfs += 1
                
            # 2. Handle Markdown
            if md_src:
                src_md_path = os.path.join(cat_dir, md_src)
                dst_md_name = f"{canonical_base}.md"
                dst_md_path = os.path.join(cat_dir, dst_md_name)
                if src_md_path != dst_md_path:
                    shutil.move(src_md_path, dst_md_path)
                final_files.append(f"{category}/{dst_md_name}")
                total_mds += 1
                
            # 3. Clean up non-essential files for this question (.webp, .html, .jpg, old duplicates)
            for f in os.listdir(cat_dir):
                if (f"_{qid}" in f or f"_{qid}." in f or f"_{qid}_" in f) and f not in [f"{canonical_base}.pdf", f"{canonical_base}.md"]:
                    try:
                        os.remove(os.path.join(cat_dir, f))
                    except Exception:
                        pass
                        
            print(f"  {qid} -> {canonical_base} | Files: {final_files}")
            
            # Parse academic session
            sess_m = re.search(r'\((\d{2})-(\d{2})\)', title)
            session_str = f"20{sess_m.group(1)}-20{sess_m.group(2)}" if sess_m else "Undated"
            clean_type_str = re.sub(r'\s*\(\d{2}-\d{2}\)', '', title).strip()
            
            course_clean_questions.append({
                "id": qid,
                "session": session_str,
                "exam_type": clean_type_str,
                "teacher": teacher or "N/A",
                "exam_date": exam_date or "N/A",
                "category": category,
                "canonical_name": canonical_base,
                "files": final_files
            })
            
        # Remove any lingering .webp or .html in cat_dirs
        for cat in os.listdir(cdir):
            cat_p = os.path.join(cdir, cat)
            if os.path.isdir(cat_p) and cat != "assets":
                for f in os.listdir(cat_p):
                    if f.endswith(".webp") or f.endswith(".html") or f.endswith(".jpg"):
                        try:
                            os.remove(os.path.join(cat_p, f))
                        except Exception:
                            pass
                            
        # Re-generate Course README
        generate_clean_course_readme(course_info, course_clean_questions)
        
        clean_metadata.append({
            "code": ccode,
            "name": cname,
            "credits": course_info["credits"],
            "dir": course_info["dir"],
            "questions": course_clean_questions
        })
        
    # Re-generate Master README
    generate_clean_master_readme(clean_metadata)
    
    # Save clean metadata.json
    with open(os.path.join(WORKSPACE, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(clean_metadata, f, indent=2)
        
    # Create .gitignore
    gitignore_path = os.path.join(WORKSPACE, ".gitignore")
    with open(gitignore_path, "w", encoding="utf-8") as f:
        f.write("""# Sensitive & Private
*cookie*
*session*
*.json
!metadata.json

# Operating System & Editors
.DS_Store
Thumbs.db
*.swp
*~
.idea/
.vscode/

# Python & Temporary
__pycache__/
*.pyc
*.tmp
*.log
""")

    # Move scripts to scripts/ folder
    scripts_dir = os.path.join(WORKSPACE, "scripts")
    os.makedirs(scripts_dir, exist_ok=True)
    for script_name in ["download_all_questions.py"]:
        src_script = os.path.join(WORKSPACE, script_name)
        if os.path.exists(src_script):
            shutil.move(src_script, os.path.join(scripts_dir, script_name))
            
    # Remove raw cookie from repo root if still present (it's backed up in Downloads/6th/)
    raw_cookie = os.path.join(WORKSPACE, "www.onebyzeroedu.com_json_1793625040572.json")
    if os.path.exists(raw_cookie):
        os.remove(raw_cookie)
        
    print("\n" + "=" * 60)
    print("RESTRUCTURING COMPLETE!")
    print(f"Total Essential PDFs: {total_pdfs}")
    print(f"Total Transcribed Markdown Papers: {total_mds}")
    print("=" * 60)

def generate_clean_course_readme(course, questions):
    course_dir = os.path.join(WORKSPACE, course["dir"])
    readme_path = os.path.join(course_dir, "README.md")
    
    total_q = len(questions)
    
    # Group by category
    by_category = {}
    for q in questions:
        by_category.setdefault(q["category"], []).append(q)
        
    md = f"""# {course['code']} - {course['name']}

> **Department of Computer Science and Engineering, University of Barishal**  
> **Level:** 6th Semester &bull; **Credits:** {course['credits']} &bull; **Total Exam Questions:** {total_q}

---

## 📑 Table of Contents
"""
    for cat in ["Final", "Midterm", "Lab_Exam", "Class_Test", "General"]:
        if cat in by_category:
            md += f"- [{cat.replace('_', ' ')} Questions (#{len(by_category[cat])})](#{cat.lower()}-questions)\n"
            
    md += "\n---\n\n"
    
    if total_q == 0:
        md += "*No exam questions are currently available for this laboratory course.*\n"
    else:
        for cat in ["Final", "Midterm", "Lab_Exam", "Class_Test", "General"]:
            if cat in by_category:
                cat_name = cat.replace('_', ' ')
                md += f"## {cat_name} Questions\n\n"
                md += "| Session | Exam | Course Teacher | Date | Formats |\n"
                md += "| :---: | :--- | :--- | :---: | :--- |\n"
                # Sort questions chronologically descending
                sorted_qs = sorted(by_category[cat], key=lambda x: x["session"], reverse=True)
                for q in sorted_qs:
                    format_links = []
                    for f in q["files"]:
                        fname = os.path.basename(f)
                        if fname.endswith(".pdf"):
                            format_links.append(f"📄 [PDF Document]({f})")
                        elif fname.endswith(".md"):
                            format_links.append(f"📝 [Markdown / Text]({f})")
                    formats_display = " &bull; ".join(format_links) if format_links else "N/A"
                    md += f"| **{q['session']}** | {q['exam_type']} | {q['teacher']} | {q['exam_date']} | {formats_display} |\n"
                md += "\n"
                
    md += """---
*Archive maintained for academic reference.*
"""
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(md)

def generate_clean_master_readme(all_courses):
    readme_path = os.path.join(WORKSPACE, "README.md")
    total_q = sum(len(c["questions"]) for c in all_courses)
    
    md = f"""# 📚 6th Semester CSE Questions Archive
### Department of Computer Science and Engineering &bull; University of Barishal

[![Semester](https://img.shields.io/badge/Semester-6th-blue.svg)](https://github.com)
[![Total Questions](https://img.shields.io/badge/Total_Questions-{total_q}-success.svg)](https://github.com)
[![Status](https://img.shields.io/badge/Format-PDF%20%7C%20Markdown-orange.svg)](https://github.com)
[![Source](https://img.shields.io/badge/Source-Onebyzero%20Edu-purple.svg)](https://www.onebyzeroedu.com/university/show_department/1/#sem6)

A curated, systematically organized repository of previous years' midterm, final, and laboratory exam questions for **6th Semester CSE students at the University of Barishal**.

Every question paper includes a high-definition **PDF document** for offline reading and printing. Transcribed papers also include native **Markdown (`.md`)** files with full questions, subquestions, marks, topic tags, and embedded diagrams.

---

## 🗂️ Courses Overview

| # | Code | Course Title | Credits | Questions | Available Sessions | Course Directory |
| :-: | :--- | :--- | :-: | :-: | :---: | :--- |
"""
    for idx, c in enumerate(all_courses, 1):
        q_count = len(c["questions"])
        sessions = sorted(list(set(q["session"] for q in c["questions"] if q["session"] != "Undated")))
        if sessions:
            sess_range = f"{sessions[0]} – {sessions[-1]}" if len(sessions) > 1 else sessions[0]
        else:
            sess_range = "N/A"
        md += f"| {idx} | **{c['code']}** | [{c['name']}]({c['dir']}/README.md) | {c['credits']} | **{q_count}** | {sess_range} | [`{c['dir']}/`]({c['dir']}/) |\n"

    md += f"""
---

## 📂 Repository Structure

The repository is structured strictly with **essential files only** (no redundant formats, no raw scrapers or session tokens):

```
Questions/
├── README.md                                             # 📖 Repository Overview & Index
├── metadata.json                                         # 📊 Machine-readable catalog
├── .gitignore                                            # 🛡️ Git hygiene rules
│
├── 01_CSE-3201_Mathematical_Analysis_for_Computer_Science/
│   ├── Final/
│   │   ├── 2021-2022_Final.pdf
│   │   ├── 2020-2021_Final_Ahsanul_Hauqe.pdf
│   │   ├── 2020-2021_Final_Ahsanul_Hauqe.md
│   │   └── ...
│   ├── Midterm/
│   │   ├── 2021-2022_1st_Mid_Ahsanul_haque.pdf
│   │   └── ...
│   └── README.md
│
├── 02_CSE-3203_Theory_of_Computation/
│   ├── Final/
│   ├── Midterm/
│   ├── assets/                                           # Diagrams, finite state automata, graphs
│   └── README.md
│
├── 03_CSE-3205_Artificial_Intelligence/
├── 04_CSE-3206_Artificial_Intelligence_Lab/
├── 05_CSE-3207_Peripherals_and_Interfacing/
├── 06_CSE-3208_Peripherals_and_Interfacing_Lab/
├── 07_CSE-3209_Simulation_and_Modeling/
├── 08_CSE-3210_Simulation_and_Modeling_Lab/
└── 09_CSE-3212_Mobile_Application_Development_Lab/
```

---

## 📄 File Formats

| Format | Purpose | Description |
| :---: | :--- | :--- |
| **`.pdf`** | **Primary Exam Document** | Original high-definition official PDF or vectorized printout of the question paper. Ready for download, printing, or in-browser reading on GitHub. |
| **`.md`** | **Searchable Transcription** | Clean Markdown containing full typed text of the questions, subquestions, marks distribution, and syllabus topic tags. |
| **`assets/`** | **Embedded Graphics** | High-resolution circuit diagrams, state transition charts, and figures linked locally inside the Markdown files. |

---

## 🚀 How to Use & Push to GitHub

### 1. Initialize and Push to GitHub:
```bash
git init
git add .
git commit -m "feat: Add comprehensive 6th Semester CSE exam questions archive"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/<REPO_NAME>.git
git push -u origin main
```

### 2. Searching Questions:
- You can search across all questions using GitHub's built-in repository search (e.g., search for `"Pumping Lemma"`, `"A* Algorithm"`, or `"8086"`).
- Markdown files render directly in the browser with full formatting and diagrams.

---

*Educational reference material. All original question papers belong to the University of Barishal.*
"""
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(md)

if __name__ == "__main__":
    restructure()
