-- CREATE DATABASE whataduudle_game;

-- CREATE USER duudle_admin WITH PASSWORD 'password';

-- GRANT ALL PRIVILEGES ON DATABASE whataduudle_game TO duudle_admin;

-- Super Admin Username: duudle ; Password: 1234

\c whataduudle_game
INSERT INTO main_app_word (prompt, difficulty) VALUES ('cat', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('dog', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('fish', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('bird', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('rabbit', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('bear', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('chicken', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('monkey', 'HARD');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('leopard', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('lion', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('tiger', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('elephant', 'HARD');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('giraffe', 'HARD');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('zebra', 'HARD');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('horse', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('pig', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('sheep', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('cow', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('deer', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('wolf', 'HARD');

-- FOOD
INSERT INTO main_app_word (prompt, difficulty) VALUES ('pizza', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('donut', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('burger', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('sandwich', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('cake', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('apple', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('banana', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('carrot', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('orange', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('pear', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('potato', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('grape', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('strawberry', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('watermelon', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('chocolate', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('ice cream', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('cookie', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('brownie', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('noodle', 'HARD');

-- INSTRUMENTS
INSERT INTO main_app_word (prompt, difficulty) VALUES ('guitar', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('piano', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('drums', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('violin', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('trumpet', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('saxophone', 'HARD');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('flute', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('ukulele', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('harmonica', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('xylophone', 'HARD');

-- OBJECTS
INSERT INTO main_app_word (prompt, difficulty) VALUES ('lamp', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('chair', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('phone', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('tv', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('computer', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('book', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('pen', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('paper', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('desk', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('table', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('bed', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('door', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('window', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('key', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('lock', 'EASY');

-- TRANSPORTATION
INSERT INTO main_app_word (prompt, difficulty) VALUES ('car', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('bus', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('bike', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('boat', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('train', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('plane', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('ship', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('motorcycle', 'MEDIUM');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('van', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('truck', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('taxi', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('helicopter', 'HARD');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('spaceship', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('rocket', 'EASY');

-- MISCELLANEOUS
INSERT INTO main_app_word (prompt, difficulty) VALUES ('face', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('smile', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('eyes', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('nose', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('mouth', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('hair', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('watch', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('camera', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('keyboard', 'EASY');
INSERT INTO main_app_word (prompt, difficulty) VALUES ('robot', 'HARD');
