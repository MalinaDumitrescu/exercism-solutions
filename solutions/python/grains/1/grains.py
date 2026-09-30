def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    number -= 1
    number_of_grains_per_square = 2 ** number
    return number_of_grains_per_square


def total():
    sum = 0
    for n in range(1, 65):
        sum += 2 ** (n - 1)
    return sum    

def total_by_using_sum():
   return sum(square(n) for n in range(1, 65))
