select job
    ,max(case when t.ra < t.rb then t.ra else t.rb end) start
    ,max(case when t.ra < t.rb then t.rb else t.rb end) end
From (
    select g.job
        ,row_number() over(partition by g.job order by score) ra
        ,row_number() over(partition by g.job order by score desc) rb
    from grade g
) t
/*where (ra = rb or case when t.ra <= t.rb then t.rb - t.ra else t.ra - t.rb end = 1)*/
where (ra = rb or if(t.ra <= t.rb, t.rb - t.ra, t.ra -t.rb) = 1)
group by job
order by t.job;
