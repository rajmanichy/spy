print("hello")
print("what's up")
print("let's get started")
spy_name = input("what's your name?")
print("welcome" + spy_name + ". glad to have you back with us")


##########providing salutation##########


spy_salutation = input("what should we call you(Mr. or Ms.)?")
spy_salutation + " " + spy_name
spy_name = spy_salutation + " " + spy_name
print(spy_name)

###further details###


spy_age = 0
spy_rating = 0.0
spyisonline = False

spy_age = int(input("what is your age"))
if spy_age>12 and spy_age<50:
    spy_rating = float(input("what is your spy rating?"))
else:
    print("sorry! you are not of the correct age to be spy")

if spy_rating>4.5:
    print("great ace!")

elif spy_rating>3.5 and spy_rating<=4.5:
    print("you are one of the good ones.")

elif spy_rating>2.5 and spy_rating<=3.5:
    print("you can always do better")

else:
    print("we can always use somebody to help in the office")

spyisonline= True
print("Authentication complete.welcome"+ spy_name)
print("your age ="+ str(spy_age))
print("your spy rating"+str(spy_rating))

