from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:blogsite@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
app.secret_key = '1234567'

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(256))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/blog', methods=['GET', 'POST'])
def index():
    if request.args:
        id=request.args.get("id")
        blog=Blog.query.get(id)

        return render_template('blog-entry.html',blog=blog)

    else:
        blogs=Blog.query.all()
        return render_template('blog.html', blogs=blogs)

def blog():
    if request.method == 'GET':
        return render_template('blog.html')

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        blog = Blog(title, body)
        db.session.add(blog)
        db.session.commit()
        new_url = "/blog?id=" + str(blog.id)
        return redirect(new_url)

    else:
        return render_template(title=title, body=body)

    
@app.route('/newpost',methods=["POST", "GET"])
def add_blog():
    if request.method=="GET":
        return render_template('newpost.html')

    if request.method=="POST":
        title = request.form['title']
        body = request.form['body']
        blog=Blog(blog_title,blog_body)
        db.session.add(blog)
        db.session.commit()
        new_url = "/blog?id=" + str(blog.id)

        return redirect(new_url)

    else:
         return render_template('newpost.html',title=title,body=body)


if __name__ == '__main__':
    app.run()