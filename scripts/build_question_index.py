#!/usr/bin/env python3
"""
Builder for .agents/skills/resources/question_index.json
Compiles all 68 questions with metadata, transcribed texts, extracted PDF texts,
and mapped syllabus topics into a fast queryable database.
"""

import os
import json
import subprocess
import re

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(WORKSPACE, ".agents", "skills", "resources", "question_index.json")

# Syllabus knowledge base
SYLLABUS = {
    "CSE-3201": {
        "Random Variables & Distributions": ["random variable", "discrete random variable", "continuous random variable", "pdf", "cdf", "sample variance", "unbiasedness", "expectation", "variance", "covariance"],
        "Stochastic Processes": ["stochastic process", "index set", "state space", "independent increment", "stationary process", "evolutionary process", "martingales", "second order process", "covariance function"],
        "Markov Chains": ["markov chain", "transition probability", "transition matrix", "chapman kolmogorov", "recurrent", "transient", "absorbing", "periodicity", "periodic", "ergodic", "first entrance decomposition"],
        "Continuous Time & Poisson Processes": ["continuous time markov chain", "pure birth process", "linear birth rate", "yule process", "death process", "poisson process"],
        "Queuing Theory": ["queuing theory", "queue", "m/m/1", "little's law", "service rate", "arrival rate", "traffic intensity"]
    },
    "CSE-3203": {
        "Finite Automata & Regular Languages": ["dfa", "nfa", "epsilon-nfa", "finite automata", "minimization", "table filling", "myhill nerode", "regular expression", "regex", "arden", "regular grammar"],
        "Pumping Lemma & Non-Regularity": ["pumping lemma", "adversary", "non-regular", "regular language closure"],
        "Context-Free Grammars & Normal Forms": ["context free grammar", "cfg", "derivation", "ambiguity", "chomsky normal form", "cnf", "greibach normal form", "gnf", "cyk"],
        "Pushdown Automata (PDA)": ["pushdown automata", "pda", "dpda", "empty stack", "final state", "instantaneous description"],
        "CFL Properties": ["pumping lemma for cfl", "closure properties of cfl"],
        "Turing Machines & Computability": ["turing machine", "multi-tape", "universal turing machine", "halting problem", "undecidable", "undecidability", "rice's theorem", "post correspondence problem", "pcp", "recursively enumerable"],
        "Chomsky Hierarchy": ["chomsky hierarchy", "type 0", "type 1", "type 2", "type 3", "context sensitive"]
    },
    "CSE-3205": {
        "Agents & Environments": ["intelligent agent", "rational agent", "peas", "environment types", "observable", "deterministic", "episodic"],
        "Uninformed Search": ["bfs", "breadth first search", "dfs", "depth first search", "depth limited search", "dls", "iterative deepening", "ids", "uniform cost search", "ucs"],
        "Heuristic Search": ["heuristic", "a* search", "greedy best first", "admissible", "admissibility", "consistent", "consistency", "ida*"],
        "Adversarial Search & Games": ["minimax", "alpha beta pruning", "game playing", "ply", "terminal state"],
        "Constraint Satisfaction Problems": ["constraint satisfaction", "csp", "backtracking", "arc consistency", "ac-3", "mrv", "forward checking"],
        "Knowledge & Logic": ["propositional logic", "first order logic", "fol", "resolution", "unification", "horn clauses", "forward chaining", "backward chaining"],
        "Probabilistic Reasoning & Learning": ["bayesian network", "conditional independence", "perceptron", "neural network", "machine learning"]
    },
    "CSE-3206": {
        "Search Implementation": ["bfs implementation", "dfs implementation", "a* implementation", "heuristic function"],
        "Prolog Programming": ["prolog", "facts", "rules", "queries", "recursion", "cut", "fail", "list processing"],
        "Game & CSP Solving": ["tic-tac-toe", "minimax coding", "n-queens", "map coloring"]
    },
    "CSE-3207": {
        "8086 Architecture & Interfacing": ["8086", "bus interface unit", "biu", "execution unit", "eu", "memory interfacing", "even bank", "odd bank", "address decoding", "74ls138", "io mapped", "memory mapped"],
        "8255 Programmable Peripheral Interface": ["8255", "ppi", "port a", "port b", "port c", "control word", "mode 0", "mode 1", "mode 2", "bsr mode", "7-segment", "stepper motor", "matrix keyboard"],
        "8254/8253 Programmable Interval Timer": ["8254", "8253", "pit", "control word", "counter", "frequency divider", "square wave", "modes 0 to 5"],
        "8259A Programmable Interrupt Controller": ["8259", "pic", "interrupt vector", "priority", "icw", "ocw", "cascading", "master", "slave"],
        "DMA Controller": ["8237", "8257", "dma", "direct memory access", "hold", "hlda", "transfer mode"],
        "Serial Communication & USART": ["8251", "usart", "rs-232", "baud rate", "asynchronous", "synchronous"],
        "Converters (ADC & DAC)": ["adc", "adc 0808", "adc 0809", "dac", "dac 0808", "successive approximation", "r-2r ladder"]
    },
    "CSE-3208": {
        "Assembly Interfacing Labs": ["assembly interfacing", "proteus", "trainer kit", "led interfacing", "stepper motor control", "dac waveform", "adc reading"]
    },
    "CSE-3209": {
        "Simulation Fundamentals": ["system", "system environment", "entity", "attribute", "activity", "state variables", "discrete event simulation", "continuous simulation", "steps in simulation"],
        "Simulation Worldviews & Queuing": ["event scheduling", "process interaction", "simulation clock", "event list", "single server queue", "m/m/1", "inventory system"],
        "Random Number Generation (RNG)": ["random number", "uniformity", "independence", "linear congruential", "lcg", "multiplicative congruential", "mixed congruential"],
        "Randomness Tests": ["frequency test", "kolmogorov smirnov", "k-s test", "chi-square", "runs test", "runs above and below", "runs up and down", "autocorrelation", "poker test", "gap test"],
        "Random Variate Generation": ["random variate", "inverse transform", "exponential distribution", "uniform distribution", "weibull", "acceptance rejection", "poisson variate", "direct transform"],
        "Verification, Validation & Output Analysis": ["verification", "validation", "input modeling", "goodness of fit", "terminating simulation", "non-terminating", "warm-up period", "replications", "confidence intervals"]
    },
    "CSE-3210": {
        "Simulation Coding & Models": ["simpy", "monte carlo", "queue simulation", "inventory model", "lcg code", "randomness test implementation"]
    },
    "CSE-3212": {
        "Android Core & Lifecycle": ["activity lifecycle", "oncreate", "onstart", "onresume", "onpause", "onstop", "ondestroy", "manifest", "androidmanifest"],
        "UI & Navigation": ["intent", "explicit intent", "implicit intent", "bundle", "layout", "linearlayout", "constraintlayout", "recyclerview", "cardview", "viewbinding", "adapter"],
        "Data Persistence": ["sharedpreferences", "sqlite", "room database", "internal storage"],
        "Background & Networking": ["services", "broadcast receiver", "workmanager", "asynctask", "retrofit", "volley", "rest api", "json"]
    }
}

