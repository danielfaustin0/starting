# programa para validar senha

# Permitir que o usuário tenha três chances para cadastrar a senha
chance = 0

while chance < 3:
    senha = input("Informe a senha: ")

    # Verificar se a senha tem mais de 8 dígitos
    if len(senha) >= 8:
        # verifica se a senha tem pelo menos um número
        if any(char.isdigit() for char in senha):
            # Imprime mensagem de que a senha é válida
            print("Senha válida!")
            break
        else:
            # Imprime mensagem de que a senha é inválida por falta de número
            print("Senha inválida - Precisa conter pelo menos um número")
            #incrementar chance
            chance += 1
    else:
        # Imprime mensagem de que a senha é inválida por caracteres insuficientes
        print("Senha inválida - Precisa de pelo menos 8 dígitos")
        #incrementar chance
        chance += 1
else:
    print("ACESSO BLOQUEADO")
