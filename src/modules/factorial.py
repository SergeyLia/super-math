def factoriak_rec(n):
    if n <= 1:
        return 1
    return n * factoriak_rec(n-1)