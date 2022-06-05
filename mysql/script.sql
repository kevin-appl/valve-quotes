DROP DATABASE IF EXISTS `valvequotes`;
CREATE DATABASE IF NOT EXISTS `valvequotes`;
USE `valvequotes`;

SET NAMES utf8;

DROP TABLE IF EXISTS `quote`;
CREATE TABLE `quote` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `content` text,
    `author` text,
    PRIMARY KEY (`id`)
);

LOAD DATA INFILE '/var/mysql-csv/quotes.csv' 
INTO TABLE quote
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(content,author);
