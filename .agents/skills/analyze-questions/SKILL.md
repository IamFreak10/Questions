---
name: analyze-questions
description: >-
  Analyze exam question patterns, high-frequency recurring topics, marks
  distribution, syllabus coverage, and teacher-specific question styles across
  6th-semester CSE courses. Use when the user asks for exam preparation guidance,
  question trend analysis, repeated question detection, weightage analysis,
  or course revision cheat-sheets.
---

# Question Analysis Skill for 6th Semester CSE Exam Archive

Use this skill to conduct data-driven exam pattern analysis, topic frequency rankings, and targeted study roadmaps across previous exam years.

---

## 🛠️ When to Activate This Skill

Activate this skill when:
- The user asks: *"What are the most repeated questions in CSE-3203?"*
- The user asks: *"Give me a study plan / cheat-sheet to pass CSE-3207 final exam."*
- The user asks: *"What kind of questions does Dr. Rahat Hossain Faisal set in Simulation and Modeling?"*
- The user asks: *"Compare how questions changed from session 2016-2017 to 2021-2022."*
- The user wants marks breakdown or high-probability question predictions.

---

## 🚀 Execution Workflow

### Step 1: Run the Analysis CLI Script

The analysis script is located at:
`[analyze_questions.py](./scripts/analyze_questions.py)`

Execute using `run_command`:

```bash
# Analyze a specific course (e.g. CSE-3201, CSE-3203, CSE-3205, CSE-3207, CSE-3209)
python3 .agents/skills/analyze-questions/scripts/analyze_questions.py --course CSE-3207

# Output machine-readable JSON for automated processing
python3 .agents/skills/analyze-questions/scripts/analyze_questions.py --course CSE-3201 --json

# Overview of all 9 courses in the repository
python3 .agents/skills/analyze-questions/scripts/analyze_questions.py --all
```

### Step 2: Reference Exam Systems & Teacher Profiles

For marks distribution, exam rules ("Answer 5 out of 8"), and teacher question tendencies, consult:
`[exam_patterns.md](./references/exam_patterns.md)`

For a complete reference report format, see:
`[sample_analysis.md](./examples/sample_analysis.md)`

### Step 3: Deep Question Verification with PDF Inspector

If analyzing specific subquestion marks or verifying recurring diagrams:
- Use `python3 .agents/skills/inspect-exam-pdf/scripts/locate_paper.py --course <CODE> --session <SESSION>`
- Use `read_file` to visually verify the question paper pages.

### Step 4: Synthesize Analysis Report for the User

Structure the analysis report clearly:
1. **Executive Course Summary**: Code, Credits, Available Exam Papers, Main Course Teachers.
2. **Topic Frequency Ranking Table**:
   - Topic name, appearances across finals/midterms, frequency percentage.
3. **Teacher-Specific Style Highlights**:
   - Focus areas, mathematical vs conceptual emphasis, common question formats.
4. **Three-Tier Preparation Roadmap**:
   - **Tier 1 (Guaranteed / Must-Pass)**: Topics appearing in >=70% of exams.
   - **Tier 2 (High Probability)**: Topics appearing in 40–69% of exams.
   - **Tier 3 (Elective / Low Frequency)**: Topics appearing in <40% of exams.
5. **Exact PDF File Links**: Provide clickable links to the relevant question PDFs.

