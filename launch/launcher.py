from setup.info import Profile
from storage.storage import Storage
from interaction.interact import Interaction


class Launcher:

    def start(self):

        profile = Storage.load("profile")

        if profile is None:

            user = Profile()

            user.collect_info()

            Storage.save("profile", user.to_dict())

            user.display_info()

        else:

            
            print(f"Welcome back, {profile['name']}!")

            interaction = Interaction(profile)

            today = interaction.start()

            print(f"\nGot it. You're working on: {today}")