'''Q1: Neighbor Digits'''
def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    if num < 10:
        return num == prev_digit
    last = num % 10
    rest = num // 10
    return int(prev_digit == last or rest % 10 == last) + neighbor_digits(num // 10, last)


'''Q2: Has Subsequence'''
#TODO: reminder
def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"
    # last, rest = seq % 10, seq // 10
    #
    # if n % 10 == last:
    #     return has_subseq(n//10, rest)
    if n == seq:
        return True
    if n < seq:
        return False

    without = has_subseq(n // 10, seq)
    if seq % 10 == n % 10 :
        return has_subseq(n //10, seq // 10) or without
    return without

has_subseq(141, 11)


'''Q3: Num eights'''
def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos < 10:
        return int(pos == 8)
    else:
        return int(pos%10 == 8) + num_eights(pos // 10)


'''Q4: Ping-pong'''
def pingpong(n):
    index = 1
    s = 0
    k = 1
    while index <= n:
        s += 1*k
        if index % 8 == 0 or "8" in list(str(index)):
            k = -k
        index += 1

    return s

#TODO:reminder
def pingpong(n):
    def helper(result, index, step):
        if index == n:
            return result
        elif index % 8 == 0 or num_eights(index)>0:
            return helper(result-step, index+1, -step)
        else:
            return helper(result+step, index+1, step)
    return helper(1, 1, 1)

    # if n-1 % 8 == 0 or "8" in list(str(n-1)):
    #     k = k * -1
    # if n == 1:
    #     return 1
    # else:
    #     return k*1 + pingpong(n-1, k)
    #
    #
    #
    # def fun(index, k):
    #     if index % 8 == 0 or "8" in list(str(index)):

pingpong(8)


'''Q5: Count coins'''
def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(change):
    def helper(all, m):
        if all == 0:
            return 1
        elif all < 0:
            return 0
        elif m == None:
            return 0
        else:
            return helper(all - m, m) + helper(all, get_smaller_coin(m))
    return helper(change, 25)

count_coins(10)