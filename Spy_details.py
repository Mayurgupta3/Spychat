from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Mayur', 'Mr.', 21, 4.5)

friend_one = Spy('Badshah', 'Mr.', 4.9, 27)
friend_two = Spy('Sonam Gupta', 'Ms.', 4.39, 21)
friend_three = Spy('Sanket', 'Dr.', 4.95, 37)


friends = [friend_one, friend_two, friend_three]