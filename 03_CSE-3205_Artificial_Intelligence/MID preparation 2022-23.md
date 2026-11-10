# CSE-3205: Artificial Intelligence — Mid-Term Preparation Guide (Session: 2022–2023)

> **Department of Computer Science and Engineering, University of Barishal**  
> **Course Code:** CSE-3205 &bull; **Course Title:** Artificial Intelligence &bull; **Credits:** 3.0  
> **Primary Course Teacher / Examiner:** Dr. Tania Islam  
> **Target Exam:** Mid-Term Examination (Session 2022–2023)  
> **Syllabus Reference:** Russell & Norvig, *Artificial Intelligence: A Modern Approach* (AIMA) — Chapters 2, 3, and 4 (Lectures 3–6)  
> **Archive Source:** [Examinations Archive](./)

---

## 📑 Syllabus Outline Covered (Lectures 3 – 6)

### 1. Intelligent Agents & Task Environments
- **Agents & Rationality:** Agent, Percept, Percept Sequence, Agent Function ($f: P^* \to A$), Agent Program, Rationality vs. Omniscience, Performance Measures.
- **Agent Architectures:** Simple Reflex Agents, Model-Based Reflex Agents, Goal-Based Agents, Utility-Based Agents, Learning Agents.
- **Task Environments (PEAS):** Performance Measure, Environment, Actuators, Sensors.
- **Environment Classifications:** Fully Observable vs. Partially Observable, Deterministic vs. Stochastic, Episodic vs. Sequential, Static vs. Dynamic, Discrete vs. Continuous, Single-Agent vs. Multi-Agent.

