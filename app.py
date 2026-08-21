#Import de biblioteca
from flask import Flask, render_template, request

#Criar objeto flask "apelido - app"
app = Flask(__name__)
lista = []

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

        return render_template('criar_atividade.html', dados_lista=lista)
    return render_template('criar_atividade.html')



@app.route('/atividades/listar')
def listar_atividades():


    return render_template('listar_atividades.html', dados_lista=lista)



@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')

# Iniciar aplicação web
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)


#Nada deve ser colocado abaixo