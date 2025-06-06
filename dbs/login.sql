create table Users (
    username varchar(50) not null unique,
    password varchar(255) not null
);