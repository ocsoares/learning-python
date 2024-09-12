from person_data import PersonData


class Worker(PersonData):
  def __init__(self, name, age, country):
    super().__init__(name, age, country)  # A classe pai já ATRIBUI
