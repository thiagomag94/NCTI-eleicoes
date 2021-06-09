from flask import Flask, render_template, request, Markup
from flask_mysqldb import MySQL
import jinja2

app = Flask(__name__)

#configure db

app.config['MYSQL_HOST'] = 'form.criuxypwt58s.sa-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] =  'D4rk0102'
app.config['MYSQL_PORT'] =  3306
app.config['MYSQL_DB'] = 'ncti_flask_el'

mysql = MySQL(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST" :
        dados = request.form
        emails = dados.get('email')
        fruts = dados.get('frutas')
        calds = dados.get('caldas')
        outro = dados.get('outro')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO inicial(email, fruta, calda, outro) values(%s,%s,%s,%s)",(emails,fruts,calds,outro))
        mysql.connection.commit()
        cur.close()
        alert = "../static/alert.js"
        return render_template('index.html', alert=alert)
    else :
        return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

