/*
方法一：
首先找出新用户第一次的登录日期，然后计算第二天的留存率，最后并上没有新用户的0.000
*/

select a.date, round(count(b.user_id) / count(a.user_id), 3) as p
from (
    select user_id, min(date) as date
    from login
    group by user_id
    ) a
left join login b
  on a.user_id = b.user_id
 and b.date = date_add(a.date, interval 1 day)
group by a.date

union
select date, 0.000 as p
from login
where date not in
(
    select min(date)
    from login
    group by user_id
)
order by date;
