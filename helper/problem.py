from helper.solution import Solution


class Problem:
    def __init__(self, expected_answer: object = None) -> None:
        self.solutions       = []
        self.expected_answer = expected_answer
       

    def add_solution(self, solution: callable, *args, **kwargs) -> "Solution":
        self.solutions.append(Solution(solution, *args, **kwargs))

    def import_solutions(self, module):
        imported_solutions = [getattr(module,function) for function in dir(module) if "solution_" in function]
        for solution in imported_solutions:
            self.add_solution(solution) 
    
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
            print(f"{t_first.name} was {t_second.time / t_first.time}x faster than previous result and was {"valid" if t_first.isValid(self.expected_answer) else "invalid"}.")
        print(f"{self.solutions[0].name} was {self.solutions[-1].time / self.solutions[0].time}x faster than the worst result ({self.solutions[-1].name}).")

