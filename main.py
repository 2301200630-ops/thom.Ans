import os
from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_secreta_super_segura'

# --- TUS VERSOS Y LA FRASE FINAL ---
versos = [
    "Esto podría ser lo más p#to que escribo",
    "regresa conmigo y no te arrepentirás.",
    "Sé que todo ha estado un poco torcido",
    "tan solo te pido otra oportunidad.",
    "No seas tonto, claro que no te olvido",
    "de tan adolorido voy a darme un tiro.",
    "Que haberte conocido lo ha sido todo"
    "no me mires así, bombón",
    "con esos ojitos de miope que se me rompe el corazón.",
    "Te amo mi negro, perdón. <‘3"
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi amor 💕</title>
    <style>
        body {
            background-color: #fce4ec;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        /* Diseño de la tarjeta exterior de la foto */
        .card {
            background-color: #fff5f7;
            border: 2px solid #ffb3c6;
            border-radius: 20px;
            padding: 40px 20px;
            width: 85%;
            max-width: 500px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(255, 179, 198, 0.3);
        }
        .ribbon {
            font-size: 35px;
            margin-bottom: 10px;
            color: #ff4d6d;
        }
        .title {
            color: #ff4d6d;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 25px;
        }
        /* Cuadro de diálogo interno con línea punteada */
        .verse-container {
            border: 1px dashed #ffb3c6;
            border-radius: 12px;
            padding: 30px 15px;
            margin-bottom: 25px;
            background-color: #fffdfd;
            min-height: 60px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .verse {
            color: #c9184a;
            font-size: 16px;
            line-height: 1.5;
            margin: 0;
        }
        .gif-container {
            margin-top: 15px;
        }
        .gif-container img {
            max-width: 150px;
            height: auto;
        }
        /* Botón ovalado estilo la imagen de referencia */
        .btn {
            background-color: #ff4d6d;
            color: white;
            border: none;
            border-radius: 25px;
            padding: 12px 35px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(255, 77, 109, 0.2);
            transition: background 0.2s;
            margin: 10px auto;
            display: block;
        }
        .btn:hover {
            background-color: #ff758f;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="ribbon">🎀</div>
        <div class="title">✨ Tú - Tino el PingÜino ✨</div>
        <div class="verse-container">
            <p class="verse">{{ verso }}</p>
            {% if es_ultimo %}
            <div class="gif-container">
                <img src="https://media.tenor.com/7S8fbeXo_68AAAAi/hello-kitty-crying.gif" alt="Hello Kitty Crying">
            </div>
            {% endif %}
        </div>
        
        <!-- BOTÓN SIGUIENTE -->
        <form action="{{ url_for('siguiente') }}" method="POST">
            <button type="submit" class="btn">Siguiente ✨</button>
        </form>

        <!-- BOTÓN CERRAR AGREGADO PERFECTAMENTE -->
        <form action="{{ url_for('cerrar') }}" method="POST">
            <button type="submit" class="btn" onclick="window.close();">cerrar 💞</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    if 'current_index' not in session:
        session['current_index'] = 0
    
    if session['current_index'] >= len(versos):
        session['current_index'] = 0
        
    verso_actual = versos[session['current_index']]
    es_ultimo = (session['current_index'] == len(versos) - 1)
    
    return render_template_string(HTML_TEMPLATE, verso=verso_actual, es_ultimo=es_ultimo)

@app.route('/siguiente', methods=['POST'])
def siguiente():
    if 'current_index' in session:
        session['current_index'] = (session['current_index'] + 1) % len(versos)
    else:
        session['current_index'] = 0
    return redirect(url_for('index'))

@app.route('/cerrar', methods=['POST'])
def cerrar():
    session.clear()
    return """
    <script>
        window.close();
        document.write('<h2 style="color: #ff4d6d; text-align: center; font-family: sans-serif; margin-top: 50px;">¡Gracias por leer! Ya puedes cerrar esta pestañita. 💕</h2>');
    </script>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
