from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class EditProfileForm(FlaskForm):
    name = StringField('姓名', validators=[Length(0, 64)])
    location = StringField('所在地', validators=[Length(0, 64)])
    about_me = TextAreaField('自我介绍')
    submit = SubmitField('提交')
