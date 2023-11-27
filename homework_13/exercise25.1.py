from sqlobject import *
import os.path
import sys

dbfile = "small_taxa.db3"

conn_str = os.path.abspath(dbfile)
conn_str = 'sqlite:' + conn_str
sqlhub.processConnection = connectionForURI(conn_str)

class Name(SQLObject):
    taxonomy = ForeignKey("Taxonomy")
    name = StringCol()
    name_class = StringCol()

# Define the Taxonomy table
class Taxonomy(SQLObject):
    taxid = IntCol(alternateID=True)
    scientific_name = StringCol()
    rank = StringCol()
    parent = ForeignKey("Taxonomy")

    names = MultipleJoin("Name")
    children = MultipleJoin("Taxonomy", joinColumn="parent_id")


query = sys.argv[1]
cname = Name.selectBy(name=query)[0]
for n in cname.taxonomy.children:
    print(n.scientific_name)