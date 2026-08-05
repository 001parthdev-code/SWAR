from zoneinfo import ZoneInfo
from datetime import datetime

class Profile:
    def __init__(self):
        self.name = None
        self.date_of_birth = None
        self.language = None
        self.local_timezone = None
        self.datetime = None

    def collect_info(self):
        print("Welcome to SWAR!")
        print("Let's get you set up\n")

        self.name = input("What should I call you?")
        self.date_of_birth = input("When's yout birthday?")
        self.language = input("What language do you speak?")

        self.local_timezone =  datetime.now().astimezone().tzinfo
        self.datetime =  datetime.now().astimezone()

    def display_info(self):
        print("------USER INFO------")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Datetime: {self.datetime}")
        print(f"Timezone: {self.local_timezone}")
        print(f"Language: {self.language}")


    def to_dict(self):
        return {
        "name": self.name,
        "date_of_birth": self.date_of_birth,
        "language": self.language,
        "timezone": str(self.local_timezone),
        "datetime": str(self.datetime)
    }