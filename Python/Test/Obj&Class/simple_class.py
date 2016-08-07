class Users():
    name = "MyName"

    def set_name(self,id):

        if id == 1:
            self.name = 'YT'
        elif id == 2:
            self.name = 'Tony'

def load_user(id):
    user = Users()
    Users.set_name(user,id)
    return user

user = load_user(1)
print user.name
