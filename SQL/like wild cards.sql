
select distinct product_name from BikeStores.production.products order by product_name --291

--The percent wildcard (%): any string of zero or more characters.
select distinct product_name from BikeStores.production.products
where product_name like 'Electra%'
order by product_name

--Sun Bicycles Cruz 3 - 2017
--Sun Bicycles Cruz 7 - Women's - 2017
--The underscore (_) wildcard: any single character.
select distinct product_name from BikeStores.production.products
where product_name like '%cruz _%'
order by product_name

--The [list of characters] wildcard: any single character within the specified set.
select distinct product_name from BikeStores.production.products 
where product_name like '[PR]%' --beginning with P or R
order by product_name

--The [character-character]: any single character within the specified range.
select distinct product_name from BikeStores.production.products 
where product_name like '[P-S]%' --beginning with letter between P-S included
order by product_name


--The [^]: any character that is not within a list or a range.
select distinct product_name from BikeStores.production.products 
where product_name like '[^P-S]%' --return all the products not beginning with letters between [P-S]
order by product_name

select * from master.sales.feedbacks where comment like '%!%%' escape '!'; --Treat ! as an escape character
select * from master.sales.feedbacks where comment like '%*%%' escape '*'; --Treat * as an escape character
select * from master.sales.feedbacks where comment like '%X%%' escape 'X'; --Treat X as an escape character

--https://www.sqlservertutorial.net/sql-server-basics/sql-server-joins/ next

select * from BikeStores.production.products 
where brand_id in (9,8,7,6)

select * from BikeStores.production.products a
where  exists (select brand_id from BikeStores.production.products --returns true, if any value returns(even null) in the subquery, else false
where brand_id in (10))

select * from BikeStores.production.products a
where  brand_id in(select brand_id from BikeStores.production.products 
where brand_id in (9,8,7,6))

--any
--all
-- cross appy