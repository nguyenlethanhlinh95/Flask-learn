#1. Install Flask-wtf
pip install flask-wtf
#2. Import validators form
<p>Trong file App:</p>
from flask import Flask, render_template <br>
from flask_wtf import FlaskForm <br>
from wtforms import StringField, PasswordField <br>
from wtforms.validators import InputRequired, Length, AnyOf <br>

app = Flask(__name__) <br>
app.config['SECRET_KEY'] = 'Mysecret!' <br>

class LoginForm(FlaskForm): <br>
    username = StringField('username', validators=[InputRequired('A username is required!'), Length(min=4, max=8,message='Must be between 4,8')])<br>
    password = PasswordField('password', validators=[InputRequired('A password is required!'), PasswordField])<br>
    
@app.route('/', methods=['GET', 'POST']) <br>
def hello_world(): <br>
    # gan cho form Class de validator <br>
    form = LoginForm() <br>
    if form.validate_on_submit(): <br>
        return '<h1>Username: {} Password: {}</h1>'.format(form.username.data, form.password.data) <br>

    return render_template('index.html', form=form)


if __name__ == '__main__': <br>
    app.run(debug=True) <br>

<p>Trong file View index template:</p>
<form action="/" method="POST"><br>
        {{ form.csrf_token }}<br>
        {{ form.username.label }}<br>
        {{ form.username }}<br>
        <u><br>
            {% for err in form.username.errors %}<br>
            <li style="color: red">{{ err }}</li><br>
            {% endfor %}<br>
        </u><br>
        {{ form.password.label }}<br>
        {{ form.password }}<br>
        <input type="submit" value="Submit"><br>
    </form><br>
    
    