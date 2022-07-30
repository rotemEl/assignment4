create database ass4;

use ass4;

create table `users` (
    `id` int(10) not null auto_increment,
    `username` varchar(20),
    `email` varchar(255) unique,
    `passwd` varchar(255),
    primary key (`id`),
    unique key (`email`)
    ) engine=InnoDB default charset=utf8mb4;