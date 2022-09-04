import string
import math
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    #print(s1)
    s2 = string.ascii_uppercase
    #print(s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
    #print(s4)

    plen = int((input("Enter the length of the password : ")))
    
    
    #Intiliazing the empty list 
    #We use extend fuction so as to add elemennts within a list
    #Here in s - s1,s2,s3,s4 elements are added 
    #if we use append instead of extend 
    #append -> a=[1,2,3,4,5], b=[6,7]

    #using b.append(a) -> [1,2,3,4,5,[6,7]]
    #if we use b.extend(a) -> [1,2,3,4,5,6,7]
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)
    #Shuffling the list
    random.shuffle(s)
    #print(s)

    print("Your Password is : ")
    print("".join(s[0:plen]))





