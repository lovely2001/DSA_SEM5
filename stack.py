# Menu driven program for stack

# Initialize empty STACK  
stack = [] 

while True:  
    print("\nSELECT APPROPRIATE CHOICE")                    
    print("1. PUSH Element into the Stack")  
    print("2. POP Element from the Stack") 
    print("3. Display Elements of the Stack")  
    print("4. Exit")  

    value = int(input("Enter the Choice:"))

    #PUSH elements into the STACK
    if value == 1:
        print("Enter data ")
        data = input() 
        stack.append(data) 

    #POP one element from the STACK     
    elif value == 2:
        # To check whether STACK is Empty or not
        if len(stack) == 0:                       
            print('The STACK is EMPTY No element to POP out') 
        else:    
            #to POP element from the STACK  
            print('\nElement POP out from the STACK is:')  
            print(stack.pop())     

    #display the STACK
    elif value == 3:
        # Check whether STACK is Empty or not
        if len(stack) == 0:                       
            print('The STACK is initially EMPTY') 
        else:         
            print('\nSTACK elements are as follows:')            
            print(stack)                          

    #EXIT from the program
    elif value == 4:  
        break  

    # Shows ERROR message if the choice is incorrect
    else:  
        print("Sorry bro!!! Incorrect Choice")