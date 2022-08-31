from Application import db

class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key = True)
    role_name = db.Column(db.String)



