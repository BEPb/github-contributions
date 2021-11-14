"""
Python 3.9 Программа для изменения количества комментариев github
Название файла 'github_paint.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-06
"""

import argparse  # модуль для работы с аргументами python
import os  # для взаимодействия с командной строкой операционной системы
from datetime import datetime, date  # для обработки дат
from datetime import timedelta  # для вычислений разницы времени
from random import randint  # генерация произвольных чисел (дат)
from subprocess import Popen  # для запуска командной строки
from PIL import Image  # подключаем модуль для работы с изображениями

def process_image(path, directory):  # функция работы с рисунком 52x7
  img = Image.open(path)  # открываем рисунок
  px = img.load()  # создаем таблицу данных рисунка
  size = img.size  # получаем размер рисунка
  os.chdir(directory)  # переходим в эту папку
  if (52, 7) != size:  # Если рисунок не 52x7
    raise Exception("Рисунок должен быть 52x7, Ваш рисунок имеет размер: " + size)

  for x in range(size[0]):  # перемещаемся по рядам от 1 до 7
    print("Ведется работа над рядом №: ", x)  # печатаем № ряда
    for y in range(size[1]):  # перемещаемся по столбцам от 1 до 52
      val = 255 - int(rgb2gray(px[x, y]))  # преобразуем цвет в оттенок серого
      val /= 16  # оттенок серого преобразуем в значения от 1 до 4
      write_px(x, y, val)  # обращаемся к функции записи коммита

def write_px(x, y, intensity, prefix=""):  # записываем коммиты на git (координаты, интенсивность)
  days_ago = numdays + offset - (x*rows+y)  # дней назад = количество дней на странице + учитываем какой сегодня день
  # недели - смещение по оси х умноженное на число строк + у
  d = start_date - timedelta(days = days_ago)  # от сегодняшнего дня отнимаем количество дельта дней
  print("val=", intensity, "x", x, "y", y, "date:", d)  # выводим полученные данные
  intensity = int(intensity)
  for i in range(0, intensity):  # в зависимости от параметра интенсивности в этот день (определяется количество
    # коммитов)
    commit(days_ago)

