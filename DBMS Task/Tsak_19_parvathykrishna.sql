-- Task - 2
-- Create a database
-- Use attached two tables for scenario creation
-- Import csv to mysql(use Table import wizard from right clicking on database name) or create and insert values to table using SQL commands
-- 1) Set suitable SQL contraints to column while creating tables.

SELECT * FROM customer_master;
SELECT * FROM sales_order;

SELECT * FROM customer_master AS cm
INNER JOIN sales_order AS so ON cm.Customer_ID = so.Customer_ID;

SELECT * FROM customer_master AS cm
LEFT JOIN sales_order AS so ON cm.Customer_ID = so.Customer_ID;

SELECT * FROM customer_master AS cm
RIGHT JOIN sales_order AS so ON cm.Customer_ID = so.Customer_ID;

SELECT * FROM customer_master AS cm
CROSS JOIN sales_order AS so ON cm.Customer_ID = so.Customer_ID;

-- 2) Write a command to display first 10 rows.
SELECT * FROM customer_master LIMIT 10;

-- 3) Identify unique items?
SELECT DISTINCT * FROM customer_master;
SELECT DISTINCT Region FROM customer_master;
SELECT DISTINCT Item FROM sales_order;

-- 4) Identify any unit cost is negative?
SELECT * FROM sales_order WHERE 'Unit Cost' < 0;

-- 5) Identify minimum and maximum unit price happened for same item.
SELECT Item, MIN(`Unit Cost`) AS min_unit_cost, MAX(`Unit Cost`) AS max_unit_cost FROM sales_order 
GROUP BY Item;

-- 6) Identify the Total sales happened in the year of 2021?
SELECT SUM(Total) AS total_sales_2021 FROM sales_order
WHERE YEAR(OrderDate) = 2021;

-- 7) Which item is sold maximum in the year 2021?
SELECT Item, SUM(Units) AS total_units_sold
FROM sales_order
WHERE YEAR(OrderDate) = 2021
GROUP BY Item
ORDER BY total_units_sold DESC
LIMIT 1;


-- 8) Identify the region with highest and lowest sales.
SELECT Region, SUM(Total) AS total_sales
FROM customer_master cm
JOIN sales_order so ON cm.Customer_ID = so.Customer_ID
GROUP BY Region
ORDER BY total_sales DESC
LIMIT 1;

SELECT Region, SUM(Total) AS total_sales
FROM customer_master cm
JOIN sales_order so ON cm.Customer_ID = so.Customer_ID
GROUP BY Region
ORDER BY total_sales ASC
LIMIT 1;

-- 9) Identify the customer name having highest sales for the year 2022.
SELECT cm.Customer, SUM(so.Total) AS total_sales
FROM customer_master cm
JOIN sales_order so ON cm.Customer_ID = so.Customer_ID
WHERE YEAR(so.OrderDate) = 2022
GROUP BY cm.Customer
ORDER BY total_sales DESC
LIMIT 1;


-- 10) Which item has highest and lowest unit cost?
SELECT Item, MAX(`Unit Cost`) AS max_unit_cost
FROM sales_order
GROUP BY Item
ORDER BY max_unit_cost DESC
LIMIT 1;

SELECT Item, MIN(`Unit Cost`) AS min_unit_cost
FROM sales_order
GROUP BY Item
ORDER BY min_unit_cost ASC
LIMIT 1;


-- 11) Identify items starts with letter 'P'.
SELECT DISTINCT Item FROM sales_order
WHERE Item LIKE 'P%';

-- 12) Filter the table having items Pen and Pencil.
SELECT * FROM sales_order
WHERE Item IN ('Pen', 'Pencil');

-- 13) Filter the table with unit cost between 1 and 100.
SELECT *
FROM sales_order
WHERE `Unit Cost` BETWEEN 1 AND 100;

-- 14) Identify the customer with more no of transaction(no of entries).
SELECT cm.Customer, COUNT(so.Sales_ID) AS transaction_count
FROM customer_master cm
JOIN sales_order so ON cm.Customer_ID = so.Customer_ID
GROUP BY cm.Customer
ORDER BY transaction_count DESC
LIMIT 1;

-- 15) Identify which item has maximum sales in each region.
SELECT cm.Region, so.Item, SUM(so.Total) AS total_sales
FROM customer_master cm
JOIN sales_order so ON cm.Customer_ID = so.Customer_ID
GROUP BY cm.Region, so.Item
ORDER BY cm.Region, total_sales DESC;

-- 16) Create 5 more scenarios using important inbuilt functions of MySQL.
-- (1) Calculate the average unit cost for each item.
SELECT Item, AVG(`Unit Cost`) AS avg_unit_cost
FROM sales_order
GROUP BY Item;

-- (2) Find the total number of units sold for each item.
SELECT Item, SUM(Units) AS total_units_sold
FROM sales_order
GROUP BY Item;

-- (3) Determine the earliest and latest order dates for each customer.
SELECT cm.Customer, MIN(so.OrderDate) AS earliest_order_date, MAX(so.OrderDate) AS latest_order_date
FROM customer_master cm
JOIN sales_order so ON cm.Customer_ID = so.Customer_ID
GROUP BY cm.Customer;

-- (4) Identify the top 5 customers with the highest total sales.
SELECT cm.Customer, SUM(so.Total) AS total_sales
FROM customer_master cm
JOIN sales_order so ON cm.Customer_ID = so.Customer_ID
GROUP BY cm.Customer
ORDER BY total_sales DESC
LIMIT 5;

-- (5) Calculate the percentage of total sales contributed by each item.
SELECT Item, (SUM(Total) / (SELECT SUM(Total) FROM sales_order)) * 100 AS sales_percentage
FROM sales_order
GROUP BY Item;


