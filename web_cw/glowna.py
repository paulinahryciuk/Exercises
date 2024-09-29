from flask import Flask, render_template,url_for, request
app = Flask(__name__)


@app.route('/')
def home():
    menu = f'''
        Go <a href="{url_for('notki')}">here</a> Notatki </br>'''
    return f'<h1 >Hello</h1></br>{menu}'

@app.route('/notatki', methods= ['GET','POST'])
def notki():
    print (request.method)
    if request.method == 'GET':
        body = f'''
                <form id="dodanie_notatki" action="{url_for('notki')}" method="POST">
                <label for="nowa">NOWA</label>
                <input type="text" 
                <input type="text" id="amount" name="amount" value="100"><br>
                <input type="submit" value="Send">
                </form>
                '''
        return body
    else:
        return url_for('lista')

@app.route('/lista')
def lista():
    return "LISTA NOTATEK"



if __name__=='__main__':
    app.run(debug=True)
