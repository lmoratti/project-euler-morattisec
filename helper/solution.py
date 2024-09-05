import timeit

class Solution:
    def __init__(self, function: callable, *args, **kwargs) -> None:
        self.function = function
        self.args     = args
        self.kwargs   = kwargs
        self.name     = f"{function.__name__}"
        self.time     = None
        self.result   = None
    
    def compare(one: "Solution", two: "Solution"):
        return one.time - two.time

    def run_solution(self):
        self.result = self.function(*self.args, **self.kwargs)

    def time_solution(self) -> int:
        if not self.time:
            self.time = timeit.timeit(self.run_solution, number=1000)
        return self.time
        
    def isValid(self, expected_answer) -> bool:
        return self.result == expected_answer