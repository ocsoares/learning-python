from person_data import PersonData
from worker import Worker


class App:
  person_data = PersonData("João", 26, "Brazil")
  worker = Worker("Guilherme", 19, "Portugal")

  def main(self):
    print("personData: ", self.person_data)
    print("personData: ", self.worker)


app = App()
app.main()
