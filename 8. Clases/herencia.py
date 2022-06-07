from calendar import c


class Mascota: #Clase padre
    
    def __init__(self, name = 'La mascota'):
        self.name = name

    def comer(self):
        print(f'{self.name} come')

    def dormir(self):
        print(f'{self.name} duerme')


class Felino:

    def cazar(self):
        print('El felino caza')


class Perro(Mascota): # Clase Hija
    pass


class Gato(Mascota, Felino):
    
    def dormir(self):
        print('El gato duerme ronrroneando')

duke = Perro('Duke')
duke.comer()
duke.dormir()

patricio = Gato('Patricio')
patricio.comer()
patricio.dormir()
patricio.cazar()