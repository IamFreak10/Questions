#!/usr/bin/env python3
"""
CLI Tool: Search Topics Across 6th Semester Exam Questions
Searches full question texts, syllabus topics, and metadata with rich filtering.
"""

import os
import sys
import json
import argparse
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

def extract_snippet(text, query, window=140):
    if not text:
        return ""
    m = re.search(r'\b' + re.escape(query) + r'\b', text, re.IGNORECASE)
    if not m:
        m = re.search(re.escape(query), text, re.IGNORECASE)
    if not m:
        return ""
    start = max(0, m.start() - window)
    end = min(len(text), m.end() + window)
    snippet = text[start:end].replace('\n', ' ').strip()
    prefix = "..." if start > 0 else ""
    suffix = "..." if end < len(text) else ""
    return f"{prefix}{snippet}{suffix}"

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

def search_questions(data, query=None, course=None, exam=None, session=None, teacher=None, topic=None):
    results = []
    q_lower = query.lower() if query else None

    for item in data["questions"]:
        # Filters
        if course:
            c_target = course.upper().replace(" ", "").replace("_", "").replace("-", "")
            c_code = item["course_code"].upper().replace(" ", "").replace("_", "").replace("-", "")
            c_name = item["course_name"].upper().replace(" ", "")
            if c_target not in c_code and c_target not in c_name:
                continue

        if exam:
            e_target = exam.lower()
            if e_target not in item["exam_type"].lower() and e_target not in item["category"].lower():
                continue

        if session:
            if not session_matches(session, item["session"]):
                continue

        if teacher:
            t_target = teacher.lower()
            if t_target not in item["teacher"].lower():
                continue

        if topic:
            top_target = topic.lower()
            matched_top = any(top_target in t.lower() for t in item["topics"])
            if not matched_top:
                continue

        # Match content
        matched = False
        match_types = []
        snippets = []

        if not q_lower:
            # If no query specified, filter match is enough
            matched = True
            match_types.append("filter_match")
        else:
            # Check topics
            for t in item["topics"]:
                if q_lower in t.lower():
                    matched = True
                    match_types.append(f"topic: {t}")

            # Check transcription text
            if item["transcription"] and q_lower in item["transcription"].lower():
                matched = True
                match_types.append("transcription")
                snippet = extract_snippet(item["transcription"], query)
                if snippet:
                    snippets.append(snippet)

            # Check extracted PDF text
            if item["pdf_text"] and q_lower in item["pdf_text"].lower():
                matched = True
                match_types.append("pdf_text")
                snippet = extract_snippet(item["pdf_text"], query)
                if snippet and snippet not in snippets:
                    snippets.append(snippet)

            # Check metadata titles/teacher
            meta_str = f"{item['course_code']} {item['course_name']} {item['teacher']} {item['canonical_name']}".lower()
            if q_lower in meta_str:
                matched = True
                match_types.append("metadata")

        if matched:
            results.append({
                "course_code": item["course_code"],
                "course_name": item["course_name"],
                "session": item["session"],
                "exam_type": item["exam_type"],
                "teacher": item["teacher"],
                "exam_date": item["exam_date"],
                "canonical_name": item["canonical_name"],
                "rel_pdf_path": item["rel_pdf_path"],
                "has_transcription": item["has_transcription"],
                "has_pdf_text": item["has_pdf_text"],
                "matched_in": list(set(match_types)),
                "topics": item["topics"],
                "snippets": snippets[:2]
            })

    return results

def main():
    parser = argparse.ArgumentParser(description="Search topics and exam questions across 6th Semester CSE courses.")
    parser.add_argument("query", nargs="?", default="", help="Keyword, concept, algorithm, or theorem to search")
    parser.add_argument("--course", "-c", help="Filter by course code (e.g. CSE-3201) or title")
    parser.add_argument("--exam", "-e", help="Filter by exam type (e.g. Final, Midterm, Lab Final)")
    parser.add_argument("--session", "-s", help="Filter by academic session (e.g. 2020-2021, 21-22)")
    parser.add_argument("--teacher", "-t", help="Filter by course teacher name")
    parser.add_argument("--topic", help="Filter by high-level syllabus topic category")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    parser.add_argument("--list-topics", action="store_true", help="List all indexed syllabus topics per course")

    args = parser.parse_args()

    index_path = find_index_file()
    if not index_path:
        sys.stderr.write("Error: Could not locate .agents/skills/resources/question_index.json\n")
        sys.exit(1)

    with open(index_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if args.list_topics:
        syllabus = data.get("syllabus", {})
        if args.json:
            print(json.dumps(syllabus, indent=2))
        else:
            print("=" * 70)
            print("📚 6th Semester CSE - Indexed Syllabus Modules & Topics")
            print("=" * 70)
            for ccode, modules in syllabus.items():
                print(f"\n[{ccode}]")
                for mod, keywords in modules.items():
                    print(f"  • {mod}: {', '.join(keywords[:6])}...")
        return

    if not args.query and not (args.course or args.exam or args.session or args.teacher or args.topic):
        parser.print_help()
        sys.exit(0)

    results = search_questions(
        data,
        query=args.query,
        course=args.course,
        exam=args.exam,
        session=args.session,
        teacher=args.teacher,
        topic=args.topic
    )

    if args.json:
        print(json.dumps({"query": args.query, "total_matches": len(results), "matches": results}, indent=2))
        return

    print("=" * 70)
    print(f"🔍 Search Results for: '{args.query}' (Found {len(results)} matches)")
    print("=" * 70)

    if not results:
        print("No matching exam questions found. Try broader keywords or use --list-topics to view indexed terms.")
        return

    for idx, r in enumerate(results, 1):
        print(f"\n{idx}. [{r['course_code']}] {r['exam_type']} ({r['session']}) - {r['course_name']}")
        print(f"   👤 Teacher: {r['teacher']} | Date: {r['exam_date']}")
        print(f"   📄 PDF: {r['rel_pdf_path']}")
        if r["matched_in"]:
            print(f"   🎯 Matched in: {', '.join(r['matched_in'])}")
        if r["topics"]:
            print(f"   🏷️  Topics: {', '.join(r['topics'])}")
        for snip in r["snippets"]:
            print(f"   💬 Excerpt: \"{snip}\"")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
