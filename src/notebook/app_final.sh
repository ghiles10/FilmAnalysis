echo ' '
echo '----> web scrapping des données film à partir du site allo ciné ...' 
echo '----> cela ne va pas prendre beaucoup de temps car le réglage du script permet de récuperer uniquement la premiere page' 

# faire appel au script qui scrapp les données et stock dans des fichiers txt
python3 src/scripts/write_to_txt.py 

echo '- veuillez entrer un titre parmis la liste des titres proposés dans la page web : '

# affiche la liste des titre de film
cat src/data/titre_film.txt 

# traitement des données 
python3  ./src/scripts/recuperation_infos_spark.py 

# run le script final qui nettoie la base de données et affiche les infos 
python3 ./src/test_flask/app.py 



