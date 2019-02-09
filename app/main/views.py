from flask import render_template, session, redirect, url_for, current_app, abort
from . import main
from ..decorators import admin_required, permission_required
from flask_login import login_required
from ..models import Permission, User


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)


@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "管理员"


@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return "仲裁者"
