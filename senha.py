# programa para validar senha

def cadastrar_senha():
    # Permitir que o usuário tenha três chances para cadastrar a senha
    chance = 0

    while chance < 3:
        senha = input("Informe a senha: ")

        # Verificar se a senha tem mais de 8 dígitos
        if len(senha) >= 8:
            # verifica se a senha tem pelo menos um número
            if any(char.isdigit() for char in senha):
                # Valida a senha e pede para o usuário confirmar
                confirma = input("Senha salva!\nConfirme a senha: ")

                if (confirma == senha):
                    print("Cadastro liberado. Efetue login.")
                    return senha
                else:
                    print("As senhas devem ser idênticas.")
                    chance += 1
                
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
        return None

def fazer_login(senha):
    # Checando a senha salva e validando o acesso
    chance = 0

    while chance < 3:
        print("\nACESSO AO SISTEMA")
        senha_acesso = input("SENHA: ")

        if (senha_acesso == senha):
            print("ACESSO LIBERADO")
            break
        else:
            print("Senha inválida. Cheque e tente novamente.")
            chance +=1
    else:
        print("ACESSO BLOQUEADO")

acesso = cadastrar_senha()
if acesso:
    fazer_login(acesso)