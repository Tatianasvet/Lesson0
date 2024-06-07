from time import sleep


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
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for member in self.users:
            if member.nickname == login:
                if member.password == hash(password):
                    self.current_user = member

    def register(self, nickname, password, age):
        new_user = self.find_user(nickname)
        if new_user is not None:
            print(f'Пользователь {new_user} уже существует')
            self.current_user = new_user
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def find_user(self, nickname):
        for user in self.users:
            if user.nickname == nickname:
                return user
        return None

    def log_out(self):
        self.current_user = None

    def add(self, videos):
        for video in videos:
            if type(video) is Video:
                self.videos.append(video)

    def get_videos(self, search):
        find_videos = []
        for video in self.videos:
            if search.lower() in video.title.lower():
                find_videos.append(video.title)
        return find_videos

    def find_video(self, title):
        for video in self.videos:
            if video.title == title:
                return video
        return None

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт чтобы смотреть видео')
        else:
            video = self.find_video(title)
            if video is not None:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for video.time_now in range(1, video.duration + 1):
                        sleep(1)
                        print(video.time_now, end=' ')
                    video.time_now = 0
                    print('Конец видео')
