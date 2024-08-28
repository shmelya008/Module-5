from time import sleep


class User:
    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title: str, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = User

    def log_in(self, nickname, password):
        # if nickname in self.users and hash(password) == ???:   # Вообще нет идей :(
        #      self.current_user = nickname
        # else:
        #     print('Неверный пароль')
        pass

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users.append(nickname)
            self.users.append(password.__hash__())
            self.current_user = nickname
            self.users.append(age)
            if age < 18:
                self.current_user = 'underage'  # В блоке проверки возраста тоже что-то не так.
                # Как установить невидимую метку?
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        list_video = [*video]
        for i in list_video:
            if i not in self.videos:
                self.videos.append(i)
        return self.videos

    def get_videos(self, search_word):
        v_list = []
        for i in self.videos:
            if search_word.lower() in i.title.lower():
                v_list.append(i.title)
        return v_list

    def watch_video(self, movie_title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for movie in self.videos:
                if movie_title in movie.title:
                    if movie.adult_mode is True and self.current_user == 'underage':
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        break
                    for i in range(movie.duration):
                        print(i + 1, end=' ')
                        movie.time_now += 1
                        sleep(1)
                    print('Конец видео')
                    movie.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 4, adult_mode=True)
v3 = Video('Язык программирования 2022 года', 12)

# print(v1.title)
# print(v3.duration)

# Добавление видео
ur.add(v1, v2)
ur.add(v2)
ur.add(v1, v3)

# Проверка поиска
print(ur.get_videos('Лучший'))
print(ur.get_videos('ПРОГ'))

# # Проверка на вход пользователя и возрастное ограничение
ur.log_out()
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# ur.log_in('vasya_pupkin', 'kjhkhkhkh')
# ur.log_in('vasya_pupkin', 'lolkekcheburek')
# print(ur.current_user)

