select * from (
    select 
        o.user_id, min(date) first_buy_date, count(*) cnt
    from order_info o
    where product_name in ('C++', 'Java', 'Python')
      and o.date >= '2025-10-15'
      and status = 'completed'
    group by o.user_id
) t
where t.cnt >= 2
order by t.user_id;
