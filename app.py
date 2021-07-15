from flask import Flask, render_template

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

@app.route("/product")
def product_page():
    # возврат страницы
    return render_template("product.html") 


# точка входа
if __name__ == "__main__":
    app.run(debug=True)