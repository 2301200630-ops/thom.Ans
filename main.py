import os
import json
from flask import Flask

app = Flask(__name__)

# --- TU MÚSICA PRINCIPAL ---
versos = [
    "Tengo días pensando en ti",
    "Y no logro entender por qué fuiste tan cruel",
    "No tenía motivos para sospechar",
    "Todos apuntaban, yo no quise mirar",
    "Era tanta ironía, realidad confundida",
    "No sé, mis ojos no podían ver."
]

versos_json = json.dumps(versos)

# --- DISEÑO FINAL HELLO KITTY X CHARLES ANS ---
html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Kitty x Charles Ans 🎀</title>
    <style>
        body {
            background-color: #FFD1DC; /* Fondo rosa pastel */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        
        /* Cuadro de diálogo estilo Hello Kitty */
        .kitty-box {
            background-color: white;
            width: 90%;
            max-width: 400px;
            padding: 25px;
            border-radius: 25px;
            border: 3px solid #FF69B4; /* Borde rosa fuerte */
            box-shadow: 0 10px 25px rgba(255, 105, 180, 0.3);
            text-align: center;
            transition: all 0.3s ease;
        }

        /* Cuadro final más grande */
        .kitty-box.final {
            max-width: 460px;
            padding: 35px 25px;
        }

        .verso-texto {
            color: #FF69B4;
            font-size: 20px;
            font-weight: bold;
            margin: 20px 0;
            line-height: 1.5;
        }

        .mensaje-final {
            color: #D11A5B;
            font-size: 22px;
            font-weight: bold;
            margin-top: 15px;
        }

        /* Botón tierno para avanzar */
        .kitty-btn {
            background-color: #FF69B4;
            color: white;
            border: none;
            padding: 10px 25px;
            font-family: 'Comic Sans MS', cursive, sans-serif;
            font-size: 16px;
            font-weight: bold;
            border-radius: 15px;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(255, 105, 180, 0.4);
            transition: transform 0.1s ease;
        }

        .kitty-btn:active {
            transform: scale(0.95);
        }

        .gif-container {
            margin-bottom: 15px;
        }

        .gif-container img {
            max-width: 160px;
            height: auto;
        }
    </style>
</head>
<body>

    <div class="kitty-box" id="box">
        <div id="contenido">
            <div class="verso-texto" id="texto-verso">"Tengo días pensando en ti"</div>
            <button class="kitty-btn" onclick="siguienteVerso()" id="btn-accion">Siguiente ✨</button>
        </div>
    </div>

    <script>
        var listaVersos = """ + versos_json + """;
        var posicion = 0;

        function siguienteVerso() {
            posicion++;
            var texto = document.getElementById("texto-verso");
            var contenedor = document.getElementById("box");
            var contenidoInterno = document.getElementById("contenido");

            if (posicion < listaVersos.length) {
                // Cambia al siguiente verso con suavidad
                texto.innerHTML = '"' + listaVersos[posicion] + '"';
            } else {
                // TRANSICIÓN AL CUADRO FINAL MÁS GRANDE
                contenedor.classList.add("final");
                
                contenidoInterno.innerHTML = `
                    <div class="gif-container">
                        <img src="https://media.tenor.com/79_zV3bU6p8AAAAi/hello-kitty-shy.gif" alt="Hello Kitty Shy">
                    </div>
                    <div class="mensaje-final">
                        Te amo mi negro, perdón por todo. <'3
                    </div>
                `;
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return html_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
