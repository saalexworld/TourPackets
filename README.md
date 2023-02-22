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
touch .env

8) Открываем файл с крытыми настройками
nano .env

9) Заполняем файл со скрытыми настройками

SECRET_KEY = django-insecure-40n^+h%z)gfp@1cxr=n8! zc5c+reo##2u07)h_mps3s9*ivlto

DEBUG = False

USER = <...name_user...>

PASSWORD = <...user_password...>

NAME = (<...name_db...> -> название базы данных любое -> ваща база данных для проета)

ENGINE = django.db.backends.postgresql

PORT = 5432

HOST = localhost

EMAIL_BACKEND = django.core.mail.backends.smtp.EmailBackend

EMAIL_HOST = smtp.gmail.com

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = <...user_emeil@gmail.com...>

EMAIL_HOST_PASSWORD = <код вашего приложения для ...@gmail.com> (необходимо создать в настройках gmail)***

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

10) Создаем базу данных (для postgreSQL)(<...name_db...> -> название базы данных любое -> ваша база данных для проета)
psql
create database <...name_db...>;
\q

11) Делаем миграции в базу данных
python manage.py makemigrations && python manage.py migrate

12) Создаём суперюзера для управления админ-панелью                        
python manage.py createsuperuser

13) Запускаем локальный сервер                                             
python manage.py runserver

14) Запускаем celery (для удобства испоьзуйте второе окно в консоле)       
celery -A Tours worker --loglevel=INFO

15) Проверяем cache который настроен через redis (для удобства испоьзуйте третье окно в консоле)
redis-cli
KEYS *

16) Доступ к админ-панели по адресу                                        
http://127.0.0.1:8000/admin/    

***************************************************************************

ВАЖНО! Еслиы вы сделали git clone https://github.com/saalexworld/TourPackets.git данного проекта и в дальнейшем решите сделать git pull origin <..branch_name..> то перед использованием этой команды обязательно проверьте url прикреплённого репозитория при помощи вот такой команды                                             

cat .git/config


Если вы получили в описании url = https://github.com/saalexworld/TourPackets.git то необходимо сменить url репозитория при помощи вот такой команды                                             

git remote set-url origin https://github.com/<...name repository owner...>


Проверьте смену репозитория                                              

cat .git/config

***************************************************************************

Основные команды для использования GIT:

1) Создайте новый репозиторий в командной строке

echo "# TourPackets" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/saalexworld/TourPackets.git
git push -u origin master

2) Запустите существующий репозиторий из командной строки

git remote add origin https://github.com/saalexworld/TourPackets.git
git branch -M master
git push -u origin master

***************************************************************************

Если вы вдруг случайно запушили (git push ...) не ТО что нужно, не ТУДА куда надо, и вам необходимо откатиться и вернуть код, то используйте следующие команды по следующему плану действий:

1) После того как вы ввели команду git push origin name вы получаете в консоле вот такое примерное сообщение

Перечисление объектов: 63, готово.
Подсчет объектов: 100% (63/63), готово.
При сжатии изменений используется до 10 потоков
Сжатие объектов: 100% (38/38), готово.
Запись объектов: 100% (38/38), 9.93 КиБ | 9.93 МиБ/с, готово.
Всего 38 (изменений 21), повторно использовано 0 (изменений 0), повторно использовано пакетов 0
remote: Resolving deltas: 100% (21/21), completed with 16 local objects.
To https://github.com/saalexworld/TourPackets.git
   c1a8cd9..7340f68  name -> name

Здесь мы видим прошлую версию коммита c1a8cd9 и новую версию 7340f68 нами создаными

2) Вводим команду со стары коммитом и возвращаем его

git push --force origin c1a8cd9:name

3) Чтобы вернуть код старого коммита в вашей рабочей дериктори, то в консоле введите такую команду

git reset --hard c1a8cd9

