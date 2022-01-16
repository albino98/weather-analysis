from flask import Flask, render_template, jsonify, request
import mysql.connector
from secrets import secrets
app = Flask(__name__)


def connectToMySql():
    mydb = mysql.connector.connect(
        host=secrets.get('DB_LOCALHOST'),
        user=secrets.get('DB_LOCALHOST_USR'),
        # password="yourpassword",
        database=secrets.get('DB_LOCALHOST_NAME')
    )
    return mydb

@app.route('/getChartData',methods=['GET'])
def getChartData():
    parameter = request.args.get('parameter')
    mydb = connectToMySql()
    arr_dt = []
    result = {}
    try:
        mycursor = mydb.cursor()
        query = "SELECT dt, "+parameter+" FROM `forecastData` ORDER BY `dt` ASC"
        mycursor.execute(query)
        query_result = mycursor.fetchall()
        mydb.close()
    except:
        mydb.close()
        query_result = False

    for row in query_result:
        arr_dt.append(str(row[0].strftime('%Y:%m:%d %H:%M:%S')))
        print(str(row[0].strftime('%Y:%m:%d %H:%M:%S')))

    return jsonify(query_result)


@app.route('/')
def index():
    return render_template('index.html')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()


