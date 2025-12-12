import time
from puzzle_generator import generate_puzzle
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

def to_number(s):
    try:
        if "." in s:
            return float(s)
        return int(s)
    except:
        return None

def run_session():
    print("Math Puzzles!!")
    name = input("Enter name: ").strip() or "Player"
    start = input("Choose start difficulty (Easy/Medium/Hard) : ").strip().title() or "Easy"
    engine = AdaptiveEngine(start)
    tracker = PerformanceTracker()

    n_questions = 10
    for i in range(n_questions):
        level = engine.current_level
        expr, ans = generate_puzzle(level)
        print(f"\nQ{i+1} | Level: {level}")
        print("Solve:", expr)

        t0 = time.time()
        user = input("Your answer: ").strip()
        t1 = time.time()
        time_taken = t1 - t0

        user_val = to_number(user)
        correct = (user_val == ans)
        tracker.record(correct, time_taken)

        next_level = engine.update(correct, time_taken)
        if correct:
            print("✔ Correct!")
        else:
            print(f"✖ Wrong. Correct: {ans}")
        print(f"Time: {round(time_taken,2)}s | Next level: {next_level}")

    summary = tracker.summary()
    print("\n---- Session Summary ----")
    print(f"Player: {name}")
    print(f"Total: {summary['total']} | Correct: {summary['correct']} | Accuracy: {summary['accuracy']}%")
    print(f"Avg time/question: {summary['avg_time']}s")
    print(f"Recommended next level: {engine.current_level}")

if __name__ == "__main__":
    run_session()
