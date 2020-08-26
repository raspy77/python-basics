

-- pet table 생성
create table pets(
name varchar(20),
owner varchar(20),
species varchar(20),
gender char(1),
birth date,
death date );

-- table scheme 확인
desc pets;

-- insert
insert 
	into pets 
    values('성탄이','raspy','dog','m','2010-12-25',null);
    
insert 
	into pets 
    values('초코','raspy','dog','f','2010-12-25','2018-4-4');

-- select
select * from pets;

select name, birth from pets;
select name, birth from pets order by birth desc;

select count(*) from pets;

-- delete
delete from pets where death is not null;

-- update
update pets set owner='hk' where name = '초코';
