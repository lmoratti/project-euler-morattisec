import timeit

class Solution:
    def __init__(self, function: callable, *args, **kwargs) -> None:
        self.function = function
        self.args     = args
        self.kwargs   = kwargs
        self.name     = f"{function}"
        self.time     = None
    
    def compare(one: "Solution", two: "Solution"):
        return one.time - two.time

    def run_solution(self):
        self.function(*self.args, **self.kwargs)

    def time_solution(self) -> int:
        if not self.time:
            self.time = timeit.timeit(self.run_solution, number=1000)
        return self.time
        
