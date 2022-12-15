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

print('voici le , ', str(input_file))

# affichage du titre -> fin du projet 
data_a_afficher = data.where(col('titre') == str(input_file)) # selection de la ligne a afficher

print('----> Infos du film :')
print('-----------------')
print( '- Titre :',data_a_afficher.select('titre').collect()[0][0] ) 
print( '- Date de sortie :',data_a_afficher.select('date').collect()[0][0] ) 
print( '- Durée :',data_a_afficher.select('duree').collect()[0][0] ) 
print( '- Note :',data_a_afficher.select('note').collect()[0][0] ) 
print( '- Type :',data_a_afficher.select('type').collect()[0][0] ) 
print( '- Nombre d\'avis :',int (data_a_afficher.select('nombre avis').collect()[0][0] ) )