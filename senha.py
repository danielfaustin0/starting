# programa para validar senha
    fazer_login(acesso)

class SistemadeLogin:
    def __init__ (self):
        self.senha_cadastrada = None
        self.senha_confirmada = None
        self.senha_acesso = None
        self.tentavivas = 0
    
    def cadastrar_senha(self):
        # programar a lógisca para cadastro
        while (self.tentavivas < 3):
            self.senha_cadastrada = input("Informe a senha: ")

            if len(self.senha_cadastrada) >= 8:
                if any(digit.isdigit() for digit in self.senha_cadastrada):
                    print("Senha salva!\nConfirme a senha: ")
                    self.senha_confirmada = input()

                    if self.senha_cadastrada == self.senha_confirmada:
                        print("SENHA SALVA!")
                        self.tentavivas = 0
                        return self.senha_cadastrada
                    else:
                        print("As senhas devem ser idênticas.")
                else:
                    print("A senha deve ter pelo menos um número.")
            else:
                print("A senha deve ter pelo menos 8 dígitos")
            self.tentavivas += 1
            print(f"tentativa:{self.tentavivas}/3")
        else:
            print("ACESSO BLOQUEADO!")


    def acesso_sistema(self):
        # programar a lógica de acesso ao sistema
        if not self.senha_cadastrada:
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

sistema = SistemadeLogin()
sistema.cadastrar_senha()
sistema.acesso_sistema()