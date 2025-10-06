# Write your MySQL query statement below


-- select coalesce(max(num),-1) as biggest_single_number from MyNumbers
-- group by num 
-- having count(*)=1;

select max(num) as num
from (select num from MyNumbers group by num having count(*)=1) as bsn;