def num_check(question, low):

    valid = False
    while not valid:

        error = "Please enter a number that is more than (or equal to) {}".format(low)

        try:

            # ask user to enter a number 
            response = int(input(question))

            # checks number is more than zero
            if 1 < response < 200:
                return response

            # outputs error if input is invalid
            else:
                    print(error)
                    print()

        except ValueError:
            print(error)





def get_factors(to_factor):
    # list to hold factors
    factors_list = []

    # square root to_factor to find 'half way'
    limit = int(to_factor ** 0.5)

    # find factor pairs and add to list 
    for item in range (1, limit +1):

        # check factor is not 1 (unity)
        if to_factor == 1:
            break       

        # check if number is a factor
        result = to_factor % item
        factor_1= int(to_factor // item)

        # add factor to list if it is not already there
        if result == 0:
            factors_list.append(item)

        if factor_1 != item and result == 0:
                factors_list.append(factor_1)


    # sort list...
    factors_list.sort()
    return (factors_list)



