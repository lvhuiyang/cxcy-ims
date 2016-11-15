from datetime import datetime
from flask_script import Manager, Shell
from app import create_app, db
from app.models import User

app = create_app('default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def create_admin():
    try:
        admin = User(
            username='admin',
            real_name='admin',
            password_hash='admin_123456',
            power=3,
            created_date=datetime.today(),
            created_people='System'
        )
        db.session.add(admin)
        db.session.commit()
        print("添加系统管理员账号成功")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    manager.run()
