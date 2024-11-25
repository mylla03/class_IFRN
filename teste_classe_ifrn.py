# Definição da superclasse
class Integrante_IFRN:
    def exibirMensagem(self):
        print("Integrante_IFRN: Seja bem vindo(a) ao IFRN!!!")

# Definição da subclasse Professor
class Professor(Integrante_IFRN):
    def exibirMensagem(self):
        print("Professor: Meus alunos são os melhores!!!")

# Definição da subclasse Aluno
class Aluno(Integrante_IFRN):
    def exibirMensagem(self):
        print("Aluno: Vou estudar pra tirar 100 em POO!!!")

# Testando as classes
integrante = Integrante_IFRN()
professor = Professor()
aluno = Aluno()

# Chamando os métodos
integrante.exibirMensagem()
professor.exibirMensagem()
aluno.exibirMensagem()
