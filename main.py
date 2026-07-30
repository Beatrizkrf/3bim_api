from fastapi import FastAPI #importaçãoda biblioteca
app= FastAPI() #criando o objeto


@app.get('/') #@ objeto e metodo (decorator) dentro dos parenteses é a rota
def ola_mundo():
    return {'mensagem': 'Minha primeira API em FastAPI!'}

@app.get('/clientes') #@ objeto e metodo (decorator) dentro dos parenteses é a rota
def Clientes():
    return {'mensagem': 'Lista de clientes'}    