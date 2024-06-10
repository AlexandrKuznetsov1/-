
# Общее ТЗ:
# Реализовать классы для взаимодействия с платоформой, каждый из которых будет содержать методы добавления видео,
# авторизации и регистрации пользователя и т.д.

# Всего будет 3 класса: UrTube, Video, User.

# Подробное ТЗ:

# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
# Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)

# Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя в users
# с такмими же логином и паролем. Если такой пользователь суещствует, то current_user меняется на найденного.
# Помните, что password передаётся в виде строки, а сравнивается по хэшу.

# Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
# если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname}
# уже существует". После регистрации, вход выполняется автоматически.

# Метод log_out для сброса текущего пользователя на None.

# Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
# если с таким же названием видео ещё не существует. В противном случае ничего не происходит.

# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
# Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).

# Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
# то ничего не воспроизводится, если же находит ведётся отчёт в консоль на какой секунде ведётся просмотр.
# После текущее время просмотра данного видео сбрасывается.


# Для метода watch_video так же следует учитывать следущие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.

# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
# В противном случае выводить в консоль надпись: "Войдите в аккаунт чтобы смотреть видео"

# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
# Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"

# После воспроизведения нужно выводить: "Конец видео"

import time

#  в ходе реализации кода, возникла необходимость создания изначально пустых глобальных переменных,
#  которые будут использоваться для сравниваемых значений
name_video = []  # для сохранения названий видео
def watch_video(*args):
    return ur.watch_video(*args)

class Video:
    """
    Класс содержит атрибуты: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        name_video.append(self.title)

    def get_title(self):
        return self.title

    # def __str__(self):
        # return f'{self.title}'


class User:
    """
    Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    """
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def get_nickname(self):
        return self.nickname

    def get_hash(self):
        return self.password

    def get_age(self):
        return self.age

    def __str__(self):
        return f'Имя: {self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password


class UrTube:
    """
    Класс содержит атрибуты: users(список объектов User), videos(список объектов Video),
    current_user(текущий пользователь, User)
    """
    users = []
    videos = {}  # список видео организован в виде словаря, где ключ - название фильма, значение,- объект видео
    current_user = None

    def log_in(self, nickname: str, password: str):
        """Метод log_in, который принимает на вход аргументы: login, password
        и пытается найти пользователя в users с такмими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу."""
        password = hash(password)
        chek_user = User(nickname, password, None)
        for user in self.users:
            if user == chek_user:
                self.current_user = user

    def register(self, nickname: str, password: str, age: int):
        """Метод register, который принимает три аргумента: nickname, password, age,
        и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически."""
        nickname = nickname
        password = hash(password)
        age = age
        us = User(nickname, password, age)
        lst_ = [u for u in self.users]
        lst_nick = []
        for nick in lst_:
            lst_nick.append(User.get_nickname(nick))
        if us.nickname not in lst_nick:
            self.users.append(us)
            self.current_user = us
            self.__str__()
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        """Метод log_out для сброса текущего пользователя на None."""
        self.current_user = None

    def add(self, *args):
        """Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        если с таким же названием видео ещё не существует. В противном случае ничего не происходит."""
        # print(self.videos)
        # print(self)
        for k in name_video:
            # print(k)
            if k not in self.videos:
                for i in args:
                    # print(i.__dict__)
                    title_args = i.__dict__
                    # print(title_args.values())
                    for j in title_args.values():
                        if j == k:
                            # print(j)
                            self.videos[j]=i
                            # print(self.videos)



    def get_videos(self, word: str):
        """Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
        содержащих поисковое слово. Следует учесть, что слово 'UrbaN'
        присутствует в строке 'Urban the best' (не учитывать регистр)."""
        list_title = []
        for i in self.videos.keys():
            if word.lower() in i.lower():
                list_title.append(i)
        return list_title

    def watch_video(self, title_video: str):
        """Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится, если же находит, ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.
        """
        if not ur.current_user:
            print('Войдите в аккаунт чтобы смотреть видео')
        else:
            # print(self.videos)
            for i in self.videos.keys():
                if title_video == i:
                    # print(i)
                    current_video = self.videos.get(i)
                    # print(current_video.__dict__)
                    if ur.current_user.get_age() < 18:
                        for j in current_video.__dict__:
                            # print(j)
                            if j == 'adult_mode' and current_video.__dict__.get(j) == True:
                                print('Вам нет 18 лет, пожалуйста покиньте страницу')

                    else:
                        sec = 0
                        for j in current_video.__dict__:
                            # print(j)
                            if j == 'duration':
                                video_duration = current_video.__dict__.get(j)
                                # print(video_duration)
                                while video_duration > sec:
                                    time.sleep(1)
                                    sec += 1
                                    time_now = sec
                                    print(time_now, end=' ')
                                time_now = 0
                                print('Конец видео')


# Код для проверки:
ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
watch_video('Лучший язык программирования 2024 года!')





