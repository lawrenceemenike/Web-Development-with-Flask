from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()], render_kw={"size": 30})
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)], render_kw={"size": 30})

app = Flask(__name__)
app.secret_key = "some secret string"  # Required for CSRF protection
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    return render_template('login.html', form=form)

app.route("/success")
def sucess():
    return render_template('sucess.html')

@app.route("/denied")
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)