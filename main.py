import os
from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_secreta_super_segura'

# --- TUS VERSOS Y LA FRASE FINAL ---
versos = [
    "Tengo días pensando en ti",
    "Y no logro entender por qué fuiste tan cruel",
    "No tenía motivos para sospechar",
    "Todos apuntaban, yo no quise mirar",
    "Era tanta ironía, realidad confundida",
    "No sé, mis ojos no podían ver.",
    "Te amo mi negro, perdón. <‘3"
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Para Ti</title>
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
            align-items: center;
            justify-content: center;
        }
        .verse {
            color: #c9184a;
            font-size: 16px;
            line-height: 1.5;
            margin: 0;
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
        }
        .btn:hover {
            background-color: #ff758f;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="ribbon">🎀</div>
        <div class="title">✨ Mis Ojos No Podían Ver - Charles Ans ✨</div>
        <div class="verse-container">
            <p class="verse">{{ verso }}</p>
        </div>
        <form action="{{ url_for('siguiente') }}" method="POST">
            <button type="submit" class="btn">Siguiente ✨</button>
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
    return render_template_string(HTML_TEMPLATE, verso=verso_actual)

@app.route('/siguiente', methods=['POST'])
def siguiente():
    if 'current_index' in session:
        session['current_index'] = (session['current_index'] + 1) % len(versos)
    else:
        session['current_index'] = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
