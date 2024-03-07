-- Task - Create a table with 10 * 10 dimensions having both numeric and non numeric columns.
-- Build your own scenario and create corresponding queries. Minimum 15 scenarios
-- Eg: Scenario 1 - Choose names with age greater than 18
-- 	Select * from Table where age > 18;

-- Use all the commands shown below and create different meaningful scenarios.
-- SELECT, INSERT, DISTINCT, WHERE, AND, OR, IN, BETWEEN

CREATE TABLE Employee (
    EmployeeID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    Department VARCHAR(50),
    Position VARCHAR(50),
    Salary DECIMAL(10, 2),
    HireDate DATE,
    Location varchar(50)
);

INSERT INTO Employee (EmployeeID, FirstName, LastName, Age, Gender, Department, Position, Salary, HireDate, Location)
VALUES
(1, 'Parvathy', 'Krishna', 23, 'Female', 'IT', 'Developer', 50000.00, '2023-07-20', 'India'),
(2, 'John', 'Pol', 25, 'Male', 'IT', 'Developer', 65000.00, '2021-09-23', 'London'),
(3, 'Blair', 'Lee', 28, 'Male', 'Marketing', 'Marketing Coordinator', 62000.00, '2019-08-10', 'Chicago'),
(4, 'Daniel', 'Muna', 38, 'Male', 'Sales', 'Sales Representative', 68000.00, '2018-06-15', 'Paris'),
(5, 'Sarah', 'Anderson', 29, 'Female', 'IT', 'System Analyst', 75000.00, '2020-03-20', 'San Francisco'),
(6, 'Mathew', 'Wilson', 42, 'Male', 'Finance', 'Financial Analyst', 72000.00, '2017-11-05', 'Chicago'),
(7, 'Anu', 'Thomas', 31, 'Female', 'HR', 'HR Specialist', 67000.00, '2019-02-25', 'India'),
(8, 'Ryan', 'Taylor', 36, 'Male', 'IT', 'Tester', 80000.00, '2018-09-30', 'London'),
(9, 'Olivia', 'Marco', 27, 'Female', 'Sales', 'Sales Associate', 60000.00, '2021-01-05', 'San Francisco'),
(10, 'David', 'Miller', 33, 'Male', 'Marketing', 'Marketing Manager', 85000.00, '2016-07-12', 'Atlanta'),
(11, 'Sophia', 'Mary', 34, 'Female', 'Finance', 'Financial Controller', 90000.00, '2015-05-20', 'London'),
(12, 'Alexander', 'Haris', 39, 'Male', 'HR', 'HR Manager', 95000.00, '2014-03-18', 'Paris');

SELECT * FROM EMPLOYEE;

SELECT * FROM Employee WHERE Salary > 70000;

SELECT DISTINCT Gender FROM Employee;

SELECT * FROM Employee WHERE Department = 'IT' and Position = 'Developer';

SELECT * FROM Employee WHERE Department IN ('Sales', 'Marketing');

SELECT * FROM Employee WHERE HireDate BETWEEN '2019-01-01' AND '2021-12-31';

SELECT * FROM Employee WHERE LastName LIKE 'M%' AND Location = 'London';

SELECT * FROM Employee WHERE Department = 'Finance' OR Location = 'India';

SELECT * FROM Employee WHERE FirstName IN ('Sarah', 'David');

SELECT * FROM Employee WHERE Age BETWEEN 25 AND 35;

SELECT * FROM Employee WHERE Salary NOT BETWEEN 50000 AND 60000;

SELECT * FROM Employee WHERE Gender = 'Female' AND (Department = 'HR' OR Age < 30);

SELECT * FROM Employee WHERE Salary NOT BETWEEN 60000 AND 80000 AND Location = 'Paris';

SELECT * FROM Employee WHERE Position != 'Developer';

SELECT * FROM Employee WHERE Position LIKE '%Manager%';

SELECT * FROM Employee WHERE FirstName LIKE 'A%' AND Salary > 60000;

SELECT DISTINCT Department, Position FROM Employee;

SELECT * FROM Employee WHERE Salary > 60000 AND Department LIKE '%Marketing%';






