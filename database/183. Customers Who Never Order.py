'''183. Customers Who Never Order
""Example:
Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+'''
#code link: https://leetcode.com/problems/customers-who-never-order/description/?envType=problem-list-v2&envId=database
# Write your MySQL query statement below
SELECT name AS "Customers" 
FROM Customers
where id NOT IN
 (SELECT customerId FROM Orders)
