from app import app
from utils.database import db

if __name__ == '__main__':
    db.init_db()
    print(db.__hash__())
    app.run(host='0.0.0.0', port=80)
