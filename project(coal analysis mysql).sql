SELECT * FROM project.mysql_eda1;

## first moment business decision
## MEAN
select avg(Coal_RB_4800_FOB_London_Close_USD) as mean_column from mysql_eda1;  
select avg(Coal_RB_5500_FOB_London_Close_USD) as mean_column from mysql_eda1;
select avg(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) as mean_column from mysql_eda1;
select avg(Coal_RB_5700_FOB_London_Close_USD) as mean_column from mysql_eda1;  
select avg(Coal_India_5500_CFR_London_Close_USD) as mean_column from mysql_eda1;  


## MODE
select Coal_RB_4800_FOB_London_Close_USD as mode_column from
(select Coal_RB_4800_FOB_London_Close_USD , count(*) as max_count from mysql_eda1
group by Coal_RB_4800_FOB_London_Close_USD
order by max_count desc
limit 1)
as subquery;   

select Coal_RB_5500_FOB_London_Close_USD as mode_column from
(select Coal_RB_5500_FOB_London_Close_USD , count(*) as max_count from mysql_eda1
group by Coal_RB_5500_FOB_London_Close_USD
order by max_count desc
limit 1)
as subquery;  

select Coal_RB_5700_FOB_London_Close_USD as mode_column from
(select Coal_RB_5700_FOB_London_Close_USD, count(*) as max_count from mysql_eda1
group by Coal_RB_5700_FOB_London_Close_USD
order by max_count desc
limit 1)
as subquery;  

select Coal_RB_6000_FOB_CurrentWeek_Avg_USD as mode_column from
(select Coal_RB_6000_FOB_CurrentWeek_Avg_USD , count(*) as max_count from mysql_eda1
group by Coal_RB_6000_FOB_CurrentWeek_Avg_USD
order by max_count desc
limit 1)
as subquery;  

select Coal_India_5500_CFR_London_Close_USD as mode_column from
(select Coal_India_5500_CFR_London_Close_USD , count(*) as max_count from mysql_eda1
group by Coal_India_5500_CFR_London_Close_USD
order by max_count desc
limit 1)
as subquery;  

## MEDIAN
select Coal_RB_4800_FOB_London_Close_USD as median_column from
(select Coal_RB_4800_FOB_London_Close_USD , row_number() over (order by Coal_RB_4800_FOB_London_Close_USD)
as row_num , count(*) over() as total_count from mysql_eda1) as subquery 
where row_num = (total_count + 1)/2 or row_num = (total_count +2)/2;

select Coal_RB_5500_FOB_London_Close_USD as median_column1 from
(select Coal_RB_5500_FOB_London_Close_USD , row_number() over (order by Coal_RB_5500_FOB_London_Close_USD)
as row_num1 , count(*) over() as total_count from mysql_eda1) as subquery
 where row_num1 = (total_count + 1)/2 or row_num1 = (total_count + 2)/2 ;
 
 select Coal_RB_5700_FOB_London_Close_USD as median_column from
(select Coal_RB_5700_FOB_London_Close_USD , row_number() over (order by Coal_RB_5700_FOB_London_Close_USD)
as row_num , count(*) over() as total_count from mysql_eda1) as subquery 
where row_num = (total_count + 1)/2 or row_num = (total_count +2)/2;

select Coal_RB_6000_FOB_CurrentWeek_Avg_USD as median_column from
(select Coal_RB_6000_FOB_CurrentWeek_Avg_USD , row_number() over (order by Coal_RB_6000_FOB_CurrentWeek_Avg_USD)
as row_num , count(*) over() as total_count from mysql_eda1) as subquery 
where row_num = (total_count + 1)/2 or row_num = (total_count +2)/2;

select Coal_India_5500_CFR_London_Close_USD as median_column from
(select Coal_India_5500_CFR_London_Close_USD , row_number() over (order by Coal_India_5500_CFR_London_Close_USD)
as row_num , count(*) over() as total_count from mysql_eda1) as subquery 
where row_num = (total_count + 1)/2 or row_num = (total_count +2)/2;

## Second Moment Business Decision

## STANDARD DEVIATION
select stddev(Coal_RB_4800_FOB_London_Close_USD) as column_stddev
from mysql_eda1;

select stddev(Coal_RB_5500_FOB_London_Close_USD) as column_stddev
from mysql_eda1;

select stddev(Coal_RB_5700_FOB_London_Close_USD) as column_stddev
from mysql_eda1;

select stddev(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) as column_stddev
from mysql_eda1;

select stddev(Coal_India_5500_CFR_London_Close_USD) as column_stddev
from mysql_eda1;

