from flask import Flask, render_template
app=Flask (__name__)

@app.route('/')
def index():
    return render_template('INDEX.html',title= 'Exalty')

@app.route('/about')
def about():
    return "ini halaman about"

@app.route('/halo/<name>')
def halo(name):
    return "Haloo <strong> Nauvall </strong> !! Apa Kabar?? "

if __name__ == '__main__':
    app.run (debug=True)