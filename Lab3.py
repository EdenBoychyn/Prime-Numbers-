# Authors:           Eden Boychyn 100752815, Patrick Traycheff
# Date:              February 28th, 2021 
# Description:       A Python application that will graphically display all the prime
#                    numbers up to a limit selected by the user

# Constants 
STARTING_POINT = 2

MINIMUM_PRIME_NUMBER = 2
MAXIMUM_NUMBER = 70

number = 0

# Constants listed for all "x" prime numbers 
TWO_XS = ("xx")
THREE_XS = ("xxx")
FIVE_XS = ("xxxxx")
SEVEN_XS = ("xxxxxxx")
ELEVEN_XS = ("xxxxxxxxxxx")
THIRTEEN_XS = ("xxxxxxxxxxxxx")
SEVENTEEN_XS = ("xxxxxxxxxxxxxxxxx")
NINETEEN_XS = ("xxxxxxxxxxxxxxxxxxx")
TWENTYTHREE_XS= ("xxxxxxxxxxxxxxxxxxxxxxx")
TWENTYNINE_XS= ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
THIRTYONE_XS = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
THIRTYNINE_XS = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
FOURTYONE_XS = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
FOURTYTHREE_XS = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
FOURTYSEVEN_XS = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
FIFTYTHREE_XS = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
FIFTYNINE_XS = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
SIXTYONE_XS = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
SIXTYSEVEN_XS = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# Application Header
print("********************************************************************")

print("                         Prime Number Finder")


print("********************************************************************")
# Application Header

# validate prime number
while not number:
    # Declaring and initalizing Variables 
    try: # Prompt the user for a prime number as an integer value. 
        ending_point = int(input("Please enter a limit to the prime numbers you want displayed: "))

        # Check that the prime number is within range
        if not (MINIMUM_PRIME_NUMBER <= ending_point <= MAXIMUM_NUMBER):
        # Prime number is not within range. Print an error message
            print("Please enter a prime number within " + str(MINIMUM_PRIME_NUMBER) + " and " + str(MAXIMUM_NUMBER))
            number = 0

    # if number is not a number or a whole number, this message will be printed
    except:
        print("Please enter a prime number as a whole numeric value.") 

    # for iteration sequence using a range starting with the constant MINIMUM_PRIME_NUMBER and using user input as the
    # end point
    for ending_point in range(MINIMUM_PRIME_NUMBER, ending_point+1):

        # Testing to see if the number inputted by the user is a prime number 
        if ending_point>2:

            # using variable i as the ending_point variable
            for i in range(STARTING_POINT, ending_point):

                # using the ending_point inputted variable to divided it by the starting point. If answer is 0 it is not 
                # a prime number and is skipped or calls the "break" variable in iteration and loops until ending_point
                if (ending_point%i) ==0:
                    break 

                # Once it reaches the ending point it prints out all the prime numbers    
                else:
                    print(ending_point)


