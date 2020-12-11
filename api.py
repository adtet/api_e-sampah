import flask
import mysql.connector
from flask import Flask, jsonify, request
import uuid
import base64
import hashlib
import json
from waitress import serve

app = Flask(__name__)


@app.route('/user/register', methods=['POST'])
def register():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"pesan": "error"}
        return jsonify(hasil)
    else:
        nama = json_data['nama']
        email = json_data['email']
        passwd = json_data['password']
        db = mysql.connector.connect(host="localhost",
                                     user="adit",
                                     password="aditPa$$word2781",
                                     database="e-sampah")
        cursor = db.cursor()
        id = str(uuid.uuid4().hex)
        passwd = hashlib.md5(passwd.encode("utf-8")).hexdigest()
        cursor.execute("SELECT email FROM user where email=%s ", (email, ))
        a = cursor.fetchone()
        if a == None:
            cursor.execute(
                "INSERT INTO user (idn,name,email,pass) values (%s,%s,%s,%s)",
                (id, nama, email, passwd))
            db.commit()
            hasil = {"pesan": "TELAH BERHASIL DAFTAR"}
            return jsonify(hasil)
        else:
            hasil = {"pesan": "EMAIL ANDA SUDAH TERDAFTAR"}
            return jsonify(hasil)


@app.route('/user/login', methods=['POST'])
def login():
    json_data_1 = flask.request.json
    if json_data_1 == None:
        hasil = {"id": "ERROR"}
        return jsonify(hasil)
    else:
        email = json_data_1['email']
        password = json_data_1['password']
        if email == None and password == None:
            hasil = {"id": "Null"}
            return flask.Response()
        else:
            password = hashlib.md5(password.encode("utf-8")).hexdigest()
            db = mysql.connector.connect(host="localhost",
                                         user="adit",
                                         password="aditPa$$word2781",
                                         database="e-sampah")
            cursor = db.cursor()
            cursor.execute("Select idn from user where email=%s and pass=%s",
                           (email, password))
            b = cursor.fetchone()
            if b == None:
                hasil = {"id": "Akun Tersebut Tidak Tersedia"}
                return jsonify(hasil)
            else:
                hasil = {"id": b[0]}
                return jsonify(hasil)


@app.route('/data/sampah', methods=['POST'])
def sampah():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"berat": "error", "jenis": "error"}
        return jsonify(hasil)
    else:
        id = json_data['id']
        db = mysql.connector.connect
        db = mysql.connector.connect(host="localhost",
                                     user="adit",
                                     password="aditPa$$word2781",
                                     database="e-sampah")
        cursor = db.cursor()
        cursor.execute("SELECT berat,jenis FROM data_sampah where ids=%s",
                       (id, ))
        c = cursor.fetchone()
        if c == None:
            hasil = {"berat": "kosong", "jenis": "kosong"}
            return jsonify(hasil)
        else:
            hasil = {"berat": c[0], "jenis": c[1]}
            return jsonify(hasil)


@app.route('/transaksi', methods=['POST'])
def transaksi():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"idn": "error", "jmlh_sampah": "error", "tabungan": "error"}
        return jsonify(hasil)
    else:
        id = json_data['id']
        db = mysql.connector.connect
        db = mysql.connector.connect(host="localhost",
                                     user="adit",
                                     password="aditPa$$word2781",
                                     database="e-sampah")
        cursor = db.cursor()
        cursor.execute(
            "SELECT idn,jmlh_sampah,tabungan FROM transaksi WHERE id_transaksi=%s",
            (id, ))
        d = cursor.fetchone()
        if d == None:
            hasil = {
                "idn": "kosong",
                "jmlh_sampah": "kosong",
                "tabungan": "kosong"
            }
            return jsonify(hasil)
        else:
            hasil = {"idn": d[0], "jmlh_sampah": d[1], "tabungan": d[2]}
            return jsonify(hasil)


@app.route('/tabungan', methods=['POST'])
def tabungan():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"jmlh_sampah": "error", "idn": "error"}
        return jsonify(hasil)
    else:
        id = json_data['id']
        db = mysql.connector.connect
        db = mysql.connector.connect(host="localhost",
                                     user="adit",
                                     password="aditPa$$word2781",
                                     database="e-sampah")
        cursor = db.cursor()
        cursor.execute(
            "SELECT jmlh_tabungan,idn FROM tabungan WHERE id_tabungan=%s",
            (id, ))
        e = cursor.fetchone()
        if e == None:
            hasil = {"jmlh_tabungan": "kosong", "idn": "kosong"}
            return jsonify(hasil)
        else:
            hasil = {"jmlh_tabungan": e[0], "idn": e[1]}
            return jsonify(hasil)


