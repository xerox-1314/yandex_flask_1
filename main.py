from flask import Flask, render_template, request, redirect
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fewp38945j954utregret46hg6u'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


if __name__ == '__main__':
    app.run(debug=True)