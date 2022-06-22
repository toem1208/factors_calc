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