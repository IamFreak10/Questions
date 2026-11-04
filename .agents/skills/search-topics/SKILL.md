---
name: search-topics
description: >-
  Search previous years' exam questions across all 6th-semester CSE courses by
  topic, syllabus concept, theorem, algorithm, formula, or keyword. Use when the
  user wants to find which exam papers, sessions, or courses tested a specific
  subject, compare topic appearances over time, or search questions mentioning
  particular concepts.
---

# Topic Search Skill for 6th Semester CSE Exam Archive

Use this skill to query and cross-reference exam questions across all 9 courses and 68 exam papers in the archive.

---

## 🛠️ When to Activate This Skill

Activate this skill when:
- The user asks: *"Has Pumping Lemma ever appeared in the midterms?"*
- The user asks: *"Find all questions about 8255 PPI mode 1 or stepper motor interfacing."*
- The user asks: *"Where can I find questions on Markov Chains and Chapman-Kolmogorov equations?"*
- The user wants to search for specific theorems, formulas, or algorithms across courses.
- The user wants to know which course teacher set questions on a particular topic.

---

## 🚀 Execution Workflow

### Step 1: Run the Topic Search CLI Tool

The primary search script is located at:
`[search_topics.py](./scripts/search_topics.py)`

Execute searches directly via the `run_command` tool:

```bash
# Basic keyword search across all courses
python3 .agents/skills/search-topics/scripts/search_topics.py "<KEYWORD_OR_PHRASE>"

# Search with Course filter (e.g. CSE-3201, CSE-3203, CSE-3205, CSE-3207, CSE-3209)
python3 .agents/skills/search-topics/scripts/search_topics.py "<KEYWORD>" --course CSE-3203

# Search with Exam filter (Final, Midterm, 1st Mid, 2nd Mid, Lab Final)
python3 .agents/skills/search-topics/scripts/search_topics.py "<KEYWORD>" --exam Final

# Search with Session filter (e.g. 2020-2021, 2019-2020)
python3 .agents/skills/search-topics/scripts/search_topics.py "<KEYWORD>" --session 2020-2021

# Search with Course Teacher filter
python3 .agents/skills/search-topics/scripts/search_topics.py "<KEYWORD>" --teacher "Dr. Tania Islam"

# Get machine-readable JSON output for deep agent reasoning
python3 .agents/skills/search-topics/scripts/search_topics.py "<KEYWORD>" --json
```

### Step 2: Syllabus Topics Reference

If the user asks what topics are covered in a course or uses informal terms, consult:
`[syllabus_topics.md](./references/syllabus_topics.md)`

You can also list all indexed syllabus modules directly:
```bash
python3 .agents/skills/search-topics/scripts/search_topics.py --list-topics
```

### Step 3: Inspect Matched Papers (If Needed)

When a matched question requires verifying diagrams, formulas, or full question details:
1. Note the `rel_pdf_path` returned by `search_topics.py`.
2. Use the `read_file` tool to open the PDF directly:
   `read_file` renders pages visually, allowing you to read handwritten text, circuit diagrams, and state machines.

### Step 4: Present Structured Answers to the User

Structure your reply with:
1. **Direct Summary**: Answer how many times and in which exams the topic appeared.
2. **Tabular Results**:
   | Session | Exam Type | Course Code | Teacher | Question Excerpt / Context | PDF Document |
   | :---: | :--- | :--- | :--- | :--- | :--- |
3. **Observation & Advice**: Mention recurring patterns or variations across years.

