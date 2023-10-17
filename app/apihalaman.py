from . import app,mysql
from flask import render_template, request, jsonify, redirect, url_for
import os
import textwrap
from PIL import Image
from io import BytesIO
import locale
import urllib.parse
##======================================================== halaman user ===============================================================
@app.route('/')
def homepage():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM berita order by id DESC")
    berita = con.fetchall()
    info_list = []
    for sistem in berita:
        des = str(sistem[3])
        des = textwrap.shorten(des,width=75, placeholder="...")
        
        list_data = {
            'id': str(sistem[0]),
            'judul': str(sistem[1]),
            'gambar': str(sistem[2]),
            'deskripsi': des,
            'deskripsifull': str(sistem[3]),
            'tanggal': str(sistem[4]),
            'link': str(sistem[5]),
        }
        info_list.append(list_data)
    return render_template('homepage.html',info_list = info_list)
@app.route('/berita/<link>')
def detail_berita(link):
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM berita where link = %s order by id DESC " , (link,))
    berita = con.fetchall()
    info_list = []
    for sistem in berita:
        des = str(sistem[3])
        des = textwrap.shorten(des,width=75, placeholder="...")
        list_data = {
            'id': str(sistem[0]),
            'judul': str(sistem[1]),
            'gambar': str(sistem[2]),
            'deskripsi': des,
            'deskripsifull': str(sistem[3]),
            'tanggal': str(sistem[4])
        }
        info_list.append(list_data)
    return render_template('detail_berita.html',info_list = info_list)
@app.route('/sejarah')
def sejarah():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM sejarah_desa")
    sejarah = con.fetchall()
    print(sejarah)
    info_list = []
    for sistem in sejarah:
        print(sistem)
        list_data = {
            'id': str(sistem[0]),
            'sejarah': str(sistem[1]),
            'visi': str(sistem[2]),
            'misi': sistem[3].split('","')
        }
        info_list.append(list_data)
    return render_template("sejarah.html", info_list = info_list)
##=================================================== halaman admin =============================================================================
@app.route('/admin')
def admin():
    return render_template("admin/login.html")
#sejarah
@app.route('/admin/infodesa')
def admininfodesa():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM sejarah_desa")
    sejarah = con.fetchall()
    print(sejarah)
    info_list = []
    for sistem in sejarah:
        print(sistem)
        list_data = {
            'id': str(sistem[0]),
            'sejarah': str(sistem[1]),
            'visi': str(sistem[2]),
            'misi': sistem[3].split('","')
        }
        info_list.append(list_data)
    return render_template("admin/infodesa.html", info_list = info_list)

@app.route('/admin/edit_sejarah', methods=['GET','POST'], endpoint='edit_sejarah_endpoint')
def edit_sejarah():
    if request.method == 'POST':
        con = mysql.connection.cursor()
        sejarah = request.form['sejarah']
        print(str(sejarah))
        con.execute("UPDATE sejarah_desa SET sejarah = %s WHERE id = 1",(str(sejarah),))
        mysql.connection.commit()
        return jsonify("msg : SUKSES")
    else:
        con = mysql.connection.cursor()
        con.execute("SELECT * FROM sejarah_desa WHERE id = 1") 
        info = con.fetchone() 
        return render_template("admin/editsejarah.html",info=info)
    
#visimisi
@app.route('/admin/visimisi')
def adminvisimisi():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM sejarah_desa")
    visi = con.fetchall()
    info_list = []
    for sistem in visi:
        print(sistem)
        list_data = {
            'id': str(sistem[0]),
            'sejarah': str(sistem[1]),
            'visi': str(sistem[2]),
            'misi': sistem[3].split('","')
        }
        info_list.append(list_data)
    return render_template("admin/visimisi.html", info_list = info_list)

@app.route('/admin/visimisiedit', methods=['POST'])
def adminvisimisiedit():
    con = mysql.connection.cursor()
    visi = request.form['visi']
    con.execute("UPDATE sejarah_desa SET visi= %s WHERE id = 1",(str(visi)))
    mysql.connection.commit()
    return redirect(url_for("adminvisimisi"))
    


#berita
@app.route('/admin/berita')
def admindberita():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM berita order by id DESC")
    berita = con.fetchall()
    info_list = []
    for sistem in berita:
        des = str(sistem[3])
        des = textwrap.shorten(des,width=75, placeholder="...")
        list_data = {
            'id': str(sistem[0]),
            'judul': str(sistem[1]),
            'gambar': str(sistem[2]),
            'deskripsi': des,
            'deskripsifull': str(sistem[3]),
            'tanggal': str(sistem[4])
        }
        info_list.append(list_data)
        

    return render_template("admin/berita.html", info_list = info_list)

