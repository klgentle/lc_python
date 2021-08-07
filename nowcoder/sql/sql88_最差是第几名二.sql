-- 老师想知道学生们综合成绩的中位数是什么档位，请你写SQL帮忙查询一下，如果只有1个中位数，输出1个，如果有2个中位数，按grade升序输出，以上例子查询结果如下: 

/*
grade number sum_grade_asc  sum_grade_desc
a   2   2   12
b   4   6   10
c   4   10  6
d   2   12  2

a   2   2   5
b   2   4   3
c   1   5   2
*/

drop table if exists class_grade;
CREATE TABLE class_grade (
grade varchar(32) NOT NULL,
number int(4) NOT NULL
);

INSERT INTO class_grade VALUES
('A',2),
('B',1),
('C',2),
('D',2);

select grade 
from (
    select grade, 
           sum(number) over(order by grade asc) rna,
           sum(number) over(order by grade desc) rnd,
           t1.sumall
    from class_grade 
    left join 
    (
        select sum(number) sumall
        from class_grade 
    ) t1
    on 1=1
    where 1=1
) t
where (rna >= sumall /2 AND rnd >= sumall /2 )
order by grade;
