from decision_making import dm
import psycopg2 
import psycopg2.extras
from flask import Flask, request, render_template, jsonify
from scikitmcda.dmuu import DMUU



   
app = Flask(__name__)
   

   
DB_HOST = "localhost"
DB_NAME = "sampledb"
DB_USER = "postgres"
DB_PASS = "admin"
   
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
   
@app.route('/')
def home():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * from decision order by id")
        decisionlist = cursor.fetchall()
        return render_template('index.html',decisionlist=decisionlist)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
  
@app.route("/update",methods=["POST","GET"])
def update():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if request.method == 'POST':
            
            field = request.form['field'] 
            value = request.form['value']
            editid = request.form['id']
              
            if field == 'alternative':
               sql = "UPDATE decision SET alternative=%s WHERE id=%s"
            if field == 'customersegments':
               sql = "UPDATE decision SET customersegments=%s WHERE id=%s"
            if field == 'valuepropositions':
               sql = "UPDATE decision SET valuepropositions=%s WHERE id=%s"
            if field == 'channels':
               sql = "UPDATE decision SET channels=%s WHERE id=%s"
            if field == 'customerrelationships':
               sql = "UPDATE decision SET customerrelationships=%s WHERE id=%s"
            if field == 'revenuestreams':
               sql = "UPDATE decision SET revenuestreams=%s WHERE id=%s"
            if field == 'keyresources':
               sql = "UPDATE decision SET keyresources=%s WHERE id=%s"
            if field == 'keyactivities':
               sql = "UPDATE decision SET keyactivities=%s WHERE id=%s"
            if field == 'keypartnerships':
               sql = "UPDATE decision SET keypartnerships=%s WHERE id=%s"
            if field == 'coststructure':
               sql = "UPDATE decision SET coststructure=%s WHERE id=%s"
            
            
            data = (value, editid)
            cursor.execute(sql, data)
            conn.commit()
            success = 1
        return jsonify(success)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
@app.route("/decide", methods=['GET', 'POST'])
def index():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        if request.form.get('add'):
            try:
                sql="INSERT INTO decision (alternative, customersegments, valuepropositions, channels, customerrelationships, revenuestreams, keyresources, keyactivities, keypartnerships, coststructure) VALUES ('Alternative Name',0,0,0,0,0,0,0,0,0)"
                cursor.execute(sql)
                conn.commit()
                cursor.execute("SELECT * from decision order by id")
                decisionlist = cursor.fetchall()
                return render_template('index.html',decisionlist=decisionlist)

            except Exception as e:
                print(e)
            finally:
                cursor.close() 
        elif(request.form.get('remove')):
            try: 
                sql="DELETE FROM decision WHERE id = (SELECT MAX(id) FROM decision)"
                cursor.execute(sql)
                conn.commit()
                cursor.execute("SELECT * from decision order by id")
                decisionlist = cursor.fetchall()
                return render_template('index.html',decisionlist=decisionlist)
            except Exception as e:
                print(e)
            finally:
                cursor.close() 
        elif(request.form.get('maximax')):
            cursor.execute("SELECT * from decision order by id")
            edit = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]
            field_names.pop(0)
            field_names.pop()
            alternatives = [i[0] for i in edit]
            values=[]
            i=0
            for List in edit:
                L=edit[i]
                L.pop()
                del L[0]
                values.append(L)
                i+=1
            
            dm.decision_making(values,alternatives,field_names,'maximax')
            cursor.execute("SELECT * from decision order by id")
            decisionlist = cursor.fetchall()
            return render_template('index.html',decisionlist=decisionlist)
           
        elif(request.form.get('maximin')):
            cursor.execute("SELECT * from decision order by id")
            edit = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]
            field_names.pop(0)
            field_names.pop()
            alternatives = [i[0] for i in edit]
            values=[]
            i=0
            for List in edit:
                L=edit[i]
                L.pop()
                del L[0]
                values.append(L)
                i+=1
            
            dm.decision_making(values,alternatives,field_names,'maximin')
            cursor.execute("SELECT * from decision order by id")
            decisionlist = cursor.fetchall()
            return render_template('index.html',decisionlist=decisionlist)
           
        elif(request.form.get('minimax_regret')):
            cursor.execute("SELECT * from decision order by id")
            edit = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]
            field_names.pop(0)
            field_names.pop()
            alternatives = [i[0] for i in edit]
            values=[]
            i=0
            for List in edit:
                L=edit[i]
                L.pop()
                del L[0]
                values.append(L)
                i+=1
            
            dm.decision_making(values,alternatives,field_names,'minimax_regret')
            cursor.execute("SELECT * from decision order by id")
            decisionlist = cursor.fetchall()
            return render_template('index.html',decisionlist=decisionlist)          
        else:
            pass # unknown
    elif request.method == 'GET':
        try:
            cursor.execute("SELECT * from decision order by id")
            decisionlist = cursor.fetchall()
            return render_template('index.html',decisionlist=decisionlist)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
    
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug = True)


    