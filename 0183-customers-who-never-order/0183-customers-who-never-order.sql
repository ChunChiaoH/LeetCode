# Write your MySQL query statement below
#select name as Customers
#from Customers
#where id not in (select customerId from Orders);
SELECT name AS Customers
FROM Customers LEFT JOIN Orders
     ON Customers.id = Orders.customerId
WHERE Orders.id is null