### 2. Search Problem Formulation & State Space Basics
- **Problem Formulation Components:** Initial State, Actions / Action Set $A(s)$, Transition Model $\text{Result}(s, a)$, Goal Test, Path Cost function $c(s, a, s')$.
- **State Space & Search Concepts:** State Space, State Graph vs. Search Tree, Search Node structure (State, Parent, Action, Path-Cost $g(n)$, Depth $d$), Branching Factor ($b$), Expanding vs. Generating nodes, Frontier (Open List) vs. Explored Set (Closed List).
- **Evaluation Criteria:** Completeness, Optimality, Time Complexity, Space Complexity.

### 3. Uninformed (Blind) Search Strategies
- **Breadth-First Search (BFS):** FIFO Queue frontier, complete, optimal for unit step costs, Time: $\mathcal{O}(b^d)$, Space: $\mathcal{O}(b^d)$.
- **Depth-First Search (DFS):** LIFO Stack frontier, incomplete in infinite spaces, non-optimal, Time: $\mathcal{O}(b^m)$, Space: $\mathcal{O}(bm)$ (memory-efficient).
- **Uniform-Cost Search (UCS):** Priority Queue by path cost $g(n)$, complete, optimal for positive step costs, Time & Space: $\mathcal{O}(b^{1 + \lfloor C^* / \epsilon \rfloor})$. Proof as a special case of $A^*$.
- **Iterative Deepening Search (IDS / IDDFS):** Repeated depth-limited search with increasing limit, complete, optimal for unit costs, Time: $\mathcal{O}(b^d)$, Space: $\mathcal{O}(bd)$. Why IDS is uninformed despite repeated expansions.

### 4. Informed (Heuristic) Search Strategies
- **Heuristic Function $h(n)$:** Definition, purpose, straight-line distance, Manhattan distance.
- **Heuristic Properties:**
  - **Admissibility:** $h(n) \le h^*(n)$ (never overestimates true cost to goal).
  - **Consistency (Monotonicity):** $h(n) \le c(n, a, n') + h(n')$ (triangle inequality).
  - Proof that admissibility guarantees optimality for tree-search $A^*$, consistency guarantees optimality for graph-search $A^*$.
- **Greedy Best-First Search (GBFS):** Evaluation function $f(n) = h(n)$, Priority Queue by $h(n)$, greedy expansion, incomplete, non-optimal, prone to false leads.
- **$A^*$ Search:** Evaluation function $f(n) = g(n) + h(n)$, step-by-step queue tracing, Open/Closed lists, tie-breaking rules.
- **Weighted $A^*$ Search:** Evaluation function $f(n) = g(n) + W \cdot h(n)$ where $W > 1$, trade-off between search speed and solution optimality.

### 5. Local Search Algorithms & The State Space Landscape
- **State Space "Landscape":** Global Maximum / Minimum, Local Maxima / Minima, Plateaus, Ridges, Shoulders.
- **Local Search Concepts:** Iterative improvement, memory-less nature ($\mathcal{O}(1)$ space), optimization focus.
- **Hill-Climbing Search:** Greedy local search, steepest-ascent hill climbing, drawbacks (local maxima, ridges, plateaus), escaping techniques (Random Restart, Simulated Annealing).
- **Genetic Algorithms (GA):** Population-based local beam search variant, Chromosome representation, Fitness function, Selection, Crossover, Mutation operators, 8-Queens problem formulation.

---

## 🎯 Topic-by-Topic Historical Questions & Marks Analysis

---

### TOPIC 1: Intelligent Agents & Task Environments

#### 1.1 Agents, Rationality & Architecture Concepts
* **"Define an Intelligent Agent. Explain the role of Sensors, Actuators, and the Environment in designing an intelligent agent."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q1(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"A smart irrigation system automatically waters crops based on soil moisture, weather conditions, and temperature. Describe the structure of this intelligent agent and explain how it makes rational decisions."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"Define Artificial Intelligence. Explain why 'rationality' is central in AI."**
  * **Marks:** 4 Marks &mdash; [2020-2021 Final: Q1(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2020-2021_Final_Dr_Tania_Islam.pdf#page=1)
* **"Describe the structure of an intelligent agent with a smart home temperature control example."**
  * **Marks:** 4 Marks &mdash; [2020-2021 Final: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2020-2021_Final_Dr_Tania_Islam.pdf#page=1)
* **"Imagine you are designing an intelligent personal shopping agent for an online store. The agent should understand the user's preferences (style, budget, and past purchase history). Negotiate discounts with the store's pricing system. Recommend the best items while balancing cost, quality, and delivery time. How would you design the perception, reasoning, and action components of this agent, and what AI techniques would you apply in each step?"**
  * **Marks:** 5 Marks &mdash; [2020-2021 1st Mid: Q3](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2020-2021_1st_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Define Agent and Rational Agent through real time example."**
  * **Marks:** 3 Marks &mdash; [2019-2020 Final: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2017-2018_Final.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2016-2017 Final: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2016-2017_Final.pdf#page=1)
* **"Define Rational Agent with example. Is vacuum cleaner agent Rational? Why or why not? Explain with suitable reasons."**
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q2(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)

#### 1.2 Agent Types & Comparative Models
* **"Differentiate among the following agent types with one real-world example of each: Simple Reflex Agent, Goal-Based Agent, Learning Agent."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q1(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"Differentiate between reactive, model-based, and goal-based agents with examples."**
  * **Marks:** 4 Marks &mdash; [2020-2021 Final: Q1(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2020-2021_Final_Dr_Tania_Islam.pdf#page=1)
* **"Explain the difference between simple reflex agents and model-based reflex agents."**
  * **Marks:** 5 Marks &mdash; [2020-2021 1st Mid: Q4](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2020-2021_1st_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Imagine, Mary is a model-based AI that builds and maintains an internal representation of the world. And Greg, on the other hand, is a goal-based AI that focuses on achieving specific objectives. Describe the fundamental differences between Model-Based Mary and Goal-Based Greg in terms of their operational strategies. How does each approach affect their decision-making processes and adaptability to changes in their environment?"**
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q2(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
* **"Describe the function of vacuum cleaner as an Agent with suitable diagram."**
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2018-2019_Final.pdf#page=1)
* **"Write short notes on agent type: (i) Simple reflex agents (ii) Model-based reflex agents."**
  * **Marks:** 3 Marks &mdash; [2016-2017 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2016-2017_Final.pdf#page=1)

#### 1.3 Task Environments & PEAS Specifications
* **"Distinguish between the following properties of a task environment: (i) Static or dynamic (ii) Discrete or continuous (iii) Single or multi-agent."**
  * **Marks:** 3 Marks &mdash; [2019-2020 Final: Q1(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q1(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2018-2019_Final.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q1(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2017-2018_Final.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2016-2017 Final: Q1(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2016-2017_Final.pdf#page=1)
* **"Briefly explain the PEAS description of the task environment for an automated taxi."**
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q1(d)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2018-2019_Final.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q1(d)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2017-2018_Final.pdf#page=1)
* **"Briefly explain the PEAS description of the task environment for an automated taxi, Part Picking Robot and Refinery Controller."**
  * **Marks:** 3 Marks &mdash; [2016-2017 Final: Q1(d)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2016-2017_Final.pdf#page=1)
* **"The Task Environment for a Virtual English Tutor must have Performance, Environment, Actuators, and Sensors. By considering these four parameters develop the PEAS descriptions for a Virtual English Tutor Agent."**
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q1(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2017-2018_Final.pdf#page=1)
* **"Illustrate the Wumpus World problem along with its PEAS."**
  * **Marks:** 4 Marks &mdash; [2016-2017 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2016-2017_Final.pdf#page=1)

---

### TOPIC 2: Search Problem Formulation & State Space Basics

#### 2.1 Search Components & Terminology Definitions
* **"Define in your own words the following terms: state, state space, search tree, search node, goal, action, transition model, and branching factor."**
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q3(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2018-2019 Final: Q3(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2018-2019_Final.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2018-2019 1st Mid: Q1(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2018-2019_1st_Mid.pdf#page=1)
* **"List the criteria to measure the performance of different search strategies."**
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2017-2018_Final.pdf#page=1)
* **"Compare uninformed search and informed search in terms of completeness, optimality, time complexity, and space complexity."**
  * **Marks:** 5 Marks &mdash; [2020-2021 1st Mid: Q1](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2020-2021_1st_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Differentiate Uninformed Search (Blind search) and Informed Search (Heuristic Search) strategies."**
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q2(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2017-2018_Final.pdf#page=1)
* **"Explain difference between uninformed and informed search. List two examples of each type of algorithm. Proof that Uniform-cost search is a special case of A* search."**
  * **Marks:** 4 Marks &mdash; [2016-2017 Final: Q2(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2016-2017_Final.pdf#page=1)

---

### TOPIC 3: Uninformed Search Strategies (BFS, DFS, UCS, IDS)

#### 3.1 Breadth-First Search (BFS) & Depth-First Search (DFS)
* **"A robot is delivering medicines inside a hospital. The rooms are Entrance (E), Reception (R), Pharmacy (P), Laboratory (L), ICU (I), Ward (W), Exit (X). The corridors are described as follows: Entrance connects to Reception; Reception connects to Pharmacy and Laboratory; Pharmacy connects to ICU; Laboratory connects to Ward; ICU connects to Exit; Ward also connects to Exit.**
  - **a) Draw the graph based on the description. Perform Breadth-First Search (BFS) from Entrance (E) to Exit (X) and show Frontier Queue, Visited Nodes and Parent Table after each iteration. [5 Marks]**
  - **b) Using the same graph, perform Depth-First Search (DFS) from Entrance (E) to Exit (X). Show the exact order of node expansion. [5 Marks]**
  - **c) Compare BFS and DFS in terms of Completeness and Optimality. Explain why they may return different solution paths. [2 Marks]"**
  * **Total:** 12 Marks &mdash; [2021-2022 Final: Q2(a, b, c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"A university website has the following structure:**
  - **The root page is Home**
  - **Home links to Admission, Academics, and Contact**
  - **Admission links to Form and Scholarship**
  - **Academics links to Departments and Syllabus**
  **A student is searching for the page Syllabus. Now consider the following question:**
  - **a) First, draw the search tree from the given description.**
  - **b) Write the visiting order of pages using (i) BFS (ii) DFS (left-to-right order).**
  - **c) Analytically explain: which search guarantees the shallowest solution, and which search is more memory-efficient."**
  * **Marks:** 8 Marks &mdash; [2021-2022 Midterm: Q2](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2021-2022_1st_2nd_Mid_Dr_Tania_Islam.pdf#page=1)
* **"A robot is exploring a building with rooms connected by corridors. The rooms are: Entrance (E), Hall (H), Office1 (O1), Office2 (O2), Lab (L), Storage (S), Exit (X). Connections (edges) are described verbally as follows: E connects to H; H connects to O1 and O2; O1 connects to L; O2 connects to S; L connects to X; S also connects to X.**
  - **a) Let's draw the graph based on this description and Perform BFS from E to find the first path to X and list every step (frontier, visited, parents). [5 Marks]**
  - **b) Perform DFS from E to X and show the exact order of node expansion. [5 Marks]**
  - **c) Explain why BFS and DFS return different paths in your graph. [2 Marks]"**
  * **Total:** 12 Marks &mdash; [2020-2021 Final: Q2(a, b, c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2020-2021_Final_Dr_Tania_Islam.pdf#page=1)
* **"Perform Breadth-First Search (BFS) starting from node A. List the order in which nodes are visited."**
  * **Marks:** 5 Marks &mdash; [2020-2021 2nd Mid: Q1](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2020-2021_2nd_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Prove that the time and space complexity of BFS is $O(b^d)$. And explain it with an example."**
  * **Marks:** 4 Marks &mdash; [2017-2018 Final: Q2(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2017-2018_Final.pdf#page=1)
* **"Among the given options, which search algorithm requires less memory? And why? Give with an example.**
  1. Optimal Search &bull; 2. Depth First Search &bull; 3. Breadth-First Search &bull; 4. Linear Search"**
  * **Marks:** 5 Marks &mdash; [2019-2020 1st Mid: Q2](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2019-2020_1st_Mid.pdf#page=1)
  * **Marks:** 6 Marks &mdash; [2018-2019 1st Mid: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2018-2019_1st_Mid.pdf#page=1)

#### 3.2 Uniform-Cost Search (UCS)
* **"A delivery company wants to transport goods from Warehouse (W) to Customer (C). Locations are: W, A, B, D, E, C. Road costs are: $W \to A = 5$, $W \to B = 2$, $A \to D = 3$, $B \to D = 4$, $D \to E = 2$, $E \to C = 3$.**
  - **a) Draw the weighted graph and Perform Uniform Cost Search (UCS). Show Priority Queue, Expanded Node, Current Path Cost after every iteration. [5 Marks]**
  - **b) Show the final optimal path. [2 Marks]"**
  * **Total:** 7 Marks &mdash; [2021-2022 Final: Q3(a, b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"The graph shows the step costs for different paths going from the start (S) to the goal (G). Use uniform cost search to find the optimal path to the goal."**
  * **Marks:** 8 Marks &mdash; [2020-2021 Final: Q6(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2020-2021_Final_Dr_Tania_Islam.pdf#page=2)
  * **Marks:** 8 Marks &mdash; [2019-2020 Final: Q6(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 8 Marks &mdash; [2018-2019 Final: Q6(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2018-2019_Final.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2017-2018 Final: Q6(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2017-2018_Final.pdf#page=1)

#### 3.3 Iterative Deepening Search (IDS)
* **"Explain the advantages of Iterative Deepening Search (IDS) over BFS and DFS. Also compare their Time Complexity and Space Complexity."**
  * **Marks:** 5 Marks &mdash; [2021-2022 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2020-2021 Final: Q6(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2020-2021_Final_Dr_Tania_Islam.pdf#page=2)
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q6(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2018-2019 Final: Q6(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2018-2019_Final.pdf#page=1)
* **"A rescue drone searches for a missing hiker. The search space is described as follows:**
  - **Each location leads to exactly 4 new locations**
  - **The starting point is the root**
  - **The hiker is guaranteed to be at depth 6**
  **You have to solve the following questions:**
  - **a) First, draw a small portion of the search tree (up to depth 2) based on the description.**
  - **b) Explain why Iterative Deepening Search (IDS) is still an uninformed search, even though it repeats node expansions.**
  - **c) Compare BFS and IDS for this problem in terms of memory usage and practical suitability for a battery-limited rescue drone."**
  * **Marks:** 6 Marks &mdash; [2021-2022 Midterm: Q3](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2021-2022_1st_2nd_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Explain iterative deepening search with example."**
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)

---

### TOPIC 4: Informed / Heuristic Search (Heuristics, GBFS, A* Search)

#### 4.1 Heuristic Functions, Admissibility & Consistency
* **"Define a Heuristic Function. Explain the characteristics of an admissible heuristic with an example."**
  * **Marks:** 3 Marks &mdash; [2021-2022 Final: Q5(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=2)
* **"Explain why heuristics are important in AI search problems with an example scenario."**
  * **Marks:** 5 Marks &mdash; [2020-2021 1st Mid: Q2](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2020-2021_1st_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Prove that A* search is optimal if $h(n)$ is admissible."**
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q3(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2017-2018_Final.pdf#page=1)
* **"Is the heuristic given in Problem 5.a admissible? Explain."**
  * **Marks:** 3 Marks &mdash; [2019-2020 Final: Q5(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
* **"Is the heuristic given in Problem 5.a consistent? Explain."**
  * **Marks:** 3 Marks &mdash; [2019-2020 Final: Q5(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)

#### 4.2 Greedy Best-First Search (GBFS)
* **"A delivery robot starts from S and wants to reach the destination G. The road connections are described as follows: S is directly connected to A and B; A is directly connected to C; B is directly connected to C; C is directly connected to G; All roads have equal cost. The heuristic values are: S:3, A:2, B:1, C:1, G:0.**
  - **a) First, draw the graph using the above description.**
  - **b) Show the node expansion order using (i) BFS (ii) Greedy Best-First Search (GBFS).**
  - **c) Identify which search is uninformed and which is informed, and analytically explain why GBFS may expand fewer nodes but does not guarantee the shortest path."**
  * **Marks:** 6 Marks &mdash; [2021-2022 Midterm: Q1](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2021-2022_1st_2nd_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Apply Greedy Best-First Search (GBFS) from S to G. Use only $h(n)$ to choose which node to expand and show the following:**
  - **priority queue sorted by $h$**
  - **visited order**
  - **final path GBFS finds."**
  * **Marks:** 5 Marks &mdash; [2020-2021 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2020-2021_Final_Dr_Tania_Islam.pdf#page=1)
* **"What is Greedy Best First Search? Explain with an example the different stages of Greedy Best First search."**
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q3(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
* **"A hypothetical state space with heuristic evaluation is given (ROOT A-5; multiple levels). If P is the goal state, how do you reach the goal state using best-first search?"**
  * **Marks:** 4 Marks &mdash; [2017-2018 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2017-2018_Final.pdf#page=1)

#### 4.3 A* Search & Weighted A* Execution Problems
* **"A robot must travel from Start (S) to Goal (G). The nodes are S, A, B, C, D, G. The path costs are $S \to A = 3$, $S \to B = 2$, $A \to C = 4$, $B \to D = 2$, $C \to G = 3$, $D \to G = 5$. The heuristic values are: $h(S)=8, h(A)=6, h(B)=5, h(C)=3, h(D)=4, h(G)=0$.**
  - **a) Draw the graph. Perform A* Search and show: $g(n)$, $h(n)$, $f(n)$, OPEN List, CLOSED List after every iteration. [6 Marks]**
  - **b) Write the final optimal path found by A*. Using the same graph, perform Greedy Best-First Search (GBFS). Show Priority Queue, Visited Order, Final Path. Compare the result with A* Search. [6 Marks]"**
  * **Total:** 12 Marks &mdash; [2021-2022 Final: Q4(a, b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=2)
* **"Using the graph in Question 4, perform Weighted A* Search with $f(n) = g(n) + 2h(n)$. Compare the search process with ordinary A*."**
  * **Marks:** 6 Marks &mdash; [2021-2022 Final: Q5(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=2)
* **"A navigation system must find the shortest path from Start (S) to Goal (G). Nodes: S, A, B, C, D, E, G. Edges and costs are $S \to A = 3$, $S \to B = 2$, $A \to C = 4$, $B \to C = 1$, $C \to D = 2$, $D \to E = 1$, $E \to G = 5$. Heuristic $h(n)$: $h(S)=10, h(A)=7, h(B)=9, h(C)=6, h(D)=4, h(E)=2, h(G)=0$.**
  - **a) Now, draw the graph and perform A* search step-by-step: compute $f(n)=g(n)+h(n)$, show OPEN, CLOSED lists and show how ties are broken. [5 Marks]**
  - **b) Show the final optimal path. [2 Marks]"**
  * **Total:** 7 Marks &mdash; [2020-2021 Final: Q3(a, b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2020-2021_Final_Dr_Tania_Islam.pdf#page=1)
* **"Using A* algorithm, find the shortest path from A to F. Assume the heuristic (straight-line distance to F) is: $h(A)=5, h(B)=4, h(C)=2, h(D)=6, h(E)=3, h(F)=0$.**
  - **Show your step-by-step calculation, including $f(n)=g(n)+h(n)$. [5 Marks]**
  - **Draw the final search tree showing the paths explored by A*. [5 Marks]**
  - **Explain which algorithm (BFS or A*) is more efficient in this case and why. [5 Marks]"**
  * **Total:** 15 Marks &mdash; [2020-2021 2nd Mid: Q2, Q3, Q4](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2020-2021_2nd_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Consider the graph shown below where the numbers on the links are link costs and the numbers next to the states are heuristic estimates. Note that the arcs are undirected. Let A be the start state and G be the goal state. Simulate A* search with a strict expanded list on this graph. At each step, show the path to the state of the node that's being expanded, the length of that path, the total estimated cost of the path (actual + heuristic), and the current value of the expanded list (as a list of states)."**
  * **Marks:** 6 Marks &mdash; [2019-2020 Final: Q5(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
* **"Perform A* Algorithm on the following figure. Explicitly write down the queue at each step."**
  * **Marks:** 8 Marks &mdash; [2018-2019 Final: Q3(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2018-2019_Final.pdf#page=1)
  * **Marks:** 10 Marks &mdash; [2018-2019 1st Mid: Q2](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2018-2019_1st_Mid.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2017-2018 Final: Q3(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2017-2018_Final.pdf#page=1)
  * **Marks:** 10 Marks &mdash; [2017-2018 1st Mid: Q2](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2017-2018_1st_Mid.pdf#page=1)
* **"The state space description for a problem is shown below, with A being the start state and D being the goal state. Shown on the graph are path costs between states. The table lists the estimated distance from a state to the goal. Assume these estimates are admissible. Perform an A* search for this problem, showing (i) the tree that represents the nodes expanded and (ii) the ordered list of nodes to expand at each step along with the node's f value. Recall that $f=g+h$."**
  * **Marks:** 5 Marks &mdash; [2016-2017 Final: Q2(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2016-2017_Final.pdf#page=1)
* **"Explain 'A* search is both complete and optimal'. Apply A* search for Bucharest in the given graph."**
  * **Marks:** 5 Marks &mdash; [2016-2017 Final: Q8(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2016-2017_Final.pdf#page=1)

#### 4.4 Multi-Algorithm Comparison on the Same Graph / Tree
* **"Consider the search space below, where S is start node and G1, G2 are goal nodes. For BFS, DFS, GBFS: (i) indicate which goal state is reached first (ii) list in order all states popped off the OPEN list."**
  * **Marks:** 12 Marks &mdash; [2018-2019 Final: Q5(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2018-2019_Final.pdf#page=1)
  * **Marks:** 8 Marks &mdash; [2017-2018 Final: Q5(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2017-2018_Final.pdf#page=1)
* **"Consider the following search tree produced after expanding nodes A and B, where each arc is labeled with the cost of the corresponding operator, and the leaves are labeled with the value of a heuristic function, h. For uninformed searches (Depth-First search, Greedy Best-First search, Uniform-Cost search, A* search) assume children are expanded left to right. In case of ties, expand in alphabetical order."**
  * **Marks:** 15 Marks &mdash; [2019-2020 1st Mid: Q1](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Midterm/2019-2020_1st_Mid.pdf#page=1)

---

### TOPIC 5: Local Search Algorithms & The State Space Landscape

#### 5.1 Local Search Concepts & State Space Landscapes
* **"Explain the concept of Local Search Algorithms. Why are Local Search algorithms preferred for solving large optimization problems?"**
  * **Marks:** 3 Marks &mdash; [2021-2022 Final: Q5(c)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=2)
* **"What is local maxima? How to escape local maxima?"**
  * **Marks:** 3 Marks &mdash; [2019-2020 Final: Q1(d)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
* **"What do you mean by Adversarial Search. Solve 8-Queen problem using Genetic Algorithm or Hill-climbing search."**
  * **Marks:** 5 Marks &mdash; [2016-2017 Final: Q3(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2016-2017_Final.pdf#page=1)
* **"How do the crossover and mutation operator work? Sketch the flow diagram of a genetic algorithm."**
  * **Marks:** 6 Marks &mdash; [2016-2017 Final: Q7(a)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2016-2017_Final.pdf#page=1)
* **"What are the differences between evolution and genetic algorithms?"**
  * **Marks:** 2 Marks &mdash; [2016-2017 Final: Q7(b)](file:///home/iamfreak/Downloads/6th/Questions/03_CSE-3205_Artificial_Intelligence/Final/2016-2017_Final.pdf#page=1)

---

## 💡 Dr. Tania Islam's Core Exam Patterns & Preparation Checklist

1. **A\* Algorithm Queue Tracing (Guaranteed 5–10 Marks):**
   - Always prepare the 6-column iteration table:
     $$\text{Iteration } k \quad | \quad \text{Node Expanded } n \quad | \quad g(n) \quad | \quad h(n) \quad | \quad f(n) = g(n) + h(n) \quad | \quad \text{OPEN (Priority Queue)} \quad | \quad \text{CLOSED}$$
   - Practice explicit tie-breaking (alphabetical or lowest $h$).
2. **IDS vs. BFS/DFS Derivations (Guaranteed 4–5 Marks):**
   - Must prove why IDS has asymptotic time complexity $\mathcal{O}(b^d)$ matching BFS:
     $$(d)b + (d-1)b^2 + \dots + (1)b^d = \mathcal{O}(b^d)$$
   - Must highlight that space complexity is linear $\mathcal{O}(bd)$, making it ideal for memory- and battery-limited autonomous agents (e.g., rescue drones).
3. **PEAS Formulation & Environment Classification (Guaranteed 3–6 Marks):**
   - Always format PEAS answers into a 4-row markdown/tabular layout specifying **Performance Measure, Environment, Actuators, and Sensors**.
   - Standard high-yield examples: **Automated Taxi**, **Vacuum-Cleaner Agent**, **Smart Irrigation**, and **Smart Home Thermostat**.
4. **BFS vs. DFS Hospital / Room Corridors (Guaranteed 5–12 Marks):**
   - Given verbal node and corridor descriptions, draw the graph accurately and track **Frontier (Queue/Stack)**, **Visited Set**, and **Parent Table** after every step.

---
*Archive maintained for academic revision and exam preparation &bull; University of Barishal CSE.*
