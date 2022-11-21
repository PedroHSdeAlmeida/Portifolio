from flask import Flask , render_template
app=Flask(__name__)

@app.route("/")
def inicio(): 
    return render_template('index.html')

@app.route("/contatos")
def contatos(): 
    return render_template('contatos.html')

@app.route("/projetos")
def projetos(): 
    return render_template('projetos.html')

@app.route("/sobreMim")
def sobreMim(): 
    return render_template('sobreMim.html')

app.debug = True
if __name__ == '__main__':
    app.run()