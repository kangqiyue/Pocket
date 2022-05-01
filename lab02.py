

'''Q3: A Hop, a Skip, and a Jump'''
def hop():
    def hop_2(x):
        def hop_3(y):
            return y
        return hop_3
    return hop_2


'''Q4: Digit Index Factory'''
def digit_index_factory(k, num):

    count = 0
    while k//10 >= 0 and num != k%10:
        k = k//10
        count+=1
        if k == 0:
            return -1
    return count

digit_index_factory(1234, 0)


'''Q5: Lambdas and Currying'''
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    from operator import add, mul, mod
    curried_add = lambda_curry2(add)
    add_three = curried_add(3)
    add_three(5)
    8
    curried_mul = lambda_curry2(mul)
    mul_5 = curried_mul(5)
    mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    "*** YOUR CODE HERE ***"

    return lambda x: lambda y:func(x,y)


'''Q6: Count van Count'''
def count_factors(n):
    count = 0
    for i in range(1, n+1):
        if n % i ==0:
            count+=1
    return count

def count_primes(n):
    count = 0
    i = 1
    while i <= n:
        if is_prime(i):
            count +=1
        i +=1
    return count

def is_prime(n):
    return count_factors(n) == 2

count_primes(6)
count_primes(13)


def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def fun_return(N):
        count = 0
        i = 1
        while i <= N:
            if condition(N,i):
                count += 1
            i += 1
        return count
    return fun_return


'''Q7: Composite Identity Function'''
def composer(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = composer(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = composer(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
    def fun(n):
        a = composer(f, g)
        b = composer(g, f)
        return a(n) == b(n)
    return fun








