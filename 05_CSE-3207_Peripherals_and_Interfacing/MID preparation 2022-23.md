# CSE-3207: Peripherals & Interfacing — Mid-Term Preparation Guide (Session: 2022–2023)

> **Department of Computer Science and Engineering, University of Barishal**  
> **Course Code:** CSE-3207 &bull; **Course Title:** Peripherals and Interfacing &bull; **Credits:** 3.0  
> **Course Teacher / Primary Examiner:** Dr. Tania Islam  
> **Target Exam:** Mid-Term Examination (Session 2022–2023)  
> **Coverage Scope:** Topics from `lectures-for-mid/` (**Interfacing Fundamentals**, **Keyboard**, **Mouse**, **Printer**)  
> **Archive Source:** [Examinations Archive](./)

---

## 📑 Syllabus Outline Covered (`lectures-for-mid`)

### 1. Peripheral & Interfacing Fundamentals
- **Peripheral Device Definition:** Auxiliary hardware used to put information into and get information out of a computer; optional nature vs. demanded core hardware.
- **Classification of Peripherals:** Input (Keyboard, Mouse, Touch Screen, Scanner, Barcode Reader), Output (CRT, LCD, Plasma, Printer, Plotter, Speaker), Storage (Magnetic Disk, CD/DVD, Flash memory), Communication/Other (Modem, Display adapter, Sound card).
- **Online vs. Offline Peripherals:** Direct autonomous CPU bus coupling vs. independent batch peripheral operation.
- **The Need for Peripheral Interface Circuits:**
  - *Speed Mismatch:* Nanosecond CPU cycle times vs. millisecond human/mechanical responses.
  - *Voltage & Signal Level Mismatch:* 1.2V–3.3V LVCMOS vs. ±12V RS-232, 5V differential USB, 24V solenoids.
  - *Data Format Mismatch:* Synchronous 32/64-bit parallel system bus vs. asynchronous serial bitstreams/analog pulses.
- **I/O Addressing Schemes:** Memory-Mapped I/O vs. Isolated / Port-Mapped I/O.
- **Data Transfer Mechanisms:** Polling / Programmed I/O vs. Interrupt-Driven I/O vs. Direct Memory Access (DMA).

### 2. Input Device: Keyboard Architecture & Interfacing
- **Keyboard Working Mechanism:** Switch depression, rubber dome collapse, matrix grid contact closure, microcontroller scanning.
- **Key Matrix Scanning & Detection:** Row-by-Column grid array, pull-up resistors, sequential active-LOW row pulsing, column read, coordinate resolution $(R_i, C_j)$, scan time ($1\text{–}10\text{ ms}$).
- **Key Bouncing & Debouncing:** Mechanical leaf/contact vibration and chatter, hardware/software debouncing delays ($5\text{–}10\text{ ms}$).
- **Encoding & Character Maps:** Make code generation on depression, Break code generation on release, ROM character lookup tables.
- **Switch Technologies:**
  - *Dome-Switch (Rubber Dome):* Plunger, carbon center contact, quiet, cheap, good tactile feel.
  - *Scissor-Switch:* Low profile, mechanical scissor guide arms, crisp, quiet, short travel (laptops).
  - *Capacitive Switch:* Non-mechanical continuous AC/DC charge, moving plate alters capacitance, zero bounce, ultra-long life.
  - *Mechanical Switch:* Individual spring and metal contact leaf switches (Cherry MX, ALPS), distinct tactile bump/click, N-Key Rollover (NKRO).
  - *Hall-Effect Switch:* Solid-state magnetic sensor detecting moving permanent magnet; contactless, 100% dustproof/waterproof, infinite endurance.
  - *Laser / Projection Keyboard:* Virtual optical projection, CMOS sensor + Virtual Interface Processing Core, zero tactile feedback.
  - *Membrane Keyboard:* Three-layer construction (top conductive trace, center spacer with holes, bottom trace).
- **Connection Interfaces:** AT (DIN-5), PS/2 (6-pin Mini-DIN), USB HID, Wireless (RF 2.4 GHz, Bluetooth spread-spectrum frequency hopping, Infrared).

### 3. Pointing Devices: Mouse Mechanics & Protocols
- **Historical Evolution:** Douglas Engelbart (1964/1968 wooden mouse), Xerox PARC, Apple Macintosh (1984), Microsoft GUI.
- **Mechanical / Optomechanical Mouse:**
  - Rubber ball driving perpendicular X and Y roller shafts.
  - Slotted optical encoder disks rotating between IR LED and phototransistor pairs.
  - Quadrature phase encoding: $90^\circ$ spatial/angular offset between two detector windows to decode direction (clockwise vs. counter-clockwise) and count velocity pulses.
