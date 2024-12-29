'''Com base na classe Pessoa descrita link abaixo:
1. Altere o código de forma a impedir que uma pessoa "casada"  possa se casar novamente. Exceções: Quando a pessoa se tornar "viúva" ou "divorciada"
2. Crie um método: "ter_filhos". Condição para este método ser executado:
a) Pessoa ser do sexo: "Feminino"
b) Segunda pessoa ser do sexo: "Masculino" . Ex: maria.ter_filho(joao), nesse caso maria é um objeto do tipo "Pessoa" do sexo: "feminino" e joao é um objeto do tipo "Pessoa" do sexo: "masculino". Esse método tem que retornar um novo objeto do tipo "Pessoa" 
c) acrescentar os atributos: Pai e Mãe (tipo: Pessoa).'''

class Pessoa:
  def __init__(self,nome,idade,peso,altura,sexo,estado="vivo",est_civil="solteiro",mãe=None):
    self.__nome = nome
    self.__idade = idade
    self.__peso = peso
    self.__altura = altura
    self.__sexo = sexo
    self.__estado = estado
    self.__est_civil = est_civil
    self.__mãe = None
    self.__pai = None
    self.__mãe_adotiva = None
    self.__pai_adotivo = None
    self.__conjuge = None
    self.filhos = []

  @property
  def nome(self):
    return self.__nome

  @property
  def conjuge(self):
    return self.__conjuge

  @property
  def est_civil(self):
    return self.__est_civil

  @nome.setter
  def nome(self,valor):
    if self.__est_civil == "casado":
      nome_antigo = self.__nome.split(" ")
      nome_conjuge = self.__conjuge.nome.split(" ")
      novo_nome = valor.split(" ")
      for i in novo_nome:
        if (i not in nome_antigo) and (i not in nome_conjuge):
           print("nome inválido!")
           return
      self.__nome = valor
      print ("Alteração efetuada com sucesso!")

  def casar(self,conjuge):
    if self.__est_civil == 'casado':
        return 'Indivíduo já casado!'
    else:
        self.__est_civil = "casado"
        if type(conjuge) == Pessoa:
            self.__conjuge = conjuge
            self.__conjuge.__est_civil = "casado"
            self.__conjuge.__conjuge = self
            return f'{self.__nome.capitalize()} casou! Parabéns!'

  def morrer(self):
    self.__estado = 'morto'
    return self.__estado
    

  def divorciar(self):
    if self.__est_civil == 'casado':
        self.__est_civil = 'divorciado'
        self.__conjuge.__conjuge = self
        return self.__est_civil
    else:
      return 'Indvivíduo não casado, não sendo possível divorciar'

  def ter_filhos(self,pessoa):
    if self.__sexo == 'F':
        self.filhos.append(pessoa)
        pessoa.__mãe = self
        pessoa.__pai = self.__conjuge
        return f'Filho {pessoa.__nome} Adicionado!'
    else:
       return 'Necessário ser do sexo feminino para ter um filho'

  def adotar_filhos(self,criança): #condição: criança ser órfã.
    if criança.__mãe == None and criança.__pai == None:
        self.filhos.append(criança)
        criança.__mãe_adotiva = self
        criança.__pai_adotivo = self.__conjuge
        return f'Filho {criança.__nome} Adotado'
    else:
       return 'A criança não é orfã'

  def __str__(self):
    return (
        f'{self.__nome}\n'
        f'{self.__idade}\n'
        f'{self.__peso}\n'
        f'{self.__altura}\n'
        f'{self.__sexo}\n'
        f'{self.__estado}\n'
        f'{self.__est_civil}\n'
        f'{self.__mãe}\n'
        f'{self.__pai}\n'
        f'{self.__mãe_adotiva}\n'
        f'{self.__pai_adotivo}\n'
        f'{self.__conjuge.nome}\n'
        f'{for i in range(len(self.filhos)): print(self.filhos[i])}'
            
    )


####### execução ########

maria = Pessoa("Maria",30,65,1.7,'F')
francisca = Pessoa("Francisca",65,60,1.6,'F')
joao = Pessoa("Joao",55,60,1.8,'M') # joão -> solteiro
print(maria.casar(joao)) # joão e maria -> casado
print(maria.casar(francisca))
print(maria.divorciar())
print(maria.morrer())
lucas= Pessoa('Lucas',0,4.4,0.38,'M')
print(maria.ter_filhos(lucas))
print(francisca.adotar_filhos(lucas))
print(maria)
'''

maria.morrer() # maria para para o estado de morto.
joao.casar(ana) # joao e ana -> casado
joao.ter_filhos(maria) # Erro! maria está morta.
julia = ana.ter_filhos(joao)
'''

#simular processo de adoção