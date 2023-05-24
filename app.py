from flask import Flask, jsonify, request, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql10.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql10620819'
app.config['MYSQL_PASSWORD'] = 'W4R29qXrxQ'
app.config['MYSQL_DB'] = 'sql10620819'
app.config['JWT_SECRET_KEY'] = 'ZdLqYSHX-YoxmsV1sGl7ZAqOP83JxbpfkVU4AhCr4gI'

mysql = MySQL(app)
jwt = JWTManager(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Rota para a página inicial
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Rota para autenticação
@app.route('/login', methods=['POST'])
def login():
    usuario = request.json.get('usuario')
    senha = request.json.get('senha')

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_cad_usuario WHERE usuario = %s', (usuario,))
    usuario_data = cursor.fetchone()
    cursor.close()

    if usuario_data and senha == usuario_data[3]:
        access_token = create_access_token(identity=usuario_data[0], expires_delta=False)
        return jsonify({'codigoUsuario': usuario_data[0], 'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Usuário ou senha inválidos'}), 401


# Rota protegida, que requer autenticação
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({'message': 'Rota protegida!'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
