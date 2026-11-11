# CSE-3203: Theory of Computation — Mid-Term Preparation Guide (Session: 2022–2023)

> **Department of Computer Science and Engineering, University of Barishal**  
> **Course Code:** CSE-3203 &bull; **Course Title:** Theory of Computation &bull; **Credits:** 3.0  
> **Course Instructor / Examiner:** Dr. Md Manjur Ahmed, Associate Professor  
> **Target Exam:** 1st Mid-Term Examination (Session 2022–2023)  
> **Syllabus Reference:** *Introduction to Automata Theory, Languages, and Computation* (Hopcroft, Motwani, Ullman) — Chapters 1, 2, 3, and 4

---

## 📑 Syllabus Outline Covered (Chapters 1 – 4)

### Chapter 1: Automata: The Methods and the Madness
- **1.1 Why Study Automata Theory?** (Introduction to Finite Automata, Structural Representations, Automata and Complexity)
- **1.2 Introduction to Formal Proof** (Deductive Proofs, Reduction to Definitions, Theorems/Lemmas/Corollaries, "If-and-Only-If" Statements)
- **1.3 Additional Forms of Proof** (Equivalences About Sets, Contrapositive, Contradiction, Counterexamples)
- **1.4 Inductive Proofs** (Inductions on Integers, Structural Inductions, Mutual Inductions)
- **1.5 The Central Concepts of Automata Theory** (Alphabets, Strings, Languages, Problems)

### Chapter 2: Finite Automata
- **2.1 An Informal Picture of Finite Automata** (Ground Rules, Protocols, State Models)
- **2.2 Deterministic Finite Automata (DFA)** (Definition, Processing Strings, Transition Tables/Diagrams, Extended Transition Function $\hat{\delta}$, Language of DFA)
- **2.3 Nondeterministic Finite Automata (NFA)** (Definition, Extended Transition Function, Language of NFA, Equivalence to DFA / Subset Construction, Bad Case for Subset Construction & Pigeonhole Principle)
- **2.4 An Application: Text Search** (Finding Strings in Text, Keyword Recognizers / Aho-Corasick Automata)
- **2.5 Finite Automata With $\epsilon$-Transitions ($\epsilon$-NFA)** (Uses of $\epsilon$-Transitions, $\epsilon$-Closures, Extended Transitions, Eliminating $\epsilon$-Transitions to DFA)