@app.route('/admin/edit_berita', methods=['POST'])
def edit_berita():
    con = mysql.connection.cursor()
    id = request.form['id']
    judul = request.form['judul']
    try:
        if request.files['gambar']:
            file = request.files['gambar']
            con.execute("SELECT gambar FROM berita WHERE id = %s", (id,))
            result = con.fetchone()
            if result:
                filename = result[0]
        
            # Delete the image file
                if filename:
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    if os.path.exists(image_path):
                        os.remove(image_path)
                        
            img = Image.open(file)
            img = img.convert('RGB')
            # Resize gambar
            width, height = 600, 300  # Atur sesuai kebutuhan Anda
            img = img.resize((width, height))

            # Simpan gambar yang diresize ke BytesIO
            img_io = BytesIO()
            img.save(img_io, 'JPEG', quality=70)
            img_io.seek(0)
            random_name = uuid.uuid4().hex+".jpg"
            destination = os.path.join(app.config['UPLOAD_FOLDER'], random_name)
            img.save(destination)  # Ganti dengan lokasi penyimpanan yang diinginkan
            deskripsi = request.form['deskripsi']
            con.execute("UPDATE berita SET judul = %s, gambar = %s, deskripsi = %s WHERE id = %s",(judul,random_name,deskripsi,id))
            mysql.connection.commit()
            # Gunakan img_io atau file yang telah diresize sesuai kebutuhan Anda
    except:
        deskripsi = request.form['deskripsi']
        con.execute("UPDATE berita SET judul = %s, deskripsi = %s WHERE id = %s",(judul,deskripsi,id))
        mysql.connection.commit()
    return jsonify({"msg" : "SUKSES"})

@app.route('/hapus_berita', methods=['POST'])
def hapus_berita():
    con = mysql.connection.cursor()
    id = request.form['id']
    
    # Get the filename of the image associated with the news article
    con.execute("SELECT gambar FROM berita WHERE id = %s", (id,))
    result = con.fetchone()
    if result:
        filename = result[0]
        
        # Delete the image file
        if filename:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if os.path.exists(image_path):
                os.remove(image_path)
    
    # Delete the news article from the database
    con.execute("DELETE FROM berita WHERE id = %s", (id,))
    mysql.connection.commit()
    return jsonify({"msg": "SUKSES"})
#Dana
@app.template_filter('format_currency')
def format_currency(value):
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    return locale.currency(value, grouping=True, symbol='RP')

@app.route('/admin/dana')
def admindana():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM dana ")
    dana = con.fetchall()
    info_list = []
    for sistem in dana:
        list_data = {
            'id': str(sistem[0]),
            'tahun': str(sistem[1]),
            'gambar': str(sistem[2]),
            'total_anggaran': str(sistem[3]),
            'realisasi': str(sistem[4]),
            'lebih': str(sistem[5])
        }
        
        info_list.append(list_data)
    return render_template("admin/dana.html", info_list = info_list)

@app.route('/admin/tambah_dana', methods=['POST'])
def tambah_dana():
    con = mysql.connection.cursor()
    tahun = request.form['tahun']
    file = request.files['gambar']
    if file:
            img = Image.open(file)
            img = img.convert('RGB')
            # Resize gambar

            # Simpan gambar yang diresize ke BytesIO
            img_io = BytesIO()
            img.save(img_io, 'JPEG', quality=70)
            img_io.seek(0)
            filename = file.filename
            destination = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img.save(destination)  # Ganti dengan lokasi penyimpanan yang diinginkan
            
            # Gunakan img_io atau file yang telah diresize sesuai kebutuhan Anda
    total_anggaran = request.form['total_anggaran']
    realisasi = request.form['realisasi']
    lebih = request.form['lebih']
    con.execute("INSERT INTO dana (tahun, gambar , total_anggaran, realisasi, lebih) VALUES (%s,%s,%s,%s,%s)",(tahun,filename,total_anggaran, realisasi, lebih))
    mysql.connection.commit()
    return redirect(url_for("admindana"))

