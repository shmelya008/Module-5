class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
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

    def log_in(self, nickname, password):  # пытается найти пользователя в users с такими же логином и паролем.
        # Если такой пользователь существует, то current_user меняется на найденного.
        # Помните, что password передаётся в виде строки, а сравнивается по хэшу.

        pass

    def register(self, nickname, password, age):  # добавляет пользователя в список, если пользователя не существует
        # (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        # После регистрации, вход выполняется автоматически.
        pass

    def log_out(self):  # сброс текущего пользователя на None.

        pass

    def add(self, *video):  # принимает неограниченное кол-во объектов класса Video и все добавляет в videos.
        # Если объект с таким же названием видео ещё не существует. В противном случае ничего не
        # происходит.
        if video not in self.videos:
            self.videos.append(video)
        return self.videos

    def get_videos(self, search_word):  # принимает поисковое слово и возвращает список названий всех видео,
        # содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best'
        # (не учитывать регистр).
        # for i in self.videos:
        #     v_list = []
        #     if i in self.videos == search_word.lower():
        #         v_list.append(i)
        #     return v_list
        pass

    def watch_video(self):  # принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        # то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        # После текущее время просмотра данного видео сбрасывается.

        pass


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.videos)
