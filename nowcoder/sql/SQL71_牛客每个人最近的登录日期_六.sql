--SQL71 牛客每个人最近的登录日期(六) 

select u.name u_n, p.date
    ,sum(p.number) over(partition by u.name order by p.date) ps_num
from passing_number p
left join user u
  on u.id = p.user_id
order by p.date, u.name;
