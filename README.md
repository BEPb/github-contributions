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
3. Запустите эту программу с ключом (адресом Вашего репозитория) как указана на примере ниже:
python github_paint.py --repository = https: //github.com/user/repo.git (Метод HTTPS: аутентификация учетной записи)


Максимальное количество коммитов в настоящее время равно 20. Внесите изменения в строки 60 и 61, если хотите 
изменить (не рекомендуется) [если max_c> 20: max_c = 20]
Процесс занимает не так уж и много времени (3-5 минут).
Если вы однажды использовали в репозитории этот скрипт, то повторить с этим же репозиторием - не получится.
Вам придется создать другой репозиторий, иначе вы получите ошибки в журналах скрипта. 
Акцент на использовании репозитория, который не был инициализирован.

Дополнительные аргументы (ключи программы)
Используйте --max_commit = X, чтобы скрипт делал от 1 до X коммитов.
Используйте --frequency = Y, чтобы скрипт выполнял фиксацию через Y% года. Например: --frequency = 50 зафиксирует 50% дней в году.
--repository = https: //github.com/user/repo.git устанавливает репозиторий, в который будут помещены все коммиты.
Используйте --no_weekends, чтобы не отправлять какие-либо коммиты в выходные дни.
Используйте --help, чтобы вызвать справку.


