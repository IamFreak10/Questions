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
- **3.4 Algebraic Laws for Regular Expressions & Closure Properties** (Associativity, Commutativity, Identity, Distributivity, Closures, Regular Language Closure under Complementation & Finite Union)

### Chapter 4: Properties of Regular Languages
- **4.1 Proving Languages Not to Be Regular** (4.1.1 The Pumping Lemma for Regular Languages, 4.1.2 Applications of the Pumping Lemma, 4.1.3 Exercises for Section 4.1)
- **4.2 Closure Properties of Regular Languages** (4.2.1 Closure of Regular Languages Under Boolean Operations, 4.2.2 Reversal, 4.2.3 Homomorphisms, 4.2.4 Inverse Homomorphisms, 4.2.5 Exercises for Section 4.2)
- **4.3 Decision Properties of Regular Languages** (4.3.1 Converting Among Representations, 4.3.2 Testing Emptiness of Regular Languages, 4.3.3 Testing Membership in a Regular Language, 4.3.4 Exercises for Section 4.3)
- **4.4 Equivalence and Minimization of Automata** (4.4.1 Testing Equivalence of States, 4.4.2 Testing Equivalence of Regular Languages, 4.4.3 Minimization of DFA's, 4.4.4 Why the Minimized DFA Can't Be Beaten, 4.4.5 Exercises for Section 4.4)
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
  * **Marks:** 7 Marks &mdash; [2021-2022 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)

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