### Chapter 3: Regular Expressions and Languages
- **3.1 Regular Expressions** (Operators: Union, Concatenation, Star; Building RE; Operator Precedence; Language of RE)
- **3.2 Finite Automata and Regular Expressions** (Equivalence of RE and FA, DFA to RE via State Elimination, RE to $\epsilon$-NFA via Thompson's Construction)
- **3.3 Applications of Regular Expressions** (Lexical Analysis, UNIX Pattern Matching)
- **3.4 Algebraic Laws for Regular Expressions** (Associativity, Commutativity, Identity, Distributivity, Redundant Expressions)

### Chapter 4: Properties of Regular Languages
- **4.1 Proving Languages Not to Be Regular** (The Pumping Lemma for Regular Languages, Applications of the Pumping Lemma, Non-Regularity Proofs by Contradiction, Exercises for Section 4.1)
- **4.2 Closure Properties of Regular Languages** (Closure Under Boolean Operations: Union, Complementation, Intersection, Difference, Addition of Finite Set of Strings; Reversal $L^R$; Homomorphisms $h(L)$; Inverse Homomorphisms $h^{-1}(L)$; Exercises for Section 4.2)
- **4.3 Decision Properties of Regular Languages** (Converting Among Representations & Complexity; Testing Emptiness via Graph Reachability; Testing Membership; Testing Finiteness; Exercises for Section 4.3)
- **4.4 Equivalence and Minimization of Automata** (Testing Equivalence of States; Table-Filling Algorithm / Moore's Algorithm; Testing Equivalence of Regular Languages & Symmetric Difference; Minimization of DFA to Quotient Automaton; Why the Minimized DFA Can't Be Beaten & Myhill-Nerode Index / Uniqueness; Exercises for Section 4.4)
- **4.5 Summary of Chapter 4**
- **4.6 Gradiance Problems for Chapter 4**
- **4.7 References for Chapter 4**

---

## 🎯 Topic-by-Topic Historical Questions & Marks Analysis

---

### CHAPTER 1: Methods, Proofs & Central Concepts

#### 1.1 Why Study Automata Theory & Applications
* **"What is Automata Theory? Describe the applications of Finite Automata."**
  * **Marks:** 6 Marks &mdash; [2019-2020 1st Mid: Q1](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2019-2020_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2016-2017 Final: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2016-2017_Final.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q1(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
* **"Describe the applications of Finite Automata."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"Describe the importance of Automata Theory."**
  * **Marks:** 4 Marks &mdash; [2020-2021 1st Mid: Q7](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2020-2021_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"Write any four application of NFA & DFA"**
  * **Marks:** 7 Marks &mdash; [2018-2019 1st Mid: Q1](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2018-2019_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)

#### 1.2 Formal Proof Forms (Theorems, Lemmas, Corollaries & Deductive Proofs)
* **"Analyze the terms: Theorems, Lemmas and Corollaries."**
  * **Marks:** 6 Marks &mdash; [2019-2020 1st Mid: Q3](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2019-2020_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2021-2022 Final: Q8(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=2)
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q1(d)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2016-2017 Final: Q1(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2016-2017_Final.pdf#page=1)
* **"Describe Deductive proof. Prove that, if $x$ is the sum of the squares of four positive integers, then $2^x \ge x^2$."**
  * **Marks:** 4 Marks &mdash; [2018-2019 Final: Q3(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
* **"Let $x$ be a real number. Then prove that, $\lfloor x \rfloor = \lceil x \rceil$ if and only if $x$ is an integer."**
  * **Marks:** 2 Marks &mdash; [2018-2019 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
* **"Prove the theorem '$a \bmod b = b \bmod a$, if and only if $a = b$'."**
  * **Marks:** 4 Marks (part of Q6 8 marks) &mdash; [2020-2021 1st Mid: Q6(i)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2020-2021_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)

#### 1.4 Inductive Proofs
* **"By method of induction, proof the theorem 'if $x \ge 4$ then $2^x \ge x^2$'."**
  * **Marks:** 4 Marks (part of Q6 8 marks) &mdash; [2020-2021 1st Mid: Q6(ii)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2020-2021_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"For all $n \ge 0$, prove that $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$."**
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q3(d)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)

#### 1.5 Central Concepts (Alphabets, Strings, Languages)
* **"Provide definitions and examples for the following terms: i) Alphabet, ii) String, and iii) language"**
  * **Marks:** 6 Marks ($2 + 2 + 2$) &mdash; [2020-2021 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 6 Marks &mdash; [2019-2020 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)

---

### CHAPTER 2: Finite Automata

#### 2.2 Deterministic Finite Automata (DFA)
* **"Construct a DFA for the following language: Let, $\Sigma = \{0, 1\}$, $L = \{w \mid w \text{ is a binary string that has even number of 1s and even number of 0s}\}$"**
  * **Marks:** 5 Marks &mdash; [2018-2019 1st Mid: Q2](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2018-2019_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 6 Marks &mdash; [2021-2022 Final: Q4(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2018-2019 Final: Q4(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
  * **Marks:** 6 Marks &mdash; [2017-2018 Final: Q5(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
  * **Marks:** 6 Marks &mdash; [2016-2017 Final: Q4(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2016-2017_Final.pdf#page=1)
* **"A DFA for $L = \{w \mid w \text{ is a binary string with even 1s and even 0s}\}$. Let the string 110101. Calculate the extension of transition to paths."**
  * **Marks:** ~5 Marks &mdash; [2017-2018 1st Mid: QC](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2017-2018_1st_Mid.pdf#page=1)
* **"Let, $\Sigma = \{0, 1\}$. Develop a DFA and make a transition table for the following language: $L = \{w \mid w \text{ is a bit string which contains the substring 11}\}$"**
  * **Marks:** ~5 Marks &mdash; [2017-2018 1st Mid: QB](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2017-2018_1st_Mid.pdf#page=1)
* **"Describe with examples: Advantages of DFA."**
  * **Marks:** 4 Marks &mdash; [2018-2019 Final: Q4(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
* **"State formal definition of a finite automata. Give an example."**
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q8(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"How a DFA processes strings?"**
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
* **"Compute the equivalent states in a DFA by using Table-filling algorithm for the following: [8-state DFA]"**
  * *(Detailed analysis, transition table, and complete step-by-step execution provided in [Chapter 4: Section 4.4.1](#441-testing-equivalence-of-states))* &mdash; [2021-2022 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)

#### 2.3 Nondeterministic Finite Automata (NFA)
* **"Construct an NFA for the following: Strings where the first symbol is present somewhere later on at least once."**
  * **Marks:** 4 Marks &mdash; [2020-2021 1st Mid: Q1](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2020-2021_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2019-2020 1st Mid: Q4](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2019-2020_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2018-2019 1st Mid: Q3](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2018-2019_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** ~5 Marks &mdash; [2017-2018 1st Mid: QE](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2017-2018_1st_Mid.pdf#page=1)
  * **Marks:** 6 Marks &mdash; [2021-2022 Final: Q4(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q4(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
  * **Marks:** 6 Marks &mdash; [2017-2018 Final: Q5(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
  * **Marks:** 6 Marks &mdash; [2016-2017 Final: Q4(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2016-2017_Final.pdf#page=1)
* **"Convert the following NFA to DFA [Standard 4-state NFA graph]"**
  * **Marks:** 10 Marks &mdash; [2021-2022 1st Mid: Q3](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2021-2022_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2020-2021 Final: Q3(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 6 Marks &mdash; [2019-2020 Final: Q3(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 6 Marks &mdash; [2017-2018 Final: Q3(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
* **"Build an NFA for $L = \{w \mid w \text{ ends in } 101 / 011 / 01\}$ and convert it to DFA."**
  * **Marks:** 10 Marks (NFA) + 5 Marks (DFA) = 15 Marks &mdash; [2019-2020 1st Mid: Q5, Q6](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2019-2020_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks (NFA) + 5 Marks (DFA) = 9 Marks &mdash; [2021-2022 Final: Q5(c, d)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks (NFA) + 5 Marks (DFA) = 9 Marks &mdash; [2018-2019 Final: Q5(a, c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
  * **Marks:** 4 Marks (NFA) + 5 Marks (DFA) = 9 Marks &mdash; [2016-2017 Final: Q5(a, c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2016-2017_Final.pdf#page=1)
* **"Describe the Advantages & Limitations / Caveats for NFA."**
  * **Marks:** 3 Marks &mdash; [2021-2022 Final: Q5(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q5(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2016-2017 Final: Q5(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2016-2017_Final.pdf#page=1)
* **"Describe the 'bad case' where $states(DFA) \gg states(NFA)$. Analyze it with the Pigeon hole principle."**
  * **Marks:** 8 Marks &mdash; [2020-2021 1st Mid: Q2(i, ii)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2020-2021_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 7 Marks &mdash; [2018-2019 1st Mid: Q4](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2018-2019_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2021-2022 Final: Q7(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=2)
  * **Marks:** 6 Marks &mdash; [2018-2019 Final: Q8(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)

#### 2.4 Text Search & Keyword Recognizer
* **"For the keyword recognizer occurrences of the words 'include', Make a transition diagram."**
  * **Marks:** ~5 Marks &mdash; [2017-2018 1st Mid: QD](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2017-2018_1st_Mid.pdf#page=1)

#### 2.5 Finite Automata With $\epsilon$-Transitions ($\epsilon$-NFA)
* **"Why explicit $\epsilon$-transitions in finite automata is important? / Describe the necessities / uses of $\epsilon$-transitions."**
  * **Marks:** 10 Marks &mdash; [2021-2022 1st Mid: Q5](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2021-2022_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 2 Marks &mdash; [2021-2022 Final: Q6(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=2)
  * **Marks:** 2 Marks (Q6a) & 2 Marks (Q8c) &mdash; [2018-2019 Final: Q6(a), Q8(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
  * **Marks:** 2 Marks &mdash; [2017-2018 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
  * **Marks:** 2 Marks &mdash; [2016-2017 Final: Q6(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2016-2017_Final.pdf#page=1)
* **"Build an $\epsilon$-NFA for $L = \{w \mid w \text{ is empty, or if non-empty will end in } 01\}$ and convert it to DFA."**
  * **Marks:** 10 Marks ($\epsilon$-NFA) &mdash; [2021-2022 1st Mid: Q6](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2021-2022_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks ($\epsilon$-NFA) &mdash; [2020-2021 1st Mid: Q3](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2020-2021_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks ($\epsilon$-NFA) + 6 Marks (DFA) = 10 Marks &mdash; [2021-2022 Final: Q6(b, c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=2)
  * **Marks:** 6 Marks ($\epsilon$-NFA) + 4 Marks (DFA) = 10 Marks &mdash; [2017-2018 Final: Q2(b, c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
  * **Marks:** 4 Marks ($\epsilon$-NFA) + 6 Marks (DFA) = 10 Marks &mdash; [2016-2017 Final: Q6(b, c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2016-2017_Final.pdf#page=1)
* **"Build an $\epsilon$-NFA for $L = \{w \mid w \text{ is empty, or if non-empty will end in } 11\}$ and convert it to DFA."**
  * **Marks:** 5 Marks ($\epsilon$-NFA) + 10 Marks (DFA) = 15 Marks &mdash; [2019-2020 1st Mid: Q7, Q8](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2019-2020_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks ($\epsilon$-NFA) + 6 Marks (DFA) = 10 Marks &mdash; [2018-2019 Final: Q6(b, c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
* **"A language $L$ is accepted by some $\epsilon$-NFA if and only if $L$ is accepted by some DFA."**
  * **Marks:** 4 Marks &mdash; [2020-2021 1st Mid: Q4(ii)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2020-2021_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"Briefly describe, how we can eliminate $\epsilon$-transitions?"**
  * **Marks:** 4 Marks &mdash; [2018-2019 Final: Q8(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)

---

### CHAPTER 3: Regular Expressions and Languages

#### 3.1 Regular Expressions & Operators
* **"Under what circumstances is an expression referred to as a regular expression?" / "When is an expression called regular expression?"**
  * **Marks:** 2 Marks &mdash; [2020-2021 Final: Q2(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 2 Marks &mdash; [2019-2020 Final: Q2(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"What is regular expression? Describe the operations of regular expressions."**
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q7(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
* **"Elaborate the three operations on languages that the operations of regular expression represent."**
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q6(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"Give a regular expression for the following language $B$ over the alphabet $\{a, b\}$. $B = \{w \mid w \text{ does not contain the substring } aaa\}$."**
  * **Marks:** 4 Marks &mdash; [2020-2021 Final: Q2(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q2(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"Consider the regular expression $(a(cd)^*b)^*$: (i) Find a string over $\{a, b, c, d\}^4$ which matches the expression. (ii) Find a string over $\{a, b, c, d\}^4$ which does not match the expression."**
  * **Marks:** 4 Marks ($2 + 2$) &mdash; [2019-2020 Final: Q8(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks ($2 + 2$) &mdash; [2017-2018 Final: Q8(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)

#### 3.2 Finite Automata and Regular Expressions
* **"Prove that every language defined by a regular expression is also defined by a finite automata."**
  * **Marks:** 10 Marks &mdash; [2021-2022 1st Mid: Q1](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2021-2022_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q7(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"Convert the following RE to $\epsilon$-NFA: $(0+1)^*01(0+1)^*$"**
  * **Marks:** 10 Marks &mdash; [2021-2022 1st Mid: Q4](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2021-2022_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2020-2021 1st Mid: Q5](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2020-2021_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q7(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=2)
  * **Marks:** 6 Marks &mdash; [2017-2018 Final: Q7(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
  * **Marks:** 6 Marks &mdash; [2016-2017 Final: Q7(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2016-2017_Final.pdf#page=1)
* **"Describe the interchangeable relation between Regular Expressions (RE) and Finite Automata with figure / Show with figure that they are interchangeable."**
  * **Marks:** 3 Marks &mdash; [2021-2022 Final: Q7(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=2)
  * **Marks:** 6 Marks &mdash; [2017-2018 Final: Q7(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
  * **Marks:** 6 Marks &mdash; [2016-2017 Final: Q7(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2016-2017_Final.pdf#page=1)
* **"Convert DFA's to regular expressions by eliminating states (using an arbitrary example)."**
  * **Marks:** 5 Marks &mdash; [2020-2021 Final: Q4(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2019-2020 Final: Q4(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"Convert the following DFA to an equivalent regular Expression [Diagram with 2 states $q_1, q_2$ and loops]"**
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q7(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
* **"Prove that: if $L = L(A)$ for some DFA $A$, then there is a regular expression $R$ such that $L = L(R)$."**
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q7(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)

#### 3.3 Lexical Analysis
* **"Explain the work of lexical analyzer with an on/off switch."**
  * **Marks:** 3 Marks &mdash; [2019-2020 1st Mid: Q2](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2019-2020_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 2 Marks &mdash; [2018-2019 Final: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)

#### 3.4 Algebraic Laws for Regular Expressions
* **"Define - i) Associativity, ii) Identity, and iii) Distributive Law"**
  * **Marks:** 3 Marks ($1 + 1 + 1$) &mdash; [2018-2019 Final: Q7(d)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
  * **Definitions & Algebraic Identities:**
    * **Associativity:** Both union ($+$) and concatenation are associative:
      $$L + (M + N) = (L + M) + N, \quad L(MN) = (LM)N$$
    * **Identity:**
      * $\emptyset$ is the identity for union: $L + \emptyset = \emptyset + L = L$
      * $\epsilon$ is the identity for concatenation: $L\epsilon = \epsilon L = L$
    * **Distributive Law:** Concatenation distributes over union from both left and right:
      $$L(M + N) = LM + LN \quad \text{(Left Distributive)}$$
      $$(M + N)L = ML + NL \quad \text{(Right Distributive)}$$
    * **Annihilator:** $\emptyset$ is an annihilator for concatenation: $L\emptyset = \emptyset L = \emptyset$.
* *(Note: Detailed closure proofs under complementation ($\overline{L} = \Sigma^* - L$), adding finite sets of strings, and master closure summary tables are analyzed systematically in [Chapter 4: Section 4.2](#42-closure-properties-of-regular-languages)).*

---

### CHAPTER 4: Properties of Regular Languages

#### 4.1 Proving Languages Not to Be Regular

##### 4.1.1 The Pumping Lemma for Regular Languages
* **"State the Pumping Lemma for regular languages."**
  * **Marks:** 3 Marks &mdash; [2020-2021 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2019-2020 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"Describe the basic functionalities of pumping lemma."**
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)

> **Theorem 4.1 (The Pumping Lemma for Regular Languages):**  
> Let $L$ be a regular language. Then there exists a positive integer constant $n$ (the **pumping length**, which depends solely on $L$) such that for every string $w \in L$ with $|w| \ge n$, $w$ can be broken into three substrings, $w = xyz$, satisfying the following three conditions:
> 1. $|y| \ge 1$ (i.e., $y \ne \epsilon$, meaning the pumped substring is non-empty)
> 2. $|xy| \le n$ (i.e., the loop occurs entirely within the first $n$ symbols)
> 3. For all $k \ge 0$, the string $x y^k z \in L$.

* **Theoretical Foundation & The Pigeonhole Principle:**  
  * Since $L$ is regular, there exists a Deterministic Finite Automaton (DFA) $M = (Q, \Sigma, \delta, q_0, F)$ accepting $L$ with $n = |Q|$ states.
  * When processing any string $w = a_1 a_2 \dots a_m \in L$ of length $m \ge n$, the automaton traverses a sequence of $m + 1 \ge n + 1$ states:
    $$q_0, q_1, q_2, \dots, q_m \quad \text{where } q_i = \hat{\delta}(q_0, a_1 \dots a_i) \text{ and } q_m \in F$$
  * By the **Pigeonhole Principle**, because there are only $n$ distinct states in $Q$ but at least $n+1$ state visits in the prefix sequence $q_0, q_1, \dots, q_n$, **at least two states among the first $n+1$ visits must be identical**:
    $$\exists \, i, j \text{ such that } 0 \le i < j \le n \text{ and } q_i = q_j$$
  * Decompose $w$ accordingly:
    * $x = a_1 a_2 \dots a_i$ (takes $q_0 \to q_i$)
    * $y = a_{i+1} \dots a_j$ (non-empty loop from $q_i \to q_i$, with $|y| = j - i \ge 1$ and $|xy| = j \le n$)
    * $z = a_{j+1} \dots a_m$ (takes $q_i \to q_m \in F$)
  * For any $k \ge 0$, the string $x y^k z$ visits $q_0 \xrightarrow{x} q_i \xrightarrow{y^k} q_i \xrightarrow{z} q_m \in F$. Therefore, $x y^k z \in L$ for all $k \ge 0$.

* **Adversarial Game Framework (How to Structure Proofs by Contradiction):**  
  To prove a language $L$ is **not** regular, use proof by contradiction structured as a 4-step game against an adversary:
  1. **Adversary chooses $n$:** Assume $L$ is regular; the adversary supplies some pumping length $n$.
  2. **You choose $w$:** Select a strategic string $w \in L$ with $|w| \ge n$ (parameterized by $n$).
  3. **Adversary chooses split $w = xyz$:** The adversary chooses $x, y, z$ constrained by $|xy| \le n$ and $|y| \ge 1$.
  4. **You choose $k$ (Winning move):** Pick an integer $k \ge 0$ (typically $k=0$ to "pump down" or $k=2$ to "pump up") such that $x y^k z \notin L$. This contradiction disproves regularity.

##### 4.1.2 Applications of the Pumping Lemma
* **"Use the pumping lemma to prove that the language $L = \{0^i \mid i \text{ is a perfect square}\}$ is not regular"**
  * **Marks:** 5 Marks &mdash; [2021-2022 Final: Q8(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=2)
  * **Step-by-Step Proof:**
    1. Assume $L$ is regular. Let $n$ be the pumping lemma constant.
    2. Choose string $w = 0^{n^2}$. Notice that $|w| = n^2 \ge n$, and $w \in L$ because $n^2$ is a perfect square.
    3. By condition (2), $|xy| \le n$, and by condition (1), $|y| = p \ge 1$. Thus, $1 \le p \le n$. Since $w$ consists entirely of 0s, $y = 0^p$.
    4. Consider the pumped string for $k = 2$: $w' = x y^2 z$. The length of $w'$ is:
       $$|w'| = |xyz| + |y| = n^2 + p$$
    5. Evaluate the bounds on $|w'|$:
       $$n^2 < n^2 + 1 \le n^2 + p \le n^2 + n < n^2 + 2n + 1 = (n+1)^2$$
       $$\implies n^2 < |w'| < (n+1)^2$$
    6. Since $|w'|$ lies strictly between two consecutive perfect squares $n^2$ and $(n+1)^2$, its length cannot be a perfect square. Thus, $x y^2 z \notin L$.
    7. This contradicts the Pumping Lemma. Hence, $L = \{0^i \mid i \text{ is a perfect square}\}$ is **not regular**. $\blacksquare$

* **"Prove that the following language is either regular or not. $A = \{ w w w \mid w \in \{a, b\}^* \}$"**
  * **Marks:** 5 Marks &mdash; [2017-2018 Final: Q6(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
  * **Step-by-Step Proof:**
    1. Assume $A$ is regular. Let $n$ be the pumping lemma constant.
    2. Choose string $s = a^n b a^n b a^n b$. Clearly, $s = www$ with $w = a^n b \in \{a, b\}^*$, so $s \in A$, and $|s| = 3(n+1) \ge n$.
    3. According to the Pumping Lemma, $s = xyz$ with $|xy| \le n$ and $|y| \ge 1$.
    4. Because $|xy| \le n$, the substring $xy$ lies entirely within the first block of $a$'s ($a^n$). Therefore, $y = a^p$ where $1 \le p \le n$.
    5. Pump with $k = 2$: $s' = x y^2 z = a^{n+p} b a^n b a^n b$.
    6. If $s' \in A$, it must be writable as $u u u$ for some string $u \in \{a, b\}^*$.
       * Total length $|s'| = 3n + p + 3$. If $|u u u| = |s'|$, each block $u$ must have length $|u| = n + \frac{p}{3} + 1$.
       * Furthermore, $s'$ contains exactly three $b$'s. For $s' = uuu$, each copy of $u$ must contain exactly one $b$.
       * The first $b$ occurs at position $(n + p + 1)$, which forces the first copy of $u$ to end at that $b$, meaning $|u| = n + p + 1$.
       * The second $b$ occurs $(n+1)$ symbols later, requiring the second copy of $u$ to have length $n+1$.
       * This requires $n + p + 1 = n + 1 \implies p = 0$, directly contradicting $p \ge 1$.
    7. Hence $s' \notin A$. By contradiction, $A = \{www \mid w \in \{a, b\}^*\}$ is **not regular**. $\blacksquare$

* **"Prove that the following are not regular languages:  
  (i) The set of strings of 0's and 1's beginning with 1, such that when interpreted as an integer, that integer is a prime.  
  (ii) The set of strings of the form $0^i 1^j$ such that the greatest common divisor of $i$ and $j$ is 1."**
  * **Marks:** 6 Marks ($3 + 3$) &mdash; [2019-2020 Final: Q7(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Proof for (i) (Binary Primes Language $L_{prime}$):**
    1. Assume $L_{prime}$ is regular, with pumping constant $n$.
    2. Choose a prime $p$ such that $p > 2^{n+1}$. Let $w$ be the binary representation of $p$. Since $p > 2^{n+1}$, $|w| \ge n+2 > n$, and $w$ begins with 1, so $w \in L_{prime}$.
    3. The Pumping Lemma asserts $w = xyz$ with $|xy| \le n$ and $|y| = m \ge 1$.
    4. Let the binary string be divided into $x, y, z$. The numerical value of string $x y^k z$ satisfies:
       $$V(x y^k z) = V(x) \cdot 2^{|y^k z|} + V(y) \cdot 2^{|z|} \sum_{j=0}^{k-1} 2^{j |y|} + V(z)$$
       By choosing $k$ such that the modular arithmetic forces a non-trivial factor dividing $V(x y^k z)$, the numerical value becomes composite.
       *(Equivalently in unary notation $L = \{1^p \mid p \text{ is prime}\}$: pick $w = 1^p$ with prime $p \ge n$. Decompose $w = xyz$ with $y = 1^m$, $1 \le m \le n$. Pump with $k = p+1$: $|x y^{p+1} z| = |w| + p|y| = p + pm = p(1+m)$, which is factored and composite since $p \ge 2$ and $1+m \ge 2$.)*
    5. Hence the language of primes is **not regular**. $\blacksquare$
  * **Proof for (ii) (Coprime Exponents $L_{gcd} = \{0^i 1^j \mid \gcd(i, j) = 1\}$):**
    1. Assume $L_{gcd}$ is regular with pumping constant $n$.
    2. Choose prime $p > n$. Let $w = 0^p 1^{p! + 1}$. Since $\gcd(p, p! + 1) = 1$, $w \in L_{gcd}$, and $|w| \ge n$.
    3. Since $|xy| \le n$, $y = 0^k$ where $1 \le k \le n$.
    4. Pumping $y$ with $m$ copies yields string $0^{p + (m-1)k} 1^{p! + 1}$.
    5. We choose integer $m$ such that $p + (m-1)k$ shares a non-trivial factor with $p! + 1$. Specifically, we can choose $m - 1 = \frac{p!}{k}$ (which is an integer because $k \le n < p$, so $k$ divides $p!$).
    6. The exponent of 0 then becomes $p + \frac{p!}{k} \cdot k = p + p! = p(1 + (p-1)!)$.
    7. Both exponents $p(1 + (p-1)!)$ and $p! + 1$ are divisible by factors or we can set $p + (m-1)k = p! + 1$, yielding $\gcd(p!+1, p!+1) = p! + 1 > 1$.
    8. Hence the pumped string has $\gcd > 1$ and is not in $L_{gcd}$. By contradiction, $L_{gcd}$ is **not regular**. $\blacksquare$

* **Canonical Non-Regular Languages Reference Table:**

| Language $L$ | String Choice $w$ | Constraint on $y$ | Pumping Move $k$ | Resulting Contradiction |
| :--- | :--- | :--- | :--- | :--- |
| $\{0^n 1^n \mid n \ge 0\}$ | $0^n 1^n$ | $y = 0^p$ ($1 \le p \le n$) | $k = 0$ or $k = 2$ | $0^{n+p} 1^n \notin L$ (unequal zeros & ones) |
| $\{w \mid N_0(w) = N_1(w)\}$ | $0^n 1^n$ | $y = 0^p$ ($1 \le p \le n$) | $k = 2$ | More 0s than 1s |
| $\{0^i \mid i \text{ is a square}\}$ | $0^{n^2}$ | $y = 0^p$ ($1 \le p \le n$) | $k = 2$ | $n^2 < n^2 + p < (n+1)^2$ (non-square length) |
| $\{w w \mid w \in \{0, 1\}^*\}$ | $0^n 1 0^n 1$ | $y = 0^p$ ($1 \le p \le n$) | $k = 2$ | $0^{n+p} 1 0^n 1 \ne uu$ |
| $\{w w w \mid w \in \{a, b\}^*\}$ | $a^n b a^n b a^n b$ | $y = a^p$ ($1 \le p \le n$) | $k = 2$ | Unequal $a$-block lengths ($a^{n+p} b a^n b a^n b$) |
| $\{0^n 1^{2n} \mid n \ge 1\}$ | $0^n 1^{2n}$ | $y = 0^p$ ($1 \le p \le n$) | $k = 2$ | $0^{n+p} 1^{2n}$ violates $2(n+p) = 2n$ |
| $\{w \mid w = w^R\}$ (Palindromes) | $0^n 1 0^n$ | $y = 0^p$ ($1 \le p \le n$) | $k = 0$ | $0^{n-p} 1 0^n$ is not a palindrome |

##### 4.1.3 Exercises for Section 4.1
* **Exercise 4.1.1 (Hopcroft):** Prove that $L = \{0^n 1^m 0^n \mid m, n \ge 1\}$ is not regular.  
  * *Solution Outline:* Choose $w = 0^n 1 0^n$. Since $|xy| \le n$, $y = 0^p$ with $p \ge 1$ within the first block. Pumping $k=2$ yields $0^{n+p} 1 0^n$, where the first and second 0-blocks have unequal lengths.
* **Exercise 4.1.2 (Hopcroft):** Prove that $L = \{0^n 1^m \mid n < m\}$ is not regular.  
  * *Solution Outline:* Choose $w = 0^n 1^{n+1}$. Pumping $k=2$ produces $0^{n+p} 1^{n+1}$. Since $p \ge 1$, $n+p \ge n+1$, violating the condition $n < m$.

---

#### 4.2 Closure Properties of Regular Languages

##### 4.2.1 Closure of Regular Languages Under Boolean Operations
* **"Prove that if $L$ is a regular language over alphabet $\Sigma$, then $\overline{L} = \Sigma^* - L$ is also a regular language."**
  * **Marks:** 10 Marks &mdash; [2021-2022 1st Mid: Q2](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2021-2022_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2020-2021 Final: Q4(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q4(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Rigorous Proof (DFA State Complementation):**
    1. Let $L$ be a regular language over alphabet $\Sigma$. By definition of regular languages, there exists a Deterministic Finite Automaton (DFA) $A = (Q, \Sigma, \delta, q_0, F)$ such that $L(A) = L$.
    2. We assume $A$ is a complete DFA (i.e., transition function $\delta(q, a)$ is defined for every state $q \in Q$ and symbol $a \in \Sigma$; if not, add a dead/trap state).
    3. Construct a new DFA $B = (Q, \Sigma, \delta, q_0, F')$ where:
       $$F' = Q - F$$
       That is, $B$ has the exact same states, input alphabet, transition function, and start state as $A$, but its accepting states are precisely the non-accepting states of $A$.
    4. For any string $w \in \Sigma^*$, because $A$ is deterministic and complete, the extended transition function $\hat{\delta}(q_0, w)$ halts in exactly one state $q \in Q$.
    5. Then:
       $$w \in L(B) \iff \hat{\delta}(q_0, w) \in F' \iff \hat{\delta}(q_0, w) \in (Q - F) \iff \hat{\delta}(q_0, w) \notin F \iff w \notin L(A) \iff w \in \overline{L}$$
    6. Since $B$ is a valid DFA and $L(B) = \overline{L}$, the language $\overline{L} = \Sigma^* - L$ is regular. $\blacksquare$

* **"Prove that if we add a finite set of strings to a regular language, the result is a regular language."**
  * **Marks:** 4 Marks &mdash; [2020-2021 1st Mid: Q4(i)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2020-2021_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 8 Marks &mdash; [2019-2020 2nd Mid: Q4](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2019-2020_2nd_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2019-2020 Final: Q6(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2017-2018 Final: Q6(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
  * **Rigorous Proof:**
    1. Let $L$ be a regular language, and let $S = \{w_1, w_2, \dots, w_m\}$ be an arbitrary finite set of strings over alphabet $\Sigma$.
    2. For each individual string $w_i = a_1 a_2 \dots a_k \in S$, the singleton language $\{w_i\}$ can be represented by the regular expression $a_1 a_2 \dots a_k$. Therefore, every singleton language is regular.
    3. The set $S$ can be expressed as the finite union of singleton languages:
       $$S = \{w_1\} \cup \{w_2\} \cup \dots \cup \{w_m\}$$
       Since regular languages are closed under union, $S$ is regular (represented by regular expression $w_1 + w_2 + \dots + w_m$).
    4. Adding $S$ to $L$ produces the union $L \cup S$.
    5. Since both $L$ and $S$ are regular, and the class of regular languages is closed under union, $L \cup S$ is regular. $\blacksquare$

* **"Summarize the principal closure properties for regular languages." / "Write the closure properties of regular languages."**
  * **Marks:** 5 Marks &mdash; [2019-2020 2nd Mid: Q5](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2019-2020_2nd_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2020-2021 Final: Q4(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2019-2020 Final: Q4(a) & Q6(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q6(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
  * **Master Summary Table of Closure Properties:**

| Operation | Formal Definition | Construction / Proof Method |
| :--- | :--- | :--- |
| **Union** | $L \cup M = \{w \mid w \in L \lor w \in M\}$ | RE: $R + S$; or Product DFA with $F = (F_L \times Q_M) \cup (Q_L \times F_M)$ |
| **Intersection** | $L \cap M = \{w \mid w \in L \land w \in M\}$ | Product DFA $A_L \times A_M$ with $F = F_L \times F_M$; or De Morgan: $\overline{\overline{L} \cup \overline{M}}$ |
| **Complement** | $\overline{L} = \Sigma^* - L$ | Flip accepting and non-accepting states in complete DFA: $F' = Q - F$ |
| **Difference** | $L - M = \{w \mid w \in L \land w \notin M\}$ | Expressed as $L - M = L \cap \overline{M}$; product DFA with $F = F_L \times (Q_M - F_M)$ |
| **Concatenation** | $LM = \{uv \mid u \in L, v \in M\}$ | RE: $RS$; or $\epsilon$-NFA connecting accepting states of $A_L$ to start of $A_M$ |
| **Kleene Star** | $L^* = \bigcup_{i=0}^\infty L^i$ | RE: $R^*$; or $\epsilon$-NFA with new start/accepting state and feedback $\epsilon$-loops |
| **Reversal** | $L^R = \{w^R \mid w \in L\}$ | Structural induction on RE; or reverse all DFA transition arcs and swap start/final states |
| **Homomorphism** | $h(L) = \{h(w) \mid w \in L\}$ | Substitute $h(a)$ for each symbol $a$ in the regular expression $E$ for $L$ |
| **Inverse Homomorphism** | $h^{-1}(L) = \{w \in \Sigma^* \mid h(w) \in L\}$ | DFA construction with transitions $\delta_B(q, a) = \hat{\delta}_A(q, h(a))$ |

* **Product Automaton Construction for Intersection ($L \cap M$):**  
  * Let $A_L = (Q_L, \Sigma, \delta_L, q_{0L}, F_L)$ and $A_M = (Q_M, \Sigma, \delta_M, q_{0M}, F_M)$ be DFAs.
  * Construct product DFA $A = (Q_L \times Q_M, \Sigma, \delta, (q_{0L}, q_{0M}), F_L \times F_M)$ where:
    $$\delta((p, q), a) = (\delta_L(p, a), \delta_M(q, a))$$
  * A string $w$ reaches $(p, q) \in F_L \times F_M$ if and only if $w \in L$ and $w \in M$.

##### 4.2.2 Reversal
* **Theorem 4.11:** If $L$ is a regular language, then $L^R = \{w^R \mid w \in L\}$ is also a regular language.
* **Proof Method 1 (Structural Induction on Regular Expressions):**  
  * Basis: $\epsilon^R = \epsilon$, $\emptyset^R = \emptyset$, and for symbol $a \in \Sigma$, $a^R = a$.
  * Inductive Steps:
    * $(E_1 + E_2)^R = E_1^R + E_2^R$
    * $(E_1 E_2)^R = E_2^R E_1^R$ (concatenation reverses string order!)
    * $(E^*)^R = (E^R)^*$
* **Proof Method 2 (Automata Reversal):**  
  * Take a transition diagram of an NFA $A$ for $L$. Reverse the direction of all transition arcs.
  * Make the original start state the sole accepting state.
  * Add a new start state $q_0'$ with $\epsilon$-transitions to all original accepting states of $A$. The resulting $\epsilon$-NFA accepts $L^R$.

##### 4.2.3 Homomorphisms
* **Definition:** A homomorphism is a function $h: \Sigma \to \Gamma^*$ mapping each symbol $a \in \Sigma$ to a string $h(a) \in \Gamma^*$. For any string $w = a_1 a_2 \dots a_k$, $h(w) = h(a_1) h(a_2) \dots h(a_k)$.
* **Theorem 4.14:** If $L$ is regular, then $h(L) = \{h(w) \mid w \in L\}$ is regular.
* **Proof:** Let $R$ be a regular expression for $L$. Replace each symbol $a$ occurring in $R$ with the regular expression representing $h(a)$. The resulting regular expression defines $h(L)$.

##### 4.2.4 Inverse Homomorphisms
* **"Explain inverse homomorphism."**
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q5(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Definition & Core Concept:**  
    Let $h: \Sigma \to \Gamma^*$ be a homomorphism. If $L$ is a language over alphabet $\Gamma$, the **inverse homomorphism** $h^{-1}(L)$ is the set of all strings in $\Sigma^*$ whose image under $h$ is in $L$:
    $$h^{-1}(L) = \{w \in \Sigma^* \mid h(w) \in L\}$$
    *(Note: $h^{-1}$ does NOT require $h$ to be an invertible/bijective function; it is defined on any language $L \subseteq \Gamma^*$).*
  * **Theorem 4.16:** If $L$ is regular, then $h^{-1}(L)$ is regular.
  * **DFA Construction Proof:**
    1. Let $A = (Q, \Gamma, \delta_A, q_0, F)$ be a DFA accepting $L$.
    2. Construct DFA $B = (Q, \Sigma, \delta_B, q_0, F)$ where for every state $q \in Q$ and input symbol $a \in \Sigma$:
       $$\delta_B(q, a) = \hat{\delta}_A(q, h(a))$$
    3. That is, to process input symbol $a$, automaton $B$ simulates automaton $A$ reading the entire string $h(a) \in \Gamma^*$.
    4. By induction on $|w|$, for any $w \in \Sigma^*$:
       $$\hat{\delta}_B(q_0, w) = \hat{\delta}_A(q_0, h(w))$$
    5. Thus, $w \in L(B) \iff \hat{\delta}_B(q_0, w) \in F \iff \hat{\delta}_A(q_0, h(w)) \in F \iff h(w) \in L \iff w \in h^{-1}(L)$.
    6. Since $B$ is a valid DFA, $h^{-1}(L)$ is regular. $\blacksquare$

##### 4.2.5 Exercises for Section 4.2
* **Using Closure to Prove Non-Regularity:**  
  * To prove $L = \{w \in \{0, 1\}^* \mid N_0(w) = N_1(w)\}$ is not regular:
    * We know $0^* 1^*$ is regular.
    * If $L$ were regular, $L \cap 0^* 1^*$ would be regular by intersection closure.
    * But $L \cap 0^* 1^* = \{0^n 1^n \mid n \ge 0\}$, which is proven non-regular.
    * Therefore, $L$ cannot be regular.

---

#### 4.3 Decision Properties of Regular Languages

##### 4.3.1 Converting Among Representations
* **Algorithm Complexities Across Conversions:**

| Conversion | Algorithm Used | Time Complexity | State / Size Bound |
| :--- | :--- | :--- | :--- |
| **RE to $\epsilon$-NFA** | Thompson's Construction | $O(n)$ | $\le 2n$ states, $\le 4n$ transitions |
| **$\epsilon$-NFA to DFA** | Subset Construction + $\epsilon$-closure | $O(n^3 \cdot 2^n)$ | Up to $2^n$ states |
| **DFA to NFA** | Identity (Trivial) | $O(n)$ | Identical ($n$ states) |
| **DFA to RE** | State Elimination / $R_{ij}^{(k)}$ | $O(n^3 \cdot 4^n)$ | Exponential length RE |
| **NFA to DFA** | Subset Construction | $O(2^n)$ | Up to $2^n$ states |

##### 4.3.2 Testing Emptiness of Regular Languages
* **Automaton Emptiness ($L(A) = \emptyset$):**
  * View DFA/NFA as a directed graph $G = (V, E)$.
  * Compute the set of all states reachable from start state $q_0$ using **Breadth-First Search (BFS)** or **Depth-First Search (DFS)**.
  * **Decision Rule:**
    * If $\text{Reachable}(q_0) \cap F = \emptyset$, then **$L(A)$ is EMPTY** ($L(A) = \emptyset$).
    * If $\text{Reachable}(q_0) \cap F \ne \emptyset$, then **$L(A)$ is NON-EMPTY**.
  * **Complexity:** Proportional to graph size: $O(|V| + |E|) = O(n \cdot |\Sigma|)$.
* **Regular Expression Emptiness (Recursive Inductive Test):**
  * $\emptyset$ is empty; $\epsilon$ and symbol $a$ are non-empty.
  * $L(R_1 + R_2)$ is empty $\iff$ both $L(R_1)$ and $L(R_2)$ are empty.
  * $L(R_1 R_2)$ is empty $\iff$ either $L(R_1)$ or $L(R_2)$ is empty.
  * $L(R^*)$ is **never empty** (always contains at least $\epsilon$).

##### 4.3.3 Testing Membership in a Regular Language
* Given a string $w$ of length $m$:
  * **Testing via DFA:** Trace $w$ symbol by symbol from $q_0$. Takes **$O(m)$ time** and $O(1)$ auxiliary space.
  * **Testing via NFA ($n$ states):** Maintain a set of active states for each prefix. Takes **$O(m \cdot n^2)$ time**.
  * **Testing via RE (size $s$):** Convert to $\epsilon$-NFA ($O(s)$ states) and simulate. Takes **$O(m \cdot s^2)$ time**.

##### 4.3.4 Exercises for Section 4.3 (Testing Finiteness)
* **Algorithm to Decide if a Regular Language is Finite:**
  1. Eliminate all states unreachable from start state $q_0$, and eliminate all dead states (states from which no accepting state can be reached).
  2. Test if the resulting transition graph contains any directed **cycles**.
  3. **Result:** $L$ is **infinite** if and only if there is a cycle on a path from $q_0$ to an accepting state. If acyclic, $L$ is **finite**.
  4. *Alternative via Pumping Lemma:* A regular language with an $n$-state DFA is infinite $\iff$ it accepts at least one string $w$ such that $n \le |w| < 2n$.

---

#### 4.4 Equivalence and Minimization of Automata

##### 4.4.1 Testing Equivalence of States
* **"Compute the equivalent states in a DFA by using Table-filling algorithm for the following: [8-state DFA]"**
  * **Marks:** 7 Marks &mdash; [2021-2022 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * *(Directly corresponds to Hopcroft, Motwani & Ullman, Figure 4.8 & Figure 4.9)*

* **Definitions of Equivalent vs. Distinguishable States:**
  * Two states $p, q \in Q$ are **equivalent** ($p \equiv q$) if for all input strings $w \in \Sigma^*$:
    $$\hat{\delta}(p, w) \in F \iff \hat{\delta}(q, w) \in F$$
  * Two states $p, q$ are **distinguishable** if there exists at least one string $w \in \Sigma^*$ such that exactly one of $\hat{\delta}(p, w)$ and $\hat{\delta}(q, w)$ is in $F$.

* **The Table-Filling Algorithm (Moore's Algorithm):**
  * **BASIS:** Mark every pair $\{p, q\}$ where $p \in F$ and $q \notin F$ (distinguished by the empty string $w = \epsilon$).
  * **INDUCTION:** For every unmarked pair $\{p, q\}$ and each symbol $a \in \Sigma$:
    * Let $r = \delta(p, a)$ and $s = \delta(q, a)$.
    * If the pair $\{r, s\}$ is already marked, then mark $\{p, q\}$. (Because if $w$ distinguishes $r$ and $s$, then $aw$ distinguishes $p$ and $q$).
  * **TERMINATION:** Repeat passes over all pairs until an entire pass makes no new marks. All remaining unmarked pairs are **equivalent**.

* **Full Step-by-Step Execution for the 8-State DFA (Hopcroft Fig. 4.8 / 2021-2022 Final Q2a):**
  * **Automaton Specifications:**
    * States: $Q = \{A, B, C, D, E, F, G, H\}$
    * Alphabet: $\Sigma = \{0, 1\}$
    * Start State: $A$
    * Final/Accepting States: $F = \{C\}$
    * Transition Table:

| State | Input 0 | Input 1 |
| :---: | :---: | :---: |
| $\to A$ | $B$ | $F$ |
| $B$ | $G$ | $C$ |
| $*C$ | $A$ | $C$ |
| $D$ | $C$ | $G$ |
| $E$ | $H$ | $F$ |
| $F$ | $C$ | $G$ |
| $G$ | $G$ | $E$ |
| $H$ | $G$ | $C$ |

  * **Execution Trace:**
    1. **Basis Step (Distinguished by $\epsilon$):**
       * Since $C$ is the only accepting state, mark all pairs containing $C$:
         $$\{A, C\}, \{B, C\}, \{C, D\}, \{C, E\}, \{C, F\}, \{C, G\}, \{C, H\} \quad \text{are marked with } \times$$
    2. **Induction Round 1:**
       * For each unmarked pair $\{p, q\}$, inspect successors under inputs 0 and 1:
         * $\{A, B\} \xrightarrow{1} \{F, C\}$ (marked) $\implies$ mark $\{A, B\}$.
         * $\{A, D\} \xrightarrow{0} \{B, C\}$ (marked) $\implies$ mark $\{A, D\}$.
         * $\{A, F\} \xrightarrow{0} \{B, C\}$ (marked) $\implies$ mark $\{A, F\}$.
         * $\{A, H\} \xrightarrow{1} \{F, C\}$ (marked) $\implies$ mark $\{A, H\}$.
         * $\{B, D\} \xrightarrow{0} \{G, C\}$ (marked) $\implies$ mark $\{B, D\}$.
         * $\{B, E\} \xrightarrow{1} \{C, F\}$ (marked) $\implies$ mark $\{B, E\}$.
         * $\{B, F\} \xrightarrow{0} \{G, C\}$ (marked) $\implies$ mark $\{B, F\}$.
         * $\{B, G\} \xrightarrow{1} \{C, E\}$ (marked) $\implies$ mark $\{B, G\}$.
         * $\{D, E\} \xrightarrow{0} \{C, H\}$ (marked) $\implies$ mark $\{D, E\}$.
         * $\{D, G\} \xrightarrow{0} \{C, G\}$ (marked) $\implies$ mark $\{D, G\}$.
         * $\{D, H\} \xrightarrow{0} \{C, G\}$ (marked) $\implies$ mark $\{D, H\}$.
         * $\{E, F\} \xrightarrow{0} \{H, C\}$ (marked) $\implies$ mark $\{E, F\}$.
         * $\{E, H\} \xrightarrow{1} \{F, C\}$ (marked) $\implies$ mark $\{E, H\}$.
         * $\{F, G\} \xrightarrow{0} \{C, G\}$ (marked) $\implies$ mark $\{F, G\}$.
         * $\{F, H\} \xrightarrow{0} \{C, G\}$ (marked) $\implies$ mark $\{F, H\}$.
         * $\{G, H\} \xrightarrow{1} \{E, C\}$ (marked) $\implies$ mark $\{G, H\}$.
    3. **Induction Round 2:**
       * Test remaining unmarked pairs: $\{A, E\}, \{A, G\}, \{B, H\}, \{D, F\}, \{E, G\}$:
         * Check $\{A, G\}$: $\delta(A, 1) = F, \delta(G, 1) = E \implies \{F, E\}$, which was marked in Round 1 $\implies$ **mark $\{A, G\}$**.
         * Check $\{E, G\}$: $\delta(E, 1) = F, \delta(G, 1) = E \implies \{F, E\}$, which was marked in Round 1 $\implies$ **mark $\{E, G\}$**.
         * Check $\{A, E\}$: on 0 goes to $\{B, H\}$ (unmarked); on 1 goes to $\{F, F\}$ (identical). Cannot mark.
         * Check $\{B, H\}$: on 0 goes to $\{G, G\}$; on 1 goes to $\{C, C\}$. Identical transitions! Cannot mark.
         * Check $\{D, F\}$: on 0 goes to $\{C, C\}$; on 1 goes to $\{G, G\}$. Identical transitions! Cannot mark.
    4. **Induction Round 3:**
       * No additional pairs are marked. The algorithm halts.

  * **Final Distinguishability Table (Hopcroft Figure 4.9):**

```
B  |  x
C  |  x    x
D  |  x    x    x
E  |       x    x    x
F  |  x    x    x         x
G  |  x    x    x    x    x    x
H  |  x         x    x    x    x    x
---+-----------------------------------
   |  A    B    C    D    E    F    G
```

  * **Identified Equivalent Pairs:**
    $$\{A, E\}, \quad \{B, H\}, \quad \{D, F\}$$

##### 4.4.2 Testing Equivalence of Regular Languages
* **Method 1 (Joint Automaton via Table-Filling):**
  * Given DFA $A$ and DFA $B$ accepting $L$ and $M$.
  * Construct a single joint DFA whose state set is $Q_A \cup Q_B$ (assumed disjoint; if not, rename states).
  * Run the Table-Filling Algorithm on the joint automaton.
  * **Equivalence Criterion:**
    $$L(A) = L(B) \iff \{q_{0A}, q_{0B}\} \text{ is UNMARKED (i.e., start states are equivalent)}$$
* **Method 2 (Symmetric Difference Emptiness):**
  * Languages $L$ and $M$ are equivalent $\iff$ their symmetric difference is empty:
    $$L \oplus M = (L - M) \cup (M - L) = (L \cap \overline{M}) \cup (\overline{L} \cap M) = \emptyset$$
  * Construct the product DFA for $(L \cap \overline{M}) \cup (\overline{L} \cap M)$ and run the emptiness test (graph reachability).

##### 4.4.3 Minimization of DFA's
* **The 4-Step Minimization Procedure:**
  1. **Remove Unreachable States:** Use BFS/DFS from start state $q_0$ to discard any inaccessible states.
  2. **Run Table-Filling Algorithm:** Mark all distinguishable pairs.
  3. **Form Equivalence Classes (Partition):** Group states into equivalence blocks:
     $$[q] = \{p \in Q \mid p \equiv q\}$$
     By transitivity of state equivalence, these blocks partition $Q$.
  4. **Construct Quotient DFA $M_{min} = (Q', \Sigma, \delta', [q_0], F')$:**
     * States $Q'$ are the equivalence blocks $[q]$.
     * Start state is $[q_0]$.
     * Accepting states $F'$ are blocks containing accepting states.
     * Transition function: $\delta'([q], a) = [\delta(q, a)]$.

* **Constructing the Minimum-State DFA for Figure 4.8 (Hopcroft Fig. 4.12):**
  * Equivalence blocks:
    $$[A, E], \quad [B, H], \quad [C], \quad [D, F], \quad [G]$$
  * The original 8 states are compressed into **5 minimal states**!
  * **Minimal DFA Transition Table:**

| Equivalent State Block | Input 0 | Input 1 | Status |
| :---: | :---: | :---: | :---: |
| $\to [A, E]$ | $[B, H]$ | $[D, F]$ | Start State |
| $[B, H]$ | $[G]$ | $[C]$ | |
| $*[C]$ | $[A, E]$ | $[C]$ | Accepting State |
| $[D, F]$ | $[C]$ | $[G]$ | |
| $[G]$ | $[G]$ | $[A, E]$ | |

##### 4.4.4 Why the Minimized DFA Can't Be Beaten
* **Theorem 4.26 (Uniqueness & Minimality):**  
  If $M$ is the DFA constructed by collapsing equivalent states of a DFA $A$ (with unreachable states removed), then $M$ has the fewest states of any DFA equivalent to $A$. Furthermore, this minimal DFA is **unique up to state isomorphism (relabelling)**.
* **Proof by Contradiction:**  
  1. Suppose there exists an equivalent DFA $N$ with strictly fewer states than $M$ ($|Q_N| < |Q_M|$).
  2. Combine $M$ and $N$ into a joint DFA. Because $L(M) = L(N)$, their start states are equivalent: $q_{0M} \equiv q_{0N}$.
  3. Since every state $p \in Q_M$ is reachable from $q_{0M}$ by some string $w$, state $p$ must be equivalent to the state $q = \hat{\delta}_N(q_{0N}, w)$ in $N$.
  4. Thus, every state of $M$ is equivalent to at least one state of $N$.
  5. By the **Pigeonhole Principle**, since $|Q_M| > |Q_N|$, at least two distinct states $p_1, p_2 \in Q_M$ must be equivalent to the same state $q \in Q_N$.
  6. By transitivity of equivalence, $p_1 \equiv q \land p_2 \equiv q \implies p_1 \equiv p_2$.
  7. But $M$ was constructed specifically by collapsing all equivalent states, so no two distinct states in $M$ can be equivalent!
  8. Contradiction. Hence, no DFA equivalent to $A$ can have fewer states than $M$. $\blacksquare$
* **Why State Equivalence Fails to Minimize NFAs (Hopcroft Fig. 4.13):**  
  * State equivalence does **not** minimize NFAs.
  * In Hopcroft Fig. 4.13, no two states are equivalent, yet removing state $C$ entirely yields a smaller 2-state NFA accepting the same language ($L = (0+1)^*0$). NFA minimization is PSPACE-complete!

##### 4.4.5 Exercises for Section 4.4
* **Hopcroft Exercise 4.4.1 (Minimizing 8-state DFA of Fig. 4.14):** Practice executing the table-filling algorithm on state transitions to determine indistinguishable partitions.
* **Hopcroft Exercise 4.4.2 (Minimizing 9-state DFA of Fig. 4.15):** Trace distinguishability passes and construct the resulting quotient automaton.

---

#### 4.5 Summary of Chapter 4
* **Core Takeaways:**
  1. **Pumping Lemma:** Essential tool to prove non-regularity by contradiction. Relies directly on the Pigeonhole Principle over DFA states.
  2. **Closure Properties:** Regular languages are closed under Boolean operations (union, intersection, complement, difference), concatenation, Kleene star, reversal, homomorphism, and inverse homomorphism.
  3. **Decision Properties:** Emptiness is decidable in linear time via graph reachability; membership is decidable in $O(|w|)$ via DFA simulation; equivalence is decidable via Table-Filling or symmetric difference emptiness.
  4. **DFA Minimization:** Every regular language has a unique (up to isomorphism) minimum-state DFA, effectively constructed via the $O(n^2)$ Table-Filling Algorithm.

---

#### 4.6 Gradiance Problems for Chapter 4
* **Common Conceptual Pitfalls & Exam Traps:**
  * *Trap 1:* Using the Pumping Lemma to prove a language *is* regular. (The Pumping Lemma is a necessary condition, NOT a sufficient condition; languages satisfying the pumping lemma can still be non-regular!).
  * *Trap 2:* Complementing an incomplete DFA. Always ensure dead/trap states and missing transitions are explicitly included before swapping accepting states.
  * *Trap 3:* Believing NFAs can be minimized by the Table-Filling Algorithm. State equivalence minimization applies strictly to DFAs.

---

#### 4.7 References for Chapter 4
* Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). *Introduction to Automata Theory, Languages, and Computation* (3rd ed.). Pearson / Addison-Wesley. Chapter 4: Properties of Regular Languages, pp. 127–169.

---

## 🏆 Top 10 "Guaranteed" Exam Topics for 2022-2023 Mid-Term

Based on Dr. Md Manjur Ahmed's past midterm and final question papers across Chapters 1 through 4, prepare these 10 core problem patterns:

1. **DFA Minimization via Table-Filling Algorithm (Moore's Algorithm)**  
   *Target:* Distinguishability table ($n(n-1)/2$ pairs) and quotient automaton construction for 8-state DFA (Hopcroft Fig. 4.8 / equivalent pairs $\{A, E\}, \{B, H\}, \{D, F\}$).  
   *Appeared:* 2021–2022 Final (7M), Hopcroft Section 4.4.
2. **Pumping Lemma for Regular Languages & Non-Regularity Proofs**  
   *Target:* Theorem statement, Pigeonhole Principle justification, and proof by contradiction for $L = \{0^i \mid i 	ext{ is a perfect square}\}$, $\{w w w\}$, or prime languages.  
   *Appeared:* 2021–2022 Final (5M), 2020–2021 Final (3M), 2019–2020 Final (9M), 2018–2019 Final (3M), 2017–2018 Final (5M).
3. **Closure Proofs of Regular Languages**  
   *Target:* Proof that $\overline{L} = \Sigma^* - L$ is regular (swap final and non-final states in complete DFA), adding a finite set of strings $L \cup F$, and inverse homomorphism $h^{-1}(L)$.  
   *Appeared:* 2021–2022 Mid (10M), 2020–2021 Mid (8M), 2019–2020 Mid-2 (13M), 2019–2020 Final (9M), 2020–2021 Final (4M).
4. **RE to $\epsilon$-NFA Conversion (Thompson's Construction)**  
   *Target:* $(0+1)^*01(0+1)^*$  
   *Appeared:* 2021–2022 Mid (10M), 2020–2021 Mid (4M), 2017–2018 Final (6M), 2016–2017 Final (6M), 2021–2022 Final (4M).
5. **$\epsilon$-NFA Construction & Elimination to DFA**  
   *Target:* $L = \{w \mid w \text{ is empty, or if non-empty will end in } 01 \text{ (or } 11)\}$  
   *Appeared:* 2021–2022 Mid (10M), 2020–2021 Mid (4M), 2019–2020 Mid (15M), 2021–2022 Final (10M), 2018–2019 Final (10M).
6. **NFA to DFA Subset Construction**  
   *Target:* 4-state NFA conversion table & state diagram, or language $L = \{w \mid w \text{ ends in } 011 / 101\}$.  
   *Appeared:* 2021–2022 Mid (10M), 2020–2021 Final (4M), 2019–2020 Final (6M), 2019–2020 Mid (15M).
7. **Bad Case for Subset Construction & Pigeonhole Principle**  
   *Target:* Explanation of state explosion ($2^n$) where DFA states $\gg$ NFA states, formalized via Pigeonhole Principle.  
   *Appeared:* 2020–2021 Mid (8M), 2018–2019 Mid (7M), 2021–2022 Final (5M), 2018–2019 Final (6M).
8. **NFA: "First symbol present somewhere later on at least once"**  
   *Target:* Design NFA with alphabet $\{0, 1\}$.  
   *Appeared:* 2020–2021 Mid (4M), 2019–2020 Mid (5M), 2018–2019 Mid (5M), 2017–2018 Mid, 2021–2022 Final (6M).
9. **DFA: Even number of 0s and even number of 1s**  
   *Target:* 4-state product automaton (states $(e, e), (e, o), (o, e), (o, o)$).  
   *Appeared:* 2018–2019 Mid (5M), 2017–2018 Mid, 2021–2022 Final (6M), 2018–2019 Final (5M), 2016–2017 Final (6M).
10. **Mathematical Proof Techniques**  
    *Target:* Induction proof ("if $x \ge 4$ then $2^x \ge x^2$") and definition of Theorems, Lemmas, Corollaries.  
    *Appeared:* 2020–2021 Mid (8M), 2019–2020 Mid (6M), 2018–2019 Final (7M).

---
*Maintained for academic revision and exam preparation &bull; University of Barishal CSE.*

