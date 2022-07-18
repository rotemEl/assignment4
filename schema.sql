CREATE DATABASE IF NOT EXISTS `ass4`
DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci
DEFAULT ENCRYPTION='N';


CREATE TABLE IF NOT EXIST `users` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `email` varchar(255) DEFAULT NULL,
    `passwd` varchar(255),
    PRIMARY KEY (`id`),
    UNIQUE KEY `email` (`email`),
    UNIQUE KEY `email_2` (`email`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;


INSERAT INTO users(id, name, email, passwd) VALUES('1', 'Tinky Winky', 't@gmail.com', 't123');
INSERAT INTO users(id, name, email, passwd) VALUES('2', 'Dipsy', 'd@gmail.com', 'd123');
INSERAT INTO users(id, name, email, passwd) VALUES('3', 'Laa-Laa', 'l@gmail.com', 'l123');
INSERAT INTO users(id, name, email, passwd) VALUES('4', 'Po', 'p@gmail.com', 'p123');
INSERAT INTO users(id, name, email, passwd) VALUES('5', 'rotem', 'r@gmail.com', 'r123');