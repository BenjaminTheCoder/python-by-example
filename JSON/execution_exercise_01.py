def is_even(num):
    is_even_result = num % 2 == 0
    return is_even_result

def sum_even_numbers(nums):
    total = 0
    for num in nums:
        if is_even(num): 
            total += num
    return total

def sum_numbers(nums):
    total = 0
    for num in nums:
        total += num
    return total


my_sum = sum_even_numbers([1,2,3,4])
print('my_sum', my_sum)

print((3 + 4) * (2 + 8))
