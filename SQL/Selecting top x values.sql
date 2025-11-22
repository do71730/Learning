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

select distinct  top 10  a.product_id,p.product_name,count(order_id) as num_order_with_products from bikestores.sales.order_items a
inner join bikestores.production.products p on a.product_id = p.product_id
group by  a.product_id,p.product_name
order by 3 desc;

select distinct  a.product_id,p.product_name,count(order_id) as num_order_with_products from bikestores.sales.order_items a
inner join bikestores.production.products p on a.product_id = p.product_id
group by  a.product_id,p.product_name
order by 3 desc
offset 0 row
fetch first 10 row only
