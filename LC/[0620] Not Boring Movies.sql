select *
from Cinema c
where c.id % 2 = 1 
  and c.description not like '%boring%'
order by c.rating desc
