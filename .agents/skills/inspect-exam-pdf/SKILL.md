---
name: inspect-exam-pdf
description: >-
  Locate, inspect, and extract questions or pages from any PDF exam paper in the
  archive. Use when the user wants to read a specific question from a PDF,
  transcribe or verify question text, inspect circuit diagrams or state automata,
  or retrieve the exact file path for a particular course, session, or exam type.
---

# PDF Question Inspector Skill for 6th Semester CSE Archive

Use this skill to quickly locate official PDF exam papers, verify exact question wording, inspect diagrams and state automata visually, and extract question details.

---

## 🛠️ When to Activate This Skill

Activate this skill when:
- The user asks: *"Show me question 3 from CSE-3203 Final 2019-2020."*
- The user asks: *"Where is the PDF for Simulation and Modeling 2021-2022 Final?"*
- The user wants you to inspect a diagram, graph, or circuit in an exam paper.
- The user wants a transcription or verification of a specific exam question directly from the PDF.

---

## 🚀 Execution Workflow

### Step 1: Locate the PDF File

Use `[locate_paper.py](./scripts/locate_paper.py)` to resolve the course code, session, and exam type:

```bash
# Locate by course and session
python3 .agents/skills/inspect-exam-pdf/scripts/locate_paper.py --course CSE-3203 --session 2019-2020

# Locate by course, session, and specific exam
python3 .agents/skills/inspect-exam-pdf/scripts/locate_paper.py --course CSE-3205 --session 2021-2022 --exam Final

# Get JSON output with absolute paths and metadata
python3 .agents/skills/inspect-exam-pdf/scripts/locate_paper.py --course CSE-3207 --session 2020-2021 --json
```

Or consult the full catalog at `[pdf_catalog.md](./references/pdf_catalog.md)`.

---

### Step 2: Open and Read the PDF

Antigravity features native multimodal file inspection via `read_file`:

1. Call `read_file` with the path to the PDF:
   ```json
   {
     "Path": "/home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf"
   }
   ```
2. The `read_file` tool renders each page visually and applies OCR, allowing you to:
   - Read scanned handwriting, printed equations, and mathematical symbols.
   - Inspect diagrams, state transition charts, and circuit layouts.
   - Confirm marks allocation for subquestions (e.g. `[4]`, `[6]`, `[12]`).

---

### Step 3: Fast Text Extraction (When Available)

If the PDF contains digital text streams (as indicated by `Text Extractable: Yes` in `locate_paper.py`):
```bash
pdftotext "<PDF_PATH>" - | head -n 50
```

---

### Step 4: Present Question Details to the User

When quoting or answering questions from a paper:
1. Provide the exact question number and marks: e.g. **Question 2(a) [4 Marks]**.
2. Quote the full prompt accurately.
3. Describe any attached diagrams or state machines clearly.
4. Include a clickable markdown link to the source PDF file:
   `📄 [View Question Paper PDF](file:///home/iamfreak/Downloads/6th/Questions/...)`