- **Optical & Laser Mouse:**
  - Agilent LED + CMOS optical sensor array ($16\times 16$ to $30\times 30$ pixels).
  - High-speed digital signal processor (DSP) calculating microscopic surface cross-correlation displacement vectors (1,500 to 6,000 frames/sec).
  - Laser mice using infrared coherent laser diode for microscopic surface penetration (functional on glass/gloss).
- **Performance & Quality Metrics:**
  - *Resolution (DPI / CPI):* Dots per inch, sensor sampling density (400–16,000+ DPI).
  - *Refresh Rate:* Optical camera image capture rate (samples/sec).
  - *Polling Rate:* Host USB controller query frequency (Hz, typically 125 Hz to 1000 Hz).
  - *Image Processing Rate:* Megapixels/sec ($\text{Sensor Area} \times \text{Refresh Rate}$).
- **Communication Protocols:**
  - *Serial RS-232C:* DB-9 connector, Mouse Systems 5-byte vs. Microsoft 3-byte protocol.
  - *PS/2 Protocol:* 3-byte streaming packet format (`Byte 1: YV XV YS XS 1 MB RB LB`, `Byte 2: X-displacement`, `Byte 3: Y-displacement`).
- **Specialized & Alternative Pointing Devices:** Trackball, Touchpad, Pointing Stick (TrackPoint), Touchscreen, Head/Camera Mouse, Eyeball-controlled pointer, Biometric Fingerprint Mouse, Gyroscopic (In-Air / Coriolis Effect) Mouse.

### 4. Output Device: Printer Technologies & Interfacing
- **Impact vs. Non-Impact Classification:**
  - *Impact Printers:* Mechanical strike against inked fabric ribbon; capability to produce multi-part carbon copies.
    - *Dot Matrix:* Solenoid-actuated pins/wires (9-pin / 24-pin), print head moving across continuous tractor-feed paper, measurement in Characters Per Second (CPS).
    - *Character Printers:* Typewriters, Daisy wheel, embossed character drums/chains.
  - *Non-Impact Printers:* Electrostatic, thermal, or fluid projection without mechanical impact.
    - *Liquid Inkjet / Bubble Jet:* Thermal bubble vaporization (resistors heating ink to $300\text{–}400^\circ\text{C}$ creating vapor bubbles) and Piezoelectric crystal vibration; microscopic picoliter droplets; stepper motors driving print carriage and platen roller.
    - *Laser Printer (Electrophotographic):* Rotating polygonal mirror, semiconductor laser assembly, organic photoconductive (OPC) drum, electrostatic charge corona/roller, toner composition (pigment + polymer resin), magnetic developer roller, heated fuser rollers ($200^\circ\text{C}$ heat + pressure).
- **Parallel Centronics Interface Signals:** `DATA [0..7]`, `#STROBE`, `BUSY`, `ACK`, `PAPER OUT`, `SELECT`, `#ERROR`, `#INIT`.

---

## 🎯 Topic-by-Topic Historical Questions & Marks Analysis (2020–21 & 2021–22)

---

### TOPIC 1: Peripheral & Interfacing Architecture

