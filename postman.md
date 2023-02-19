! ВАЖНО ! обращать строгое внимание к написаную домена ! если стоит слеш "/" значит надо его прописывать обязательно ! если нету слеш "/" то можно не прописывать !

Команды для Postman, чтобы проверить работу и логику кода:

http://34.70.204.237/

http://127.0.0.1:8000/

1. Admin [GET]

admin/
**************************************************

2. Swagger [GET]

docs/
**************************************************

3. account app [POST] (приложение аккаунта)

 - регистрация нового пользователя
api/v1/register/

 - активация происходит автоматически **в данном случае используется запрос [GET]
 * не используем api/v1/activate/<str:email>/<str:activation_code>/ [name='activate']
 * не используем activate/qwerty@gmail.com/4873282981/

 - логинимся
api/v1/login/
 * api/v1/login/ [name='token_obtain_pair']

 - обновляем токен
api/v1/refresh/
 * api/v1/ refresh/ [name='token_refresh']

 - удаляем аккаунт
api/v1/delete/
 * api/v1/ delete/ [name='delete']

 - обновляем пароль аккаунта
api/v1/update/
 * api/v1/ update/ [name='update']

 - читаем информацию об аккаунте
api/v1/read_info/
 * api/v1/ read_info/ [name='read_info']

 - меняем пароль
api/v1/change_password/
 * api/v1/ change_password/ [name='change_password']

 - забыи пароль (часть первая)
api/v1/forgot_password/
 * api/v1/ forgot_password/ [name='forgot_password']

 - забыи пароль (часть вторая)
api/v1/forgot_password_complete/
 * api/v1/ forgot_password_complete/ [name='forgot_password_complete']
**************************************************

4. Packets app [GET] (приложение по всем туристическим пакетам компании)

 - список разделов в приложении Packets
api/v1/
 * api/v1/

 - список пакетов
api/v1/packets/
 * api/v1/ ^packets/$ [name='packets-list']

 - информация по одному из пакетов
api/v1/packets/<id packets>/
 * api/v1/ ^packets/(?P<pk>[^/.]+)/$ [name='packets-detail']

 - поставить лайк/дизлайк пакету **в данном случае используется запрос [POST]
api/v1/packets/<id packets>/like/
 * api/v1/ ^packets/(?P<pk>[^/.]+)/like/$ [name='packets-like']

 - информация по избранным
api/v1/packets/favorits/
 * api/v1/ ^favorits/$ [name='favorits-list']

 - информация по одному из избранного
api/v1/packets/favorits/<id number favorite>/
 * api/v1/ ^favorits/$ [name='favorits-list']

 - добавить/удалить в избранное **в данном случае используется запрос [POST]
api/v1/packets/<id number packet>/favorite/
 * api/v1/ ^packets/(?P<pk>[^/.]+)/favorite/$ [name='packets-favorite']

 - категории пакетов
api/v1/categories/
 * api/v1/ ^categories/$ [name='categories-list']

 - информация по одной из категорий
api/v1/categories/<id category>/
 * api/v1/ ^categories/(?P<pk>[^/.]+)/$

 - информация по ателям
api/v1/hotels/
 * api/v1/ ^hotels/$ [name='hotels-list']

 - информация по одному из ателей
api/v1/hotels/<id hotel>/
 * api/v1/ ^hotels/(?P<pk>[^/.]+)/$ [name='hotels-detail']

 - информация по картинкам/фото к пакетам
api/v1/image_packets/
 * api/v1/ ^image_packets/$ [name='image_packets-list']

 - информация по одной из картинок/фоток к пакету
api/v1/image_packets/<id number image>/
 * api/v1/ ^image_packets/(?P<pk>[^/.]+)/$ [name='image_packets-detail']
**************************************************

5. Reviews app [GET] (приложение по лайкам, комментариям, рейтингам)

 - информация по рейтингам
api/v1/ratings/
 * api/v1/ ^ratings/$ [name='ratings-list']

 - информация по одному из вариантов рейтинга
api/v1/ratings/<id number rating>/
 * api/v1/ ^ratings/(?P<pk>[^/.]+)/$ [name='ratings-detail']

 - добавить рейтинг **в данном случае используется запрос [POST]
api/v1/ratings/
 * api/v1/ ^ratings/$ [name='ratings-list']

 - информация по комментариям
api/v1/comments/
 * api/v1/ ^comments/$ [name='comments-list']

 - информация по одному из вариантов комментария
api/v1/comments/<id number comment>/
 * api/v1/ ^comments/(?P<pk>[^/.]+)/$ [name='comments-detail']

 - добавить комментарий **в данном случае используется запрос [POST]
api/v1/comments/
 * api/v1/ ^comments/$ [name='comments-list']

 - добавить лайк к комментарию **в данном случае используется запрос [POST]
api/v1/comments/<id number comment>/like/
 * api/v1/ ^comments/(?P<pk>[^/.]+)/like/$ [name='comments-like']
**************************************************
