import sys
import sqlite3
import pandas as pd

#organism name
query = [str(sys.argv[1])]
conn = sqlite3.Connection('taxa.db3')
c = conn.cursor()

c.execute("""
    SELECT scientific_name
    FROM taxonomy
    WHERE tax_id = (SELECT tax_id
    FROM name
    WHERE name_class = 'common name' AND name = ?)
    """, query)

for row in c:
    print(row)
