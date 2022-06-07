class Usuario:

    #constructor
    def __init__(self, username, password):
        #Añadiendo attrs al objeto
        self.username = username
        self.password = password


user1 = Usuario('User1','1234')
user2 = Usuario('User2','4567')

print(user1.__dict__)
print(user2.__dict__)