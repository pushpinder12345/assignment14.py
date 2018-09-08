#Q.1- Write a python program to print the cube of each value of a list using list comprehension.

lst = [i*i*i for i in range(1,16)]
print('List with cubes:-')
print(lst)

#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.

max = int(input('Enter the maximum number to check: '))
l = []
l = [num for num in range(2, max) if 0 not in [num %d for d in range(2, num)]]
print(l)

#Q.3- Write the main differences between List Comprehension and Generator Expression.
'''In terms of syntax, the only difference is that you use parenthesis instead of square brackets.
The type of data returned by list comprehensions and generator expressions differs.
The generator yields one item at a time?—?thus it is more memory efficient than a list.'''

#Q.4- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
deg = [39.2 ,36.5, 37.3, 37.8]
fah = list(map(lambda c : 1.8*c + 32, deg))
print(fah)

#Q.5- Apply an anonymous function to square all the elements of a list using map and lambda.
lst=[1,2,3,4,5,6,7,8,9,0]
sq = list(map(lambda i : i**2, lst))
print(sq)

#Q.6- Filter out all the primes from a list.
lst = [12, 544, 3, 55, 47, 43, 54, 541, 4441, 843]

def isPrime(n):
    flag=1
    if(n>1):
        for i in range(2,n):
        
            if(n%i==0):
                flag=0
                break
        if(flag==1):
            return n

for i in range(1, 100): 
     n = list(filter(lambda x: isPrime(x), lst))

print('Prime Numbers are:-',n)

#Q.7- Write a python program to multiply all the elements of a list using reduce.
import functools

l = [2, 4, 6, 8, 10]
x = functools.reduce(lambda a, b: a*b, l)

print('Final Product:- ',x)
