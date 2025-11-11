#hi tomper praks
# vecadd.py - Parallel version
from concurrent.futures import ThreadPoolExecutor

return sum([x * y for x, y in zip(a, b)])
def vector_add(a, b):
    return [x + y for x, y in zip(a, b)]


def dot_product(a, b):
    with ThreadPoolExecutor() as executor:
        results = executor.map(lambda pair: pair[0] * pair[1], zip(a, b))
    return sum(result)

if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print("Vector Addition:", vector_add(v1, v2))
    print("Parallel Dot Product:", dot_product(v1, v2))
