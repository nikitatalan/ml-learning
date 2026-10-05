# Part 1

## 1.
select *
from movies.movie
where year=2000 

## 2.
select year, COUNT(year)
from movies.movie
GROUP BY year