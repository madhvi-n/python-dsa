def squares_under(a: int):
    for i in range(1, a + 1):
        sqr = i ** 2
        yield sqr


a = squares_under(5)
print(f"Generator object of the function -> {a}")
print(f"Values -> {list(a)}")
