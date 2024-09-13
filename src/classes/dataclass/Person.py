from dataclasses import dataclass


@dataclass
class Person:
  name: str
  age: int
  country: str
  is_working: bool

  def show_info(self):
    print(
      f"name: {self.name}, age: {self.age}, country: {self.country}, isWorking: {self.is_working}")


person = Person("Hugo", 21, "Brazil", True)
person.show_info()
