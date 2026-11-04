# 6th Semester CSE Syllabus & Topic Taxonomy
### Department of Computer Science and Engineering &bull; University of Barishal

This reference maps every 6th-semester course to its syllabus modules, core theoretical concepts, algorithms, and frequent exam keywords.

---

## 1. CSE-3201: Mathematical Analysis for Computer Science (3.0 Credits)

### Module 1: Random Variables & Distributions
- **Concepts**: Discrete & Continuous Random Variables, Probability Mass Function (PMF), Probability Density Function (PDF), Cumulative Distribution Function (CDF).
- **Moments & Metrics**: Expectation \(E[X]\), Variance \(\text{Var}(X)\), Covariance \(\text{Cov}(X,Y)\), Sample Variance \(S^2\), Proof of Unbiasedness of Sample Variance.
- **Distributions**: Binomial, Poisson, Normal, Exponential, Geometric, Uniform distributions.

### Module 2: Stochastic Processes
- **Definitions**: Stochastic process \(\{X(t), t \in T\}\), Index set / Parameter space, State space.
- **Classifications**: Discrete vs Continuous time, Discrete vs Continuous state space.
- **Properties**: Processes with Independent Increments, Stationary processes (Strict-sense vs Wide-sense / Weakly stationary), Evolutionary processes, Second-Order processes, Covariance function properties.
- **Martingales**: Definition of Martingale, Submartingale, Supermartingale, Stopping times.

### Module 3: Markov Chains (Discrete Time)
- **Fundamentals**: Markov property, 1-step and n-step Transition Probability Matrix (TPM), Chapman-Kolmogorov equations.
- **State Classification**: Accessible, Communicating states, Recurrent (Positive vs Null recurrent), Transient states, Periodic / Aperiodic states, Ergodic chains, Absorbing states.
- **Theorems & Proofs**: First entrance decomposition formula, Stationary distribution \(\pi = \pi P\).

### Module 4: Continuous Time Markov Chains & Poisson Processes
- **Birth-Death Processes**: Pure Birth process, Linear birth rate (Yule-Furry process), Pure Death process, Birth-Death equations.
- **Poisson Process**: Postulates, Inter-arrival times, Exponential distribution relation.

### Module 5: Queuing Theory
- **Queuing Systems**: Kendall's notation \(A/B/c/K\), Single-server queue (M/M/1), Multi-server queue (M/M/c).
- **Metrics**: Little's Law (\(L = \lambda W\), \(L_q = \lambda W_q\)), Server utilization (\(\rho = \lambda / \mu\)), Average queue length, Waiting time in queue and system.

---

## 2. CSE-3203: Theory of Computation (3.0 Credits)

### Module 1: Finite Automata & Regular Languages
- **Automata Models**: Deterministic Finite Automata (DFA), Non-deterministic Finite Automata (NFA), \(\epsilon\)-NFA.
- **Equivalence & Conversions**: Subset construction (NFA to DFA), \(\epsilon\)-closure, DFA Minimization (Table-filling algorithm / Myhill-Nerode theorem).
- **Regular Expressions**: Regex operators, Arden's Theorem for solving state equations, Equivalence between Regular Expressions and Finite Automata.
- **Regular Grammars**: Right-linear and Left-linear grammars.

### Module 2: Non-Regular Languages & Properties
- **Pumping Lemma for Regular Languages**: Statement, Adversarial proof strategy, Proving non-regularity (e.g., \(a^n b^n\), \(0^n 1^n\), palindromes).
- **Closure Properties**: Union, Intersection, Complement, Concatenation, Kleene star, Homomorphism.
- **Decision Properties**: Emptiness, Finiteness, Equivalence of DFAs.

### Module 3: Context-Free Grammars (CFG) & Languages (CFL)
- **Grammars**: Formal definition of CFG, Derivations (Leftmost, Rightmost), Parse trees, Ambiguity in grammars (inherent ambiguity).
- **Normal Forms**: Elimination of \(\epsilon\)-productions, unit productions, useless symbols.
- **Chomsky Normal Form (CNF)**: Conversion steps, Parsing with CYK algorithm.
- **Greibach Normal Form (GNF)**: Definition and transformation.

