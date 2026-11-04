# 6th Semester CSE Questions Archive - AI Agent Guidelines

This repository is a curated archive of previous years' midterm, final, and laboratory examination papers for **6th Semester Computer Science and Engineering at the University of Barishal**.

All exam question papers are preserved exclusively as official **PDF documents** (68 papers across 9 courses, covering academic sessions 2016-2017 through 2021-2022).

---

## 🛠️ Specialized Repository Skills

Three specialized skills are installed in `.agents/skills/` to empower AI agents with fast search, deep analysis, and visual question inspection:

### 1. `search-topics`
- **Location**: `.agents/skills/search-topics/`
- **Use Case**: Finding which exam papers or sessions covered a specific syllabus topic, algorithm, theorem, or keyword.
- **CLI Tool**:
  ```bash
  python3 .agents/skills/search-topics/scripts/search_topics.py "<QUERY>" [--course <CODE>] [--exam <TYPE>] [--session <YEAR>] [--json]
  ```
- **Example**:
  ```bash
  python3 .agents/skills/search-topics/scripts/search_topics.py "pumping lemma" --course CSE-3203
  ```

### 2. `analyze-questions`
- **Location**: `.agents/skills/analyze-questions/`
- **Use Case**: Analyzing question frequency, recurring topics, marks allocation, teacher preferences, and generating study roadmaps.
- **CLI Tool**:
  ```bash
  python3 .agents/skills/analyze-questions/scripts/analyze_questions.py --course <CODE> [--json]
  python3 .agents/skills/analyze-questions/scripts/analyze_questions.py --all
  ```
- **Example**:
  ```bash
  python3 .agents/skills/analyze-questions/scripts/analyze_questions.py --course CSE-3207
  ```

### 3. `inspect-exam-pdf`
- **Location**: `.agents/skills/inspect-exam-pdf/`
- **Use Case**: Resolving exact PDF file paths, page counts, file sizes, and inspecting questions/diagrams.
- **CLI Tool**:
  ```bash
  python3 .agents/skills/inspect-exam-pdf/scripts/locate_paper.py --course <CODE> [--session <YEAR>] [--exam <TYPE>] [--json]
  ```
- **Visual PDF Inspection**: Use the `read_file` tool to visually render and read scanned/printed PDF pages.

---

## 📚 Course Directory Mapping

| Course Code | Course Name | Credits | Directory |
| :--- | :--- | :---: | :--- |
| **CSE-3201** | Mathematical Analysis for Computer Science | 3.0 | [`01_CSE-3201_Mathematical_Analysis_for_Computer_Science/`](01_CSE-3201_Mathematical_Analysis_for_Computer_Science/) |
| **CSE-3203** | Theory of Computation | 3.0 | [`02_CSE-3203_Theory_of_Computation/`](02_CSE-3203_Theory_of_Computation/) |
| **CSE-3205** | Artificial Intelligence | 3.0 | [`03_CSE-3205_Artificial_Intelligence/`](03_CSE-3205_Artificial_Intelligence/) |
| **CSE-3206** | Artificial Intelligence Lab | 1.5 | [`04_CSE-3206_Artificial_Intelligence_Lab/`](04_CSE-3206_Artificial_Intelligence_Lab/) |
| **CSE-3207** | Peripherals and Interfacing | 3.0 | [`05_CSE-3207_Peripherals_and_Interfacing/`](05_CSE-3207_Peripherals_and_Interfacing/) |
| **CSE-3208** | Peripherals and Interfacing Lab | 1.5 | [`06_CSE-3208_Peripherals_and_Interfacing_Lab/`](06_CSE-3208_Peripherals_and_Interfacing_Lab/) |
| **CSE-3209** | Simulation and Modeling | 3.0 | [`07_CSE-3209_Simulation_and_Modeling/`](07_CSE-3209_Simulation_and_Modeling/) |
| **CSE-3210** | Simulation and Modeling Lab | 0.75 | [`08_CSE-3210_Simulation_and_Modeling_Lab/`](08_CSE-3210_Simulation_and_Modeling_Lab/) |
| **CSE-3212** | Mobile Application Development Lab | 1.5 | [`09_CSE-3212_Mobile_Application_Development_Lab/`](09_CSE-3212_Mobile_Application_Development_Lab/) |

---

## 💡 Best Practices for Agents

1. **Always cite exact PDF paths**: When referencing a question, provide a clickable link to its PDF document.
2. **Use visual inspection for complex questions**: Many papers contain circuit diagrams or state automata; use `read_file` on the PDF rather than guessing.
3. **Reference teacher styles**: Note who set the exam paper when explaining question patterns (e.g. Dr. Tania Islam, Dr. Rahat Hossain Faisal, Dr. Md Manjur Ahmed, Ahsanul Haque, Md. Erfan).

