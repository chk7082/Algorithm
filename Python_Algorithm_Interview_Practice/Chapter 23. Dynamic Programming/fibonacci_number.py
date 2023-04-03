class fibonacci_calculator:
    '''
    class for calculating fibonacci numbers
    '''
    def __init__(self, max_n):
        self.max_n = max_n
        self.previously_computed = [0] * (max_n+1)
        self.previously_computed[1] = 1

        self.stored_up_to = 1

    def compute_fibonacci(self, n):
        # trivial cases
        if n <= 1:
            return n

        # if it has been computed before, just use it
        elif self.previously_computed[n]:
            return self.previously_computed[n]

        # otherwise, we need to compute it
        else:
            self.previously_computed[n] = self.compute_fibonacci(n-1) + self.compute_fibonacci(n-2)
            return self.previously_computed[n]

    def __call__(self, n):
        # if we computed it before, just return it
        if self.stored_up_to >= n:
            return self.previously_computed[n]
        # otherwise, compute it & return it
        else:
            result = self.compute_fibonacci(n)
            self.stored_up_to = n
            return result


fibonacci = fibonacci_calculator(max_n=100)
print(fibonacci(10)) # 55
print(fibonacci.previously_computed)