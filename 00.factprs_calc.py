# Functions go here

# Put series of symbols at start and end of the text
def statement_generator(text, decoration):

    # Make string with five character
    ends = decoration * 5

    # add decoration to start and end of statement 
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Display instructions / information
def instructions():
    
    statement_generator("Instructions / information", "=")
    print()
    print("Print choose an integer between 1 and 200")
    print()
    print("Program will find the factors of the integer you picked and dispaly the factors on your screen")
    print()
    print("Program will also state if the number is a prime or perfect square")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calaculation or any key to quit.")
    print()
    return ""

# checks input more than a given value 
def num_check(question):

    valid = False
    while not valid:

        error = "Please enter a number that is more than or equal to 1 or less than or equal to 200"

        try:

            # ask user to enter a number 
            response = int(input(question))

            # checks number is more than zero
            if 0 < response < 201:
                return response

            # outputs error if input is invalid
            else:
                    print(error)
                    print()

        except ValueError:
            print(error)


# gets factors, returns a sorted list 
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


 

# Main routine goes here

# Heading 
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue ")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""
    
    # ask user for number to be factored...
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! It only has one factor. Itself :)"

    # comment for square / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number. ".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # output factors and comment

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "factors of {}".format(var_to_factor)

    # Output factors and comment 
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit")
    print()

print()
print("Thank you for using the factors calculator")
print()
