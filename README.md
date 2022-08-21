# PostgreSQL
Bitcoin and Other Crypto Balance Checker

PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance.
It was originally named POSTGRES, referring to its origins as a successor to the Ingres database developed at the University of California, Berkeley. 

License: PostgreSQL License (free and open-source, permissive)

Developer(s): PostgreSQL Global Development Group

Repository: git.postgresql.org/gitweb/?p=postgresql.git

Initial release: 8 July 1996; 26 years ago

Operating system: macOS, Windows, Linux, FreeBSD, OpenBSD

Stable release: 14.5 / 11 August 2022; 1 day ago

## Install PostgreSQL

https://user-images.githubusercontent.com/88630056/185788464-b4d02e62-1069-4a29-83d4-95bb2cbc9e51.mp4


## Create Table
```
CREATE TABLE hunter(
address VARCHAR(80) not null,
balance VARCHAR(30) not null
);
```
https://user-images.githubusercontent.com/88630056/185788481-044d26ed-213e-4a86-8c8d-118395f85225.mp4


## Install Flask 
```
pip install flask
pip install psycopg2
pip install waitress
pip install virtualenv
```
https://user-images.githubusercontent.com/88630056/185788486-e08b1685-db89-4af1-b6a5-9267798ac20c.mp4


## Import and Use
```
C:\Program Files\PostgreSQL\14\bin
```

```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --host=0.0.0.0
```
https://user-images.githubusercontent.com/88630056/185788493-6b38bdbd-d327-4606-926d-54c2ea898cb3.mp4

```
http://127.0.0.1:5000/balance?active=1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF
```

![image](https://user-images.githubusercontent.com/88630056/185788729-6b1434d5-23e2-4c2d-9a49-0995f428eb1d.png)
