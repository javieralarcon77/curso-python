def operacion(cantidad, balance, tipo='deposito'):

    def deposito(cantidad, balance):
        return cantidad + balance

    
    def retiro(cantidad, balance):
        if cantidad >= balance:
            return cantidad - balance
        else:
            return None

    
    return deposito(cantidad, balance) if tipo == 'deposito' else retiro(cantidad, balance)


resultado = operacion(30, 20, 'retiro')
print(resultado)