#HOW TO FIND NEXT PALINDROME NUMBER

print("Please provide any Palindrome number!!")
num = input()

n = len(num)//2                    

if(num == '9'):                     #Find middle position              
    next = 11
elif(l%2 != 0):                     #If numer is ODD
    temp = str(int(num[:n+1])+1)
    next = temp[:n] + temp[::-1]
else:                               #If number is EVEN
    temp = str(int(num[:n])+1)
    next = temp[:n] + temp[::-1]
    
print("Next Palindrome is: ", next)
