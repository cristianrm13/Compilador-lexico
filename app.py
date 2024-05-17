from flask import Flask, request, render_template
from lexer import lexer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analizar', methods=['POST'])
def analizar():
    codigo = request.form['codigo']
    lexer.input(codigo)
    tokens = []
    pr_count = id_count = cad_count = num_count = lparen_count = rparen_count = simb_count = 0

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
        if tok.type in {'PROGRAMA', 'INT', 'READ', 'PRINTF', 'A', 'B', 'C', 'SUMA', 'RESTA', 'END'}:
            pr_count += 1
        if tok.type == 'ID':
            id_count += 1
        if tok.type == 'CADENA':
            cad_count += 1
        if tok.type == 'NUMBER':
            num_count += 1
        if tok.type == 'LPAREN':
            lparen_count += 1
        if tok.type == 'RPAREN':
            rparen_count += 1
        if tok.type in {'PLUS', 'SEMI'}:
            simb_count += 1

    pr = {'PROGRAMA', 'INT', 'READ', 'PRINTF', 'A', 'B', 'C', 'SUMA', 'RESTA', 'END'}
    symbols = {'PLUS', 'SEMI','EQUAL','LBRACE', 'RBRACE'}
    counts = {'pr_count': pr_count, 'id_count': id_count, 'cad_count': cad_count, 'num_count': num_count, 'lparen_count': lparen_count, 'rparen_count': rparen_count, 'simb_count': simb_count}
    
    return render_template('index.html', tokens=tokens, pr=pr, symbols=symbols, counts=counts)

if __name__ == '__main__':
    app.run(debug=True)
