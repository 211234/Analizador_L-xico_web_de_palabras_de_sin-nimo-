# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Diccionario de palabras con sus sinónimos
synonyms = {
    "alegre": ("feliz", "contento"),
    "anciano": ("viejo", "mayor"),
    "rápido": ("veloz", "ágil"),
    "bonito": ("hermoso", "bello"),
    "difícil": ("complicado", "arduo"),
    "enorme": ("grande", "gigantesco"),
    "delicioso": ("rico", "sabroso"),
    "inteligente": ("listo", "brillante"),
    "triste": ("deprimido", "melancólico"),
    "caliente": ("tibio", "templado"),
    "lleno": ("completo", "repleto"),
    "fácil": ("sencillo", "simple"),
    "oscuro": ("tenebroso", "sombrío"),
    "claro": ("luminoso", "brillante"),
    "fuerte": ("robusto", "sólido"),
    "débil": ("frágil", "endeble"),
    "barato": ("económico", "asequible"),
    "caro": ("costoso", "oneroso"),
    "hermoso": ("bonito", "bello"),
    "lento": ("pausado", "despacio"),
    "alto": ("elevado", "alto"),
    "bajo": ("pequeño", "reducido"),
    "gordo": ("grueso", "corpulento"),
    "delgado": ("flaco", "esbelto"),
    "sano": ("saludable", "robusto"),
    "enfermo": ("malo", "doliente"),
    "importante": ("significativo", "relevante"),
    "insignificante": ("trivial", "nimio"),
    "agradable": ("placentero", "ameno"),
    "horrible": ("terrible", "espantoso"),
    "amable": ("cortés", "atento"),
    "grosero": ("rudo", "descortés"),
    "humilde": ("modesto", "sencillo"),
    "orgulloso": ("altivo", "arrogante"),
    "famoso": ("célebre", "conocido"),
    "desconocido": ("anónimo", "ignorado"),
    "viejo": ("antiguo", "vetusto"),
    "joven": ("nuevo", "moderno"),
    "aburrido": ("tedioso", "monótono"),
    "interesante": ("atractivo", "fascinante"),
    "valiente": ("intrépido", "audaz"),
    "cobarde": ("miedoso", "temeroso"),
    "rico": ("adinerado", "opulento"),
    "pobre": ("necesitado", "indigente"),
    "lógico": ("razonable", "sensato"),
    "ilógico": ("absurdo", "disparatado"),
    "justo": ("equitativo", "imparcial"),
    "injusto": ("desigual", "arbitrario"),
    "corto": ("breve", "escueto"),
    "pequeño": ("diminuto", "minúsculo"),
    "grande": ("enorme", "colosal"),
    "frio": ("helado", "glacial"),
    "calor": ("ardiente", "abrasador"),
    "pesado": ("lento", "gravoso"),
    "ligero": ("liviano", "leve"),
    "ruidoso": ("estridente", "bullicioso"),
    "silencioso": ("callado", "tranquilo"),
    "firme": ("seguro", "estable"),
    "blando": ("suave", "tierno"),
    "nuevo": ("reciente", "novedoso"),
    "brillante": ("resplandeciente", "luminoso"),
    "mate": ("opaco", "apagado"),
    "incompleto": ("parcial", "fragmentado"),
    "confuso": ("difuso", "ambiguo"),
    "educado": ("cortés", "civilizado"),
    "maleducado": ("grosero", "incivil"),
    "eficaz": ("eficiente", "efectivo"),
    "inútil": ("ineficaz", "ineficiente"),
    "húmedo": ("mojado", "empapado"),
    "seco": ("árido", "desecado"),
    "limpio": ("aseado", "pulcro"),
    "sucio": ("mugriento", "manchado"),
    "estrecho": ("angosto", "reducido"),
    "ancho": ("amplio", "vasto"),
    "duro": ("firme", "sólido"),
    "pesimista": ("desesperanzado", "negativo"),
    "optimista": ("esperanzado", "positivo"),
    "amigable": ("cordial", "simpático"),
    "hostil": ("agresivo", "antagónico"),
    "flexible": ("maleable", "adaptable"),
    "rígido": ("inflexible", "duro"),
    "abundante": ("profuso", "copioso"),
    "escaso": ("limitado", "exiguo"),
    "divertido": ("entretenido", "ameno"),
    "cauteloso": ("precavido", "prudente"),
    "imprudente": ("temerario", "descuidado"),
    "insípido": ("soso", "desabrido")
}

# Operadores y tokens
operators = {
    '+': 'operador suma',
    '-': 'operador resta',
    '*': 'operador multiplicación',
    '/': 'operador división',
    '(': 'paréntesis apertura',
    ')': 'paréntesis cierre',
    ',': 'coma',
    '.': 'punto'
}

def analyze_text(text):
    lines = text.split('\n')
    results = []

    for line_num, line in enumerate(lines, 1):
        tokens = re.findall(r'\w+|\S', line)
        for token in tokens:
            original_token = token.lower()
            if original_token in synonyms:
                syn1, syn2 = synonyms[original_token]
                results.append([token, syn1, syn2, '', '', line_num])
            elif token.isdigit():
                results.append([token, '', '', 'X', '', line_num])
            elif token in operators:
                results.append([token, '', '', '', 'X', line_num])
            else:
                results.append([token, '', '', '', '', line_num])
    
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        results = analyze_text(user_input)
        return render_template('index.html', results=results)
    return render_template('index.html', results=[])

if __name__ == "__main__":
    app.run(debug=True)