### Module 4: Pushdown Automata (PDA)
- **Models**: Non-deterministic PDA (NPDA), Deterministic PDA (DPDA).
- **Acceptance Modes**: Acceptance by Final State vs Acceptance by Empty Stack (and their equivalence).
- **Equivalence**: Equivalence between PDA and CFG.
- **Pumping Lemma for CFLs**: Statement and proofs of non-context-free languages (e.g., \(a^n b^n c^n\)).

### Module 5: Turing Machines & Computability
- **Turing Machines**: Formal definition, Instantaneous Descriptions, Multi-tape TMs, Non-deterministic TMs, Universal Turing Machine (UTM).
- **Chomsky Hierarchy**: Type 0 (Unrestricted), Type 1 (Context-Sensitive), Type 2 (Context-Free), Type 3 (Regular).
- **Decidability**: Decidable vs Undecidable languages, Recursively Enumerable (RE) languages, Halting Problem proof by diagonalization.
- **Reduction & Theorems**: Post Correspondence Problem (PCP), Rice's Theorem.

---

## 3. CSE-3205: Artificial Intelligence (3.0 Credits)

### Module 1: Intelligent Agents & Problem Formulation
- **Agents**: Agent architecture, Rationality, Performance measure, PEAS formulation.
- **Environments**: Fully vs Partially observable, Deterministic vs Stochastic, Episodic vs Sequential, Static vs Dynamic, Discrete vs Continuous, Single vs Multi-agent.

### Module 2: Uninformed (Blind) Search
- **Algorithms**: Breadth-First Search (BFS), Depth-First Search (DFS), Depth-Limited Search (DLS), Iterative Deepening Search (IDS), Uniform Cost Search (UCS), Bidirectional Search.
- **Performance Evaluation**: Completeness, Time complexity, Space complexity, Optimality.

### Module 3: Informed (Heuristic) Search
- **Heuristics**: Heuristic functions \(h(n)\), Greedy Best-First Search, A* Search (\(f(n) = g(n) + h(n)\)).
- **Properties**: Admissibility of heuristics, Consistency (monotonicity), Dominance, Memory-bounded search (IDA*, SMA*).

### Module 4: Adversarial Search (Game Playing)
- **Game Trees**: Optimal decisions in games, Two-player zero-sum games, Minimax algorithm.
- **Pruning**: Alpha-Beta pruning (Alpha cut-off, Beta cut-off, node evaluation order).

### Module 5: Constraint Satisfaction Problems (CSP)
- **Formulation**: Variables, Domains, Constraints.
- **Solving Techniques**: Backtracking search, Heuristics (Minimum Remaining Values - MRV, Degree heuristic, Least Constraining Value - LCV), Forward Checking, Constraint Propagation (Arc Consistency AC-3).

### Module 6: Knowledge Representation & Logic
- **Propositional Logic**: Syntax, Semantics, Entailment, Truth tables, Inference rules (Modus Ponens, Resolution).
- **First-Order Logic (FOL)**: Syntax, Quantifiers (\(\forall, \exists\)), Unification, Most General Unifier (MGU), Conjunctive Normal Form (CNF) conversion, Resolution refutation proofs, Horn clauses, Forward and Backward chaining.

### Module 7: Probabilistic Reasoning & Learning Basics
- **Uncertainty**: Conditional probability, Bayes' Rule, Bayesian Networks (DAGs, conditional probability tables, conditional independence).
- **Machine Learning**: Supervised vs Unsupervised learning, Perceptron algorithm, Activation functions, Neural network fundamentals.

---

## 4. CSE-3206: Artificial Intelligence Lab (1.5 Credits)
- **Implementations**: Search algorithms (BFS, DFS, UCS, A*) in Python/C++.
- **Logic Programming**: Prolog syntax, facts, rules, queries, recursion, list manipulation (member, append, reverse), cut (`!`) and fail.
- **Game AI**: Minimax implementation for Tic-Tac-Toe, Connect Four.
- **CSP**: Solving N-Queens, Map Coloring, Cryptarithmetic puzzles.

---

