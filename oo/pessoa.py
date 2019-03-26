class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=0):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, menu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return "42"

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f' {cumprimentar_da_classe} - Aperto de mão'


class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    galo = Mutante(nome='galo')
    william = Homem(galo, nome='William')
    print(william.cumprimentar())
    print(william.nome)
    for filho in william.filhos:
        print(filho.nome)
    william.sobrenome = "campolina"
    galo.olhos = 1
    del galo.olhos
    print(william.__dict__)
    print(galo.__dict__)
    #Pessoa.olhos = 3
    print(galo.olhos)
    print(william.olhos)

    print(Pessoa.olhos)

    print(Pessoa.metodo_estatico(), galo.metodo_estatico())

    print(Pessoa.nome_e_atributos_de_classe(), galo.nome_e_atributos_de_classe())



    pessoa = Pessoa()
    print( isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(galo, Pessoa))
    print(isinstance(galo, Homem))

    print(galo.olhos)

    print(galo.cumprimentar())
    print(william.cumprimentar())
    # william.
