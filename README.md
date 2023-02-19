Запускаем проект на своей машине (все команды применимы к MacOS, Linux "Ubuntu") :

1) Клонируем репозиторий                                                  
git clone https://github.com/saalexworld/TourPackets.git

2) Переходим в папку с проектом                                           
cd TourPackets

3) Устанавливаем виртуальное окружение (для python 3)                     
python3 -m venv venv

4) Запускаем виртуальное окружение                                        
. env/bin/activate

5) Обновляем систему управления пакетами                                  
pip install --upgrade pip

6) Устанавливаем в виртуальном окружении зависимости для проекта          
pip install -r req.txt

7) Создаем файл со скрытыми настройками в рабочей области TourPackets
сенсорный .env

8) Открываем файл с крытыми настройками
nano.env

9) Заполняем файл со скрытыми настройками

SECRET_KEY = django-insecure-40n^+h%z)gfp@1cxr=n8! zc5c+reo##2u07)h_mps3s9*ivlto
DEBUG = Ложь

ПОЛЬЗОВАТЕЛЬ = <назовите пользователя>
ПАРОЛЬ = <ваш пароль>
NAME = (<name_db> -> название базы данных любое -> ваща база данных для проета)
ДВИГАТЕЛЬ = django.db.backends.postgresql
ПОРТ = 5432
HOST = локальный хост

EMAIL_BACKEND = django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST = smtp.gmail.com
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = <ваш emeil@gmail.com>
EMAIL_HOST_PASSWORD = <применение emeil> (необходимо создать в настройках gmail)***

*** - как настроить EMAIL_HOST_PASSWORD
- настройте двухэтапную аутентификацию, так как без нее не могут быть эти настройки
- перейти на свой личный "Google-аккаунт"
- перейти в раздел "Безопасность"
- найти раздел/окно "Вход в аккаунт Google"
- найти и перейти в этом разделе/окне "Примененные приложения" кнопку "Применить"
- в окне "Ваши пароли" выберите "Приложение" -> выберите "Другое (введите название)" -> ввести название: QDPro
- в окне "Ваши пароли приложений" выберите "Устройство" -> выберите "Другое (введите название)" -> не вводим ничего здесь
- нажмите на кнопку "Создать"
- появляется окно с ПАРОЛЕМ, который нужно сохранить! ВАЖНО! сохраните код надежно, так как вы больше не увидите его!
- все! вы получили ПАРОЛЬ и можете вставить его в раздел EMAIL_HOST_PASSWORD = <код вашего приложения emeil>

8) Создаем базу данных (для postgreSQL)(<имя_db> -> название базы данных любое -> ваша база данных для проета)
psql
создать базу данных <name_db>;
\q

9) Делаем миграции в базу данных
python manage.py makemigrations && python manage.py migrate

10) Создаём суперюзера для управления админ-панелью                        
python manage.py createsuperuser

11) Запускаем локальный сервер                                             
python manage.py runserver

12)Запускаем celery (для удобства испоьзуйте второе окно в консоле)       
celery -A Tours worker --loglevel=INFO

13)Доступ к админ-панели по адресу                                        
http://127.0.0.1:8000/admin/    


ВАЖНО! Еслиы вы сделали git clone https://github.com/saalexworld/TourPackets.git данного проекта и в дальнейшем решите сделать git pull origin <branch_name> то перед использованием этой команды обязательно проверьте url прикреплённого репозитория при помощи вот такой команды                                             

cat .git/config


Если вы получили в описании url = https://github.com/saalexworld/TourPackets.git то необходимо сменить url репозитория при помощи вот такой команды                                             

git remote set-url origin https://github.com/<...name repository owner...>


Проверьте смену репозитория                                              

cat .git/config



Основные команды для использования GIT:
1)
…or create a new repository on the command line
echo "# TourPackets" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/saalexworld/TourPackets.git
git push -u origin master

2)
…or push an existing repository from the command line
git remote add origin https://github.com/saalexworld/TourPackets.git
git branch -M master
git push -u origin master
