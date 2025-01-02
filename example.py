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