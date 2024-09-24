create table pokedex(
id int primary key auto_increment,
nom varchar(50) unique
);

create table pokemonsportif (
id int primary key auto_increment,
nom varchar(50),
poids decimal(5,2),
nombrepattes int,
taille decimal(5,2), 
frequencecardiaque int,
pokedex_id int default null,
FOREIGN KEY(pokedex_id) references pokedex(id)
);

create table pokemoncasanier (
id int primary key auto_increment,
nom varchar(50),
poids decimal(5,2),
nombrepattes int,
taille decimal(5,2),
nbheurestv int,
pokedex_id int default null,
FOREIGN KEY(pokedex_id) references pokedex(id)
);

create table pokemonmer(
id int primary key auto_increment,
nom varchar(50),
poids decimal(5,2),
nombrenageoires int,
pokedex_id int default null,
FOREIGN KEY(pokedex_id) references pokedex(id)
);

create table pokemoncroisiere(
id int primary key auto_increment,
nom varchar(50),
poids decimal(5,2),
nombrenageoires int,
pokedex_id int default null,
FOREIGN KEY(pokedex_id) references pokedex(id)
);



