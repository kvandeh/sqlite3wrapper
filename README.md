This module is meant to be used in small to medium scale applications and makes SQLite3 Read and Write functions python.
Changing every DataBase, Table and Row object to classes.

# Quickstart
1. To get the entire DataBase use:
   ```py
   with data.open() as db:
     print(db.getColumns()) 
   ```
   , or use `with data.open(table="YourTable") as table:` to get just one table.
3. Index a table with `databaseObject["YourTable"]`
4. Read data with `table.get()`, you can narrow down your search by using `table.get(column=value)` or use `table.first()` to get only the first value
5. Adding/updating/removing data works as following: table.add(column=value, column=value...), table.update(column=value)(column=value, column=value...), table.remove(column=value)
6. By adding, finding or updating data you will be returned a rowObject which you can index with columns to find one value, you can use .pk to get just the primaryKey, it can also be converted to a Dict or you can edit your row by using rowObject["column"] = value or rowObject(column=value, column=value)

