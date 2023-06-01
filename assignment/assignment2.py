# Write a Python to count number of odd and even number from the series of the list:
# [ 2,3,4,55,56,78,75,69,66,101,100 ]
l = [ 2,3,4,55,56,78,75,69,66,101,100 ]

def countEvOdd(l):
    e=0 # Count the even number from the list
    o=0 # Count the odd number from the list
    for number in l:
        if number%2==0:
            e=e+1
        else:
            o=o+1
    return print(f"The number of times even and odd numbers appears in the list {l} is {e} and {o} respectively")

countEvOdd(l)