def is_armstrong_number(number):
    list_of_numbers = [int(num) for num in str(number)]
    sum_of_powers = 0
    for num in list_of_numbers:
        sum_of_powers += num ** len(list_of_numbers)
    if sum_of_powers == number:
        return True
    else:
        return False