## 5. CSE-3207: Peripherals and Interfacing (3.0 Credits)

### Module 1: 8086 Architecture & Interfacing Concepts
- **Internal Architecture**: Bus Interface Unit (BIU), Execution Unit (EU), Segment Registers, Pipelining.
- **Bus Cycles & Timing**: Minimum mode vs Maximum mode, Control signals (RD, WR, IO/M, ALE, DEN, DT/R), Wait state generation.
- **Memory Interfacing**: Even (Lower) and Odd (Higher) memory banks, \(\overline{\text{BHE}}\) and \(A_0\) decoding, Address decoding using 74LS138 decoders.
- **I/O Interfacing**: Memory-Mapped I/O vs Direct / I/O-Mapped I/O (Isolated I/O).

### Module 2: 8255 Programmable Peripheral Interface (PPI)
- **Architecture**: Internal block diagram, Ports (Port A, Port B, Port C Upper, Port C Lower).
- **Modes of Operation**:
  - Mode 0: Basic Input/Output.
  - Mode 1: Strobed Input/Output (Handshaking signals: STB, IBF, INTR, ACK, OBF).
  - Mode 2: Strobed Bidirectional Bus (Port A only).
  - BSR Mode: Bit Set/Reset mode for Port C pins.
- **Control Word**: Formats for I/O mode and BSR mode.
- **Interfacing Applications**: 7-Segment display, Matrix keyboard, Stepper motor (step sequence, half-step, full-step).

### Module 3: 8254/8253 Programmable Interval Timer (PIT)
- **Architecture**: Three independent 16-bit counters (Counter 0, 1, 2), Control Word Register.
- **Modes of Operation**: Mode 0 (Interrupt on terminal count), Mode 1 (Hardware retriggerable one-shot), Mode 2 (Rate generator), Mode 3 (Square wave generator), Mode 4 (Software triggered strobe), Mode 5 (Hardware triggered strobe).
- **Programming**: Writing count values, read-back commands.

### Module 4: 8259A Programmable Interrupt Controller (PIC)
- **Interrupt Handling**: 8086 Interrupt Vector Table (IVT), Dedicated interrupts (Type 0-4), Hardware vs Software interrupts.
- **8259A Features**: Priority resolver, Interrupt Request Register (IRR), In-Service Register (ISR), Interrupt Mask Register (IMR).
- **Initialization & Operation**: Initialization Command Words (ICW1 - ICW4), Operation Command Words (OCW1 - OCW3), Cascading master and slave PICs (supporting up to 64 interrupt levels).

### Module 5: Direct Memory Access (DMA) & 8237/8257 Controller
- **DMA Concept**: Cycle stealing, Burst mode, Handshaking (HOLD and HLDA).
- **DMA Controller**: Channel registers (Current Address, Current Count, Base Address, Base Count), Channel priority modes.

### Module 6: Serial Communication & 8251A USART
- **Serial Transmission**: Asynchronous vs Synchronous transmission, Framing (Start bit, Stop bit, Parity), Baud rate calculation, RS-232C standard.
- **8251A**: Internal architecture, Mode instruction, Command instruction, Status read.

### Module 7: Converters (ADC & DAC)
- **ADC 0808/0809**: Successive approximation register (SAR), Start of Conversion (SOC), End of Conversion (EOC), Analog channel selection (ADD A, B, C).
- **DAC 0808**: R-2R ladder network, Binary weighted resistor network, Settling time, Interfacing with microprocessor.

---

## 6. CSE-3208: Peripherals and Interfacing Lab (1.5 Credits)
- 8086 Assembly Language Programming on trainer kit / emu8086.
- Hardware Interfacing simulations with Proteus / physical kits:
  - 8255 interfacing with LED arrays and traffic light controllers.
  - 7-Segment multiplexed display interfacing.
  - Stepper motor speed and directional control.
  - DAC interfacing for generating Square, Triangular, and Sawtooth waveforms.
  - ADC interfacing for reading temperature/potentiometer values.

---

## 7. CSE-3209: Simulation and Modeling (3.0 Credits)

