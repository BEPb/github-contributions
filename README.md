![Profile views](https://gpvc.arturio.dev/BEPb) 
![GitHub top language](https://img.shields.io/github/languages/top/BEPb/github-contributions) 
![GitHub language count](https://img.shields.io/github/languages/count/BEPb/github-contributions)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/BEPb/github-contributions)
![GitHub repo size](https://img.shields.io/github/repo-size/BEPb/github-contributions) 
![GitHub](https://img.shields.io/github/license/BEPb/github-contributions) 
![GitHub last commit](https://img.shields.io/github/last-commit/BEPb/github-contributions)
![GitHub User's stars](https://img.shields.io/github/stars/BEPb?style=social)
<p align="left">
<img src="https://visitor-badge.laobi.icu/badge?page_id=BEPb.github-contributions" alt="visitors"/>
</p>

# GitHub Contributions
(перевод с англ. вклад в GitHub)

## Переделываем активность на GitHub, рисуем в профиле

Если Вы желаете украсить историю своей активности на GitHub, то возможности Python скрипта ``github_paint.py`` 
помогут Вам заменить contributions за указанный период.

В качестве источника Вы должны заблаговременно подготовить изображение размером 52 на 7 пикселй: оно будет 
автоматически переобразовано в коммиты от Вашего имени в Ваш отдельный репозиторий.


Данная программа сама инициализирует пустой репозиторий файлом README.md и начинает генерировать обновления файла с 
добавлением вкладов: ГГГГ-ММ-ДД ЧЧ: ММ для каждой фиксации вашего коммита. 

Использует переключатель --date для создания 
коммитов в прошлом.

### Порядок использования
1. Создайте новый пустой репозиторий на GitHub. Не добавляйте файл README.md и не инициализируйте репозиторий.
2. Клонируйте этот репозиторий или скопируйте файл github_paint.py и Ваш рисунок коммитов.
3. В репозитории откройте html-страницу Git.html и нарисуйте свой рисунок
4. Сохраните свой рисунок
5. Преобразуйте его к размеру 52х7
6. Измените в github_paint.py строки с названием файла вашего рисунка и поледнего дня года в котором вы будете 
   размещать Ваш рисунок
7. Запустите программу github_paint.py с ключом (адресом Вашего репозитория) как указана на примере ниже:
```commandline
python github_paint.py --repository = https: //github.com/user/repo.git
```
 (Метод HTTPS: аутентификация учетной записи)
Процесс занимает не так уж и много времени (3-5 минут). 
7. Наслаждайтесь результатом

> Примечание:
Если вы однажды использовали в репозитории этот скрипт, то повторить с этим же репозиторием - не получится.
Вам придется создать другой репозиторий, иначе вы получите ошибки в журналах скрипта. 
Акцент на использовании репозитория, который не был инициализирован.



### Примеры работ:
1. Исходный рисунок `ГЕНОМ`:

![](./example/genom.png)

Тот же рисунок но в разрешении 52х7:
![](./example/genom_mini.png)

Результат:
![](./example/genom_res.png)

2. Исходный рисунок `Я люблю Python`:

![](./example/i_l_p.png)

Тот же рисунок но в режиме 52х7:
![](./example/i_l_p_mini.png)

Результат:
![](./example/i_l_p_res.png)

2. Исходный рисунок `Я люблю Python`:

![](./example/heart.png)

Тот же рисунок но в режиме 52х7:
![](./example/heart_mini.png)

Результат:
![](./example/heart_res.png)

Все примеры работ размещены в папке `example`
п.с. в дальнеидущих планах создать GUI приложение или html страницу на которой можно выполнить все операции от 
рисования до заливки в репозиторий, но пока на это нет времени..... так что всех энтузиастов развить этот проект 
приглашаю по учавствовать, создать свою ветку.

п.с.с. Если проект понравился не забывайте поставить звезду и если интерестны мои проекты то и записаться в followers


