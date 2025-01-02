This module is meant to be used in small to medium scale applications and makes SQLite3 Read and Write functions python.
Changing every DataBase, Table and Row object to classes.

# Quickstart
```cmd
pip install data3
```
1. To get the entire DataBase use:
   ```py
   with data.open() as db:
     print(db.getColumns()) 
   ```
   , or use `with data.open(table="YourTable") as table:` to get just one table.
2. Index a table with `databaseObject["YourTable"]`
3. Read data with `table.get()`, you can narrow down your search by using `table.get(column=value)` or use `table.first()` to get only the first value
4. Adding/updating/removing data works as following: table.add(column=value, column=value...), table.update(column=value)(column=value, column=value...), table.remove(column=value)
5. By adding, finding or updating data you will be returned a rowObject which you can index with columns to find one value, you can use .pk to get just the primaryKey, it can also be converted to a Dict or you can edit your row by using rowObject["column"] = value or rowObject(column=value, column=value)

# Example
```py
import data

with data.open(table="matches") as table:
    for row in table.find():
        row["started"] = True
    
    table.update(5)(started = False)

    table(id = 90, started = False)

    print(table.first(3)["started"])

    with table.pause():
        print("Free from the database.")

    print("Back to reading and writing.")

    table.remove(3)
```  

# Edit default values
```py
import data

# These are the default values and you can edit them accordingly
data.path = './'
data.defaultFile = "data"
data.fileExtension = ".db"
data.defaultTimeout = 10

# This is the default onError function, which you can modify
def onError(error, cmd):
    print(f"[Error\t] {error}\n[input\t] {cmd}")
self.onError = onError
```
