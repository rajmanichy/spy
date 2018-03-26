print("hello")
print("what's up")
print("let's get started")
def entry():
    spy_name = raw_input("what's your name?")
    print("welcome" + spy_name + ". glad to have you back with us")

    ##########providing salutation##########
    spy_salutation = raw_input("what should we call you(Mr. or Ms.)?")
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


def spy_chat(new):
    i=0
    while i<5:
        print ("what do you want to do?")
        menu_choices="1. Add a status update \n2. Exit the application \nInput:-"
        menu_choice=raw_input(menu_choices)
        if menu_choice=="1":
            if new==0:
                from spy_details import status
                print ("your current status is: %s" % status)    ####Display your current status####
            elif new==2:
                print ("your status is: %s" % status)     ####Display status of new user
            else:
                print ("Add your status")   ####ask for new status
                status=raw_input()
                print ("your status is= %s" % status)
                new =2
                i=i+1
        elif menu_choice=="2":
            print ("Quitting...")    ####quite the program
            exit()
        else:
            i=i+1
            pass
user=raw_input("do you want to continue with the default user ?(Y/N)")
new_user=0
if user=="Y":
    from spy_details import name
    from spy_details import spy_salutation
    from spy_details import spy_age
    from spy_details import spy_rating
    print ("welcome, %s %s with %d years of age and %d rating. welcome to spyChat..." % (spy_salutation, name, spy_age,spy_rating))
else :
    new_user=1
    entry()    #####taking details of new user
spy_chat(new_user)

