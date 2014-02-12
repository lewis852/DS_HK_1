-- What customers are from the UK
SELECT * FROM customers
	Where Country = 'UK'

-- What is the name of the customer who has the most orders?
SELECT Customers.CustomerName, Count(Orders.CustomerID) FROM Orders
JOIN Customers on (Orders.CustomerID = Customers.CustomerID)
GROUP BY Orders.CustomerID
ORDER BY Count(Orders.CustomerID) DESC
LIMIT 1

-- What supplier has the highest average product price?
SELECT SupplierName, Avg(Products.Price) FROM Suppliers
JOIN Products on (Suppliers.SupplierID = Products.SupplierID)
GROUP BY Suppliers.SupplierID
ORDER BY Avg(Products.Price) DESC
LIMIT 1


-- What category has the most orders?


-- What employee made the most sales (by number of sales)?


-- What employee made the most sales (by value of sales)?


-- What employees have BS degrees? (Hint: Look at LIKE operator)


-- What supplier has the highest average product price assuming they have at least 2 products (Hint: Look at the HAVING operator)


-- Submit these SQL queries as a .sql file to GitHub, using SQL comments to have the question referring to each: