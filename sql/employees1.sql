select count(*) from salarires;


select first_name as '이름', gender as '성 별', hire_date as '입사일'
 from employees;

select concat(first_name, ' ', last_name) as '이름', gender as '성 별',
	hire_date as '입사일'
    from employees;
    
select distinct title from titles;

select concat(first_name, ' ', last_name) as '이름', gender as '성 별',
	hire_date as '입사일'
    from employees
    order by hire_date desc;
    
select concat(first_name, ' ', last_name) as '이름', gender as '성 별',
	date_format(hire_date, '%Y년 %m월 %d일 %h:%i:%s') as '입사일'
    from employees
    where hire_date < '1991-01-01' 
    and gender = 'F'
    order by hire_date desc;
    
    
-- 예제 : salaries 테이블에서 현재 전체 직원별로 평균급여가 35000이상인 직원의 평균급여를 큰순서로출력
select emp_no, avg(salary) as avg_salary
	from salaries
    where to_date = '9999-01-01'
    group by emp_no
    having avg_salary > 35000
    order by avg_salary desc;
    
-- 예제 : 사원별 몇 번의 직책 변경이 있었는지 조회
select emp_no,count(*) as cnt
	from titles
    group by emp_no
    order by cnt desc;
    
-- 예제 : 현재 직책별 인원수를 구하되 직책별로 인원이 100명이상인 직책만 출력.
select title, count(*) as cnt
	from titles
    where to_date='9999-01-01'
    group by title
    having cnt > 100;
    
-- 예제 : 