from flask import Flask, render_template, request, jsonify
from lexer import lexer
from syntax_analyzer import parser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form['code']
    
    # Análisis Léxico
    lexer.input(code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(f"{tok.type}({tok.value}) at line {tok.lineno}, position {tok.lexpos}")
    
    # Análisis Sintáctico
    try:
        parser.parse(code)
        syntax_result = "No syntax errors"
    except SyntaxError as e:
        syntax_result = str(e)
    
    return jsonify({
        'tokens': tokens,
        'syntax_result': syntax_result
    })

if __name__ == '__main__':
    app.run(debug=True)
