#Wrap your code from Exercise 10-6 in a while loop so the user can continue
# entering numbers even if they make a mistake and enter text instead of a number.


print("Type 'xddd' to exit")


while True:    
    try:
        num_1 = input("Number 1: ")
        num_2 = input("Number 2: ")  
        if num_1 == "xddd":
            break
        if num_2 == 'xddd':
            break
        else:
            xnum_1 = int(num_1)
            xnum_2 = int(num_2)
    except ValueError:
        print("Need a number, not a string.")
    else:
        answer = xnum_1 + xnum_2
        print(f"The sum of {num_1} + {num_2} = {answer}.")