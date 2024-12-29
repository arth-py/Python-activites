class Pessoa:
  def __init__(self,nome,endereço,cpf):

    self.__nome = nome
    self.__endereço = endereço
    self.__cpf = cpf
    self.gato = None
  
  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self,nome):
    self.__nome = nome

  @property
  def endereço(self):
    return self.__endereço

  @endereço.setter
  def endereço(self,endereço):
    self.__endereço = endereço

  @property
  def cpf(self):
    return self.__cpf

  def adotar_gato(self,gato):
    if not gato.tem_dono:
       self.gato = gato
       gato.tem_dono = True
       # IMPRIME SOMENTE O ATRIBUTO 'NOME' DO GATO, CASO EXISTAM MAIS ATRIBUTOS NO __STR__
       return f'Gato {self.gato.nome} Adotado!'
    else:
      return "Gato já tem dono!"
    
  def __str__(self):
        return self.__nome

class Gato:
    def __init__(self,nome,peso,idade,raca):
        self.__nome = nome
        self.__peso = peso
        self.__idade = idade
        self.__raca = raca
        self.__tem_dono = False

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def peso(self):
        return self.__peso

    @property
    def idade(self):
        return self.__idade

    @property
    def raca(self):
        return self.__raca

    @property
    def tem_dono(self):
        return self.__tem_dono

    @tem_dono.setter
    def tem_dono(self,tem_dono):
        self.__tem_dono = tem_dono

    def __str__(self):
       return self.__nome
    
def main():
  pessoa1 = Pessoa('Sandra','Rua das Orquídeas',8783491368)
  gato1 = Gato('Scat',1.85,4,'Siamês')
  print(pessoa1.adotar_gato(gato1))
  print(pessoa1)
  print(gato1)
  

if __name__ == '__main__':
  main()