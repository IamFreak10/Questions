# CSE-3207: Peripherals & Interfacing — Mid-Term Preparation Guide (Session: 2022–2023)
### Core Focus: Keyboard, Mouse & Printer Only

> **Department of Computer Science and Engineering, University of Barishal**  
> **Course Code:** CSE-3207 &bull; **Course Title:** Peripherals and Interfacing &bull; **Credits:** 3.0  
> **Course Teacher / Primary Examiner:** Dr. Tania Islam  
> **Target Exam:** Mid-Term Examination (Session 2022–2023)  
> **Scope of Coverage:** Exclusively **Keyboard**, **Mouse / Pointing Devices**, and **Printer (Technologies & Interfacing)** from `lectures-for-mid/`  
> **Archive Source:** [Examinations Archive](./)

---

## 📑 Syllabus Outline Covered (`lectures-for-mid`)

```
                          CSE-3207 MID-TERM SCOPE
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         ▼                           ▼                           ▼
    1. KEYBOARD                  2. MOUSE                    3. PRINTER
  • Matrix Scanning           • Optical vs Mechanical     • Dot Matrix (Impact)
  • Debouncing & Scan Time    • DPI, Polling/Refresh Rate • Inkjet (Thermal/Piezo)
  • Switch Technologies       • Quadrature Encoding       • Laser (6 Electro Steps)
  • Make / Break Codes        • PS/2 & USB HID Packets    • Centronics Handshaking
  • Role Recommendations      • Sterile Medical Mice      • Publishing Recommendation
```

---

### 1. Input Device: Keyboard Architecture & Interfacing
- **Keyboard Working Mechanism:** Switch depression, contact closure, row-column scanning, coordinate resolution, scan code transmission.
- **Key Matrix Scanning & Detection:**
  - Row-by-Column grid array ($8 \times 16$ or $16 \times 8$).
  - Internal pull-up resistors holding input lines HIGH ($+5\text{V}$ / $+3.3\text{V}$).
  - Sequential active-LOW row grounding and column reading.
  - Coordinate resolution $(R_i, C_j)$ and Scan Time ($1\text{–}10\text{ ms}$).
- **Key Bouncing & Debouncing:**
  - Contact chatter duration ($5\text{–}20\text{ ms}$).
  - Hardware debouncing (RC filter, SR latch) vs. Software debouncing (timer delay validation).
- **Encoding & Scan Codes:** Make code on key depression, Break code on key release, ROM character lookup.
- **Switch Technologies:**
  - *Membrane Switch:* Three-layer flexible film (top conductive trace, insulating spacer with holes, bottom trace).
  - *Dome-Switch (Rubber Dome):* Silicone dome with carbon conductive puck, tactile springback.
  - *Scissor-Switch:* Low profile, mechanical stabilizing arms, short travel (laptops/compact).
  - *Mechanical Switch:* Individual spring and metal leaf switches (Cherry MX, ALPS), distinct tactile bump, N-Key Rollover (NKRO).
  - *Hall-Effect Switch:* Solid-state magnetic sensor detecting moving permanent magnet; contactless, 100% dustproof/waterproof, infinite endurance.
  - *Laser / Projection Keyboard:* Virtual optical projection with CMOS optical sensor + processing core.
- **Ergonomics & Health:** Repetitive Strain Injury (RSI), Carpal Tunnel Syndrome, split key layout, wrist rests, negative tilt.

---

### 2. Pointing Devices: Mouse Mechanics & Protocols
- **Mechanical / Ball Mouse:**
  - Rubber ball driving orthogonal X and Y roller shafts.
  - Slotted optical encoder disks interrupting IR LED beams.
  - Quadrature phase encoding ($90^\circ$ spatial offset) to resolve direction and count distance pulses.
- **Optical & Laser Mouse:**
  - Agilent/PixArt LED or coherent infrared laser diode illumination.
  - Microscopic CMOS image sensor array ($16\times 16$ to $30\times 30$ pixels).
  - High-speed DSP cross-correlating surface texture frames (1,500 to 6,000+ frames/sec) into displacement vectors $(\Delta X, \Delta Y)$.
