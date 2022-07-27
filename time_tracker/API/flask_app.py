from flask import Flask, request, jsonify
import sqlite3 as sq
from flask_restful import Resource, Api
import os, sys
from datetime import timedelta
#
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
app = Flask(__name__)
api = Api(app)
#
class Time(Resource):
    def get(self):
        dbcon = sq.connect(os.path.join(currentdir,'Time.db'))
        dbcur = dbcon.cursor()
        data = dbcur.execute('select * from Time').fetchall()
        return jsonify(data)
    def post(self):
        try:
            data = request.get_json()
            start_time = data['start_time']
            stop_time = data['stop_time']
            project_name = data['project_name']
            project_source = data['project_source']
            project_number = data['project_number']
            run_time = str(timedelta(seconds=stop_time-start_time))
            dbcon = sq.connect(os.path.join(currentdir,'time.db'))
            dbcur = dbcon.cursor()
            dbcur.execute("""insert into Time values (?, ?, ?, ?, ?, ?)""",(project_source,project_number,project_name,start_time,stop_time,run_time,))
            dbcon.commit()
            dbcon.close()
            return jsonify({'message':f'Successfully inserted time into database. Thank you for using the tool you created for yourself in hopes of actually needing it.'})
        except Exception as e:
            return jsonify({'message':f'Unable to insert time into database. Please record the following manually.\n{request.headers}'})

api.add_resource(Time, '/')

if __name__ == '__main__':
    app.run(debug = False,host='0.0.0.0',port=5000)