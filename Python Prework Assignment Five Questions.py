import os

#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    print("Greetings, citizen " + user_name + "." + "\n")

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    quotient = 0
    ListOfOddNumbers = []
    for oddnumber in range(101):
        quotient = oddnumber % 2
        if quotient > 0:
            ListOfOddNumbers.append(oddnumber)
    print("Here is a list of all odd numbers from 1 - 100.")
    print(ListOfOddNumbers)
    print("(This list was presented to you by the print() function.)" + "\n")

#Question 3. Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    a_list.sort()
    greatest = len(a_list) - 1
    return a_list[greatest]

#Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    a_year = int(a_year)
    fourdivide = a_year % 4
    hundreddivide = a_year % 100
    fourhundreddivide = a_year % 400
    if fourdivide == 0 and hundreddivide > 0:
        return "\n" + "The year " +  str(a_year) + " is indeed a leap year." + "\n" + "It is divisible by 4." + "\n"
    elif fourdivide == 0 and hundreddivide == 0 and fourhundreddivide == 0:
        return "\n" + "The year " +  str(a_year) + " is indeed a leap year." + "\n" + "It is divisible by 100 and 400." + "\n"
    elif fourdivide == 0 and hundreddivide == 0 and fourhundreddivide > 0:
        return "\n" + "The year " +  str(a_year) + " is not a leap year." + "\n" + "It is not divisible by 400." + "\n" 
    else:
        return "\n" + "The year " +  str(a_year) + " is not a leap year." + "\n" + "It is not divisible by 4." + "\n" 

#Question 5: Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    for digit in a_list:
        listspot = a_list.index(digit)
        if listspot < (len(a_list)-1):
            if(digit+1) != a_list[listspot+1]:
                print(a_list)
                print("This list is not consecutive." + "\n")
                break
        else:
            print(a_list)
            print("This list is indeed consecutive." + "\n")

onoffswitch = True
selection = None
chosennumber = None
functionlist = []
rawlist = []

while onoffswitch:
    
    def getdecision():

        getinputswitch = True

        os.system('cls')
        print("Welcome to my collection of functions.")
        if rawlist:
            print("Here is your current List: " + str(rawlist) + "\n")
        print("Please choose which function you would like to use:" + "\n")
        print("Question 1: Write a function to print 'hello_USERNAME!' USERNAME is the input of the function." )
        print("Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.")
        print("Question 3: Please write a Python function, max_num_in_list to return the max number of a given list.")
        print("Question 4: Write a function to return if the given year is a leap year.")
        print("Question 5: Write a function to check to see if all numbers in list are consecutive numbers.")
        print("Type 6 to exit the program." + "\n")        

        while getinputswitch:
            chosennumber = input("Please enter the number (integer) of the Question you would like to use (digits ranging from 1 - 6).: ")
            try:
                chosennumber = int(chosennumber)
            except:
                print("'"+ chosennumber + "'"+ " is not an integer." + "\n")
            
            if type(chosennumber) == type(1):
                if chosennumber < 1 or chosennumber > 7:
                    print("This is not an integer in between 1 - 6." + "\n")
                else:
                    getinputswitch = False
      
        return chosennumber

    if selection == None:
        selection = getdecision()
        if selection == 6:
            break

    if selection == 1:
        os.system('cls')
        personsname = input("\n" + "Pray tell: what doth your name be?: ")
        hello_name(personsname)

    if selection == 2:
        os.system('cls')
        first_odds()

    if selection == 3:
        os.system('cls')
        if rawlist:
            functionlist = []
            print("Here is your current List: " + str(rawlist) + "\n")
            print("Option 1: Use Current List")
            print("Option 2: Enter new list.")
            choice = input("Option#?: ")
            choice = int(choice)
            if choice == 1:
                for entry in rawlist:
                    functionlist.append(entry)
                greatestnumber = max_num_in_list(functionlist)
                
            elif choice == 2:
                rawlist = []
                functionlist = []
                while len(rawlist) < 6:
                    print(rawlist)
                    listselect = input("Please add 6 numbers in total to the above list (the brackets above): ")
                    listselect = int(listselect)
                    rawlist.append(listselect)
                    functionlist.append(listselect)
        else:
            rawlist = []
            functionlist = []
            while len(rawlist) < 6:
                print(rawlist)
                listselect = input("Please add 6 numbers in total to the above list (the brackets above): ")
                listselect = int(listselect)
                rawlist.append(listselect)
                functionlist.append(listselect)

        os.system('cls')              
        greatestnumber = max_num_in_list(functionlist)
        print("Pre-Sorted List: " + str(rawlist))
        print("Post-Sorted List: " + str(functionlist))
        print("\n" + "The greatest number in this list is: " + str(greatestnumber) + "\n")

    if selection == 4:
        os.system('cls')
        yearinput = input("Give me a specific year, and I will have my function figure out if it's a Leap Year or not: ")
        result = is_leap_year(yearinput)
        print(result)
        
    if selection == 5:
        os.system('cls')
        print("This is a function to see if the list of numbers you submit are consecutive." + "\n")
        print("Con·sec·u·tive")
        print("/kən" + "'" + "sekyədiv/")
        print("adjective" + "\n")
        print("1: Following continuously.")
        print("'five consecutive months of serious decline'")
        print("2: In unbroken or logical sequence." + "\n")
        if rawlist:
            print("Here is your current List: " + str(rawlist) + "\n")
            print("Option 1: Use Current List")
            print("Option 2: Enter new list.")
            choice = input("Option#?: ")
            choice = int(choice)
            if choice == 1:
                print(rawlist)
                is_consecutive(rawlist)
            elif choice == 2:
                newlist = []
                while len(newlist) < 6:
                    print(newlist)
                    choice = input("Enter 6 numbers into this list: ")
                    choice = int(choice)
                    newlist.append(choice)
                is_consecutive(newlist)
                rawlist = newlist
        else:
            newlist = []
            print(newlist)
            while len(newlist) < 6:
                choice = input("Enter 6 numbers into this list: ")
                choice = int(choice)
                newlist.append(choice)
                print(newlist)
            is_consecutive(newlist)
            rawlist = newlist
        
    print("1: Return to the title screen.")
    print("2: Re-use this function.")
    print("3: Exit the program."+ "\n")
    selection2 = input("Number select: ")
    selection2 = int(selection2)
    if selection2 == 1:
        selection = None
        continue
    elif selection2 == 2:
        continue
    elif selection2 == 3:
        break
