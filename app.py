from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Mysecret!'


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('A username is required!'), Length(min=4, max=8,message='Must be between 4,8')])
    password = PasswordField('password', validators=[InputRequired('A password is required!'), PasswordField])


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # gan cho form Class de validator
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>Username: {} Password: {}</h1>'.format(form.username.data, form.password.data)

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
