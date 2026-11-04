# Sample Question Analysis Report
### Course: CSE-3207 — Peripherals and Interfacing

*This document illustrates the expected format and depth when an AI agent generates an exam analysis report for a user.*

---

## 📌 Executive Summary
- **Course**: CSE-3207: Peripherals and Interfacing (3.0 Credits)
- **Exam Archive**: 12 Papers (6 Semester Finals, 6 Midterms)
- **Primary Instructor**: Dr. Tania Islam
- **Target Final Exam**: 60 Marks (Answer 5 out of 8 questions, 12 marks each)

---

## 📈 Topic Frequency Breakdown (Semester Finals)

| Topic / Module | Appearances in Finals | Frequency Rate | Typical Subquestion Type |
| :--- | :---: | :---: | :--- |
| **8255 PPI (Modes 0, 1, 2, BSR)** | 6 / 6 | **100%** | Control word calculation, block diagram, handshaking signals |
| **8086 Memory Interfacing** | 5 / 6 | **83.3%** | Even/Odd bank design, 74LS138 decoder, address map |
| **8254/8253 PIT** | 5 / 6 | **83.3%** | Modes of operation, counter initialization, square wave generation |
| **8259A PIC** | 4 / 6 | **66.7%** | Interrupt Vector Table (IVT), ICW/OCW, Master-Slave cascading |
| **DMA Controller (8237/8257)** | 4 / 6 | **66.7%** | HOLD/HLDA handshaking, cycle stealing vs burst transfer |
| **Converters (ADC 0808 / DAC 0808)** | 3 / 6 | **50.0%** | Successive approximation, R-2R ladder circuit, interfacing |
| **Serial Communication (8251A USART)** | 3 / 6 | **50.0%** | Asynchronous vs synchronous framing, baud rate generator |

---

## 🎯 High-Yield Revision Strategy (Targeting 50+ / 60 Marks)

### Tier 1: Guaranteed Core (Answer 3 Full Questions)
1. **8255 PPI**: Master the 8-bit Control Word format for I/O and BSR mode. Prepare interfacing diagrams for Stepper Motor and 7-Segment display.
2. **8086 Memory Interfacing**: Practice designing a memory system with specific RAM/ROM chip capacities (e.g. 64KB RAM using 8KB chips) using 74LS138 decoder and \(\overline{\text{BHE}}/A_0\).
3. **8254 PIT**: Understand Modes 0 through 5. Focus on Mode 2 (Rate Generator) and Mode 3 (Square Wave).

### Tier 2: High Probability (Answer Remaining 2 Questions)
4. **8259A PIC**: Memorize the IVT memory map (00000H to 003FFH) and the sequence of ICWs for cascading.
5. **DMA 8237**: Explain the transfer sequence between peripheral, DMA controller, and 8086 CPU.

---

## 📄 Relevant Question Papers
- `05_CSE-3207_Peripherals_and_Interfacing/Final/2021-2022_Final_Dr_Tania_Islam.pdf`
- `05_CSE-3207_Peripherals_and_Interfacing/Final/2020-2021_Final_Dr_Tania_Islam.pdf`
- `05_CSE-3207_Peripherals_and_Interfacing/Final/2019-2020_Final_Dr_Tania_Islam.pdf`

