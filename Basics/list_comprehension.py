squares = [x ** 2 for x in range(10)]
print(squares)

cubes = [x ** 3 for x in range(10)]
print(cubes)

pythagorean_triplets = [(x, y, z) for x in range(15) for y in range(x, 15) for z in range(y, 15)
                        if x * x + y * y == z * z and x != 0 and y != 0 and z != 0]
print(pythagorean_triplets)


even_numbers = [x for x in range(11) if x % 2 == 0]
print(even_numbers)


matrix = [[0 for _ in range(3)] for _ in range(3)]
print(matrix)
