# prerequisite: a > b
def euclidean_gcd(a, b):
    assert a > b
    if b == 0:
        # replace this by 'return max(a, -a)' if negative inputs are allowed
        return a
    return euclidean_gcd(b, a % b)

# prerequisite: a > b
# solves for u, v in u*a + v*b = gcd(a, b)
def extended_euclidean(a, b):
    assert a > b
    if b == 0:
        return (1, 0, a)
    u1, v1, gcd =  extended_euclidean(b, a % b)
    u = v1
    v = u1 - (a // b) * v1
    return u, v, gcd
# exercise: try to implement the above fn iteratively
# this was easy to implement recursively cause we are solving for u0, v0 in:
# u0*a0 + v0*b0 = gcd(a0, b0) and we know that after n-iterations
# un = 1, an = gcd, vn = 0, bn = 0 (i.e., 1 * gcd + 0 * 0 = gcd)
# so to compute u(i-1) we need value of ui --> easy to do this in recursion
#                   u(i-1) = vi
#                   v(i-1) = ui - q * vi where, where q is quotient of ai/bi

# Fermat's Theorem: a ≅ a^p (mod p), for any prime p and a < p
# Generalized Fermat's Theorem: a^φ(n) ≅ 1 (mod n), where φ is Euler's totient function
# φ(n) = n - 1 when n is prime

# prerequisite: a < n
def inverse(a, n):
    assert a < n
    u, v, gcd = extended_euclidean(n, a)
    if gcd != 1:
        raise ValueError ('a is not invertible in (mod n)')
    return v % n
