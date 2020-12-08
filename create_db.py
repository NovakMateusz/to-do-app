"""This script is responsible for creating and populating the database with sample user and admins"""
from sqlalchemy import exc
from token_manager.app.extensions import db
from token_manager.app.app_factory import create_app
from token_manager.blueprints.token.models import User, Role


if __name__ == '__main__':
    new_app = create_app()
    try:
        with new_app.app_context():
            # Create database with tables based on imported models
            db.create_all()

            # Populate database with sample roles
            admin_role = Role(name='Admin')
            db.session.add(admin_role)
            user_role = Role(name='User')
            db.session.add(user_role)

            # Populate database with sample Users
            new_user = User(username='SampleAdmin', email='admin@admin.com', role_id=1)
            new_user.set_password('Admin123')
            db.session.add(new_user)

            new_user = User(username='SampleAdminTest', email='admin_test@admin.com', role_id=1)
            new_user.set_password('Admin123')
            db.session.add(new_user)

            new_user = User(username='SampleUser', email='user@user.com', role_id=2)
            new_user.set_password('User123')
            db.session.add(new_user)

            db.session.commit()

    except exc.IntegrityError:
        print('Database already created')
