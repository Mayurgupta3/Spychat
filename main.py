#This is for importing Spy, spy, ChatMessage from the Spy_details
from Spy_details import Spy, spy, ChatMessage, friends

#This is for importing steganography form the steganography
from steganography.steganography import Steganography

#This is for importing datetime from datetime
from datetime import datetime

#This is for importing colored from termcolor
from termcolor import colored


#Here are some Status where we can easily add
status_message = ['Hey there, I am using Spychat','Battery Down','Call Only','can\'t talk']

#This message is come, when we run the program
print colored('Hello! You are using SpyChat program.I hope you like it.' , 'red')
print colored('Let\'s Start the program','blue')

#Here we are ask from the user to continue with existing user or u want to continue with another one
question = 'Do you want to continue as  ' + spy.salutation + ' ' + spy.name+ '(Y/N)?'
existing = raw_input(question)

#This is add_status function, where we can add a new status or choose from the older one
def add_status():

    updated_status_message = None

    if spy.current_status_message != None:

        print 'Hi, Your current status message is %s \n' % spy.current_status_message
    else:
        print colored('Sorry!, You don\'t have any current status message','red')

    default = raw_input(colored('Do you want to select status from the older one (y/n)?','yellow'))

    if default.upper() == 'N':
        new_status_message = raw_input('From the above, Which status you want to set?')

        if len(new_status_message) > 0:
            status_message.append(new_status_message)
            updated_status_message=colored(new_status_message,'red')

    elif default.upper() == 'Y':

        position = 1

        for message in status_message:
            print '%d %s' % (position, message)
            position= position + 1

        message_selection=int(raw_input('Choose from the above one'))

        if len(status_message) >= message_selection:
            updated_status_message=status_message[message_selection-1]

    else:
            print colored('You choose invalid option. Please choose a valid one. Press Y or N' , 'red')

    if updated_status_message:
         print 'Your updated status message is this: %s' %(colored(updated_status_message,'blue'))
    else:
         print colored('you don\'t have any updated message','red')
    return updated_status_message


#This is add_friend function, where we add new friends in our friend's list
def add_friend():

    new_friend=Spy('','',0,0.0,)

    new_friend.name= raw_input('Add your Friend\'s Name')
    new_friend.salutation= raw_input('Are they Mr. or Ms.')

    new_friend.name= new_friend.salutation + ' ' +new_friend.name

    new_friend.age= int(raw_input('Enter the Age of your friend'))
    new_friend.rating= float(raw_input('enter rating of your friend'))


    #Here we are checking the age of the new friend
    if len(new_friend.name) >0 and new_friend.age > 12 and new_friend.rating>=spy.rating:
        friends.append(new_friend)
        print 'Friend Added'

    else:
        print colored('Sorry! We can\'t add this friend to your friends list','red')

    return len(friends)


#This is select_friend function, which is use to select friends from our existing list
def select_friend():
     item_number=0

     for friend in friends:
         print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name,
                                                                 friend.age,
                                                                 friend.rating)
         item_number = item_number + 1

     friend_choice = raw_input("Choose from your friends")

     friend_choice_position = int(friend_choice) - 1

     return friend_choice_position


#This is send_messgae function, which is use to send a secret message to a selected friend
def send_message():

    friend_choice = select_friend()

    original_image = raw_input('What is the name of the image?')
    output_path = 'output.jpg'
    text = raw_input('What do you want to say?')

    #This is condition where we are checking the length of the text
    if len(text) > 0:
        Steganography.encode(original_image, output_path, text)
        new_chat = ChatMessage(text, True)

        friends[friend_choice].chats.append(new_chat)

        print colored('Your secret message image is ready!', 'yellow')
    else:
        print colored('Please enter any valid message','red')





#This is read_message, which is use to read a secret message which is send by your friends
def read_message():

    sender = select_friend()

    output_path = raw_input('What is the name of the file?')

    secret_text = Steganography.decode(output_path)

    #This the case when the reciever in the danger and he/ she send word like SOS and save me
    if secret_text == 'sos' or secret_text == 'save me':
        print 'You are in danger! please terminate the program'
    elif len(secret_text) <= 0:
        print 'Sorry we cant print your message, because it is empty'
    else:
        print secret_text

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print 'Your secret message has been saved!'


#This is for reading the chat history
def read_chat_history():

    read_for = select_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print colored('[%s] %s: %s','red') % (chat.time.strftime("%d %B %Y"), colored('You said:','blue'), colored(chat.message),'yellow')
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


#This is a function to start a chat
def start_chat(spy):

    spy.name=spy.salutation+ ' ' +spy.name


    if spy.age > 12 and spy.age < 50:


        print 'Authentication complete. Welcome ' + spy.name + ' Age: ' + str(spy.age) + ' and Rating of: ' + str(
            spy.rating) + ' Proud to have you onboard'

        show_menu = True

        #Here is the menu choice where we choose what we want to do
        while show_menu:
            menu_choices = 'What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n'
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'


#This is for the existing one, when we enter the existing user
if existing == 'Y':
    start_chat(spy)
else:
    spy=Spy('','',0,0.0)
    spy.name = raw_input('Welcome to the program, Can I Have your Name Please')


    #here we are checking the length of the
    if len(spy.name) > 0:
        spy.salutation = raw_input('What i call you Mr. or Ms.')
        spy.age= int(raw_input('May i have your age please'))
        spy.rating = float(raw_input('your rating please'))
        spy_Online = True
        start_chat(spy)
    else:
        print ' enter a valid name'


