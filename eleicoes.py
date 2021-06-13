from flask import Flask, render_template, request, jsonify
import jinja2
import time
from flask_mysqldb import MySQL



app = Flask(__name__)

#configure db

app.config['MYSQL_HOST'] = 'form.criuxypwt58s.sa-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] =  'D4rk0102'
app.config['MYSQL_PORT'] =  3306
app.config['MYSQL_DB'] = 'eleicao2'

mysql = MySQL(app)

alert = '''function Aviso() {
                    alert("Eleição agendada!")
                }'''


@app.route('/getUnidadesByCampus', methods= ['POST'])
def inicio():
    dados = request.form
    campus = dados['select1_value'] 
    cur = mysql.connection.cursor()
    
    #result = cur.execute('select  unidades.nome_unidades from campus inner join unidades on campus.id_campus = unidades.id_fk where nome_campus = "{}"'.format(campus))
    result = cur.execute('select nome_unidade from tudo where nome_campus = "{}"'.format(campus))
    if result > 0: 
        unidade_nome = cur.fetchall()
        print(unidade_nome)
        return jsonify('',  render_template('update.html', unidade_nome=unidade_nome))
       
         
   

@app.route('/', methods=['POST'])
def post():
    
    dados = request.form
    campus = dados.get('campus')    
    matriculas = dados.get('matricula')
    nome_completo = dados.get('nomecompleto')
    emails = dados.get('email')
    nome_comissao = dados.get('nomecomissao')   
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
    return render_template("index.html", alert=alert )

    

    

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

