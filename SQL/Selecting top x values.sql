--Select top 20 rows by customer id
select top 20 * from bikestores.sales.orders 
order by customer_id;

--Select top 20 rows by customer id
select * from bikestores.sales.orders 
order by customer_id 
offset 0 rows
fetch next 20 rows only;

--Select top 20 rows by customer id
select * from bikestores.sales.orders 
order by customer_id 
offset 0 rows
fetch first 20 rows only;

--Skip the first 5 and start at the 6th value all the way to the first 20
select * from bikestores.sales.orders 
order by customer_id 
offset 5 rows
fetch first 20 rows only;

select distinct * from bikestores.sales.order_items a
inner join bikestores.production.products p on a.product_id = b. product_id