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

# checks input more than a given value 

# gets factors, returns a sorted list 

# Main routine goes here

# Heading 
statement_generator("Factors Calculator", "-")