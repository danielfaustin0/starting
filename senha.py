# programa para validar senha
senha = input("Infomre a senha: ")

# Verificar se a senha tem mais de 8 dígitos
if len(senha) >= 8:
    # verifica se a senha tem pelo menos um número
    if any(char.isdigit() for char in senha):
        # Imprime mensagem de que a senha é válida
        print("Senha válida!")
    else:
        # Imprime mensagem de que a senha é inválida por falta de número
        print("Senha inválida - Precisa conter pelo menos um número")
else:
    # Imprime mensagem de que a senha é inválida por caracteres insuficientes
    print("Senha inválida - Precisa de pelo menos 8 dígitos")

