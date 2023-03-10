import film
import os 

def extract_data() : 

    """stocke les donnes dans un fichier texte"""
    
    if not os.path.exists("src/data"):
        os.mkdir("src/data")

    # écrire vers un fichier txt
    raw_data = film.get_donnees_film()
    with open('src/data/data_film.txt', 'w') as f :
        for titre, info in raw_data.items() : 

            f.write( str(titre)+ '\t' + str(info[0][0])+ '\t' + str(info[0][1]) + '\t' + str(info[0][2])\
            +'\t' + str(info[1][0]) + '\t' + str(info[1][1]) + '\t' +str(info[2])+ '\n' )
    
        f.close()

   
def write_titre_txt() :

    """ permet d'ecrire le titre des films dans un fichier txt et utilisation dans bash"""
    
    raw_data = film.get_donnees_film()
    with open(r'src/data/titre_film.txt', 'w') as f :
        for titre in raw_data.keys() :
            f.write('-' + titre + '\n') 
    f.close()


if __name__ == '__main__' : 
    extract_data()
    write_titre_txt() 
    print('extracting data done')

