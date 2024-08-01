#Defina um usuário e senha e depois verifique se 
#login do usuário é valido.

usuario = "wikten"
senha = "wikten123"

while True:
    usuario_log = input("Digite o usuário: ")
    senha_log = input("Digite a senha")
    
    if usuario == usuario_log and senha == senha_log:
        print("Login efetuado com sucesso!")
        break
    else:
        print("Senha ou usuárion inválido, tente novamente.")
    