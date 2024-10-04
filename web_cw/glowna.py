from flask import Flask, render_template,url_for, request
app = Flask(__name__)


@app.route('/')
def home():
    menu = f'''
        Go <a href="{url_for('notki')}">here</a> Notatki </br>'''
    return f'<h1 >Hello</h1></br>{menu}'


lista = ["pranie", "sprzatanie"]
@app.route('/lista_zadan',methods= ['GET','POST'])
def lista_zadan():
    if request.method == 'POST':
        lista.append(request.form['task'])
    return render_template("lista_zadan.html",task=lista)


if __name__=='__main__':
    app.run(debug=True)
