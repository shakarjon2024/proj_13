from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(f"Bu yerda request.form: {request.form} GA TENG!")
        n = request.form.get("ismjon")
        a = request.form.get("yoshjon")
        if n == 'azamat' and a == '12345':
            return f"Muvaffaqiyatli kirdingiz"
        return f"Parol yoki login xato"
    return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)
