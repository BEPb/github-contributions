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
  d = date.today() - timedelta(days = days_ago)  # высчитываем день начала рисунка (первого комментария)
  t = str(d) + " 00:00:00"  # строчное значение полученной величины + " 00:00:00"
  os.system("echo " + msg + " > .tmpfile")
  os.system("git add .tmpfile")
  os.system('GIT_COMMITTER_DATE="'+t+'"' + ' GIT_AUTHOR_DATE="'+t+'"' + ' git commit -m "' + msg + '" 2>&1 >/dev/null')

def rgb2gray(rgb):  # преобразовываем цветной рисунок в серый
    r, g, b = rgb[0:3]  # выделяем три переменные r,g,b, параметр alpha не учитываем
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b  # преобразуем в оттенок серого
    return gray  # функция возвращает результат, оттенок серого

def write_px(x, y, intensity, prefix=""):  # рисуем пиксели (координаты, интенсивность)
  days_ago = numdays+offset - (x*rows+y)  # дней назад = количество дней на странице + учитываем какой сегодня день
  # недели - смещение по оси х умноженное на число строк + у
  d = date.today() - timedelta(days = days_ago)  # от сегодняшнего дня отнимаем количество дельта дней
  t = str(d) + " 00:00:00"  # преобразуем в строчную величину и добавляем " 00:00:00"
  print("val=", intensity, "x", x, "y", y, "date:", d)  # выводим полученные данные
  for i in range(0, intensity):  # в зависимости от параметра интенсивности в этот день (определяется количество
    # коммитов)
    msg = prefix + os.urandom(8).encode("hex")  # сообщение
    commit(days_ago, msg)


def process_image(path):  # функция работы с рисунком 52x7
  img = Image.open(path)
  px = img.load()
  size = img.size
  if (52,7) != size:
    raise Exception("Image should be 52x7, got " + size)
  for x in range(size[0]):
    print("processed line", x)
    for y in range(size[1]):
      val = 255-int(rgb2gray(px[x, y]))
      val /= 16
      write_px(x, y, val, prefix="ign-")

def process_text(txt, offset=2):  # функция преобразования текста (фразы) в рисунок
  f = 1
  image = Image.new("RGB", [x*f for x in size], (255, 255, 255))
  draw = ImageDraw.Draw(image)
# see https://mail.python.org/pipermail/image-sig/2005-August/003497.html
  draw.fontmode = "1"
  font = ImageFont.truetype("font/5x5_pixel.ttf", 8)
  draw.text((offset, 1), txt, (0, 0, 0), font=font)
  image.save(txt+".bmp")  # сохраняем изображение в файл .bmp

def main():
  if sys.argv[1] == "--text":  # если программа запущена с аргументом "--text", то коммит делается из фразы
    process_text(sys.argv[2])
  else:  # иначе коммит делается из рисунка
    process_image(sys.argv[1])

# Определяем используемые переменные
# GitHub начинает неделю с воскресенья, добавим 1 (какой сегодня день недели???)
offset = (date.today().weekday() + 300) % 7  # от сегодняшней даты, формируем матрицу 7 на 52
rows = 7  # строки
cols = 52  # столбцы
size = (cols, rows)  # общий размер 7 на 52
numdays = rows * cols  # количество дней на одной странице

if __name__ == "__main__":
  main()
