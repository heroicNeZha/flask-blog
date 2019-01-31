from ..models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class LoginFrom(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email()])

    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    name = StringField('用户名', validators=[DataRequired(), Length(4, 64),
                                          Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '应由字母数字下划线或点构成')])
    password = PasswordField('密码', validators=[DataRequired(),
                                               EqualTo('password2', message='你这两次输入也不一样啊')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('注册')

    #如果表单中出现以validate_开头后面跟着字段名的方法
    #这个方法就和常规验证函数一起调用
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经注册')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('用户名已存在')
