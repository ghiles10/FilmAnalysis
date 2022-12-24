echo ' '
echo '----> web scrapping des données film à partir du site allo ciné ...' 
echo '----> cela ne va pas prendre beaucoup de temps car le réglage du script permet de récuperer uniquement la premiere page' 

# faire appel au script qui scrapp les données et stock dans des fichiers txt
python3  /app/scripts/write_to_txt.py 

echo ' '
echo '----> veuillez copier et entrer un titre parmis la liste des titres proposés : '
echo ' ' 

# affiche la liste des titre de film
cat /app/titre_film.txt 

# demander a l'utilisateur d'entrer le titre
echo ' '
read -p "écrire le nom : " titre
export titre 

echo ' ' 
echo '----> vous avez choisit : ' $titre
echo '----> Récupération des informations ...'
echo ' '

# run le script final qui nettoie la base de données et affiche les infos 
python3 /app/notebook/pyspark_traitement.py "$titre" 


