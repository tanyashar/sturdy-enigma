CREATE - создать базу данных или таблицу
названия таблиц принято писать мал буквами - чтобы различать
//? полей ограниченное число, записей может быть сколько угодно 
python - язык с нестрогой типизацией (можно менять тип переменной)
sql - со СТРОГОЙ типизацией
VARCHAR - текстовый тип
INTEGER - число

CREATE TABLE users (id INTEGER PRIMARY KEY,
				  	first_name VARCHAR(100));		//100 - макс длина текста
ф-ия	что создаем(тип)	название	(поле, тип поля);

(!) ;  

INSERT добавить 
INSERT INTO users (id, first_name) VALUES (1, "as");

достать инфу из поля
SELECT * FROM users;	//из всех полей *
SELECT id FROM users;	//из поля id

SELECT * FROM users WHERE first_name="abc";		// --||-- с условием
SELECT id FROM users WHERE first_name="abc" AND id=3;		//AND

SELECT id FROM users GROUP BY id;

.
пример 
users, login, main_table - таблицы
SELECT users.first_name, login.login FROM main_table, users, login WHERE main_table.users = users.id AND main_table.login = login.id;
способ взаимодействия с реляционной базой данной с пом id
