from flask import Flask,render_template

app = Flask(__name__)

data = {
    "nama": "Nauval Risqullah",
    "umur": 16,
    "alamat": "Jl. Bunga No. 123, Banda Aceh",
    "pekerjaan": "Software Engineer",
    "hobi": "Berolahraga"
}

@app.route('/')
def index():
    return render_template('index.html',title="halaman index", isi="Selamat Datang di Website Flask")

@app.route('/about')
def about():
    return render_template('about.html',title="Halaman About", isi="ini adalah halaman about")

@app.route('/biodata')
def biodata():
    return render_template('biodata.html',title="Biodata", isi=data)

if __name__ == '__main__':
    app.run(debug=True)
