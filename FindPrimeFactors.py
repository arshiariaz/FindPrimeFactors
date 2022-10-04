# File: FindPrimeFactors.py
# Student: Arshia Riaz
# 
# Date Created: 10/28/2021
# Date Last Modified: 10/29/2021
# Description of Program: This program returns a list of prime factors for a series of positive integers.

print('Find Prime Factors:\n',end='')
while True:
    num = int(input('Enter a positive integer (or 0 to stop): '))
    a = int(num)
    if (num == 0):
        print('Goodbye!')
        break
    elif(num == 1):
        print('  1 has no prime factorization.',end='\n\n')
    elif (num < 0):
        print('  Negative integer entered.  Try again.',end='\n\n')
    else:
        factors = []
        while(num != 1):
            for i in range(2,num + 1):
                if(num % i == 0):
                    factors.append(i)
                    num=int(num / i)                    
                    break
        print('  The prime factorization of',a,'is:',factors,end='\n\n')
