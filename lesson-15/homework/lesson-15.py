##Homework
# 1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. 
# The Name and Species columns should be text fields, and the Age column should be an integer field.
import pyodbc
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "Server=DESKTOP-QSPM8B9;"
    "trusted_Connection=yes;",
    autocommit=True
 )

cursor = conn.cursor()
drop_sql_database = "DROP DATABASE IF EXISTS Lesson_15"
cursor.execute(drop_sql_database)
print("Old database (if existed) dropped.")

cursor.execute("CREATE DATABASE Lesson_15")
print("Database created.")

conn.close()

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "Server=DESKTOP-QSPM8B9;"
    "DATABASE=Lesson_15;"
    "trusted_Connection=yes;"
)
cursor = conn.cursor()
drop_sql = "DROP TABLE IF EXISTS Roster"
cursor.execute(drop_sql)
create_table = ("CREATE TABLE Roster (Name NVARCHAR(100), Species NVARCHAR(100), Age INT)")
cursor.execute(create_table)
print("Roster table created.")
##2.Populate your new table with the following values:
insert_sql = """
    INSERT INTO Roster (Name, Species, Age) VALUES  
    ('Benjamin Sisko', 'Human', 40), 
    ('Jadzia Dax', 'Trill', 300), 
    ('Kira Nerys', 'Bajoran', 29)
"""
cursor.execute(insert_sql)
##3.Update the Name of Jadzia Dax to be Ezri Dax
update_sql = """
    UPDATE Roster 
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax'"""
cursor.execute(update_sql)
conn.commit()
print("Name updated✅")

##4.Display the Name and Age of everyone in the table classified as Bajoran.
select_sql = "SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'"
cursor.execute(select_sql)
rows = cursor.fetchall()
for row in rows:
    print(f"Name: {row.Name}, Age: {row.Age}")



cursor.close()
conn.close()
##-------------------------------------------------------------------------------------------------------
