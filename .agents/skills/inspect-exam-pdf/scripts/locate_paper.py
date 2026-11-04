#!/usr/bin/env python3
"""
CLI Tool: Locate Exam Question PDF Papers
Quickly finds official exam PDFs by course code, session, and exam type.
Reports file path, page count, file size, and text extractability.
"""

import os
import sys
import json
import argparse
import subprocess
import re

def find_index_file():
    candidates = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "resources", "question_index.json"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "resources", "question_index.json"),
        os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), ".agents", "skills", "resources", "question_index.json"),
        os.path.join(os.getcwd(), ".agents", "skills", "resources", "question_index.json")
    ]
    for c in candidates:
        norm = os.path.normpath(c)
        if os.path.exists(norm):
            return norm
    return None

def get_pdf_metadata(abs_path):
    info = {"exists": os.path.exists(abs_path), "size_kb": 0, "pages": 0}
    if not info["exists"]:
        return info
    try:
        info["size_kb"] = round(os.path.getsize(abs_path) / 1024, 1)
        res = subprocess.run(["pdfinfo", abs_path], capture_output=True, text=True, errors="ignore")
        for line in res.stdout.split("\n"):
            if line.startswith("Pages:"):
                info["pages"] = int(line.split(":")[1].strip())
    except Exception:
        pass
    return info

def session_matches(query_sess, target_sess):
    if not query_sess or not target_sess:
        return False
    if query_sess in target_sess or target_sess in query_sess:
        return True
    m_short = re.match(r'(\d{2})-(\d{2})', query_sess)
    if m_short:
        long_sess = f"20{m_short.group(1)}-20{m_short.group(2)}"
        if long_sess == target_sess:
            return True
    return False

def main():
    parser = argparse.ArgumentParser(description="Locate exam question PDF papers in the archive.")
    parser.add_argument("--course", "-c", required=True, help="Course code (e.g. CSE-3201) or name")
    parser.add_argument("--session", "-s", help="Session (e.g. 2020-2021, 2019-2020, 2018-2019)")
    parser.add_argument("--exam", "-e", help="Exam type (Final, Midterm, 1st Mid, 2nd Mid, Lab Final)")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")

    args = parser.parse_args()

    index_path = find_index_file()
    if not index_path:
        sys.stderr.write("Error: Could not locate question_index.json\n")
        sys.exit(1)

    with open(index_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_target = args.course.upper().replace("-", "").replace(" ", "").replace("_", "")
    matches = []

    for q in data["questions"]:
        c_code = q["course_code"].upper().replace("-", "").replace(" ", "").replace("_", "")
        c_name = q["course_name"].upper().replace(" ", "")
        if c_target not in c_code and c_target not in c_name:
            continue

        if args.session:
            if not session_matches(args.session, q["session"]):
                continue

        if args.exam:
            e_target = args.exam.lower()
            if e_target not in q["exam_type"].lower() and e_target not in q["category"].lower():
                continue

        pdf_info = get_pdf_metadata(q["abs_pdf_path"])
        matches.append({
            "course_code": q["course_code"],
            "course_name": q["course_name"],
            "session": q["session"],
            "exam_type": q["exam_type"],
            "teacher": q["teacher"],
            "exam_date": q["exam_date"],
            "canonical_name": q["canonical_name"],
            "rel_pdf_path": q["rel_pdf_path"],
            "abs_pdf_path": q["abs_pdf_path"],
            "file_size_kb": pdf_info["size_kb"],
            "page_count": pdf_info["pages"],
            "has_transcription": q["has_transcription"],
            "has_pdf_text": q["has_pdf_text"],
            "topics": q["topics"]
        })

    if args.json:
        print(json.dumps({"total_matches": len(matches), "matches": matches}, indent=2))
        return

    print("=" * 75)
    print(f"📄 Located Exam Papers for [{args.course}] (Found {len(matches)} papers)")
    print("=" * 75)

    if not matches:
        print("No papers matched the specified filters.")
        return

    for idx, m in enumerate(matches, 1):
        print(f"\n{idx}. [{m['course_code']}] {m['session']} {m['exam_type']}")
        print(f"   👤 Teacher: {m['teacher']} | Date: {m['exam_date']}")
        print(f"   📁 File: {m['rel_pdf_path']}")
        print(f"   📊 Pages: {m['page_count']} | Size: {m['file_size_kb']} KB | Text Extractable: {'Yes' if m['has_pdf_text'] else 'Scanned/Image'}")
        if m["topics"]:
            print(f"   🏷️  Topics: {', '.join(m['topics'][:4])}")

    print("\n" + "=" * 75)

if __name__ == "__main__":
    main()
