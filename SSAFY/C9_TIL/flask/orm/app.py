from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask 
app = Flask(__name__)

# sqlalchemy 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlalchemy 초기화 (Flask와 sqlalchemy 연동)
db = SQLAlchemy(app)

# migrate 초기화 (Flask와 sqlalchemy와 같이 연동)
migrate = Migrate(app,db)

# table 만들기
# unique = 중복되지 않게/ nullable = 빈값허용 X
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    memo = db.Column(db.Text)
    
    def __repr__(self):
        return f'<User {self.id}: {self.username}, {self.email}>'
    
    
    
    
    
    
    
# flask db init
# flask db migrate
# flask db upgrade

# 정리
# Create
# INSERT INTO users (username, email) VALUES ('ryanlee5646', 'ryanlee5646@gmail.com' )
# user = User(usename='ryanlee5646', email='ryanlee5646@gmail.com')
# db.session.add(user)
# db.session.commit() # commit을 해줘야지 Datebase에 기록이됨.

# [Read]
# SELECT * FROM users;/ (sqlite)
# users = User.query.all() # 복수 /(파이썬)

# SELECT * FROM users WHERE username='nwith'; /(sqlite)
# users = User.query.filter_by(username='nwith').all()/(파이썬)

# SELECT * FROM users WHERE username='nwith' LIMIT 1; /(sqlite)
# users = User.query.filter_by(username='nwith').first() /(파이썬)

# SELECT * FROM users WHERE id=2 LIMIT 1; / (sqlite)
# user = User.query.get(2)
# primary key만 get으로 가져올 수 있음. / (파이썬)

# SELECT * FROM users WHERE email LIKE '%ryanlee5646%'; / (sqlite)
# users = User.query.filter(User.email.like(%ryanlee5646%')).all()

# ORDER
# users = User.query.order_by(User.username).all()

# LIMIT
# users = User.query.limit(1).all()

# OFFSET
# users = User.query.offset(2).all()

# ORDER + LIMIT + OFFSET
# users = User.query.order_by(User.username).limit(1).offset(2).all()

# [DELETE]
# DELETE FROM users WHERE id=1;
# user = User.query.get(1)
# db.session.delete(user)
# db.session.commit()

# [UPDATE]
# UPDATE users SET username='Gyujin' WHERE id-2;
# user = User.query.get(2)
# user.username = 'Gyujin'
# db.session.commit()

