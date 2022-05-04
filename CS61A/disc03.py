'''disc 03'''
def factorial(n):
    """Return the factorial of N, a positive integer."""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


'''Q1: Warm Up: Recursive Multiplication'''
def fac(m,n):
    if n == 1:
        return m
    else:
        return m + fac(m, n-1)

fac(5,3)


def rec(x, y):
    if y > 0:
        return x * rec(x, y - 1)
    return 1

rec(4, 3)


'''Q3: Find the Bug'''
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n ==2 or n == 1:
        return n
    else:
        return n * skip_mul(n - 2)


'''Q4: Recursive Hailstone'''
def hailstone(n, len=0):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return len + 1

    if n % 2 == 0:
        return hailstone(n / 2, len+1)
    else:
        return  hailstone(n * 3 + 1, len+1)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)

a = hailstone(10)


def hailstone(n):
    '''
    :param n: init number
    :return: list of hailstone
    '''
    # "*** YOUR CODE HERE ***"
    if n == 1:
        return [n]
    elif n % 2 == 0:
        return [n] + hailstone(n / 2)
    else:
        return  [n] + hailstone(n * 3 + 1)


'''Q5: Merge Numbers'''
def dig(n):
    lst = []
    while n >0:
        lst.append(n%10)
        n = n // 10
    return lst

#not perfect
def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order"""
    if n1 == 0 and n2:
        return n2
    elif n1 and n2 == 0:
        return n1
    elif n1 % 10 <= n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10


'''Q6: Is Prime'''
#TODO:reminder
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i):
        if i == n:
            return True
        elif n % i == 0:
            return False
        return helper(i+1)
    return helper(2)



