class Pessoa:
    listador = []


    def __init__(self,nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


    def __str__(self):
        return f"nome: {self.nome}, idade: {self.idade} anos, sexo: {self.sexo}"
    

    def criador(lista):
        nome = str(input('insira o nome: '))
        idade = int(input('insira a idade: '))
        sexo = str(input('insira o sexo: '))
        p = Pessoa(nome, idade, sexo)
        lista.append([p.nome, p.idade, p.sexo])


    def substituidor(lista):
        localizacao = int(input('insira a posição do objeto a ser alterado: '))
        if localizacao < len(lista):
            nome = str(input('insira o nome: '))
            idade = int(input('insira a idade: '))
            sexo = str(input('insira o sexo: '))
            p = Pessoa(nome, idade, sexo)
            try:
                lista.pop(localizacao)
                lista.insert(localizacao, [p.nome, p.idade, p.sexo])
            except:
                print('localização inválida ')
        else:
            print('a lista não possui esta posição preenchida, use a função ADICIONAR OBJETO')


    def deletador(lista):
        localizacao = int(input('insira a posição do objeto a ser deletado: '))
        try:
            lista.pop(localizacao)
        except:
            print('localização inválida ')