#geografi
@app.route('/admin/geografi')
def admingeo():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM tanah")
    tanah = con.fetchall()
    info_list = []
    for sistem in tanah:
        list_data = {
            'id': str(sistem[0]),
            'luas': str(sistem[1]),
            'sawahteri': str(sistem[2]),
            'sawahhu': str(sistem[3]),
            'pemukiman': str(sistem[4])
        }
        info_list.append(list_data)
        
    con.execute("SELECT * FROM wilayah")
    wilayah = con.fetchall()
    info_list2 = []
    for sistem2 in wilayah:
        list_data2 = {
            'id': str(sistem2[0]),
            'utara': str(sistem2[1]),
            'selatan': str(sistem2[2]),
            'timur': str(sistem2[3]),
            'barat': str(sistem2[4])
        }
        info_list2.append(list_data2)
        
    return render_template("admin/geografi.html", info_list=info_list, info_list2=info_list2)

@app.route('/admin/wilayah', methods=['POST'])
def adminwilayahedit():
        con = mysql.connection.cursor()
        utara = request.form['utara']
        selatan = request.form['selatan']
        timur= request.form['timur']
        barat = request.form['barat']
        print(str(utara))
        print(str(selatan))
        print(str(timur))
        print(str(barat))
        con.execute("UPDATE wilayah SET utara = %s, selatan = %s, timur = %s, barat = %s WHERE id = 1",(str(utara),str(selatan),str(timur),str(barat)))
        mysql.connection.commit()
        return redirect(url_for("admingeo"))
    
@app.route('/admin/tanah', methods=['POST'])
def admintanahedit():
        con = mysql.connection.cursor()
        luas = request.form['luas']
        sawahteri = request.form['sawahteri']
        sawahhu= request.form['sawahhu']
        pemukiman = request.form['pemukiman']
        print(str(luas))
        print(str(sawahteri))
        print(str(sawahhu))
        print(str(pemukiman))
        con.execute("UPDATE tanah SET luas = %s, sawahteri = %s, sawahhu = %s, pemukiman = %s WHERE id = 1",(str(luas),str(sawahteri),str(sawahhu),str(pemukiman)))
        mysql.connection.commit()
        return redirect(url_for("admingeo"))


#monografi
@app.route('/admin/monografi')
def adminmono():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM monografi")
    mono = con.fetchall()
    info_list = []
    for sistem in mono:
        list_data = {
            'id': str(sistem[0]),
            'tahun': str(sistem[1]),
            'jpenduduk': str(sistem[2]),
            'jkk': str(sistem[3]),
            'laki': str(sistem[4]),
            'perempuan': str(sistem[5]),
            'jkkprese': str(sistem[6]),
            'jkkseja': str(sistem[7]),
            'jkkkaya': str(sistem[8]),
            'jkksedang': str(sistem[9]),
            'jkkmiskin': str(sistem[10]),
            'islam': str(sistem[11]),
            'kristen': str(sistem[12]),
            'protestan': str(sistem[13]),
            'katolik': str(sistem[14]),
            'hindu': str(sistem[15]),
            'budha': str(sistem[16])
        }
        info_list.append(list_data)
    return render_template("admin/monografi.html", info_list = info_list)

@app.route('/admin/monoedit', methods=['POST'])
def adminmonoedit():
        con = mysql.connection.cursor()
        jpenduduk = request.form['jpenduduk']
        jkk = request.form['jkk']
        laki= request.form['laki']
        perempuan = request.form['perempuan']
        jkkprese = request.form['jkkprese']
        jkkseja = request.form['jkkseja']
        jkkkaya = request.form['jkkkaya']
        jkksedang = request.form['jkksedang']
        jkkmiskin = request.form['jkkmiskin']
        islam= request.form['islam']
        kristen= request.form['kristen']
        protestan= request.form['protestan']
        katolik= request.form['katolik']
        hindu= request.form['hindu']
        budha= request.form['budha']
        
        query = """
        UPDATE monografi 
        SET jpenduduk = %s, jkk = %s, laki = %s, perempuan = %s, 
            jkkprese = %s, jkkseja = %s, jkkkaya = %s, jkksedang = %s, 
            jkkmiskin = %s, islam = %s, kristen = %s, protestan = %s, 
            katolik = %s, hindu = %s, budha = %s 
        WHERE id = 1
    """
        con.execute(query, (
        jpenduduk, jkk, laki, perempuan, jkkprese, jkkseja, jkkkaya, jkksedang, 
        jkkmiskin, islam, kristen, protestan, katolik, hindu, budha
    ))
        mysql.connection.commit()
        return redirect(url_for("adminmono"))