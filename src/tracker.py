class PerformanceTracker:
    def __init__(self):
        self.records = []

    def record(self, correct, time_taken):
        self.records.append({"correct": bool(correct), "time": float(time_taken)})

    def summary(self):
        total = len(self.records)
        correct = sum(1 for r in self.records if r["correct"])
        avg_time = sum(r["time"] for r in self.records) / total if total else 0.0
        accuracy = (correct / total) * 100 if total else 0.0
        return {
            "total": total,
            "correct": correct,
            "accuracy": round(accuracy, 2),
            "avg_time": round(avg_time, 2),
            "records": self.records
        }
