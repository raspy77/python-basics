-- 1.
select concat(first_name, ' ', last_name) as '이름' from employees
	where emp_no = 10944;
    
-- 2.
select concat(first_name, ' ', last_name) as '이름' ,
	gender as '성별', hire_date as '입사일'
    from employees
    order by hire_date asc;

-- 3.
select sum(gender = 'M') as '남자', sum(gender = 'F') as '여자' 
	from employees;

-- 4.
select count(distinct emp_no) as '직원 수' from salaries;

    
-- 5.
select count(distinct dept_no) as '부서 개수' from departments;

-- 6.
select count(*) 
    from dept_manager;
    
-- 7.
select distinct dept_name
  from departments
order by length(dept_name) desc;  

-- 8.
select	count(*) from salaries 
	where 120000 < salary and
    to_date = '9999-01-01';
    
-- 9.
select distinct title
  from titles
order by length(title) desc;  

-- 10.
select count(*) from titles 
	where title = 'Engineer'
	and to_date = '9999-01-01';    
    
-- 11.
select * from titles 
	where emp_no = 13250
	order by from_date asc; 