### Module 1: Principles of Simulation & System Concepts
- **Systems & Models**: System, Subsystem, Entities, Attributes, Activities, Events, State Variables.
- **Model Types**: Static vs Dynamic, Deterministic vs Stochastic, Continuous vs Discrete.
- **Simulation Methodology**: 12 steps in a simulation study, Advantages, Disadvantages, When simulation is appropriate vs not appropriate.

### Module 2: Discrete-Event System Simulation (DESS)
- **Core Mechanics**: Simulation clock, Event list, Event scheduling worldview, Process-interaction worldview.
- **Queuing Simulation**: Single-server queue (M/M/1 manual event-by-event simulation tracking clock, arrival, departure, server idle time, customer waiting time).
- **Inventory Simulation**: Order quantity \(Q\), Reorder point \(R\), Lead time, Holding cost, Shortage cost.

### Module 3: Random Number Generation (RNG)
- **Pseudo-Random Properties**: Uniformity in \([0, 1)\), Statistical independence, Long cycle / period.
- **Generators**: Linear Congruential Generator (LCG) \(X_{i+1} = (aX_i + c) \pmod m\), Multiplicative Congruential Generator (\(c = 0\)), Mixed Congruential Generator (\(c \neq 0\)).
- **Randomness Tests**:
  - Tests for Uniformity: Kolmogorov-Smirnov (K-S) test, Chi-Square (\(\chi^2\)) goodness-of-fit test.
  - Tests for Independence: Runs tests (runs up & down, runs above & below the mean), Autocorrelation test, Poker test, Gap test.

### Module 4: Random Variate Generation
- **Inverse-Transform Technique**: Direct derivation of \(X = F^{-1}(R)\) for Exponential distribution (\(X = -\frac{1}{\lambda}\ln(1-R)\)), Uniform distribution, Weibull distribution, Triangular distribution, Empirical continuous distributions.
- **Acceptance-Rejection Technique**: Bounded density functions, Generating Poisson variates, Non-homogeneous Poisson processes.
- **Direct Transformation**: Box-Muller transformation for Normal distribution.

### Module 5: Input Modeling & Verification/Validation
- **Input Modeling**: Data collection, Identifying probability distribution with histograms, Parameter estimation (Method of Moments, Maximum Likelihood Estimation - MLE).
- **Goodness-of-Fit Tests**: Chi-Square test, Kolmogorov-Smirnov test.
- **Verification & Validation (V&V)**: Verification (building the model right), Validation (building the right model), Calibration, Turing test for validation.

### Module 6: Output Data Analysis
- **Simulation Types**: Terminating (transient) vs Non-terminating (steady-state) simulations.
- **Techniques**: Warm-up period identification (Welch's method), Independent replications, Batch means method, Point estimates and Confidence intervals.

---

## 8. CSE-3210: Simulation and Modeling Lab (0.75 Credits)
- Discrete-event simulation implementation in Python/C++ / SimPy.
- Single-server queue and multi-server queue simulations.
- Monte Carlo simulations (e.g., estimation of \(\pi\), probabilistic area integration).
- Random number generator implementation (LCG) and statistical testing suites (Chi-Square, Runs test, K-S test).
- Inventory management simulation.

---

## 9. CSE-3212: Mobile Application Development Lab (1.5 Credits)
- **Android Architecture**: Linux kernel, HAL, Native libraries, Android Runtime (ART), Application Framework.
- **Activity & UI**: Activity lifecycle states and callbacks (`onCreate`, `onStart`, `onResume`, `onPause`, `onStop`, `onDestroy`, `onRestart`), Layouts (`LinearLayout`, `ConstraintLayout`, `RelativeLayout`), UI widgets (`TextView`, `EditText`, `Button`, `ImageView`, `RecyclerView`, `CardView`).
- **Navigation & Components**: Explicit & Implicit Intents, Passing Bundles, Fragments and Fragment lifecycle, Menus, Dialogs, Toasts, Snackbars.
- **Data Persistence**: `SharedPreferences`, Internal/External storage, SQLite databases, Room ORM.
- **Asynchronous & Networking**: Background threads, Coroutines, Services, BroadcastReceivers, WorkManager, REST API consumption with Retrofit/Volley, JSON deserialization.

