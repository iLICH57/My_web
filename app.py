from flask import Flask, render_template, request
from hashlib import sha256

# создание экземпляра сервера
app = Flask(__name__)

# проверка переменной __name__
# print(__name__)

def hashing(password, num_char):
    # кодирование
    byte_str = password.encode()
    # хешироапние
    hash_str = sha256(byte_str)
    # преобразование в hex-строка
    if num_char == '-':
        hex_str = hash_str.hexdigest()
    else: 
        hex_str = hash_str.hexdigest()[:int(num_char)] 
    # возврат строки
    return hex_str

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

        msg = hashing(pwd + salt, num_char)

    return render_template("product.html", message=msg) 

@app.route("/contact")
def contact_page():
    return "<h1>Contact</h1>"

# точка входа
if __name__ == "__main__":
    app.run(debug=True)