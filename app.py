from flask import Flask, render_template, request

# создание экземпляра сервера
app = Flask(__name__)

# проверка переменной __name__
# print(__name__)

# основная логика нашего сервера
@app.route("/")
def index_page():
    #  return "Hello, comp! I am flask server!"
    # возврат страницы
    return render_template("index.html") 

@app.route("/product", methods=["GET", "POST"])
def product_page():
    # возврат страницы
    msg = ""
    if request.method == "POST":
        pwd = request.form.get("pwd")
        salt = request.form.get("salt")
        num_char = request.form.get("num")

        msg = pwd + salt + num_char

    return render_template("product.html", message=msg) 


# точка входа
if __name__ == "__main__":
    app.run(debug=True)