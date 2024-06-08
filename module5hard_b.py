from time import sleep


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def log_in(self, login, password):
        if login in self.users.keys():
            user = self.users[login]
            if user.password == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):
        if nickname in self.users.keys():
            print(f'Пользователь {nickname} уже существует')
            self.log_in(nickname, password)
        else:
            self.current_user = self.users[nickname] = User(nickname, password, age)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if type(video) is Video:
                if video.title not in self.videos.keys():
                    self.videos[video.title] = video

    def get_videos(self, search_title):
        found_videos = []
        for title in self.videos.keys():
            if search_title.lower() in title.lower():
                found_videos.append(title)
        return found_videos

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт чтобы смотреть видео')
        else:
            if title in self.videos.keys():
                video = self.videos[title]
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for video.time_now in range(1, video.duration + 1):
                        sleep(1)
                        print(video.time_now, end=' ')
                    video.time_now = 0
                    print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
