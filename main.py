from steganography.steganography import Steganography
from datetime import datetime

print("Hello world")
print 'what\'s up?'
print 'Let\'s get started...'

#####asking name#####
def entry():
    spy_name =raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(spy_name) > 0:
        print 'Welcome ' + spy_name + '. Glad to have you back with us.'

   #####providing salutation######
        spy_salutation =raw_input("What should we call you (Mr. or Ms.)?")
        spy_salutation + " " + spy_name
        spy_name = spy_salutation + " " + spy_name
        print(spy_name)
        print "Alright " + " " + spy_name +". I'd like to know a little bit more about you before we proceed..."
    else:
        print "A spy needs to have a valid name. Try again please."

#####further details#####
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False
#####asking age#####
    spy_age = input("What is your age?")
    if spy_age > 12 and spy_age < 50:
        spy_rating = float(input("What is your spy rating?"))
    else:
        print 'Sorry you are not of the correct age to be a spy'
    if spy_rating > 4.5:
        print 'Great ace!'
    elif spy_rating > 3.5 and spy_rating <= 4.5:
        print 'You are one of the good ones.'
    elif spy_rating >= 2.5 and spy_rating <= 3.5:
        print 'You can always do better'
    else:
        print 'We can always use somebody to help in the office.'
    spy_is_online = True
    print 'Authentication complete. Welcome ', spy_name
    print 'Your age =' , spy_age
    print 'Your spy rating=',spy_rating

#################################

def spy_chat():
    show_menu=True
    current_status_message=None
    while show_menu:
        print ("What do you want to do?")
        menu_choices="1. Add a status update \n2. Add a friend \n3. Send message \n4. Receive message \n5. Exit the application \nInput:-"
        menu_choice=raw_input(menu_choices)
        if menu_choice=="1":
            current_status_message=add_status(current_status_message)
        elif menu_choice=="2":
            no=add_friend()   ###no of friends returned
            print ("No. of friends: %d" % no)
        elif menu_choice == "3":
            send_message()
        elif menu_choice=="4":
            read_message()
        elif menu_choice=="5":
            print ("Quitting...")   ####quits the program
            show_menu=False
        else:
            print("Invalid input.")
            pass

#####status updation#####

def add_status(current_status_message):
    if current_status_message is not None:
        print("Your current status is: %s" % current_status_message)
    else:
        print("You don't have any status right now.")
    default=raw_input("Do you want to select from the previous statement?(Y/N)")
    if default.upper()=='N':
        new_status_message=raw_input("Which status you want to set?")
        if len(new_status_message)>0:
            updated_status_message=new_status_message        ###update status###
            STATUS_MESSAGE.append(updated_status_message)     ###Enter in the list
            print(updated_status_message + " : is now set as your as status")
        else:
            print("Please enter a valid status...")     ###invalid status###
            updated_status_message=current_status_message     ###assign previous status
            print(updated_status_message + " : Remains as your as status")
    elif default.upper()=='Y':
        item_position=1
        for message in STATUS_MESSAGE:
            print("%d . %s" % (item_position, message))
            item_position=item_position+1
        menu_selection=int(input("What is your desired status?"))
        if len(STATUS_MESSAGE)>=menu_selection:
            updated_status_message=STATUS_MESSAGE[menu_selection-1]   ###set desired status###
            print(updated_status_message + " : is now set as your as status")  # print desired stat
        else:
            print("Invalid input...")
            updated_status_message=current_status_message   ###assign previous status###
    else:
        print("Invalid input")
        pass
    return updated_status_message

#####Friend function start#####

def add_friend():
    new_friend = {"Name": "", "Salutation": "", "age": 0, "Rating": 0.0, "Chats": [] }
    new_friend["Name"] =raw_input("Whats your friend spy name?")
    new_friend["Salutation"] =raw_input("what would be the salutation, Mr. or Mrs??")
    new_friend["Name"] = new_friend["Salutation"] + " " + new_friend["Name"]
    new_friend["age"] = int(input("what is friends age?"))
    new_friend["Rating"] = float(input("what's your friend spy rating??"))
    if len(new_friend["Name"]) > 0 and 12 < new_friend["age"] < 50:  # add friend
        Friends.append(new_friend)
    else:
        print("Sorry we can't add your friend's details please try again.")
    return len(Friends)

def select_a_friend():
    item_no = 0
    if len(Friends)!=0:
        for friend in Friends:
            print("%d . %s" % (item_no+1, friend["Name"]))
            item_no = item_no + 1
        friend_no = int(input("Select your Friend : "))
        if friend_no<=len(Friends) and friend_no!=0:
            print("You selected %d no Friend" % friend_no)
            return friend_no-1
        else:
            print("Wrong raw_input, please try again...")
    else:
        print("Sorry no Friend added till now, plz add a friend first...")
        friend_no=add_friend()
        print("No. of Friends: %d" % friend_no)
        select_a_friend()

#####sending message#####

def send_message():
    selection = select_a_friend();
    image = raw_input("Name of image to be encoded :")
    out_path = "abc.jpg"
    text = raw_input("what text do you want to encode :")
    Steganography.encode(image, out_path, text)
    print("Message sent... ")
    text = "You : " + text
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "send_by_me": True
    }
    Friends[selection]["Chats"].append(new_chat)


#####receiving message#####

def read_message():
    selection = select_a_friend()
    image = raw_input("Name of image to be decoded : ")
    text = Steganography.decode(image)
    text = Friends[selection]["Name"] + " : " + text
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "send_by_me": False
    }
    Friends[selection]["Chats"].append(new_chat)
    print(text)


user=raw_input("Do you want to continue with the default user ?(Y/N)")
new_user=0
if user=="Y":
    from spy_details import spy

    print('Welcome,%s  %s with %d years of age and %.1f rating. Welcome to SpyChat.... ' % (spy["Salutation"], spy["Name"], spy["age"], spy["Rating"]))
else:
    new_user=1
    entry()  ######taking details of new user
STATUS_MESSAGE=['You are in...', 'How are you..?', 'Lets move further']
Friends=[]
spy_chat()

####################

