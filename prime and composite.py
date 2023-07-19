def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_and_composite_nums(lst):
    prime_nums = []
    composite_nums = []
    for num in lst:
        if is_prime(num):
            prime_nums.append(num)
        else:
            composite_nums.append(num)
    return prime_nums, composite_nums

lst = [2, 3, 4, 5, 6, 7, 8, 9]
prime_nums, composite_nums = find_prime_and_composite_nums(lst)
print("Prime numbers in list:", prime_nums)
print("Composite numbers in list:", composite_nums)
