# SQLALCHEMY_DATABASE_URI = 'mysql://root:@mysql:3306/wanted?charset=utf8'  # For Docker
SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1:3306/wanted?charset=utf8'  # For pyTest
SQLALCHEMY_TRACK_MODIFICATIONS = False