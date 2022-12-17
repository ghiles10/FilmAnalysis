echo '----> web scrapping des données film à partir du site allo ciné ...' 
echo '----> cela ne va pas prendre beaucoup de temps car le script récupere uniquement la premiere page' 

# faire appel au script qui scrapp les données et stock dans des fichiers txt
python3  /app/scripts/write_to_txt.py 

echo '- veuillez entrer un titre parmis la liste des titres proposés dans la page web : '

# affiche la liste des titre de film
cat /app/titre_film.txt 

# run le script final qui nettoie la base de données et affiche les infos 
streamlit run /app/notebook/api.py 


