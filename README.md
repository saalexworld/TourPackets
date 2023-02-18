Запускаем проект на своей машине (все команды применимы к MacOS, Linux "Ubuntu") :

1) Клонируем репозиторий                                                  
git clone https://github.com/saalexworld/TourPackets.git

2) Переходим в папку с проектом                                           
cd TourPackets

3) Устанавливаем виртуальное окружение (для python 3)                     
python3 -m venv venv

4) Запускаем виртуальное окружение                                        
source env/bin/activate

5) Обновляем систему управления пакетами                                  
pip install --upgrade pip

6) Устанавливаем в виртуальном окружении зависимости для проекта          
pip install -r req.txt

7) Создаём базу данных (для postgreSQL)                                   
psql -> create database <name_db> ; -> \q

8) Делаем миграции в создания базу данных                                 
python manage.py makemigrations && python manage.py migrate

9) Создаём суперюзера для управления админ-панелью                        
python manage.py createsuperuser

9) Запускаем локальный сервер                                             
python manage.py runserver

10)Запускаем celery (для удобства испоьзуйте второе окно в консоле)       
celery -A Tours worker --loglevel=INFO

11)Доступ к админ-панели по адресу                                        
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