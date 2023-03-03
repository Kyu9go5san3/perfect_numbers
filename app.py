perfect_numbers = list()

def find_divisors(number):
    divisors = list()
    i = 0
    while i < number:
        i += 1
        if number % i == 0:
            divisors.append(i)
    return divisors

def sum_of_divisors(list):
    return sum(list[:-1])

def perfect_detector(number, sum_of_divisors):
    if sum_of_divisors == number:
        perfect_numbers.append(number)
        print(f"New perfect number detected: {number}")
        print(f"Perfect numbers: {perfect_numbers} \n")

def num_iterator(max):
    i = 0
    while i < max:
        i += 1
        divisors = find_divisors(i)
        perfect_detector(i, sum_of_divisors(divisors))

num_iterator(10000)