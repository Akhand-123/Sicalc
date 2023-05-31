p = int(input("Enter the principle amount p: "))
t = int(input("Enter the Time t: "))

def simpleInterest(p,r,t):
    print("The principle amount is ",p)
    print("The Rate is ",r)
    print("The Time is ",t)
    si = (p*r*t)/100
    print("Your interest is ",si)
    print(f"Your total amount after time {t} is Rs.{p+si}")

def siCalc():
    print("Enter your category 1)Female Senior Citizen 2)Male Senior Citizen 3)Female 4)Male")
    
    param={
        1:"Female Senior Citizen",2:"Male Senior Citizen",3:"Female",4:"Male"
    }
    
    x = input("Select: ")
    try:
        
        if int(int(x))==1:
            print("You are Female Senior Citizen for you interest rate =8%")
            r=8
            return simpleInterest(p,r,t)
        elif int(x) == 2:
            print("You are Female Senior Citizen for you interest rate =8%")
            r=7
            return simpleInterest(p,r,t)
        elif int(x) == 3:
            print("You are Female Senior Citizen for you interest rate =8%")
            r=6
            return simpleInterest(p,r,t)
        elif int(x) == 4:
            print("You are Female Senior Citizen for you interest rate =8%")
            r=5
            return simpleInterest(p,r,t)
        else:
            print("1 for Female Senior Citizen, 2 for Male Senior Citizen, 3 for Female, 4 for Male")

    except Exception as e:
        print("Please select following options as")
        print("1 for Female Senior Citizen, 2 for Male Senior Citizen, 3 for Female, 4 for Male")

siCalc()            
        