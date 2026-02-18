import re

phone_numbers = ["    +38(050)123-32-34", "     0503451234","(050)8889900","38050-111-22-22","38050 111 22 11   "]

def normalize_numbers(numbers_list):

    normalized_list = []
    
    for num in phone_numbers:

        normalized_numbers = num.replace(" ", "").replace("(", "").replace(")", "").replace("-", "").replace("+", "").replace("380", '')

        if normalized_numbers.startswith('0'):

            normalized_numbers = normalized_numbers.removeprefix('0')


        normalized_list.append("+380" + normalized_numbers)


    return normalized_list

normalize_numbers(phone_numbers)