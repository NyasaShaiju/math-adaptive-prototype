class AdaptiveEngine:
    def __init__(self, start_level="Easy"):
        self.levels = ["Easy", "Medium", "Hard"]
        if start_level not in self.levels:
            start_level = "Easy"
        self.current_level = start_level
        self.score = 0

    def update(self, correct, time_taken, fast_threshold=4.0):
        if correct:
            if time_taken <= fast_threshold:
                self.score += 2
            else:
                self.score += 1
        else:
            self.score -= 2

        if self.score >= 4:
            self.change_level(up=True)
            self.score = 0
        elif self.score <= -4:
            self.change_level(up=False)
            self.score = 0

        return self.current_level

    def change_level(self, up=True):
        idx = self.levels.index(self.current_level)
        if up and idx < len(self.levels) - 1:
            self.current_level = self.levels[idx + 1]
        elif not up and idx > 0:
            self.current_level = self.levels[idx - 1]
