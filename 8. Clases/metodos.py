class Usuario:

    def inicializar(self, username, password):
        #Añadiendo attrs al objeto
        self.username = username
        self.password = password


user1 = Usuario()
user2 = Usuario()

user1.inicializar('User1','1234')
user2.inicializar('User2','4567')

print(user1.__dict__)
print(user2.__dict__)