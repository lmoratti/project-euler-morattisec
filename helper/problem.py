from helper.solution import Solution


class Problem:
    def __init__(self) -> None:
        self.solutions = []
        pass

    def add_solution(self, solution: callable, *args, **kwargs) -> "Solution":
        self.solutions.append(Solution(solution, *args, **kwargs))
    
    def time_solve(self)-> None:
        for solution in self.solutions:
            solution.time_solution()
        self.solutions.sort(key=lambda sol: sol.time)

    
    def fastest_time(self)-> int:
        if not self.solutions:
            self.time_solve()
        return self.solutions[0]
    
    def announce_results(self):
        times = [s.time for s in self.solutions]
        print(times)
        for t_first, t_second in zip(self.solutions, self.solutions[1:]):
            print(f"Solution was {t_second.time / t_first.time}x faster than previous result")
        print(f"Solution was {self.solutions[-1].time / self.solutions[0].time}x faster than the worst result.")