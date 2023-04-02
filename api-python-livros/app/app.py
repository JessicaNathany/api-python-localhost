# importando biblioteca do Flask
from flask import Flask, jsonify, request

#  criando uma aplicação Flask com o nome atual
app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Programador Programático',
        'autor': ' Andrew Hunt '
    },
    {
        'id': 2,
        'título': '14 Hábitos de Desenvolvedores Altamente Produtivos',
        'autor': ' Zeno Rocha'
    },
    {
        'id': 3,
        'título': 'Refatoração: Aperfeiçoando o Design de Códigos Existentes',
        'autor': ' Martin Fowler'
    }
]

#consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# obter por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_por_id(id):
    
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
        
# editar um recurso
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
        
# adicionar um livro
@app.route('/livros', methods=['POST'])       
def adicionar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


# excluir um livro 
@app.route('livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
        return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)