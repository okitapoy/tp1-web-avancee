create table article (
  id integer primary key,
  titre varchar(100),
  identifiant varchar(50),
  auteur varchar(100),
  date_publication text,
  paragraphe varchar(500)
);


insert into article values(1,"titre 1","id 1","auteur 1","date 1", "parag 1");
insert into article values(2,"titre 2","id 2","auteur 2","date 2", "parag 2");
insert into article values(3,"titre 3","id 3","auteur 3","date 3", "parag 3");
insert into article values(4,"titre 4","id 4","auteur 4","date 4", "parag 4");
