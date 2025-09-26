from flask import Flask, render_template
app=Flask (__name__)

@app.route('/index')
def index():
    return render_template('INDEX.html',title= 'INDEX', judul="Ini Halaman Index")

@app.route('/biodata')
def biodata():
    return render_template('BIODATA.html',title= 'BIODATA', judul="Ini Halaman Biodata")

@app.route('/about')
def about():
    return render_template('ABOUT.html',title= 'ABOUT', judul="Ini Halaman ABOUT")

@app.route('/halo/<name>')
def halo(name):
    return "Haloo <strong> Nauvall </strong> !! Apa Kabar?? "

if __name__ == '__main__':
    app.run (debug=True)