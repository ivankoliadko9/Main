import time


numbers_list = list(range(1000000))
numbers_set = set(numbers_list)


target = 999999


start = time.perf_counter()

result_list = target in numbers_list

end = time.perf_counter()
list_time = end - start


start = time.perf_counter()

result_set = target in numbers_set

end = time.perf_counter()
set_time = end - start

print("Пошук у List:", list_time)
print("Пошук у Set:", set_time)

print("List:", result_list)
print("Set:", result_set)