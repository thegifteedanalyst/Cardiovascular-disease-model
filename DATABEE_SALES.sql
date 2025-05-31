SELECT TOP (1000) [customer_id]
      ,[signup_date]
      ,[country]
      ,[column4]
      ,[column5]
      ,[column6]
       
	 FROM [DATABEE_SALES].[dbo].[Customers]
 
 ALTER TABLE Customers
DROP COLUMN column4, column5, column6;



  -- Query to get Top 3 countries by total sales
  USE DATABEE_SALES;  
GO
SELECT TOP 3
    Customers.country,
    SUM(Order_Items.quantity * Order_Items.price) AS total_sales,
    COUNT(DISTINCT Orders.order_id) AS number_of_orders,
    CAST(SUM(Order_Items.quantity * Order_Items.price) AS FLOAT) / COUNT(DISTINCT Orders.order_id) AS average_order_value
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id
JOIN Order_Items ON Orders.order_id = Order_Items.order_id
WHERE Customers.country != 'Other'
GROUP BY Customers.country
ORDER BY total_sales DESC;