SELECT
    e.name 
FROM employee e
LEFT JOIN employee m
  ON e.id = m.managerId
GROUP BY e.id, e.name
HAVING COUNT(m.id) >= 5
ORDER BY COUNT(m.id) DESC;
