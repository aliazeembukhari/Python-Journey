class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name


class Message:
    def __init__(self, sender, content):
        self.sender = sender   
        self.content = content
    def __str__(self):
        return f"{self.sender}: {self.content}"


class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []
    def join(self, user):
        self.users.append(user)
        print(f"{user} joined the chat")
    def leave(self, user):
        self.users.remove(user)
        print(f"{user} left the chat")
    def send_message(self, user, content):
        if user in self.users:
            msg = Message(user, content)
            self.messages.append(msg)
        else:
            print("User not in chat room!")
    def show_history(self):
        print("\nChat History:")
        for msg in self.messages:
            print(msg)

user1 = User("Ali")
user2 = User("Azeem")

chat = ChatRoom()

chat.join(user1)
chat.join(user2)

chat.send_message(user1, "Hi there!")
chat.send_message(user2, "Hello Ali!")

chat.show_history()

chat.leave(user1)