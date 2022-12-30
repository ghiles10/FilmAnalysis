from flask import Flask, request, render_template
import sys

# ajouter le module dans liste des modules pour faire appel
sys.path.append(r"./scripts")
import affichage_info 

app = Flask(__name__)

def get_title_info(title):

    # récupérer les informations du titre ici
    title_info = test_run_docker.affichage_info(str(title))
    return title_info

@app.route('/', methods=['GET', 'POST'])

def index():

    if request.method == 'POST':
        # récupérer le titre entré par l'utilisateur
        title = request.form['title']
        # appeler la fonction pour récupérer les informations du titre
        title_info = get_title_info(title)
        # retourner les informations du titre à l'utilisateur
        return render_template('index.html', title_info=title_info)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
