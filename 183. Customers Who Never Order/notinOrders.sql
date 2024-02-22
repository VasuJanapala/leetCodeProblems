SELECT name AS Customers from Customers WHERE id NOT IN (
SELECT c.id
FROM Customers C
INNER JOIN Orders O ON O.customerID = C.id
WHERE O.id)