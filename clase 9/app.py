from flask import Flask, render_template, render_template_string
import random
import string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/secret")
def secret():
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    password = "".join(random.choice(caracteres) for _ in range(10))

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Página Secreta</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    </head>
    <body>

        <header class="hero">
            <h1>🔐 Página Secreta</h1>
            <p>Generador de contraseñas</p>
        </header>

        <section class="cards">
            <div class="card">
                <h2>Tu contraseña:</h2>
                <p>{{ password }}</p>
            </div>
        </section>

        <footer>
            <a href="/">Volver al inicio</a>
        </footer>

    </body>
    </html>
    """, password=password)

if __name__ == "__main__":
    app.run(debug=True)