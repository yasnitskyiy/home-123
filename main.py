# git init

# Для командної роботи

# git config user.name "name"
# git config user.email "email"


# Доступаємось до файлика з налаштуваннями
# core, user - секції, що в них це значення

# cat .git/config

# є системні налаштування --system
# --globals на рівні користувача (для ніків краще, бо нові проєкти їх підтягують)
# --local на рівні проєкту (default)

# git config --global user.name "Yurii Yasnitskyi"
# git config --global user.email "yura.yasnitskiy@gmail.com"

# https://docs.github.com/en/get-started/getting-started-with-git/associating-text-editors-with-git
# вказування редакору для коментарів
# git config --global core.editor "code --wait"

# alias
# Скоротити якусь команду під іншу псевдоназву
# git config --global alias.c 'config'
# git config --global alias.TEXT '!git ...; git ...'



# *** СТВОРЕННЯ РЕПОЗИТОРІЮ ***

# Є 3 серидовище в яких міститься інфомраці про проєкт
# 1. Це наша робоча папка (working directory)
# 2. Index
# 3. Repository


# git status

# проіндексувати цей файл
# git add main.py

# git commit

# Заголовок
#
# *дія 1
# *дія 2


# Додати усі файли з проєкту
# git add .

# .idea містить службові файли програми в якій ми працюємо
# їх не потрбіно зберігати у нашому репозиторії

# git restore --staged прибрати їх з index



# ** ХОРОШІ КОМІТИ **
# Commit early. Commit often





