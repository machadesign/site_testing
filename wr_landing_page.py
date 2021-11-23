from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask import Flask, render_template, request
from DB_Insertdata import add_data
import datetime

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="Secret_key",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


# Wtf verification class
class NameForm(FlaskForm):
    entered_name = StringField("name", validators=[DataRequired()])
    entered_email = StringField("email", validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")


@app.after_request
def add_header(response):
    # check if cache control is setup header ,if not do not store cache for static files
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response


@app.errorhandler(404)
def page_not_found(error):
    return '''
    <h1> 404 </h1>
    <p> This page does not exist </p>
    <a href="http://127.0.0.1:5000/">Return to the dashboard</a> '''


@app.route('/', methods=('GET', 'POST'))
def form_entry():
    entered_name = None
    entered_email = None
    form = NameForm()
    if form.validate_on_submit():
        todays_date = datetime.datetime.now()
        entered_name = form.entered_name.data
        entered_email = form.entered_email.data
        add_data(entered_name, entered_email, todays_date)
        form.entered_name.data = ' '
        form.entered_email.data = ' '
    return render_template("wr.html", entered_name=entered_name, entered_email=entered_email, form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8888)
