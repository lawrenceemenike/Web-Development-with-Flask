from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

# Create the database and the books table
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template('index.html', all_books=all_books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=float(request.form['rating'])
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit_rating(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        book.rating = float(request.form['rating'])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", book=book)
if __name__ == "__main__":
    app.run(debug=True)