# programa para validar senha
class SistemaDeLogin:
    def __init__ (self):
        self.senha_cadastro = None
        self.senha_acesso = None
        self.tentavivas_cadastro = 0
        self.tentavivas_acesso = 0
        self.msg_bloqueio = "ACESSO BLOQUEADO"
    
    def cadastrar(self):
        # programar a lógisca para cadastro
        while (self.tentavivas_cadastro < 3):
            senha1 = input("Informe a senha: ")

            if len(senha1) >= 8 and any(digit.isdigit() for digit in senha1):
                # Confirmar senha
                senha2 = input("Confirme a senha:\n")
                if (senha1 == senha2):
                    print("Senha salva!")
                    self.senha_cadastro = senha1
                    return self.senha_cadastro
                else:
                    print("As senhas devem ser identicas.")
            else:
                print("Senha inválida!\nA senha deve ter pelo menos 8 dígitos e um número.")
            self.tentavivas_cadastro += 1
            print(f"tentativa:{self.tentavivas_cadastro}/3")
        else:
            print(self.msg_bloqueio)
            return

    '''def validar_senha(self):
        # Validar senha cadastrada
        if not self.senha_cadastrada:
            return

        while (self.tentavivas < 3):
            self.senha_confirmada = input("Confirme a senha:\n")

            if (self.senha_cadastrada == self.senha_confirmada):
                print("SENHA SALVA!")
                self.tentavivas = 0
                return self.senha_confirmada
            else:
                print("As senhas devem ser idênticas.")
            self.tentavivas += 1
            print(f"Tentivas: {self.tentavivas}/3")
        else:
            print(self.msg_bloqueio)'''


    def acessar(self):
        # programar a lógica de acesso ao sistema
        if not self.senha_cadastro:
            print("Nenhuma senha salva. Programa encerrado.")
            return
        while self.tentavivas_acesso < 3:
            print("ACESSO AO SISTEMA")
            self.senha_acesso = input("SENHA: ")

            if (self.senha_acesso == self.senha_cadastro):
                print("ACESSO LIBERADO")
                break
            else:
                print("Senha inválida.")
            self.tentavivas_acesso += 1
            print(f"Tentativa: {self.tentavivas_acesso}/3")
        else:
            print("PROGRAMA ENCERRADO")

sistema = SistemaDeLogin()
sistema.cadastrar()
sistema.acessar()