def commit(days_ago):  # функция коментария (указываем на сколько дней назад делаем сдвиг, сообщение)
    date = start_date - timedelta(days=days_ago)  # высчитываем день начала рисунка (первого комментария)
    with open(os.path.join(os.getcwd(), 'README.md'), 'a') as file:  # открывает файл 'README.md'
        file.write(message(date) + '\n\n')  # дописывае дату, пропускает две строки
    run(['git', 'add', '.'])  # запускает в командной строке команды проверить файлы на изменение
    run(['git', 'commit', '-m', '"%s"' % message(date),
         '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])  # запускает в командной строке отправить комит по дате
    # при этом коммит подписывается датой внесения измениний


# преобразовываем цветной рисунок в серый
def rgb2gray(rgb):
    r, g, b = rgb[0:3]  # выделяем три переменные r,g,b, параметр alpha не учитываем
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b  # преобразуем в оттенок серого
    return gray  # функция возвращает результат, оттенок серого

# функция записи одного коммита (сообщения) по дате
def contribute(date):
    with open(os.path.join(os.getcwd(), 'README.md'), 'a') as file:  # открывает файл 'README.md'
        file.write(message(date) + '\n\n')  # дописывае дату, пропускает две строки
    run(['git', 'add', '.'])  # запускает в командной строке команды проверить файлы на изменение
    run(['git', 'commit', '-m', '"%s"' % message(date),
         '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])  # запускает в командной строке отправить комит по дате
    # при этом коммит подписывается датой внесения измениний

# функция запуска команд в командной строке (полученных аргументов фукнции)
def run(commands):
    Popen(commands).wait()  # ожидает выполнения команд (полученных аргументов фукнции)

# функция преобразует дату в установленный формат
def message(date):
    return date.strftime('Contribution: %Y-%m-%d %H:%M')

# функция формирует произвольное число в диапазоне (количество коммитов в этот день)
def contributions_per_day(args):
    max_c = args.max_commits
    if max_c > 20:
        max_c = 20
    if max_c < 1:
        max_c = 1
    return randint(1, max_c)  # возвращает произвольное число

# функция абработки аргументов
def arguments():
    parser = argparse.ArgumentParser()  # считываем все аргументы
    parser.add_argument('-nw', '--no_weekends',  # аргумент работы без выходных
                        required=False, action='store_true', default=False,
                        help="""do not commit on weekends""")
    parser.add_argument('-mc', '--max_commits', type=int, default=10,  # аргумент, максимального числа коммитов в день
                        required=False, help="""Defines the maximum amount of
                        commits a day the script can make. Accepts a number
                        from 1 to 20. If N is specified the script commits
                        from 1 to N times a day. The exact number of commits
                        is defined randomly for each day. The default value
                        is 10.""")
    parser.add_argument('-fr', '--frequency', type=int, default=80,  # аргумент сколько процентов в год закомичено
                        required=False, help="""Percentage of days when the
                        script performs commits. If N is specified, the script
                        will commit N%% of days in a year. The default value
                        is 80.""")
    parser.add_argument('-r', '--repository', type=str, required=False,  # аргумент репозитория
                        help="""A link on an empty non-initialized remote git
                        repository. If specified, the script pushes the changes
                        to the repository. The link is accepted in SSH or HTTPS
                        format. For example: git@github.com:user/repo.git or
                        https://github.com/user/repo.git""")
    return parser.parse_args()  # возращает результат функции

# главная функция
def main():
    args = arguments()  # обработка аргументов при запуске программы
    curr_date = datetime.now()  # определяем сегодняшнюю дату
    directory = 'repository-' + curr_date.strftime('%Y-%m-%d-%H-%M-%S')  # название папки
    print('directory', directory)
    repository = args.repository  # этой переменной присваиваем названия репозитория на github
    if repository is not None:  # если репозиторий существует
        start = repository.rfind('/') + 1  # определяем начало от слеша
        end = repository.rfind('.')  # определяем конец до точки
        directory = repository[start:end]  # меняем название папки
        print('directory', directory)
    os.mkdir(directory)  # создаем папку с соотв. названием
    os.chdir(directory)  # переходим в эту папку
    run(['git', 'init'])  # запускаем инициализацию этой папки

    # start_date = curr_date.replace(hour=20, minute=0) - timedelta(366)  # определяем первый день (год назад)
    print('start_date', start_date)

    # рандомное заполнение
    # for day in (start_date + timedelta(n) for n in range(364)):  # переходим от 1-го дня до последнего
    #     if (not no_weekends or day.weekday() < 5) \
    #             and randint(0, 100) < frequency:
    #         for commit_time in (day + timedelta(minutes=m)
    #                             for m in range(contributions_per_day(args))):  # в зависимости от количества коммитов
    #             # в этот день повторяет функцию отправки одного коммита
    #             contribute(commit_time)  # запуск отправки одного коммита

    # заполнение по картинке
    os.chdir('..')  # вернемся на 2 уровня вверх
    process_image('example/send_nudes_mini.png', directory)  # коммит делается из рисунка


    if repository is not None:  # если репозиторий существует
        run(['git', 'remote', 'add', 'origin', repository])  # запускаем команды в командной строке
        run(['git', 'push', '-u', 'origin', 'master'])  # запускаем команды в командной строке

    print('\nRepository generation ' +
          '\x1b[6;30;42mcompleted successfully\x1b[0m!')

start_date = date(2011, 12, 26)
now = date.today()
days_ago = now - start_date
offset = (date.today().weekday() + 1) % 7  # сегодняшней даты, на матрице 7 на 52 (от этого зависит какой день
rows = 7  # строки
cols = 52  # столбцы
size = (cols, rows)  # общий размер 7 на 52
numdays = rows * cols  # количество дней на одной странице 7 x 52 = 354


if __name__ == "__main__":
    main()

# python github_paint.py --repository=https://github.com/BEPb/test2018.git