@app.route('/penarikan', methods=['POST'])
def penarikan():
    json_data = flask.request.json
    if json_data == None:
        hasil = {
            "idn": "error",
            "id_tabungan": "error",
            "jumlah_ditarik": "error",
            "tgltarik": "error"
        }
        return jsonify(hasil)
    else:
        id = json_data['id']
        db = mysql.connector.connect(host="localhost",
                                     user="adit",
                                     password="aditPa$$word2781",
                                     database="e-sampah")
        cursor = db.cursor()
        cursor.execute(
            "SELECT idn,id_tabungan,jumlah_ditarik,tgltarik FROM penarikan WHERE id_penarikan=%s",
            (id, ))
        x = cursor.fetchone()
        if x == None:
            hasil = {
                "idn": "kosong",
                "id_tabungan": "kosong",
                "jumlah_ditarik": "kosong",
                "tgltarik": "kosong"
            }
            return jsonify(hasil)
        else:
            hasil = {
                "idn": x[0],
                "id_tabungan": x[1],
                "jumlah_ditarik": x[2],
                "tgltarik": x[3]
            }
            return jsonify(hasil)


@app.route('/update/sampah', methods=['POST'])
def updatesampah():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"sampah": "error", "berat": "error", "ids": "error"}
        return jsonify(hasil)
    else:
        ids = json_data["id"]
        berat = json_data["berat"]
        jenis = json_data["jenis"]
        con = mysql.connector.connect(host="localhost",
                                      user="adit",
                                      password="aditPa$$word2781",
                                      db="e-sampah")
        dbcursor = con.cursor()
        sql = "UPDATE data_sampah SET berat=%s WHERE ids=%s"
        dbcursor.execute(sql, (berat, ids))
        con.commit()
        hasil = {"sampah": jenis, "berat": berat, "ids": ids}
        return jsonify(hasil)


@app.route('/transaksi/input', methods=['POST'])
def inputTransaksi():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"pesan": "failed"}
        return jsonify(hasil)
    else:
        id = json_data['id']
        jmlh_sampah = json_data['berat']
        tabungan = json_data['tabungan']
        con = mysql.connector.connect(host="localhost",
                                      user="adit",
                                      password="aditPa$$word2781",
                                      db="e-sampah")
        cursor = con.cursor()
        cursor.execute(
            'INSERT INTO `transaksi`(`id_nasabah`, `jmlh_sampah`, `tabungan`) VALUES (%s,%s,%s)',
            (id, jmlh_sampah, tabungan))
        con.commit()
        hasil = {"pesan": "Berhasil"}
        return jsonify(hasil)


@app.route('/transaksi/cek', methods=['POST'])
def cek_transaksi():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"pesan": "failed"}
        return jsonify(hasil)
    else:
        id = json_data['idn']
        cek = cek_id_nasabah(id)
        if cek == 0:
            hasil = {"pesan": "Null"}
            return jsonify(hasil)
        else:
            total = sum_tabungan_transaksi(id)

            hasil = {"pesan": str(total)}
            return jsonify(hasil)


def cek_id_nasabah(a):
    con = mysql.connector.connect(host="localhost",
                                  user="adit",
                                  password="aditPa$$word2781",
                                  db="e-sampah")
    cursor = con.cursor()
    cursor.execute("SELECT id_nasabah FROM transaksi where id_nasabah=%s",
                   (a, ))
    a = cursor.fetchone()
    if a == None:
        return 0
    else:
        return 1


def sum_tabungan_transaksi(a):
    con = mysql.connector.connect(host="localhost",
                                  user="adit",
                                  password="aditPa$$word2781",
                                  db="e-sampah")
    cursor = con.cursor()
    cursor.execute("SELECT SUM(tabungan) FROM transaksi where id_nasabah=%s",
                   (a, ))
    b = cursor.fetchone()
    if b == None:
        return 0
    else:
        return b[0]


if __name__ == "__main__":
    #app.run(port=1000,debug=True)
    serve(app, host="0.0.0.0", port=1000)
