#  Python Detective

Python Detective is a Python-based case investigation system that helps manage suspects, evidence, and investigation scores.

The project simulates a detective investigation where evidence is assigned points to suspects, and the system calculates which suspect has the highest evidence score.

##  Features

-  Register a new case
-  View suspects
-  Add new suspects
-  View evidence
-  Add new evidence
-  Calculate investigation scores
-  Identify the most likely suspect
-  Generate an investigation report
-  Save investigation results to a text file

## Python Concepts Used

- Variables
- Input and Output
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Exception Handling
- File Handling
- Dictionary operations
- `max()` function

##  How the Investigation Works

The Python Detective system analyzes the evidence collected during an investigation and assigns points to each suspect.

Each piece of evidence is linked to a suspect and given a specific number of points. The program then adds all the evidence points for each suspect to calculate their total investigation score.

The suspect with the highest score is identified as the **Most Likely Suspect**.

The system also determines the suspicion level based on the highest evidence score:

- **100+ points** → High Suspicion
- **50–99 points** → Moderate Suspicion
- **Below 50 points** → Low Suspicion

 ## Project Structure

```text
Python-Detective/
│
├── detective.py
├── investigation_report.txt
└── README.md


## Future Improvements

- Some features that can be added in future versions:

- Add a graphical user interface (GUI)
- Support multiple investigation cases
- Store case data using a database
- Add more advanced evidence analysis
- Add data visualization for suspect scores
- Add a case history feature
- Add authentication for investigators

##  Author

**Muskan Kadyan**

This project was built as part of my Python learning journey to practice programming fundamentals, problem-solving, data structures, functions, and file handling.

```text
git clone https://github.com/MuskanKadyan/Python-Detective.git
