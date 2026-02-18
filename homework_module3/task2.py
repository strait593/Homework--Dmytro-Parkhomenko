import random

def get_numbers_ticket(min,max,quantity):

    numbers = []

    for i in range(min,max):
        numbers.append(i)

    winning_numbers_list = []

    winning_numbers = random.sample(numbers, k=quantity)
    winning_numbers_list.append(winning_numbers)

    return print(f"The winning numbers are: {winning_numbers}")

get_numbers_ticket(1,1001, 10)