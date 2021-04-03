def classify(number):
    sm = 0
    if number <= 0 or number % 1 != 0:
        raise ValueError('Input needs to be a positive integer.')
    for i in range(1, number):
        if number % i == 0:
            sm += i
    if sm == number:
        return 'perfect'
    elif sm < number:
        return 'deficient'
    else:
        return 'abundant'

