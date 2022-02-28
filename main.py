from flask import Flask,
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

db_name = 'data.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "my-secret-key"



if __name__ == '__main__':
    app.run(debug=True, port=1233)
e