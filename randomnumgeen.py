# This program asks the user how many random numbers they want added to a file, and the program will carry out this task
import random # Random is imported as we need to generated ranged random integers
def main(): #defining main function
    try: 
        myfile = open('random_numbers.txt','w') # We are opening a file called random_numbers.txt to write in
        amount_of_numbers = int(input('How many numbers do you want to input: ')) # user is asked for input for amount of numbers they want put in file
        for num in range(amount_of_numbers): # in the range of the amount of numbers the user inputs,
            x = random.randint(1,501) # random values from 1 to 500 will be generated
            myfile.write(str(x) + '\n') # These random values plus a newline character to make new lines will be written to the file
        myfile.close() # After the for loop has finished adding the random integers we close this file.
    except ValueError: # If user enters anything other than "int", this will cause a ValueError, and the user 
        print('Please enter valid integer. ') # has to enter an integer value
        amount_of_numbers = int(input('Try again: How many numbers do you want to input: ')) # User asked for new input
main() # main function called