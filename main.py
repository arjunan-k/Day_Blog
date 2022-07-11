from flask import Flask, render_template, request
from post import Post
import smtplib
my_email = "your email"
password = "email password"

app = Flask(__name__)
p = Post()


@app.route('/')
def home():
    data = p.blog()
    return render_template("index.html", posts=data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact.html', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        data = request.form
        quote = f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="to email",
                                msg=f"Subject:New Message\n\n{quote}")
        return render_template("contact.html", message_send=True)
    else:
        return render_template("contact.html")


@app.route('/post.html/<int:num>')
def post(num):
    data_new = p.blog()
    return render_template("post.html", id=num, posts=data_new)


# @app.route('/form-entry',  methods=["POST"])
# def receive_data():
#     print(request.form["name"])
#     print(request.form["email"])
#     print(request.form["phone"])
#     print(request.form["message"])
#     return "<h1>Successfully sent your message.</h1>"


# if __name__ == "__main__":
#     app.run(debug=True)