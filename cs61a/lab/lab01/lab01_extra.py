"""Optional questions for Lab 1"""

# While Loops


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    #compute the falling factorial of n to depth k
    #if k is 0, return 1
    #if k is 1, return n
    #if k is 2, return n * (n-1)
    #if k is 3, return n * (n-1) * (n-2)
    #if k is 4, return n * (n-1) * (n-2) * (n-3)
    product = 1
    while k > 0:
        product *= n
        n -= 1
        k -= 1
    return product


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    #if n is less than 2, return false
    #if n is greater than 2, check if the last two digits are 8
    #if they are, return true
    #if they are not, return false
    # if n < 2:
    #     return False
    # else:
    #     if n % 10 == 8 and (n // 10) % 10 == 8:
    #         return True
    #     else:
    #         return False

    # return '88' in str(n)

    while n > 10:
        if n % 100 == 88:
            return True
        n //= 10
    return False
