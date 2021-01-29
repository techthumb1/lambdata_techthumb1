import os
import sqlite3

DB_FILEPATH =  os.path.join(os.path.dirname(__file__), "/Users/jasonrobinson/Downloads/rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection) 

cursor = connection.cursor()
print("CURSOR", cursor)

# How many total Characters are there?
query1 = """ SELECT 
Count(name)
FROM charactercreator_character
"""

# How many of each specific subclass?
query2 = """SELECT 
Count(distinct name)
FROM charactercreator_character;
"""

# How many total Items?
query3 = """SELECT 
Count(item_id)
FROM armory_item
"""

# How many of the Items are weapons? How many are not?
query4 = """SELECT 
Count(distinct name) as armory_count
FROM armory_item, armory_weapon
WHERE item_ptr_id = item_id;
"""

# How many of the Items are weapons? How many are not?
query5 = """SELECT character.name, item.name
FROM charactercreator_character AS character,
charactercreator_character_inventory AS inventory,
armory_item AS item
WHERE character.character_id = inventory.character_id
AND inventory.item_id = item.item_id
LIMIT 20
"""

# How many Weapons does each character have? 
# (Return first 20 rows) 
query6 = """SELECT c.character_id,
      c.name as character_name
-- ,inv.item_id
-- ,w.item_ptr_id as weapon_id
   ,count(distinct w.item_ptr_id) as weapon_count
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
LEFT JOIN armory_weapon w ON w.item_ptr_id = inv.item_id
GROUP BY 1
LIMIT (20)
"""

# On average, how many Weapons does each character have?query7 = """
query7 = """Select AVG (weapon_count) as Average_Weapons
from (
	SELECT 
	  c.character_id
	  ,c.name as character_name
   -- ,inv.item_id
   -- ,w.item_ptr_id as weapon_id
	  ,count(distinct w.item_ptr_id) as weapon_count
	FROM charactercreator_character c
	LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
	LEFT JOIN armory_weapon w ON w.item_ptr_id = inv.item_id
	GROUP BY 1
	)
"""
#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

#queries = print(query1, query2, query3, query4, query5, query6, query7)
result2 = cursor.execute(query1).fetchall()
result3 = cursor.execute(query2).fetchall()
result4 = cursor.execute(query3).fetchall()
result5 = cursor.execute(query4).fetchall()
result6 = cursor.execute(query5).fetchall()
result7 = cursor.execute(query6).fetchall()
result8 = cursor.execute(query7).fetchall()
print("RESULT 2", result2)
print("RESULT 3", result3)
print("RESULT 4", result4)
print("RESULT 5", result5)
print("RESULT 6", result6)
print("RESULT 7", result7)
print("RESULT 8", result8)

#or row in result2:
#   print(type(row))
#   print(row)
#   print(row[0])
#   #print(row[1])
#   print("-----")