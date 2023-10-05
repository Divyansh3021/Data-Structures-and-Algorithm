def myPow(x: float, n: int) -> float:
    if n < 0: n, x = -n, 1/x
    if n == 0:
        return 1
    else:
        return x * myPow(x, abs(n)-1)
    pass