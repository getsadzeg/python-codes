class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def display(self):
        print self.username
        print self.password
 
 
if __name__ == "__main__":
    usr = User("guri", "password")
    usr.display()