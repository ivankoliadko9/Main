def fast_power(a, n):
    if n == 0:
        return 1

    half = fast_power(a, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return a * half * half


# Автотесты
assert fast_power(2, 10) == 1024
assert fast_power(3, 3) == 27
assert fast_power(5, 0) == 1
assert fast_power(2, 5) == 32

print("Автотест пройшов успішно")