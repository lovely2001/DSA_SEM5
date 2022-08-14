# Menu driven program for Queue

# Initial empty QUEUE 
queue=[] 
size = int(input("Enter the size of Queue:")) 

while True:  
    print("\nSELECT APPROPRIATE CHOICE")                    
    print("1. Enqueue Element")  
    print("2. Dequeue Element") 
    print("3. Display Elements of the Queue")  
    print("4. Exit")  
    value = int(input("Enter the Choice:"))  

    # To Enqueue Element
    if value == 1: 
        # check wether the stack is full or not
        if len(queue)==size: 
            print("Queue is Full!!!!")
        else:
            #to push elements into the QUEUE
            element=input("Enter the element:")
            queue.append(element)

    #To Dequeue Element   
    elif value == 2:  
        if len(queue)==0:
            print("Queue is Empty!!!")
        else:
            print(queue.pop())

    #To display the QUEUE
    elif value == 3:
        # Check whether QUEUE is Empty or not
        if len(queue)==0:                   
            print('The QUEUE is initially EMPTY') 

        else:
            print(queue)                        

    #To EXIT from the program
    elif value == 4:  
        break  

    # Shows ERROR message if the choice is not correct
    else:  
        print("Sorry bro!!!! Incorrect Choice")