- **Performance & Quality Metrics:**
  - *Resolution (DPI / CPI):* Counts per linear inch of physical movement.
  - *Polling Rate:* USB query frequency from host CPU (typically 125 Hz to 1000 Hz).
  - *Refresh Rate:* Sensor image acquisition speed (frames per second).
  - *DPI Adjustment:* Dynamic software/hardware scaling for high-resolution displays vs. high-precision tasks.
- **Data Packets Sent to CPU:**
  - Standard 3-byte PS/2 packet format:
    - `Byte 1:` Status (`Y-overflow`, `X-overflow`, `Y-sign`, `X-sign`, `1`, `Middle-Btn`, `Right-Btn`, `Left-Btn`).
    - `Byte 2:` 8-bit X-displacement $(\Delta X)$.
    - `Byte 3:` 8-bit Y-displacement $(\Delta Y)$.
- **Specialized & Hygienic Devices:** IP68 sealed washable medical silicone mice, contactless foot-pedal pointers, trackballs, gesture control.

---

### 3. Output Device: Printer Technologies & Interfacing
- **Impact vs. Non-Impact Classification:**
  - *Impact (Dot Matrix):* Solenoid-actuated pins (9-pin / 24-pin) striking inked ribbon; multi-part continuous carbon copy printing; Characters Per Second (CPS).
  - *Non-Impact:* Liquid Inkjet and Electrophotographic Laser.
- **Liquid Inkjet Printing:**
  - *Thermal Bubble-Jet:* Resistors flash-heat ink to $300\text{–}400^\circ\text{C}$, forming vapor bubbles that propel droplets through micro-nozzles.
  - *Piezoelectric:* Voltage applied to piezo crystal creates mechanical deflection, ejecting picoliter droplets without heat.
- **Laser Printing (6 Electrophotographic Steps):**
  1. *Charging:* Primary corona/roller places uniform negative electrostatic charge ($-600\text{V}$) on the OPC drum.
  2. *Exposing:* Rotating polygonal mirror sweeps laser beam across drum, discharging exposed areas to $-100\text{V}$ (latent electrostatic image).
  3. *Developing:* Toner particles (negatively charged) adhere to discharged laser areas on the drum.
  4. *Transferring:* High positive voltage beneath paper attracts negatively charged toner from drum to paper.
  5. *Fusing:* Heated rollers ($200^\circ\text{C}$) and pressure melt toner resin permanently into paper fibers.
  6. *Cleaning & Discharging:* Rubber wiper blade removes residual toner, erase lamp neutralizes surface charge.
- **Parallel Centronics Interface Handshake:**
  - `DATA [0..7]:` 8-bit parallel ASCII data.
  - `#STROBE:` Active-LOW pulse from CPU indicating valid data on the bus.
  - `BUSY:` Active-HIGH signal from printer indicating buffer full or printing in progress.
  - `#ACK:` Active-LOW pulse from printer confirming byte received and ready for next.
  - `PAPER OUT / PE:` Active-HIGH out-of-paper alarm.
  - `#ERROR / #FAULT:` Active-LOW signal for paper jam, offline, or cover open.
  - `#INIT:` Active-LOW CPU reset pulse to clear printer buffer.

---

## 🎯 Topic-by-Topic Historical Questions & Marks Analysis

---

### TOPIC 1: Keyboard Interfacing & Switch Technologies

