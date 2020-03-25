# Linguagem de Programação II
# Atividade Contínua 02 - Classes e Herança
#
# e-mail: thais.verissimo@aluno.faculdadeimpacta.com.br

"""
Implementar aqui as cinco classes filhas de Mamifero ou Reptil,
de acordo com o caso, conforme dado no diagrama apresentado no padrão UML.
Os atributos específicos de cada classe filha devem ser recebidos
como parâmetros no momento da criação, a única exceção é o número de vidas
do gato, que sempre começa em 7.
Os métodos de cada classe filha devem sempre RETORNAR uma string
no seguinte formato '<nome do animal> <método em questão no gerúndio>'
Sem nenhuma pontuação, conforme os exemplos a seguir.
Exemplo:
método trocar_pele() retorna '<nome> trocando de pele'
método dormir() retorna '<nome> dormindo'
método miar() retorna '<nome> miando'
Onde <nome> é o nome dado para cada animal (o valor atributo nome de
cada instância, não o nome da classe)
"""

class Reptil:
    """
    Classe mãe - não deve ser editada
    """
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return '{} ainda não atingiu maturidade sexual'.format(self.nome)

class Mamifero:
    """
    Classe mãe - não deve ser editada
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata

    def correr(self):
        return '{} correndo'.format(self.nome)

    def mamar(self):
        if self.idade <= 1:
            return '{} mamando'.format(self.nome)
        else:
            return '{} já desmamou'.format(self.nome)

class Camaleao(Reptil):
    """
    Exemplo de solução do exercício:
    Além dos atributos da classe mãe, possui o atributo:
    inseto_favorito, do tipo string.
    Implementa os métodos específicos:
    mudar_de_cor() e comer_inseto()
    """
    def __init__(self, nome, cor, idade, inseto_favorito):
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)

class Cavalo(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    cor_crina, do tipo string.
    Implementa os métodos específicos:
    galopar() e relinchar()
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata, cor_crina):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.cor_crina = cor_crina

    def galopar(self):
        return '{} galopando'.format(self.nome)

    def relinchar(self):
        return '{} relinchando'.format(self.nome)

class Cobra(Reptil):
    """
    Além dos atributos da classe mãe, possui o atributo:
    veneno, do tipo booleano.
    Implementa os métodos específicos:
    rastejar() e trocar_pele()
    """
    def __init__(self, nome, cor, idade, veneno):
        super().__init__(nome, cor, idade)
        self.veneno = veneno

    def rastejar(self):
        return '{} rastejando'.format(self.nome)

    def trocar_pele(self):
        return '{} trocando de pele'.format(self.nome)

class Cachorro(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    raca, do tipo string. (raça, porém sem o ç)
    Implementa os métodos específicos:
    latir() e rosnar()
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata, raca):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.raca = raca

    def latir(self):
        return '{} latindo'.format(self.nome)

    def rosnar(self):
        return '{} rosnando'.format(self.nome)

class Jacare(Reptil):
    """
    Além dos atributos da classe mãe, possui o atributo:
    num_dentes, do tipo inteiro.
    Implementa os métodos específicos:
    atacar() e dormir()
    """
    def __init__(self, nome, cor, idade, num_dentes):
        super().__init__(nome, cor, idade)
        self.num_dentes = num_dentes

    def atacar(self):
        return '{} atacando'.format(self.nome)

    def dormir(self):
        return '{} dormindo'.format(self.nome)

class Gato(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    vidas, do tipo inteiro.
    Implementa os métodos específicos:
    miar() e morrer()
    No método morrer, você deve verificar quantas vidas o gato ainda
    tem sobrando, se for igual a zero, retornar:
    '<nome> morreu'
    se ainda houver vidas sobrando, retirar uma vida (que começa em 7),
    e retornar:
    '<nome> tem <vidas> vidas sobrando'
    Onde <vidas> é o número de vidas restantes do gato em questão.
    """
    
    def __init__(self, nome, cor_pelo, idade, tipo_pata, vidas=7):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.vidas = vidas
                
    def miar(self):
        return '{} miando'.format(self.nome)

    def morrer(self):
        self.vidas -= 1
        if self.vidas <=0:
            return '{} morrreu'.format(self.nome)
        else:
            return '{} tem {} vidas sobrando'.format(self.nome, self.vidas)

def main():
    #Teste do Camaleao
    print("Teste do Camaleão:")
    Rafa=Camaleao("Rafa", "cinza", 7, "grilo")
    print(Rafa.__dict__)
    print(Rafa.comer_inseto())
    print(Rafa.mudar_de_cor())
    print(Rafa.tomar_sol())
    print(Rafa.botar_ovo())
    
    #Teste do Jacaré
    print("Teste do jacaré:")
    Mel=Jacare("Mel", "branco", 5, 81)
    print(Mel.__dict__)
    print(Mel.tomar_sol())
    print(Mel.botar_ovo())
    print(Mel.atacar())
    print(Mel.dormir())

    #Teste da Cobra
    print("Teste da Cobra:")
    Sogra=Cobra("Sogra", "verde", 3, True)
    print(Sogra.__dict__)
    print(Sogra.tomar_sol())
    print(Sogra.botar_ovo())
    print(Sogra.rastejar())
    print(Sogra.trocar_pele())

    #Teste do Cachorro
    print("Teste do Cachorro:")
    Lily=Cachorro("Lily", "preto", 4, "garra", "SRD")
    print(Lily.__dict__)
    print(Lily.correr())
    print(Lily.mamar())
    print(Lily.latir())
    print(Lily.rosnar())

    #Teste do Cavalo
    print("Teste do Cavalo:")
    Iran=Cavalo("Iran", "branco", 3, "Casco", "amarelo")
    print(Iran.__dict__)
    print(Iran.correr())
    print(Iran.mamar())
    print(Iran.galopar())
    print(Iran.relinchar())
    
    #Teste do Gato
    print("Iniciando os testes do Gato...")
    #Primeiro Gato chamada Cristal
    print("Primeiro teste do Gato:")
    Cristal=Gato("Cristal", "malhada", 5, "garra")
    print(Cristal.__dict__)
    print(Cristal.correr())
    print(Cristal.mamar())
    print(Cristal.miar())

    #Matando a Cristal 7 vezes com método de repetição e verificando 2 vezes se ela morreu
    print("{} nasceu com {} vidas".format(Cristal.nome, Cristal.vidas))
    # Essa primeira linha (anterior) serve para mostrar com quantas vidas Cristal foi criado
    print(Cristal.morrer())
    print(Cristal.morrer())
    print(Cristal.morrer())
    print(Cristal.morrer())
    print(Cristal.morrer())
    print(Cristal.morrer())
    print(Cristal.morrer())
    print(Cristal.morrer())
    print(Cristal.morrer())

    #Segundo gato chamado Faisca
    print("Segundo teste do Gato:")
    Faisca=Gato("Faisca", "preto", 1, "garra")
    print(Faisca.__dict__)
    print(Faisca.correr())
    print(Faisca.mamar())
    print(Faisca.miar())
    
    #Matando o Faisca 7 vezes com método de loop e verificando 2 vezes se ele morreu
    print("{} nasceu com {} vidas".format(Faisca.nome, Faisca.vidas))
    # Essa linha (anterior) serve para mostrar com quantas vidas Faisca foi criado
    for i in range(0, 9):
        print(Faisca.morrer())
        i=i-1

if __name__ == "__main__":
    main()
    
# fim dos testes           
