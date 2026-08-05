from setup.info import Profile
from storage.storage import Storage


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