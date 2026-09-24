#Import de biblioteca
from flask import Flask, render_template, request, redirect, url_for

#Criar objeto flask "apelido - app"
app = Flask(__name__)
#base fake 1
lista = []
#base fake 2
lista_pessoas = []

#-------------------------------------
#Rotas
@app.route('/')
def index():
    return render_template('index.html', dados_lista=lista)

@app.route('/atividades/criar', methods=['GET', 'POST'])
def criar_atividade():
    if request.method == 'POST':
        #aqui recebe dados do formulario
        nome_atividade = request.form.get('form_nome_atividade')
        data_atividade = request.form.get('form_data_atividade')
        recurso_atividade = request.form.getlist('form_recurso')
        recurso_atividade = ", ".join(recurso_atividade)
        categoria_atividade = request.form.get('form_categoria')
        descricao_atividade = request.form.get('form_descricao')

        dados = {
            'nome_atividade': nome_atividade,
            'data_atividade': data_atividade,
            'recurso_atividade': recurso_atividade,
            'categoria_atividade': categoria_atividade,
            'descricao_atividade': descricao_atividade

        }

        print(f'dados: {dados}')

        lista.append(dados)
        print(lista)

        return render_template('listar_atividades.html', dados_lista=lista)
    return render_template('criar_atividade.html')



@app.route('/atividades/listar')
def listar_atividades():


    return render_template('listar_atividades.html', dados_lista=lista)



@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html', dados_pessoas=lista_pessoas)


@app.route('/pessoa/criar', methods=['GET', 'POST'])
def criar_pessoa():
    if request.method == 'POST':
        nome_pessoa = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')  # geralmente não é getlist para senha única
        data_nascimento = request.form.get('data_nascimento')

        dados_pessoa = {
            'nome': nome_pessoa,
            'email': email,
            'senha': senha,
            'data_nascimento': data_nascimento
        }

        lista_pessoas.append(dados_pessoa)
        return redirect(url_for('pessoa', dados_pessoas=lista_pessoas))  # ou render_template adequado
    return render_template('criar_pessoa.html')


#Excluir teste
@app.route('/atividades/excluir/<int:indice>')
def excluir_atividade(indice):
    try:
        lista.pop(indice)
    except IndexError:
        print('ERRO ao excluir atividade')
    return redirect(url_for('listar_atividades'))

#Excluir
@app.route('/pessoa/excluir/<int:indice>')
def excluir_pessoa(indice):
    if 0 <= indice < len(lista_pessoas):
        lista_pessoas.pop(indice)
    return redirect(url_for('pessoa'))

# Iniciar aplicação web
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)


#Nada deve ser colocado abaixo