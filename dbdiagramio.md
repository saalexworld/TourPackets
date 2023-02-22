Для удобного восприятия моделей составлен roadmap данного проекта

Можно ознакомится с ним по ссылке https://dbdiagram.io/d/63e6440c296d97641d7fffa5

Чтобы воспользоваться данной картой моделей проекта, необходимо:
- необходимо перейти на сайт https://dbdiagram.io и зарегистрироваться
- выбрать вкладку New Diagram
- создать новую диаграмму
- в ней будет чистый лист
- скопировать данный код и получить для работы данный roadmap

Table account as A {
  id autoincrement pk
  username None
  email email [not null, unique]
  is_active boolean
  is_staff boolean
  activation_code char
}

Table Hotel as H {
  id autoincrement pk
  title char
  image image
  address char
  stars char
  breakfast boolean
  description text
}

Table Comment as C {
  id autoincrement pk
  body text
  packet fk
  created_at date
}

Table Favorite as F {
  id autoincrement pk
  body text
  packet fk
  is_favorite boolean
}

Table Like as L {
  id autoincrement pk
  author fk
  packet fk
  is_lifed boolean
}

Table LikeComment as LC {
  id autoincrement pk
  author fk
  packet fk
  is_lifed boolean
}

Table Category as CAT {
  id autoincrement pk
  title char
  description text
}

Table Packet as P {
  id autoincrement pk
  packet_category fk
  date_start date
  date_end date
  price int
  quantity int
  departure char
  arrival char
  description text
  schedule file
  hotel fk
  availability int
  in_stock boolean
  image image
  title char
  day_1 text
  day_2 text
  day_3 text
  day_4 text
  day_5 text
  day_6 text
  day_7 text
}

Table Rating as R {
  id autoincrement pk
  author fk
  rating positivesmallint
  packet fk
}

Table PacketImage as PI {
  id autoincrement pk
  packet_image fk
  is_active boolean
  image image
  created_at date
  updated_at date
}

Table HotelImage as HI {
  id autoincrement pk
  hotel_image fk
  is_active boolean
  image image
  created_at date
  updated_at date
}




Ref: "Packet"."packet_category" < "Category"."id"

Ref: "Packet"."hotel" < "Hotel"."id"

Ref: "HotelImage"."hotel_image" < "Hotel"."id"

Ref: "PacketImage"."packet_image" < "Packet"."id"

Ref: "Favorite"."packet" < "Packet"."id"

Ref: "Like"."packet" < "Packet"."id"

Ref: "Comment"."packet" < "Packet"."id"

Ref: "Like"."author" < "account"."id"

Ref: "LikeComment"."author" < "account"."id"

Ref: "Rating"."author" < "account"."id"