CREATE TABLE employees (
    id     INTEGER      PRIMARY KEY AUTOINCREMENT,
    name   VARCHAR (30) NOT NULL,
    job    VARCHAR (10),
    salary INTEGER (7)
);


insert into employees(name,job,salary) values('Micheal Dell','prog',2000000);
insert into employees(name,job,salary) values('Scott Guithrie','prog',2500000);
insert into employees(name,job,salary) values('Kevin Loney','dba',3000000);


update employees set job = 'cto'
where id = 2;

select * from employees;

delete from employees where id = 7