#### 3.4 Algebraic Laws & Regular Language Closures
* **"Prove that if $L$ is a regular language over alphabet $\Sigma$, then $\overline{L} = \Sigma^* - L$ is also a regular language."**
  * **Marks:** 10 Marks &mdash; [2021-2022 1st Mid: Q2](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2021-2022_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2020-2021 Final: Q4(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q4(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"Prove that if we add a finite set of strings to a regular language, the result is a regular language."**
  * **Marks:** 4 Marks &mdash; [2020-2021 1st Mid: Q4(i)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2020-2021_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2019-2020 Final: Q6(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 8 Marks &mdash; [2019-2020 2nd Mid: Q4](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2019-2020_2nd_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2017-2018 Final: Q6(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
* **"Summarize the principal closure properties for regular languages." / "Write the closure properties of regular languages."**
  * **Marks:** 5 Marks &mdash; [2019-2020 2nd Mid: Q5](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2019-2020_2nd_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2020-2021 Final: Q4(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2019-2020 Final: Q4(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q6(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
* **"Define - i) Associativity, ii) Identity, and iii) Distributive Law"**
  * **Marks:** 3 Marks ($1 + 1 + 1$) &mdash; [2018-2019 Final: Q7(d)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)

---

### CHAPTER 4: Properties of Regular Languages

#### 4.1 Proving Languages Not to Be Regular
* **"State the Pumping Lemma for regular languages."**
  * **Marks:** 3 Marks &mdash; [2020-2021 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2019-2020 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"Describe the basic functionalities of pumping lemma."**
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2018-2019_Final.pdf#page=1)
* **"Use the pumping lemma to prove that the language $L = \{0^i \mid i \text{ is a perfect square}\}$ is not regular"**
  * **Marks:** 5 Marks &mdash; [2021-2022 Final: Q8(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=2)
* **"Prove that the following language is either regular or not. $A = \{ w w w \mid w \in \{a, b\}^* \}$"**
  * **Marks:** 5 Marks &mdash; [2017-2018 Final: Q6(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
* **"Prove that the following are not regular languages:  
  (i) The set of strings of 0's and 1's beginning with 1, such that when interpreted as an integer, that integer is a prime.  
  (ii) The set of strings of the form $0^i 1^j$ such that the greatest common divisor of $i$ and $j$ is 1."**
  * **Marks:** 6 Marks ($3 + 3$) &mdash; [2019-2020 Final: Q7(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)

#### 4.2 Closure Properties of Regular Languages
* **"Prove that if $L$ is a regular language over alphabet $\Sigma$, then $\overline{L} = \Sigma^* - L$ is also a regular language."**
  * **Marks:** 10 Marks &mdash; [2021-2022 1st Mid: Q2](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2021-2022_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2020-2021 Final: Q4(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q4(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
* **"Prove that if we add a finite set of strings to a regular language, the result is a regular language."**
  * **Marks:** 4 Marks &mdash; [2020-2021 1st Mid: Q4(i)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2020-2021_1st_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 8 Marks &mdash; [2019-2020 2nd Mid: Q4](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2019-2020_2nd_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2019-2020 Final: Q6(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2017-2018 Final: Q6(b)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
* **"Summarize the principal closure properties for regular languages." / "Write the closure properties of regular languages."**
  * **Marks:** 5 Marks &mdash; [2019-2020 2nd Mid: Q5](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Midterm/2019-2020_2nd_Mid_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2020-2021 Final: Q4(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2020-2021_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2019-2020 Final: Q4(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q6(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2017-2018_Final.pdf#page=1)
* **"Explain inverse homomorphism."**
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q5(c)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2019-2020_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)

#### 4.4 Equivalence and Minimization of Automata
* **"Compute the equivalent states in a DFA by using Table-filling algorithm for the following: [8-state DFA]"**
  * **Marks:** 7 Marks &mdash; [2021-2022 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/02_CSE-3203_Theory_of_Computation/Final/2021-2022_Final_Dr_Md_Manjur_Ahmed.pdf#page=1)

---

## 🏆 Top 10 "Guaranteed" Exam Topics for 2022-2023 Mid-Term

Based on Dr. Md Manjur Ahmed's past midterm and final question papers across Chapters 1 through 4, prepare these 10 core problem patterns:

1. **RE to $\epsilon$-NFA Conversion (Thompson's Construction)**  
   *Target:* $(0+1)^*01(0+1)^*$  
   *Appeared:* 2021–2022 Mid (10M), 2020–2021 Mid (4M), 2017–2018 Final (6M), 2016–2017 Final (6M), 2021–2022 Final (4M).
2. **$\epsilon$-NFA Construction & Elimination to DFA**  
   *Target:* $L = \{w \mid w \text{ is empty, or if non-empty will end in } 01 \text{ (or } 11)\}$  
   *Appeared:* 2021–2022 Mid (10M), 2020–2021 Mid (4M), 2019–2020 Mid (15M), 2021–2022 Final (10M), 2018–2019 Final (10M).
3. **NFA to DFA Subset Construction**  
   *Target:* 4-state NFA conversion table & state diagram, or language $L = \{w \mid w \text{ ends in } 011 / 101\}$.  
   *Appeared:* 2021–2022 Mid (10M), 2020–2021 Final (4M), 2019–2020 Final (6M), 2019–2020 Mid (15M).
4. **Bad Case for Subset Construction & Pigeonhole Principle**  
   *Target:* Explanation of state explosion ($2^n$) where DFA states $\gg$ NFA states, formalized via Pigeonhole Principle.  
   *Appeared:* 2020–2021 Mid (8M), 2018–2019 Mid (7M), 2021–2022 Final (5M), 2018–2019 Final (6M).
5. **NFA: "First symbol present somewhere later on at least once"**  
   *Target:* Design NFA with alphabet $\{0, 1\}$.  
   *Appeared:* 2020–2021 Mid (4M), 2019–2020 Mid (5M), 2018–2019 Mid (5M), 2017–2018 Mid, 2021–2022 Final (6M).
6. **DFA: Even number of 0s and even number of 1s**  
   *Target:* 4-state product automaton (states $(e, e), (e, o), (o, e), (o, o)$).  
   *Appeared:* 2018–2019 Mid (5M), 2017–2018 Mid, 2021–2022 Final (6M), 2018–2019 Final (5M), 2016–2017 Final (6M).
7. **Closure Proofs of Regular Languages**  
   *Target:* Proof that $\overline{L} = \Sigma^* - L$ is regular (swap final and non-final states in DFA) and finite union closure.  
   *Appeared:* 2021–2022 Mid (10M), 2020–2021 Mid (8M), 2019–2020 Final (9M), 2020–2021 Final (4M).
8. **Mathematical Proof Techniques**  
   *Target:* Induction proof ("if $x \ge 4$ then $2^x \ge x^2$") and definition of Theorems, Lemmas, Corollaries.  
   *Appeared:* 2020–2021 Mid (8M), 2019–2020 Mid (6M), 2018–2019 Final (7M).

9. **DFA Minimization via Table-Filling Algorithm (Moore's Algorithm)**  
   *Target:* Distinguishability table and quotient automaton construction for 8-state DFA (Hopcroft Fig. 4.8 / equivalent pairs $\{A, E\}, \{B, H\}, \{D, F\}$).  
   *Appeared:* 2021–2022 Final (7M), Hopcroft Section 4.4.
10. **Pumping Lemma for Regular Languages & Non-Regularity Proofs**  
    *Target:* Theorem statement, Pigeonhole Principle justification, and proof by contradiction for $L = \{0^i \mid i \text{ is a perfect square}\}$, $\{w w w\}$, or prime languages.  
    *Appeared:* 2021–2022 Final (5M), 2020–2021 Final (3M), 2019–2020 Final (9M), 2018–2019 Final (3M), 2017–2018 Final (5M).

---
*Maintained for academic revision and exam preparation &bull; University of Barishal CSE.*

