#logical operators(and,or,not)=used to check two or more conditional statements
temp=int(input("what is the temperature outside broh?:"))
if not(temp>=0 and temp<=30): 
    #b oth the conditions should satisfies
    print("The temperture is good outside,u can go out broh!")
    print("Go outside")
elif not(temp<0 or temp>30):
     # atleast one condition should satisfes
    print("The temperture is not good outside today,better stop ur plans dude!")
    print("stay inside")

    #not= if we around not operator it gives the opposite output
