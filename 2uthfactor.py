import random 


# Empty list used to be appened by the while loop
my_lst = []



# While len my list is not two append to the list till 2 is reached then print the list
while len(my_lst) != 2: 
    random_num = random.randint(100, 999) # Picks a random number for the 2fa
    my_lst.append(random_num)
print(my_lst)

# Turn List into strings as they are integers then join them with a - with the .join function
stringit = [str(x) for x in my_lst]
fact = " ".join(stringit)
print(f'Your 2FA code is {fact}!') 

# Input that tells you to enter your 2fa code
verify = input("Enter your 2fa code!")
# while loop to make sure the 2fa is valid
while verify != fact: # If verify is not equal to fact then it will go to print invalid 2fa
    print("Invalid 2fa Code!")
    verify = input("Enter a 2fa code!") # Asks again if you can enter 2fa code
    if verify == verify: # If the verify turns out to be equal it will go and break the loop
        print("You are now in the website!")


# Note this is a little project and its just rough draft 