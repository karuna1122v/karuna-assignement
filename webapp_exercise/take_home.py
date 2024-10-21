from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import os
db_user = os.environ['POSTGRES_USER']
db_name = os.environ['POSTGRES_DB']
db_host = os.environ['POSTGRES_HOST']
db_port = os.environ['POSTGRES_PORT']
db_pwd_file_path = os.environ['POSTGRES_PASSWORD_FILE']
db_pwd = open(db_pwd_file_path,'r').read().strip()
db_url = "postgresql://"+db_user+":"+db_pwd+"@"+db_host+":"+db_port+"/"+db_name

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)

class Moment(db.Model):
    __tablename__ = 'moments'
    mid = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f'<Moment {self.name} parent_id:{self.parent_id}>'

Moment.parent_id = db.Column(db.Integer, db.ForeignKey(Moment.mid))
Moment.parent = relationship(Moment, backref='children', remote_side=Moment.mid)

@app.route('/')
def index():
    mid = request.args.get('id', default=1)
    return str(db.session.get(Moment, mid))

@app.route('/moments/<int:mid>/descendants')
def descendants(mid):
    parent = db.session.get(Moment, mid)
    # TODO: Uh-oh, I don't know how to implement this
    return parent.name

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