##RANGE
select max(Coal_RB_4800_FOB_London_Close_USD) - min(Coal_RB_4800_FOB_London_Close_USD) as col_range
from mysql_eda1;

select max(Coal_RB_5500_FOB_London_Close_USD) - min(Coal_RB_5500_FOB_London_Close_USD) as col_range 
from mysql_eda1;

select max(Coal_RB_5700_FOB_London_Close_USD) - min(Coal_RB_5700_FOB_London_Close_USD) as range_col from mysql_eda1;

select max(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) - min(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) as col_range
from mysql_eda1;

select max(Coal_India_5500_CFR_London_Close_USD) - min(Coal_India_5500_CFR_London_Close_USD) as col_range
from mysql_eda1;

## VARIANCE 
select variance(Coal_RB_4800_FOB_London_Close_USD) as col_variance from mysql_eda1;
select variance(Coal_RB_5500_FOB_London_Close_USD) as col_variance from mysql_eda1;
select variance(Coal_RB_5700_FOB_London_Close_USD) as col_variance from mysql_eda1;
select variance(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) as col_variance from mysql_eda1;
select variance(Coal_India_5500_CFR_London_Close_USD) as col_variance from mysql_eda1;

##SKEWNESS
select( sum(power(Coal_RB_4800_FOB_London_Close_USD -( select avg(Coal_RB_4800_FOB_London_Close_USD) from mysql_eda1),3))/
(count(*) *power ((select stddev(Coal_RB_4800_FOB_London_Close_USD) from mysql_eda1),3))
) as skewness from mysql_eda1;

select( sum(power(Coal_RB_5500_FOB_London_Close_USD -( select avg(Coal_RB_5500_FOB_London_Close_USD) from mysql_eda1),3))/
(count(*) *power ((select stddev(Coal_RB_5500_FOB_London_Close_USD) from mysql_eda1),3))
) as skewness from mysql_eda1;

select( sum(power(Coal_RB_5700_FOB_London_Close_USD -( select avg(Coal_RB_5700_FOB_London_Close_USD) from mysql_eda1),3))/
(count(*) *power ((select stddev(Coal_RB_5700_FOB_London_Close_USD) from mysql_eda1),3))
) as skewness from mysql_eda1;

select( sum(power(Coal_RB_6000_FOB_CurrentWeek_Avg_USD -( select avg(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) from mysql_eda1),3))/
(count(*) *power ((select stddev(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) from mysql_eda1),3))
) as skewness from mysql_eda1;

select( sum(power(Coal_India_5500_CFR_London_Close_USD -( select avg(Coal_India_5500_CFR_London_Close_USD) from mysql_eda1),3))/
(count(*) *power ((select stddev(Coal_India_5500_CFR_London_Close_USD) from mysql_eda1),3))
) as skewness from mysql_eda1;

## KURTOSIS
select ((sum (power(Coal_RB_4800_FOB_London_Close_USD - (select avg(Coal_RB_4800_FOB_London_Close_USD) from mysql_eda1),4))/
(count(*) *power((select stddev(Coal_RB_4800_FOB_London_Close_USD) from mysql_eda1) , 4 ))) - 3)
 as kurtosis from mysql_eda1;

select ((sum (power(Coal_RB_5500_FOB_London_Close_USD - (select avg(Coal_RB_5500_FOB_London_Close_USD) from mysql_eda1),4))/
(count(*) *power((select stddev(Coal_RB_5500_FOB_London_Close_USD) from mysql_eda1) , 4 ))) - 3)
 as kurtosis from mysql_eda1;

select ((sum (power(Coal_RB_5700_FOB_London_Close_USD - (select avg(Coal_RB_5700_FOB_London_Close_USD) from mysql_eda1),4))/
(count(*) *power((select stddev(Coal_RB_5700_FOB_London_Close_USD) from mysql_eda1) , 4 ))) - 3)
 as kurtosis from mysql_eda1;

select ((sum (power(Coal_RB_6000_FOB_London_Close_USD - (select avg(Coal_RB_6000_FOB_London_Close_USD) from mysql_eda1),4))/
(count(*) *power((select stddev(Coal_RB_6000_FOB_London_Close_USD) from mysql_eda1) , 4 ))) - 3)
 as kurtosis from mysql_eda1;

select ((sum (power(Coal_India_5500_CFR_London_Close_USD - (select avg(Coal_India_5500_CFR_London_Close_USD) from mysql_eda1),4))/
(count(*) *power((select stddev(Coal_India_5500_CFR_London_Close_USD) from mysql_eda1) , 4 ))) - 3)
 as kurtosis from mysql_eda1;



