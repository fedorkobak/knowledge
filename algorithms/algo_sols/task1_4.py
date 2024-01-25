def solve(a, b, c):
    if c < 0:
        return "NO SOLUTION"
    if a == 0:
        return "NO SOLUTION" if c**2!=b else "MANY SOLUTIONS"
    sol = (c**2 - b)/a
    return ("NO SOLUTION" if sol%1 else int(sol))

if __name__ == "__main__":
    print(
        solve(*[int(input()) for i in range(3)])
    )