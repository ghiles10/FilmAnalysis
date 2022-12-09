def titre_films_to_txt(data) : 

    """ permet d'ecrire dans le fichier txt titre_film les titres des films afin de les utilsier quand on fera appel à l'utilisateur"""
    
    with open(r'/workspaces/web-scrapping-Machine-learning-/titre_films.txt',"a") as f : 
        for i in range(data.count()): 
            titre = data.select('titre').collect()[i][0]
            f.write(titre+'\n')
    
    f.close()
    print('ok')

titre_films_to_txt() 
