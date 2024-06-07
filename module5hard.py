class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos =[]
        self.current_user = None

    def log_in(self, login, password):
        for member in self.users:
            if member.nickname == login:
                if member.password == hash(password):
                    self.current_user = member

    def register
