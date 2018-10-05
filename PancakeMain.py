#Miguel Fuentes AI homework 2

import PancakeStack as ps #brings in all the sorting algorithms in the other file

running = True #starts the program running

while running:
    #asks for the user input
    stackAndKey = input('Enter the initial stack and the choice of algorithm: ')

    while len(stackAndKey) > 5:
        stackAndKey = input("Invalid input, try again: ") #rejects input if it's too long

    algorithm = stackAndKey[-1] #gets the algorithm
    stack = stackAndKey[:4] #gets the initial state

    #This section will apply the chosen algorithm to the initial state then print the output
    if(stack == '4321'):
        print('No flips required, goal state inputed')
    elif algorithm == 'd':
        path = ps.dfs(stack)
        if path == False:
            print("Failed")
        else:
            ps.prettyPrint(stack,path)
    elif algorithm == 'g':
        path = ps.greedy(stack)
        if path == False:
            print("Failed")
        else:
            ps.prettyPrint(stack,path)
    elif algorithm == 'u':
        path = ps.ucs(stack)
        if path == False:
            print("Failed")
        else:
            ps.prettyPrint(stack,path)
    elif algorithm == 'a':
        path = ps.aStar(stack)
        if path == False:
            print("Failed")
        else:
            ps.prettyPrint(stack,path)
    else:
        print("algorithm key not recognized")


    #Asks the user if they want to start over
    check = input("Type 'y' to start over, anything else will exit: ")

    if not check == 'y':
        running = False #Exits the loop if the user doesn't want to repeat