from Setup.info  import Info
from Storage.storage import Storage


user = Info()

user.collect_info()

Storage.save("profile", user.to_dict())

user.display_info()