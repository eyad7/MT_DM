import psycopg2



conn = psycopg2.connect(database="sampledb", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    
# except:
#     print("I am unable to connect to the database") 
print(conn)
cur = conn.cursor()
sql ='''CREATE TABLE decision (
		id serial PRIMARY KEY,
		alternatvie VARCHAR ( 100 ) NOT NULL,
		customerSegments INT NOT NULL, 
		valuePropositions INT NOT NULL, 
		channels INT NOT NULL,
		customerRelationships INT NOT NULL, 
		revenueStreams INT NOT NULL, 
		keyResources INT NOT NULL, 
		keyActivities INT NOT NULL,
		keyPartnerships INT NOT NULL, 
		costStructure  INT NOT NULL

)'''
try:
   cur.execute(sql)
except Exception as e:
        print(e)

conn.commit() # <--- makes sure the change is shown in the database
conn.close()
cur.close()

