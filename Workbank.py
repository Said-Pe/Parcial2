from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Cargar los datos del archivo CSV
datos = pd.read_csv(r'C:\Users\saidc\OneDrive\Documentos\DS analisis\Vasarampion.csv')

# Ruta para la página principal
@app.route('/')
def index():
    # Pasar los datos al template HTML
    return render_template('Pag.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
