Math Puzzles — AI-Powered Adaptive Learning Prototype
A small, rule-based adaptive math practice prototype for children (ages 5–10) that adjusts puzzle difficulty based on correctness and response time.

Features
- Three difficulty levels: Easy, Medium, Hard
- Generates simple math puzzles (addition, subtraction, multiplication, division)
- Tracks correctness and response time
- Rule-based adaptive engine to change difficulty dynamically
- Session summary with accuracy and average response time


Requirements
- Python 3.8+
- No external libraries required for the console prototype

How to run
1. Clone repo
```bash
git clone https://github.com/NyasaShaiju/math-adaptive-prototype.git
cd math-adaptive-prototype
```
2. Install requirements (none are required for the console app):

       pip install -r requirements.txt

3. Run the console app

       python src/main.py

Adaptive Logic:

Rule-based scoring:
Correct & fast (<= 4s): +2 points
Correct & slow: +1 point
Wrong: -2 points
Thresholds:
Score >= +4 -> increase level
Score <= -4 -> decrease level
Score reset to 0 after a level change