def extract_pdf_text(pdf_abs_path):
    try:
        res = subprocess.run(["pdftotext", pdf_abs_path, "-"], capture_output=True, text=True, errors="ignore")
        txt = res.stdout.strip()
        return txt if len(txt) > 30 else ""
    except Exception:
        return ""

def load_git_transcriptions():
    cmd = ["git", "ls-tree", "-r", "ee6e3d9"]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    paths = [l.split()[-1] for l in res.stdout.strip().split("\n") if l.endswith(".md") and not l.endswith("README.md")]
    trans = {}
    for p in paths:
        content = subprocess.run(["git", "show", f"ee6e3d9:{p}"], capture_output=True, text=True, errors="ignore").stdout
        trans[p] = content
    return trans

def tag_topics(course_code, full_text):
    text_lower = full_text.lower()
    matched_topics = []
    course_syl = SYLLABUS.get(course_code, {})
    for topic_name, keywords in course_syl.items():
        found = False
        for kw in keywords:
            # Word boundary regex matching
            pattern = r'\b' + re.escape(kw) + r'\b'
            if re.search(pattern, text_lower):
                matched_topics.append({"topic": topic_name, "matched_keyword": kw})
                found = True
                break
    return matched_topics

def main():
    metadata_path = os.path.join(WORKSPACE, "metadata.json")
    with open(metadata_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    git_transcriptions = load_git_transcriptions()
    print(f"Loaded {len(git_transcriptions)} transcriptions from git history.")

    indexed_questions = []
    total_q = 0
    transcribed_count = 0
    extracted_count = 0

    for course in meta:
        ccode = course["code"]
        cname = course["name"]
        cdir = course["dir"]
        credits = course["credits"]

        for q in course["questions"]:
            total_q += 1
            qid = q["id"]
            session = q["session"]
            exam_type = q["exam_type"]
            teacher = q["teacher"]
            exam_date = q["exam_date"]
            category = q["category"]
            canonical = q["canonical_name"]
            rel_pdf = q["files"][0] if q["files"] else f"{category}/{canonical}.pdf"
            abs_pdf = os.path.join(WORKSPACE, cdir, rel_pdf)

            # Check transcription from git history
            git_md_rel = os.path.join(cdir, rel_pdf.replace(".pdf", ".md"))
            transcription = git_transcriptions.get(git_md_rel, "")
            has_trans = bool(transcription.strip())
            if has_trans:
                transcribed_count += 1

            # Check text extraction
            pdf_text = extract_pdf_text(abs_pdf)
            has_pdf_text = bool(pdf_text.strip())
            if has_pdf_text:
                extracted_count += 1

            combined_search_text = f"{ccode} {cname} {session} {exam_type} {teacher} {category} {transcription} {pdf_text}"
            matched_topics = tag_topics(ccode, combined_search_text)

            indexed_questions.append({
                "id": qid,
                "course_code": ccode,
                "course_name": cname,
                "credits": credits,
                "course_dir": cdir,
                "session": session,
                "exam_type": exam_type,
                "teacher": teacher,
                "exam_date": exam_date,
                "category": category,
                "canonical_name": canonical,
                "rel_pdf_path": os.path.join(cdir, rel_pdf),
                "abs_pdf_path": abs_pdf,
                "has_transcription": has_trans,
                "has_pdf_text": has_pdf_text,
                "transcription": transcription,
                "pdf_text": pdf_text,
                "topics": [m["topic"] for m in matched_topics],
                "topic_details": matched_topics
            })

    output_data = {
        "version": "1.0",
        "description": "Comprehensive index of 6th semester CSE exam questions, transcripts, and syllabus topics",
        "total_questions": total_q,
        "transcribed_questions": transcribed_count,
        "text_extracted_questions": extracted_count,
        "syllabus": SYLLABUS,
        "questions": indexed_questions
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)

    print(f"Indexed {total_q} questions successfully to {OUTPUT_PATH}.")
    print(f"Transcriptions linked: {transcribed_count}")
    print(f"Text-extracted PDFs: {extracted_count}")

if __name__ == "__main__":
    main()
