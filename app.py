from xmlrpc.client import Boolean

from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, AnyOf, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Mysecret!'
app.config['WTF_CSRF_ENABLED'] = True
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcJxdgUAAAAAJUv0cqHutzKMAJRyJZOBCi3sqPW'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcJxdgUAAAAANDmf2EfDcG9VdlaUdhbuCTduXtz'

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('A username is required!'),
                                                   Length(min=4, max=8, message='Must be between 4,8')])
    password = PasswordField('password', validators=[InputRequired('A password is required!')])
    age = IntegerField('age', default=25)
    true = BooleanField('Click here')
    email = StringField('email', validators=[Email()])
    recaptcha = RecaptchaField()

class User:
    def __init__(self, username, password, age, email):
        self.username = username
        self.password = password
        self.age = age
        self.email = email


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # gan cho form Class de validator
    myUser = User('Linh', 123, 25, 'nguyenlethanhlinh95@gmail.com')
    form = LoginForm(obj=myUser)
    if form.validate_on_submit():
        return '<h1>Username: {} Password: {} Age: {} True: {} Email: {}</h1>'.format(form.username.data,
                                                                                      form.password.data,
                                                                                      form.age.data, form.true.data,
                                                                                      form.email.data)

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
