import time

array1 = list(range(1000))
array2 = list(range(500, 1500))


def intersection_slow(a, b):
    result = []

    for x in a:
        for y in b:
            if x == y:
                result.append(x)
                break

    return result



def intersection_fast(a, b):
    set_b = set(b)
    result = []

    for x in a:
        if x in set_b:
            result.append(x)

    return result



start = time.perf_counter()
result1 = intersection_slow(array1, array2)
time1 = time.perf_counter() - start


start = time.perf_counter()
result2 = intersection_fast(array1, array2)
time2 = time.perf_counter() - start


assert result1 == result2

print("Повільний алгоритм:", time1)
print("Швидкий алгоритм:", time2)
print("Кількість спільних елементів:", len(result1))
print("Результати однакові!")