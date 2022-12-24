# ajouter le module dans liste des modules pour faire appel
import sys
sys.path.append(r"/app/scripts")

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import preprocess_linux 
import warnings
warnings.filterwarnings("ignore")
import re

# spark session 
spark_session = SparkSession.builder.appName('data_film').getOrCreate()

# base de données
raw_data = spark_session.read.option("delimiter", "\t").csv(r'/app/data_film.txt', header=False)
raw_data = raw_data.toDF('titre', 'date', 'duree', 'type', 'note', 'nombre avis', 'avis')

# PREPROCESS
data = preprocess_linux.preproces_for_machine_learning(raw_data, spark_session)


# affichage du titre -> fin du projet 
input_file = sys.argv[1]
# affichage du titre -> fin du projet 
def fin_projet(input_file) : 

    """permet d'afficher les resultats """
    try : 
        data_a_afficher = data.where(col('titre') == str(input_file)) # selection de la ligne a afficher
        print()
        print('--------> Infos du film :')
        print('----------------------')
        print()
        print( '- Titre :',data_a_afficher.select('titre').collect()[0][0] ) 
        print( '- Date de sortie :',data_a_afficher.select('date').collect()[0][0] ) 
        print( '- Durée :',data_a_afficher.select('duree').collect()[0][0] ) 
        print( '- Note :',data_a_afficher.select('note').collect()[0][0] ) 
        print( '- Type :',data_a_afficher.select('type').collect()[0][0] ) 
        print( '- Nombre d\'avis :',int (data_a_afficher.select('nombre avis').collect()[0][0] ) )

    except IndexError: 
        print('--------------> Bien écrire le titre svp')
        nouveau_titre_bien_ecrit = str(input('Réecrire :'))
        fin_projet(nouveau_titre_bien_ecrit) 

fin_projet(input_file)

def demande_nouveau_titre() :

    demande_nv_titre = input('Un autre titre? oui/non ')

    if str(demande_nv_titre) == 'oui' : 

        nouveau_titre = input('Ecrire titre : ')
        fin_projet(str(nouveau_titre))
        demande_nouveau_titre() #récursivité 

    else :
        print('Au revoir !')

demande_nouveau_titre()