class PersonData:
  def __init__(self, name, age, country):
    self.name = name
    self.age = age
    self.country = country

  # Faz ler o OBJETO em String, se não sai com Hexadecimais lá !!
  def __str__(self):
    return f'Worker(name={self.name}, age={self.age}, country={self.country})'
