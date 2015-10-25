#!flask/bin/python
import sqlite3
from flask import Flask, jsonify, request, abort
from classes import Pulpit

app = Flask(__name__)


def return_objects_from_table(table):
    conn = sqlite3.connect('lab')
    c = conn.cursor()
    objects = []
    for row in c.execute('select * from %s' % table):
        objects.append(row)

    conn.close()

    return objects

@app.route('/pulpits/get', methods=['GET'])
def get_pulpits():
    pulpits = []
    for row in return_objects_from_table('pulpits'):
        pulpit = Pulpit(row[0], row[1], row[2])
        pulpits.append(pulpit.jason())
    return jsonify({'pulpits': pulpits})

@app.route('/pulpits/get/<int:pulpit_id>', methods=['GET'])
def get_pulpit(pulpit_id):
    pulpits = []
    for row in return_objects_from_table('pulpits'):
        pulpit = Pulpit(row[0], row[1], row[2])
        pulpits.append(pulpit.jason())
    pulpit = filter(lambda p: p['id'] == pulpit_id, pulpits)
    if not pulpit:
        return jsonify({'error': 'Not found'})
    return jsonify({'pulpit': pulpit[0]})

@app.route('/pulpits/post', methods=['POST'])
def post_pulpit():
    if not request.json or not 'title' in request.json:
        abort(400)

    conn = sqlite3.connect('lab')
    c = conn.cursor()

    row = c.execute('select max(pulpit_id) from pulpits').fetchone()
    pulpit_id = row[0]

    pulpit = Pulpit(pulpit_id+1, request.json['title'], request.json['description'])
    c.execute('insert into pulpits values(?,?,?)', pulpit.sqlitify())

    conn.commit()
    conn.close()

    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
