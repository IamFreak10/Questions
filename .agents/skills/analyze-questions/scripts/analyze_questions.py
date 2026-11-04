#!/usr/bin/env python3
"""
CLI Tool: Analyze Exam Questions, Frequency, and Patterns
Generates statistical breakdowns, topic frequency rankings, teacher profiles,
and exam preparation recommendations.
"""

import os
import sys
import json
import argparse
from collections import Counter, defaultdict

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

def analyze_course(course_code, data):
    norm_code = course_code.upper().replace("-", "").replace(" ", "").replace("_", "")
    course_questions = [
        q for q in data["questions"]
        if norm_code in q["course_code"].upper().replace("-", "").replace(" ", "").replace("_", "") or
           norm_code in q["course_name"].upper().replace(" ", "")
    ]

    if not course_questions:
        return None

    c_info = course_questions[0]
    total_q = len(course_questions)
    
    # Categorize by exam type
    exams_by_type = Counter(q["exam_type"] for q in course_questions)
    
    # Categorize by teacher
    teachers = Counter(q["teacher"] for q in course_questions)
    
    # Categorize by session
    sessions = sorted(list(set(q["session"] for q in course_questions if q["session"] != "Undated")))
    
    # Topic frequencies
    all_topics = []
    final_topics = []
    mid_topics = []
    
    teacher_topics = defaultdict(list)
    
    for q in course_questions:
        for t in q["topics"]:
            all_topics.append(t)
            if "Final" in q["exam_type"] or "Final" in q["category"]:
                final_topics.append(t)
            elif "Mid" in q["exam_type"] or "Mid" in q["category"]:
                mid_topics.append(t)
            teacher_topics[q["teacher"]].append(t)

    topic_counts = Counter(all_topics)
    final_topic_counts = Counter(final_topics)
    mid_topic_counts = Counter(mid_topics)
    
    # Recurring topic tiers
    total_finals = sum(1 for q in course_questions if "Final" in q["exam_type"] or "Final" in q["category"])
    
    tiers = {
        "Tier 1: Guaranteed / Must-Study (>=70% Final Frequency)": [],
        "Tier 2: High Yield (40% - 69% Final Frequency)": [],
        "Tier 3: Moderate / Elective (<40% Final Frequency)": []
    }
    
    for top, count in final_topic_counts.most_common():
        rate = (count / total_finals * 100) if total_finals > 0 else 0
        entry = {"topic": top, "finals_count": count, "total_finals": total_finals, "percentage": round(rate, 1)}
        if rate >= 70:
            tiers["Tier 1: Guaranteed / Must-Study (>=70% Final Frequency)"].append(entry)
        elif rate >= 40:
            tiers["Tier 2: High Yield (40% - 69% Final Frequency)"].append(entry)
        else:
            tiers["Tier 3: Moderate / Elective (<40% Final Frequency)"].append(entry)

    return {
        "course_code": c_info["course_code"],
        "course_name": c_info["course_name"],
        "credits": c_info["credits"],
        "total_papers": total_q,
        "available_sessions": sessions,
        "exam_type_breakdown": dict(exams_by_type),
        "teacher_breakdown": dict(teachers),
        "top_topics_overall": dict(topic_counts.most_common(8)),
        "top_topics_finals": dict(final_topic_counts.most_common(8)),
        "top_topics_midterms": dict(mid_topic_counts.most_common(8)),
        "study_priority_tiers": tiers,
        "questions_list": [
            {
                "session": q["session"],
                "exam_type": q["exam_type"],
                "teacher": q["teacher"],
                "rel_pdf_path": q["rel_pdf_path"],
                "topics": q["topics"]
            } for q in course_questions
        ]
    }

def print_course_report(analysis):
    print("=" * 75)
    print(f"📊 Exam Question Analysis: [{analysis['course_code']}] {analysis['course_name']}")
    print("=" * 75)
    print(f"• Credits: {analysis['credits']} | Total Exam Papers: {analysis['total_papers']}")
    print(f"• Sessions Covered: {analysis['available_sessions'][0]} – {analysis['available_sessions'][-1]}" if analysis['available_sessions'] else "• Sessions: N/A")
    
    print("\n📂 Exam Type Breakdown:")
    for etype, cnt in analysis["exam_type_breakdown"].items():
        print(f"   - {etype}: {cnt} papers")
        
    print("\n👨‍🏫 Course Teachers:")
    for teacher, cnt in analysis["teacher_breakdown"].items():
        print(f"   - {teacher}: {cnt} papers")
        
    print("\n🔥 Top Tested Topics in Final Exams:")
    if not analysis["top_topics_finals"]:
        print("   (No final exam data)")
    else:
        for top, cnt in analysis["top_topics_finals"].items():
            print(f"   - {top}: {cnt} appearances")

    print("\n🎯 Exam Preparation Revision Priority:")
    for tier_name, items in analysis["study_priority_tiers"].items():
        print(f"\n   [{tier_name}]")
        if not items:
            print("     None")
        for item in items:
            print(f"     ✓ {item['topic']} — {item['finals_count']}/{item['total_finals']} Finals ({item['percentage']}%)")

    print("\n" + "=" * 75)

def print_all_summary(data):
    print("=" * 75)
    print("📚 6th Semester CSE Exam Archive Overview")
    print("=" * 75)
    courses = defaultdict(list)
    for q in data["questions"]:
        courses[q["course_code"]].append(q)

    print(f"{'Code':<10} {'Course Name':<42} {'Papers':<8} {'Finals':<8} {'Mids':<6}")
    print("-" * 75)
    for ccode, qs in sorted(courses.items()):
        cname = qs[0]["course_name"][:40]
        finals = sum(1 for q in qs if "Final" in q["exam_type"] or "Final" in q["category"])
        mids = sum(1 for q in qs if "Mid" in q["exam_type"] or "Mid" in q["category"])
        print(f"{ccode:<10} {cname:<42} {len(qs):<8} {finals:<8} {mids:<6}")
    print("=" * 75)

def main():
    parser = argparse.ArgumentParser(description="Analyze exam questions and topic trends across 6th Semester CSE.")
    parser.add_argument("--course", "-c", help="Course code (e.g. CSE-3201, CSE-3203, CSE-3207) or title")
    parser.add_argument("--all", "-a", action="store_true", help="Print summary of all courses")
    parser.add_argument("--json", action="store_true", help="Output analysis in JSON format")

    args = parser.parse_args()

    index_path = find_index_file()
    if not index_path:
        sys.stderr.write("Error: Could not locate .agents/skills/resources/question_index.json\n")
        sys.exit(1)

    with open(index_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if args.all or not args.course:
        if args.json:
            all_res = {}
            for c in ["CSE-3201", "CSE-3203", "CSE-3205", "CSE-3206", "CSE-3207", "CSE-3208", "CSE-3209", "CSE-3210", "CSE-3212"]:
                res = analyze_course(c, data)
                if res:
                    all_res[c] = res
            print(json.dumps(all_res, indent=2))
        else:
            print_all_summary(data)
            print("\n💡 Run with --course <COURSE_CODE> (e.g. --course CSE-3203) for deep topic pattern analysis.")
        return

    res = analyze_course(args.course, data)
    if not res:
        print(f"Course '{args.course}' not found. Available: CSE-3201 to CSE-3212")
        return

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print_course_report(res)

if __name__ == "__main__":
    main()

