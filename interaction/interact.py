from datetime import datetime

class Interaction:

    def __init__(self,user):
        self.user = user 
        self.current_time = datetime.now().astimezone()

    def get_greetings(self):
        hour = self.current_time.hour

        if hour<12:
            return "Good morning"
        elif hour < 17:
            return "Good afternoon"
        else:
            return "Good evening"

    def start(self):
        greeting = self.get_greetings()

        print(f"\n{greeting}, {self.user['name']}.")
        print("What are you doing today?")

        response = input("> ")

        return response
    

        
