from sqlobject import *
import os.path
import sys

dbfile = "taxa.db3"
query = str(sys.argv[1])

conn_str = os.path.abspath(dbfile)
conn_str = 'sqlite:' + conn_str

sqlhub.processConnection = connectionForURI(conn_str)

class Taxonomy(SQLObject):
    class sqlmeta:
        idName = "tax_id"
        fromDatabase = True
    names = MultipleJoin('name', joinColumn="tax_id")


class Name(SQLObject):
    class sqlmeta:
        fromDatabase = True
    taxa = ForeignKey('Taxonomy', dbName="tax_id")


cname = Name.selectBy(name=query)[0]
print(cname.taxa.scientificName)