* **"Describe how a keyboard is interfaced with a computer. Mention at least two types of keyboards (e.g., membrane, mechanical) and their basic principle difference. Explain the steps from pressing a key to the CPU receiving the data."**
  * **Marks:** 7 Marks &mdash; [2021-2022 Mid-I: Q1(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2021-2022_1st_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Describe the working principle of a keyboard. Explain how a key press is detected using the keyboard matrix concept."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q2(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"Compare membrane, mechanical, and wireless keyboards. Discuss advantages, disadvantages, and applications."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q2(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"A software company has programmers, graphic designers, and data-entry operators. Recommend suitable keyboards for each and justify your answer."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q2(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"What is keyboard interfacing. What is scanning in keyboard and what is scan time?"**
  * **Marks:** 5 Marks &mdash; [2019-2020 Mid-I: Q1](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2019-2020_1st_Mid.pdf#page=1)
* **". What is Key bouncing? How a keyboard matrix is formed in keyboard interface ?"**
  * **Marks:** 5 Marks &mdash; [2019-2020 Mid-I: Q2](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2019-2020_1st_Mid.pdf#page=1)
* **"Draw and Define the membrane keyboard layers."**
  * **Marks:** 4 Marks &mdash; [2018-2019 Mid-I: Q1](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2018-2019_1st_Mid.pdf#page=1)
* **"Write short notes on the Hall effect keyboard."**
  * **Marks:** 4 Marks &mdash; [2018-2019 Final: Q8(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q8(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q1(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2017-2018_Final.pdf#page=1)
  * **Marks:** 2 Marks &mdash; [2016-2017 Final: Q6(d)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2016-2017_Final.pdf#page=1)
* **"Write down the difference between laser keyboard and dome switch keyboard"**
  * **Marks:** 4 Marks &mdash; [2018-2019 Final: Q8(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q8(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
* **"Discuss the impact of proper keyboard ergonomics on user productivity and health. What are some key ergonomic tips for reducing strain when using a keyboard for long periodspp?"**
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q8(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)

---

### TOPIC 2: Mouse / Pointing Devices & Motion Detection

* **"Describe how a mouse is connected to a computer system. Mention at least two types of mice (e.g., optical, mechanical/ball) and the principle of how they detect movement. Explain what types of data the mouse sends to the CPU."**
  * **Marks:** 6 Marks &mdash; [2021-2022 Mid-I: Q1(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2021-2022_1st_Mid_Dr_Tania_Islam.pdf#page=1)
* **"Explain the working principle of an optical mouse. How does it detect movement compared with a mechanical mouse?"**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q3(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"Differentiate among laser, optical, and wireless mice in terms of accuracy, power consumption, cost, and applications."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q3(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"A hospital wants computers in operating rooms where hygiene is important. Recommend suitable pointing devices and justify your answer."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"What do you mean by the accuracy of an optical mouse? Describe the factors that affect the quality of an optical mouse."**
  * **Marks:** 5 Marks &mdash; [2018-2019 Final: Q3(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2019-2020 Mid-I: Q3](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2019-2020_1st_Mid.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q3(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
* **"Write short notes on: i. Polling rate ii. Refresh rate"**
  * **Marks:** 4 Marks &mdash; [2018-2019 Final: Q3(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 5 Marks &mdash; [2019-2020 Mid-I: Q4](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2019-2020_1st_Mid.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q3(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
* **"Can a mouse's sensitivity (DPI) be adjusted, and why might someone want to change it?"**
  * **Marks:** 3 Marks &mdash; [2018-2019 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2019-2020 Final: Q3(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2019-2020_Final_Dr_Tania_Islam.pdf#page=1)
* **"Write down the benefits and the limitations of optical mice over mechanical mice."**
  * **Marks:** 4 Marks &mdash; [2018-2019 Mid-I: Q4](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2018-2019_1st_Mid.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q2(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2017-2018_Final.pdf#page=1)

---

### TOPIC 3: Printer Technologies & Interfacing

* **"Explain the working principles of Inkjet Printer and Laser Printer with neat diagrams."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q4(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"Compare Inkjet, Laser, and Dot Matrix printers using printing speed, print quality, cost per page, maintenance, and applications."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q4(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"Recommend a printer for a publishing company that prints thousands of pages daily. Justify your answer."**
  * **Marks:** 4 Marks &mdash; [2021-2022 Final: Q4(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf#page=1)
* **"Write down the functions of the printer."**
  * **Marks:** 5 Marks &mdash; [2018-2019 Mid-II: Q1](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2018-2019_2nd_Mid.pdf#page=1)
* **"Describe the types of the printer and the differences among them"**
  * **Marks:** 5 Marks &mdash; [2018-2019 Mid-II: Q2](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Midterm/2018-2019_2nd_Mid.pdf#page=1)
* **"Describe the functions of the signals BUSY, PAPER, #ERROR, #INI and #STR of the parallel printer."**
  * **Marks:** 5 Marks &mdash; [2018-2019 Final: Q5(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
* **"Define printer. What are the basic technologies of Printer?"**
  * **Marks:** 4 Marks &mdash; [2018-2019 Final: Q7(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q7(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2017-2018_Final.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2016-2017 Final: Q8(a)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2016-2017_Final.pdf#page=1)
* **"Briefly explain the inkjet printer printing process."**
  * **Marks:** 4 Marks &mdash; [2018-2019 Final: Q7(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)
  * **Marks:** 3 Marks &mdash; [2017-2018 Final: Q7(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2017-2018_Final.pdf#page=1)
  * **Marks:** 4 Marks &mdash; [2016-2017 Final: Q8(b)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2016-2017_Final.pdf#page=1)
* **"Why Laser printer is so popular over other printers?"**
  * **Marks:** 4 Marks &mdash; [2018-2019 Final: Q7(c)](file:///home/iamfreak/Downloads/6th/Questions/05_CSE-3207_Peripherals_and_Interfacing/Final/2018-2019_Final_Dr_Tania_Islam.pdf#page=1)

---

## ⚖️ Pinpoint Analysis: The Real Engineering Trade-Offs (Modern Trend)

Dr. Tania Islam's recent exam papers place heavy emphasis on **real engineering trade-offs and recommendations**. The examiner expects structured tabular comparisons followed by technical justification.

---

### Trade-Off 1: Keyboard Switch Selection by User Profile
* **Software Programmers:** **Mechanical Keyboard (Tactile MX Brown/Blue)**.
  - *Engineering Reason:* High actuation point prevents finger fatigue from bottoming out; N-Key Rollover (NKRO) prevents missing simultaneous key combinations; rated for 50–100 million keystrokes.
* **Graphic Designers:** **Low-Profile Scissor-Switch Keyboard**.
  - *Engineering Reason:* Ultra-short travel distance allows fast single-handed shortcut execution; low physical profile allows seamless, fatigue-free hand movement between keyboard and digitizing tablet.
* **Data-Entry Operators:** **Membrane Keyboard with Dedicated Numpad**.
  - *Engineering Reason:* Soft actuation reduces repetitive strain during high-volume numeric entry; sealed membrane structure protects against liquid spills in open office environments.

---

### Trade-Off 2: Pointing Device Selection in Sterile Operating Rooms
* **Mechanical Ball Mice:** Disqualified immediately. Roller shafts accumulate skin oils, dust, and biological debris. Cannot be chemically disinfected.
* **Standard Optical Mice:** Disqualified due to seams, crevices, and scroll wheel apertures that trap blood, pathogens, and bacteria.
* **Engineering Recommendation:** **Touchless Eye/Head-Tracking Camera Mouse or Hermetically Sealed IP68 Medical Silicone Optical Mouse / Touchpad**.
  - *Engineering Reason:* Touchless pointers eliminate physical contact, preserving sterile scrub integrity when surgeons view CT/MRI scans. Sealed IP68 medical mice can be submerged in hospital sterilizing solutions (bleach/isopropyl alcohol) without liquid ingress.

---

### Trade-Off 3: Printer Selection for High-Volume Publishing
* **Dot Matrix:** Extremely low page cost ($\approx \$0.002$), but print speed (CPS) is far too slow and mechanical pin noise is unacceptable for office publishing.
* **Liquid Inkjet:** High resolution, but cost per page is astronomical ($\approx \$0.10\text{–}\$0.20$), wet ink bleeds on cheap paper, and print heads clog during heavy duty cycles.
* **Engineering Recommendation:** **Commercial High-Duty Laser Printer / Digital Press**.
  - *Engineering Reason:* 40–100+ PPM throughput; dry polymer toner fuses into paper fibers via heated rollers ($200^\circ\text{C}$), producing instantly dry, smudge-proof, waterproof text at $\approx \$0.01\text{–}\$0.02$ per page.

---

## 🔬 The Canonical 7-Step Pipeline: Key Press to CPU Data Reception

Candidates must reproduce this complete physical-to-logical sequence:

```
[1. Switch Actuation]  --> Finger depresses keycap; flexible dome collapses; conductive contact bridges circuit.
          │
          ▼
[2. Matrix Intersect]  --> Row line i is electrically connected to Column line j.
          │
          ▼
[3. Matrix Scanning]   --> Onboard microcontroller pulses Rows with logic LOW (0) sequentially; reads Columns.
          │
          ▼
[4. Debounce Delay]    --> Microcontroller runs 5-10 ms debounce timer to filter mechanical contact chatter.
          │
          ▼
[5. Make Code Lookup]  --> Coordinate (R_i, C_j) is matched against ROM Character Map to produce Scan Code.
          │
          ▼
[6. Serial Framing]    --> Scan code is framed and transmitted over PS/2 clock/data or USB HID Interrupt Endpoint.
          │
          ▼
[7. CPU Interrupt]     --> Host controller asserts IRQ 1 (PIC) / Message Signaled Interrupt; OS driver reads port 60h.
```

---

## 🖨️ The 6-Step Electrophotographic Laser Printing Process

```
[1. Charge]   Primary corona roller places uniform negative charge (-600V) on rotating OPC drum.
     │
     ▼
[2. Expose]   Laser beam reflected by rotating polygon mirror discharges drum to -100V (latent image).
     │
     ▼
[3. Develop]  Magnetic roller attracts negatively charged toner particles to discharged (-100V) drum areas.
     │
     ▼
[4. Transfer] High positive transfer roller beneath paper pulls negatively charged toner onto paper surface.
     │
     ▼
[5. Fuse]     Teflon heat roller (200°C) and pressure roller melt toner polymer resin permanently into paper.
     │
     ▼
[6. Clean]    Rubber wiper blade scrapes residual toner into waste hopper; discharge lamp clears electrostatic charge.
```

---

## 🔁 Master Repeated Questions Matrix (Quick Exam Hit-List)

| Repeated Topic | Exact Prompts | Frequency | Total Marks |
| :--- | :--- | :---: | :---: |
| **Optical Mouse Accuracy & Quality Factors** | *"What do you mean by the accuracy of an optical mouse? Describe the factors that affect the quality of an optical mouse."* | **3 Times** (2018-19 Final, 2019-20 Mid-I, 2019-20 Final) | **14 Marks** |
| **Polling Rate vs Refresh Rate** | *"Write short notes on: i. Polling rate ii. Refresh rate"* | **3 Times** (2018-19 Final, 2019-20 Mid-I, 2019-20 Final) | **13 Marks** |
| **Hall Effect Keyboard** | *"Write short notes on the Hall effect keyboard" / "What is hall effect keyboard & working principle"* | **4 Times** (2016-17 Final, 2017-18 Final, 2018-19 Final, 2019-20 Final) | **13 Marks** |
| **Inkjet Printing Process** | *"Briefly explain the inkjet printer printing process."* | **3 Times** (2016-17 Final, 2017-18 Final, 2018-19 Final) | **11 Marks** |
| **Mouse Sensitivity (DPI)** | *"Can a mouse's sensitivity (DPI) be adjusted, and why might someone want to change it?"* | **2 Times** (2018-19 Final, 2019-20 Final) | **7 Marks** |
| **Membrane vs Mechanical vs Wireless** | *"Compare membrane, mechanical, and wireless keyboards"* | **2 Times** (2018-19 Mid-I, 2021-22 Final) | **8 Marks** |

---
*Maintained for academic revision and exam preparation &bull; Department of Computer Science and Engineering, University of Barishal.*
