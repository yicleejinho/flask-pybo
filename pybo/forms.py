from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class QuestionForm(FlaskForm):
    subject = StringField('제 목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내 용', validators=[DataRequired('내용은 필수입력 항목입니다.')])


class AnswerForm(FlaskForm):
    content = TextAreaField('내 용', validators=[DataRequired('내 용 은 필 수 입 력 항 목  입 니 다.')])


class UserCreateForm(FlaskForm):
    username = StringField('사 용 자 이 름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비 밀 번 호', validators=[DataRequired(), EqualTo('password2', '비 밀 번 호 가 일 치 하 지 않 습 니 다')])
    password2 = PasswordField('비 밀 번 호 확 인', validators=[DataRequired()])
    email = EmailField('이 메 일', validators=[DataRequired(), Email()])


class UserLoginForm(FlaskForm):
    username = StringField('사 용 자 이 름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비 밀 번 호', validators=[DataRequired()])
