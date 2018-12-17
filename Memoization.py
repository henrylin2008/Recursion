# Memoization effectively refers to remembering ("memoization" -> "memorandum" -> to be remembered) results of method calls based 
# on the method inputs and then returning the remembered result rather than computing the result again. You can think of it as a cache
#  for method results. We'll use this in some of the interview problems as improved versions of a purely recursive solution.


# Create cache for known results
factorial_memo = {}

def factorial(k):
    
    if k < 2: 
        return 1
    
    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
        
    return factorial_memo[k]


class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]



def factorial(k):
    
    if k < 2: 
        return 1
    
    return k * factorial(k - 1)

factorial = Memoize(factorial)