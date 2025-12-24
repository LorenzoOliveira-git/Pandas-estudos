SELECT seller_id,
sum(price) AS totalRevenue,
count(DISTINCT order_id) AS qtSalles
FROM tb_order_items 
GROUP BY seller_id