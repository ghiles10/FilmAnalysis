echo '----> web scrapping des données film à partir du site allo ciné ...' 
echo '----> cela ne va pas prendre beaucoup de temps car le script récupere uniquement la premiere page' 

python3  /app/scripts/write_to_txt.py 

echo '- veuillez entrer un titre parmis la liste des titres proposés : '

cat /app/titre_film.txt 

read titre 

python3 /app/notebook/test_run_docker.py ${titre} 


