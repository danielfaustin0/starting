# programa para validar senha
class SistemaDeLogin:
    def __init__ (self):
        self.senha_cadastrada = None
        self.senha_confirmada = None
        self.senha_acesso = None
        self.tentavivas = 0
        self.msg_bloqueio = "ACESSO BLOQUEADO"
    
    def cadastrar_senha(self):
        # programar a lógisca para cadastro
        while (self.tentavivas < 3):
            self.senha_cadastrada = input("Informe a senha: ")

            if len(self.senha_cadastrada) >= 8 and any(digit.isdigit() for digit in self.senha_cadastrada):
                print("Senha salva!")
                self.tentavivas=0
                return self.senha_cadastrada
            else:
                print("Senha inválida!\nA senha deve ter pelo menos 8 dígitos e um número.")
            self.tentavivas += 1
            print(f"tentativa:{self.tentavivas}/3")
        else:
            print(self.msg_bloqueio)

    def validar_senha(self):
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
            print(self.msg_bloqueio)


    def acesso_sistema(self):
        # programar a lógica de acesso ao sistema
        if not self.senha_confirmada:
            print("Nenhuma senha salva. Programa encerrado.")
            return
        while self.tentavivas < 3:
            print("ACESSO AO SISTEMA")
            self.senha_acesso = input("SENHA: ")

            if (self.senha_acesso == self.senha_cadastrada):
                print("ACESSO LIBERADO")
                break
            else:
                print("Senha inválida.")
            self.tentavivas += 1
            print(f"Tentativa: {self.tentavivas}/3")
        else:
            print("PROGRAMA ENCERRADO")

sistema = SistemaDeLogin()
sistema.cadastrar_senha()
sistema.validar_senha()
sistema.acesso_sistema()