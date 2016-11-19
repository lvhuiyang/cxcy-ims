from datetime import datetime
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User, Project
from app.constant import COMPETITION_PROJECTS

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def create_admin():
    """
    部署项目时添加的系统权限管理员
    :return:
    """
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


@manager.command
def project_init():
    """
    部署项目时添加的100+个比赛项目
    :return:
    """
    try:
        length = len(COMPETITION_PROJECTS)
        for i, pro in enumerate(COMPETITION_PROJECTS):
            this_project = Project(
                name=pro,
                created_date=datetime.today(),
                created_people='System'
            )
            db.session.add(this_project)
            print('正在添加 --> %r 进度： %d/%d' % (this_project.name, i + 1, length))
        db.session.commit()
        print('数据添加完成')
    except Exception as e:
        db.session.rollback()
        print(e)


if __name__ == '__main__':
    manager.run()
