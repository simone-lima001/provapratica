from flask import Flask, render_template, request, redirect

app = Flask(__name__)

times = []

@app.route('/')
def index():
    return redirect('/listar_times')

@app.route('/listar_times')
def listar_times():
    return render_template('listar_times.html', times=times,)

@app.route('/cadastrar_times', methods=['GET', 'POST'])
def cadastrar_times():
    if request.method == 'POST':
        
        time= {
            'id': len(times)+1,
            'nome': request.form['nome'],
            'cidade': (request.form['cidade']),
            'estado': (request.form['estado'])
        }
        times.append(time)
        

        return redirect('/')
    return render_template('cadastrar_times.html')

@app.route('/editar-time/<int:id>', methods=['GET', 'POST'])
def editar_time(id):
    for time in times:
        if time['id'] == id:
            if request.method == 'POST':
                time['nome'] = request.form['nome']
                time['cidade'] = (request.form['cidade'])
                time['estado'] = (request.form['estado'])
                return redirect('/listar_times')
            return render_template('editar_time.html', time=time)
    return redirect('/listar_times')

@app.route('/excluir-time/<int:id>')
def excluir_time(id):
    for time in times:
        if time['id'] == id:
            times.remove(time)
            break
    return redirect('/listar_times')



if __name__ == '__main__':
    app.run(debug=True)
