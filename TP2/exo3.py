def fibonacci1(n):
    if n <= 1:
        return n
    else:
        return fibonacci1(n - 1) + fibonacci1(n - 2)


if __name__ == '__main__':
    f1 = fibonacci1(30)
    print(f1)
