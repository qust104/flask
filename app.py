from flask import Flask, render_template, request, url_for, redirect, flash
from flask import session
from werkzeug.utils import secure_filename
from forms import TravelerForm, UploadForm
import os
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = 'static/img'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Создаем папки, если они не существуют
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('static/css', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/image')
def image():
    return render_template('image.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = TravelerForm()
    if form.validate_on_submit():
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html', form=form)

@app.route('/choice/<name>')
def choice(name):
    return render_template('choice.html', name=name)

@app.route('/archive/<name>/<int:number1>/<float:number2>')
def archive(name, number1, number2):
    total = number1 * number2
    return render_template('archive.html', 
                         name=name, 
                         number1=number1, 
                         number2=number2,
                         total=total)

@app.route('/delete_photo/<filename>', methods=['POST'])
def delete_photo(filename):
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            flash('Фото удалено!', 'success')
    except Exception as e:
        flash('Ошибка при удалении фото', 'danger')
    return redirect(url_for('upload'))

@app.route('/upload', methods=['GET'])
def upload():
    form = UploadForm()
    return render_template('upload.html', form=form)

# Добавьте этот код в ваш файл app.py
# Добавьте этот код в ваш файл app.py
@app.route('/gallery')
def gallery():
    gallery_photos = [
        {
            'filename': 'travel9.jpg',
            'title': 'Горный пейзаж',
            'desc': 'Красивый вид на горы'
        },
        {
            'filename': 'travel8.jpg',
            'title': 'Морской берег',
            'desc': 'Пляж с белым песком'
        },
        {
            'filename': 'travel7.jpg',
            'title': 'Городская панорама',
            'desc': 'Ночной город'
        }
    ]
    return render_template('gallery.html', photos=gallery_photos)


def get_uploaded_photos():
    return [f for f in os.listdir(app.config['UPLOAD_FOLDER']) 
            if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], f))]

if __name__ == '__main__':
    app.run(debug=True)




