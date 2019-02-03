from unittest import TestCase
from app import create_app
from app.models import db,Role


class RoleModelTest(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_insert_roles(self):
        Role.insert_roles()
        self.assertIsNotNone(Role.query.first())
