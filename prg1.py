'''
August 28, 2019
CSC246, Programming Languages
Dr. Kendall-Morwick
Jonathan Webber

        Basic Python Programming
'''
import random
import sys

#create a dictionary 
d = {}

#try to open the file
try:
    with open("flashcards.txt") as f:

    #loop line by line through the text file
        for line in f:

        #split the line by semicolon and put it in the dictionary in a key-value pair
            (key, value) = line.strip().split(":")
            d[key] = value.strip()

#create a file not found exception
except FileNotFoundError:
    sys.exit("File not found.")
        

#create variables to track total questions and the number correct
total = 1
correct = 0
#print(d)

#start the indefinite loop with user input
while True:

    #choose a random integer between 0 and the length of the dictionary-1
    rand = random.randint(0,len(d)-1)

    #get the answer and definition of that random integer
    answer = list(d)[rand]
    definition = d[answer]

    #strip of whitespaces
    answer = answer.strip()

    #print the definition to the user
    print("Definition: " + definition)
    
    #get the user input
    userIn = (input("What term does this define? ")).lower().strip()

    #continue waiting for user input if empty (empty strings are considered false)
    while not userIn: 
        print("Please answer the question.")
        userIn = (input("What term does this define? ")).lower().strip()

    #break our of the loop on 'exit'
    if userIn == "exit":
        break

    #if the user inputs the correct answer
    if userIn == answer:  
        print("Correct!")
        correct = correct + 1

    #if the user inputs an incorrect answer
    else:
        print("Wrong!")
        print("Correct answer: " + answer)

    total = total + 1

print("Total Questions: " + str(total - 1))
print("Total Correct: " + str(correct))
sys.exit(0)
