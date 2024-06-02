select s.user_id,
round(sum(case when s.time_stamp is null then 0.00 
               when c.action='confirmed' then 1 
               else 0 
               end)/count(*) ,2) as confirmation_rate
from Signups s left join Confirmations c on s.user_id=c.user_id
group by s.user_id


-----
-- this is not working, debut later
-----
/* Write your T-SQL query statement below */
with cte_confirmed as(
    select s0.user_id as user_id, 
           sum(case when isnull(s0.time_stamp, 0)=0 then 0.00 else 1.0 end) as confirmed_num
      from Signups s0 left join Confirmations c0 on s0.user_id=c0.user_id and c0.action='confirmed'
    group by s0.user_id         
), cte_ttl_action as (
    select c1.user_id,
           count(*) as ttl_action_num
    from Confirmations c1  
    group by c1.user_id  
)select cfmed.user_id, 
        isnull(round(cfmed.confirmed_num/nullif(ttl.ttl_action_num,0), 2),0) as confirmation_rate
   from cte_confirmed cfmed left join cte_ttl_action ttl 
     on cfmed.user_id = ttl.user_id
