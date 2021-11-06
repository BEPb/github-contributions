"""
Python 3.9 Программа для изменения коментариев github
Название файла 'github_contributions.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-05
"""

import os  # подключаем модуль для работы с операционной системой
import sys  # подключаем модуль для работы с системными файлами
from PIL import Image, ImageDraw, ImageFont  # подключаем модуль для работы с изображенями
from datetime import date, timedelta  # подключаем модуль для работы со временем
# from subprocess import call


def commit(days_ago, msg):  # функция коментария (указываем на сколько дней назад делаем сдвиг, сообщение)
  # d = date.today() - timedelta(days = days_ago)  # высчитываем день начала рисунка (первого комментария)
  d = off_day - timedelta(days = days_ago)  # высчитываем день начала рисунка (первого комментария)
  t = str(d) + " 00:00:00"  # строчное значение полученной величины + " 00:00:00"
  os.system("echo " + msg + " > .tmpfile")
  os.system("git add .tmpfile")
  os.system('GIT_COMMITTER_DATE="'+t+'"' + ' GIT_AUTHOR_DATE="'+t+'"' + ' git commit -m "' + msg + '" 2>&1 >/dev/null')
  print('GIT_COMMITTER_DATE="'+t+'"' + ' GIT_AUTHOR_DATE="'+t+'"' + ' git commit -m "' + msg + '" 2>&1 >/dev/null')

def rgb2gray(rgb):  # преобразовываем цветной рисунок в серый
    r, g, b = rgb[0:3]  # выделяем три переменные r,g,b, параметр alpha не учитываем
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b  # преобразуем в оттенок серого
    return gray  # функция возвращает результат, оттенок серого

def write_px(x, y, intensity, prefix=""):  # записываем коммиты на git (координаты, интенсивность)
  days_ago = numdays + offset - (x*rows+y)  # дней назад = количество дней на странице + учитываем какой сегодня день
  # недели - смещение по оси х умноженное на число строк + у
  # d = date.today() - timedelta(days = days_ago)  # от сегодняшнего дня отнимаем количество дельта дней
  d = off_day - timedelta(days = days_ago)  # от сегодняшнего дня отнимаем количество дельта дней
  print("val=", intensity, "x", x, "y", y, "date:", d)  # выводим полученные данные
  intensity = int(intensity)
  for i in range(0, intensity):  # в зависимости от параметра интенсивности в этот день (определяется количество
    # коммитов)
    priv = os.urandom(8)
    msg = prefix + priv.hex()  # сообщение
    commit(days_ago, msg)


def process_image(path):  # функция работы с рисунком 52x7
  img = Image.open(path)  # открываем рисунок
  px = img.load()  # создаем таблицу данных рисунка
  size = img.size  # получаем размер рисунка
  if (52, 7) != size:  # Если рисунок не 52x7
    raise Exception("Рисунок должен быть 52x7, Ваш рисунок имеет размер: " + size)
  for x in range(size[0]):  # перемещаемся по рядам от 1 до 7
    print("Ведется работа над рядом №: ", x)  # печатаем № ряда
    for y in range(size[1]):  # перемещаемся по столбцам от 1 до 52
      val = 255 - int(rgb2gray(px[x, y]))  # преобразуем цвет в оттенок серого
      val /= 16  # оттенок серого преобразуем в значения от 1 до 4
      write_px(x, y, val, prefix="ign-")  # обращаемся к функции записи коммита

def main():
    process_image('test.png')  # коммит делается из рисунка
    # print('now  ', now)
    # print('offset  ', offset)
    # print('d ', d)
    # print('date.today() ', date.today())
    # print('date.today().weekday()', date.today().weekday())

# Определяем используемые переменные
# GitHub начинает неделю с воскресенья, добавим 1 (какой сегодня день недели???)
# offset = (date.today().weekday() + 1) % 7  # сегодняшней даты, на матрице 7 на 52 (от этого зависит какой день
now = date.today()
off_day = date(2020, 12, 20)
days_ago = now - off_day
# print('days_ago ', days_ago)
offset = (date.today().weekday() + 1) % 7  # сегодняшней даты, на матрице 7 на 52 (от этого зависит какой день
# d = date.today() - timedelta(days = days_ago.days)
# выбрать начальным для рисования рисунка)
# ear_ago = 3  # определяем сколько лент назад рисовать коммит рисунок
# first_day = str('2020-01-04')  # первый день
rows = 7  # строки
cols = 52  # столбцы
size = (cols, rows)  # общий размер 7 на 52
numdays = rows * cols  # количество дней на одной странице 7 x 52 = 354

if __name__ == "__main__":
  main()
