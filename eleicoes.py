from flask import Flask, render_template, request, Markup
from flask_mysqldb import MySQL
import jinja2
import time

app = Flask(__name__)

#configure db

app.config['MYSQL_HOST'] = 'form.criuxypwt58s.sa-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] =  'D4rk0102'
app.config['MYSQL_PORT'] =  3306
app.config['MYSQL_DB'] = 'eleicao2'

mysql = MySQL(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST" :
        dados = request.form
        matriculas = dados.get('matricula')
        nome_completo = dados.get('nomecompleto')
        emails = dados.get('email')
        nome_comissao = dados.get('nomecomissao')
        campus = dados.get('campus')
        unidade = dados.get('unidade')
        eleicao = dados.get('eleicao')
        colegio = dados.get('colegio')
        data_inicio = dados.get('data-inicio')
        data_fim = dados.get('data-fim')
        hora_inicio = dados.get('hora-inicio')
        hora_fim = dados.get('hora-fim')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO principal(eleicao, campus, unidade, matricula, nome_completo, email, nome_comissao, colegio, datainicio, datafim, horainicio, horafim ) values( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(eleicao, campus, unidade, matriculas,nome_completo,emails, nome_comissao, colegio, data_inicio, data_fim, hora_inicio, hora_fim))
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