* **"Explain the need for a peripheral interface in a computer system. Draw a block diagram showing a CPU connected to multiple peripherals through an I/O interface. Describe the basic functions of the interface. Give one advantage of using an interface instead of direct connection."**
  * **Marks:** 7 Marks &mdash; [2021-2022 Mid-I: Q1(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2021-2022_1st_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Explain why peripherals cannot be directly connected to a microprocessor. Describe how an interface unit helps in matching speed, data format, and voltage levels between the CPU and external devices. Give one simple example."**
  * **Marks:** 5 Marks &mdash; [2020-2021 Final: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2020-2021_Final_Dr_Tania_Islam.pdf#page=1)
* **"What is Interface? Briefly explain different types of Interfaces. Differentiate between off-line and on-line peripherals."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q1(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"What do you mean by Computer peripheral? List down the input and output Peripherals."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"A university plans to build a modern computer laboratory. Recommend suitable peripheral devices for student programming, online classes, multimedia presentations, and document digitization. Justify your choices."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q1(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"What is an interrupt? Explain how it helps in interfacing peripherals with a microprocessor."**
  * **Marks:** 4 Marks &mdash; [2020-2021 Final: Q8(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2020-2021_Final_Dr_Tania_Islam.pdf#page=2)

---

### TOPIC 2: Keyboard Interfacing & Switch Technologies

* **"Describe how a keyboard is interfaced with a computer. Mention at least two types of keyboards (e.g., membrane, mechanical) and their basic principle difference. Explain the steps from pressing a key to the CPU receiving the data."**
  * **Marks:** 7 Marks &mdash; [2021-2022 Mid-I: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2021-2022_1st_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Describe the working principle of a keyboard. Explain how a key press is detected using the keyboard matrix concept."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"Compare membrane, mechanical, and wireless keyboards. Discuss advantages, disadvantages, and applications."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q2(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"A software company has programmers, graphic designers, and data-entry operators. Recommend suitable keyboards for each and justify your answer."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q2(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)

---

### TOPIC 3: Mouse / Pointing Devices & Motion Detection

* **"Describe how a mouse is connected to a computer system. Mention at least two types of mice (e.g., optical, mechanical/ball) and the principle of how they detect movement. Explain what types of data the mouse sends to the CPU."**
  * **Marks:** 6 Marks &mdash; [2021-2022 Mid-I: Q1(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2021-2022_1st_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Explain the working principle of an optical mouse. How does it detect movement compared with a mechanical mouse?"**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q3(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"Differentiate among laser, optical, and wireless mice in terms of accuracy, power consumption, cost, and applications."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q3(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"A hospital wants computers in operating rooms where hygiene is important. Recommend suitable pointing devices and justify your answer."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)

---

### TOPIC 4: Printer Technologies & Interfacing

* **"Explain the working principles of Inkjet Printer and Laser Printer with neat diagrams."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q4(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"Compare Inkjet, Laser, and Dot Matrix printers using printing speed, print quality, cost per page, maintenance, and applications."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q4(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"Recommend a printer for a publishing company that prints thousands of pages daily. Justify your answer."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q4(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)

---

## ⚖️ Pinpoint Analysis: The Real Engineering Trade-Offs ("Trade Issues")

Dr. Tania Islam's recent exam papers place heavy emphasis on **real engineering trade-offs**. The examiner expects structured tabular comparisons followed by technical justification.

### Trade-Off 1: Direct CPU Bus vs. I/O Interface
- **Speed Mismatch:** Nanosecond CPU cycle times ($\approx 0.3\text{ ns}$) vs. millisecond peripheral times ($10\text{–}100\text{ ms}$). Direct wiring halts CPU execution.
- **Voltage Incompatibility:** 1.2V–3.3V LVCMOS CPU silicon vs. ±12V RS-232, 5V USB, 24V printer solenoids. Direct connection burns out the microprocessor.
- **Protocol Mismatch:** Synchronous parallel CPU words vs. asynchronous serial bitstreams/analog signals.
- **Engineering Verdict:** The I/O interface decouples the CPU from peripheral physical layers through status/control registers, FIFO buffering, and interrupt management.

---

### Trade-Off 2: Keyboard Switch Selection by User Profile
* **Software Programmers:** **Mechanical Keyboard (Tactile MX Brown/Blue)**.
  - *Engineering Reason:* High actuation point prevents finger fatigue from bottoming out; N-Key Rollover (NKRO) prevents missing simultaneous key combinations; rated for 50–100 million keystrokes.
* **Graphic Designers:** **Low-Profile Scissor-Switch Keyboard**.
  - *Engineering Reason:* Ultra-short travel distance allows fast single-handed shortcut execution; low physical profile allows seamless, fatigue-free hand movement between keyboard and digitizing tablet.
* **Data-Entry Operators:** **Membrane Keyboard with Dedicated Numpad**.
  - *Engineering Reason:* Soft actuation reduces repetitive strain during high-volume numeric entry; sealed membrane structure protects against liquid spills in open office environments.

---

### Trade-Off 3: Pointing Device Selection in Sterile Operating Rooms
* **Mechanical Ball Mice:** Disqualified immediately. Roller shafts accumulate skin oils, dust, and biological debris. Cannot be chemically disinfected.
* **Standard Optical Mice:** Disqualified due to seams, crevices, and scroll wheel apertures that trap blood, pathogens, and bacteria.
* **Engineering Recommendation:** **Touchless Eye/Head-Tracking Camera Mouse or Hermetically Sealed IP68 Medical Silicone Optical Mouse / Touchpad**.
  - *Engineering Reason:* Touchless pointers eliminate physical contact, preserving sterile scrub integrity when surgeons view CT/MRI scans. Sealed IP68 medical mice can be submerged in hospital sterilizing solutions (bleach/isopropyl alcohol) without liquid ingress.

---

### Trade-Off 4: Printer Selection for High-Volume Publishing
* **Dot Matrix:** Extremely low page cost ($\approx \$0.002$), but print speed (CPS) is far too slow and mechanical pin noise is unacceptable for office publishing.
* **Liquid Inkjet:** High resolution, but cost per page is astronomical ($\approx \$0.10\text{–}\$0.20$), wet ink bleeds on cheap paper, and print heads clog during heavy duty cycles.
* **Engineering Recommendation:** **Commercial High-Duty Laser Printer / Digital Press**.
  - *Engineering Reason:* 40–100+ PPM throughput; dry polymer toner fuses into paper fibers via heated rollers ($200^\circ\text{C}$), producing instantly dry, smudge-proof, waterproof text at $\approx \$0.01\text{–}\$0.02$ per page.

---

## 🔬 The Canonical 7-Step Pipeline: Key Press to CPU Data Reception

Candidates must reproduce this complete physical-to-logical sequence:

```
[1. Switch Actuation]  --> Finger depresses keycap; flexible dome collapses; conductive contact bridges circuit.
          |
[2. Matrix Intersect]  --> Row line i is electrically connected to Column line j.
          |
[3. Matrix Scanning]   --> Onboard microcontroller pulses Rows with logic LOW (0) sequentially; reads Columns.
          |
[4. Debounce Delay]    --> Microcontroller runs 5-10 ms debounce timer to filter mechanical contact chatter.
          |
[5. Make Code Lookup]  --> Coordinate (R_i, C_j) is matched against ROM Character Map to produce Scan Code.
          |
[6. Serial Framing]    --> Scan code is framed and transmitted over PS/2 clock/data or USB HID Interrupt Endpoint.
          |
[7. CPU Interrupt]     --> Host controller asserts IRQ 1 (PIC) / Message Signaled Interrupt; OS driver reads port 60h.
```

---

## 📜 Historical Question Matrix: Sessions 2018–2019 & 2019–2020

### Session 2018–2019
* **Mid Term-I (2018–19):**
  * **Q1:** *Draw and Define the membrane keyboard layers.* [4 Marks] &mdash; [Mid Term-I: Q1](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2018-2019_1st_Mid.pdf#page=1)
  * **Q4:** *Write down the benefits and the limitations of optical mice over mechanical mice.* [4 Marks] &mdash; [Mid Term-I: Q4](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2018-2019_1st_Mid.pdf#page=1)
* **Mid Term-II (2018–19):**
  * **Q1:** *Write down the functions of the printer.* [5 Marks] &mdash; [Mid Term-II: Q1](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2018-2019_2nd_Mid.pdf#page=1)
  * **Q2:** *Describe the types of the printer and the differences among them.* [5 Marks] &mdash; [Mid Term-II: Q2](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2018-2019_2nd_Mid.pdf#page=1)
* **Final Exam (2018–19):**
  * **Q3 (a):** *Optical mouse accuracy and quality factors.* [5 Marks] &mdash; [Final: Q3(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
  * **Q3 (b):** *Short notes on Polling rate and Refresh rate.* [4 Marks] &mdash; [Final: Q3(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
  * **Q3 (c):** *Mouse sensitivity (DPI) adjustment.* [3 Marks] &mdash; [Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
  * **Q5 (c):** *Parallel printer Centronics signals (BUSY, PAPER, #ERROR, #INI, #STR).* [5 Marks] &mdash; [Final: Q5(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
  * **Q7 (a), (b), (c):** *Printer technologies, Inkjet process, Laser printer advantages.* [4 + 4 + 4 Marks] &mdash; [Final: Q7](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
  * **Q8 (a), (b), (c):** *Hall effect keyboard, Laser vs Dome switch, Hall effect principle.* [4 + 4 + 4 Marks] &mdash; [Final: Q8](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)

### Session 2019–2020
* **Mid Term-I (2019–20):**
  * **Q1:** *Keyboard interfacing, scanning, and scan time.* [5 Marks] &mdash; [Mid Term-I: Q1](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2019-2020_1st_Mid.pdf#page=1)
  * **Q2:** *Key bouncing and keyboard matrix formation.* [5 Marks] &mdash; [Mid Term-I: Q2](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2019-2020_1st_Mid.pdf#page=1)
  * **Q3:** *Optical mouse accuracy and factors.* [5 Marks] &mdash; [Mid Term-I: Q3](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2019-2020_1st_Mid.pdf#page=1)
  * **Q4:** *Polling rate vs Refresh rate.* [5 Marks] &mdash; [Mid Term-I: Q4](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2019-2020_1st_Mid.pdf#page=1)
* **Final Exam (2019–20):**
  * **Q3 (a), (b), (c):** *Optical mouse accuracy, polling/refresh rate, DPI adjustment.* [4 + 4 + 4 Marks] &mdash; [Final: Q3](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
  * **Q8 (a), (b), (c):** *Hall effect keyboard, Laser vs Dome keyboard, Keyboard ergonomics & health.* [4 + 4 + 4 Marks] &mdash; [Final: Q8](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)

---
*Maintained for academic revision and exam preparation &bull; Department of Computer Science and Engineering, University of Barishal.*
