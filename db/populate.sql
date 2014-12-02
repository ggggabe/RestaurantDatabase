DROP DATABASE IF EXISTS Food;
CREATE DATABASE Food;
use Food;

CREATE TABLE Patron (
    firstname   VARCHAR(20),
    lastname    VARCHAR(20),
    veggie      CHAR(1),
    PRIMARY KEY (firstname, lastname)
);
CREATE TABLE Restaurant (
    name        VARCHAR(50),
    PRIMARY KEY (name)
);
CREATE TABLE Item (
    name        VARCHAR(50),
    veggie      CHAR(1),
    PRIMARY KEY (name)
);
CREATE TABLE Serves (
    restaurant_name VARCHAR(50),
    item_name       VARCHAR(50),
    price           FLOAT,
    PRIMARY KEY     (restaurant_name, item_name)
);
CREATE TABLE Visit (
    order_id        INT,
    firstname       VARCHAR(20),
    lastname        VARCHAR(20),
    restaurant_name VARCHAR(50),
    tip             FLOAT,
    day             DATE,
    PRIMARY KEY (order_id)
);
CREATE TABLE Ordered (
    order_id    INT,
    item_name   VARCHAR(50),
    PRIMARY KEY (order_id)
);
CREATE TABLE Reviewed (
    restaurant_name VARCHAR(50),
    firstname       VARCHAR(20),
    lastname        VARCHAR(20),
    positive        CHAR(1),
    PRIMARY KEY (restaurant_name, firstname, lastname)
);

LOAD DATA LOCAL INFILE 'Patron.csv' INTO TABLE Patron COLUMNS TERMINATED BY ',';
LOAD DATA LOCAL INFILE 'Restaurant.csv' INTO TABLE Restaurant COLUMNS TERMINATED BY ',';
