def affichage_info(input_file) :

    '''affiche les infos du titre choisit'''
    
    import sys
    # Récupération du titre du film passé en argument
    # input_file = sys.argv[1]

    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col
    import preprocess_linux 
    import warnings
    warnings.filterwarnings("ignore")
    import re

    # spark session 
    spark_session = SparkSession.builder.appName('data_film').getOrCreate()

    # base de données
    raw_data = spark_session.read.option("delimiter", "\t").csv(r'./data/data_film.txt', header=False)
    raw_data = raw_data.toDF('titre', 'date', 'duree', 'type', 'note', 'nombre avis', 'avis')

    # PREPROCESS
    data = preprocess_linux.preproces_for_machine_learning(raw_data, spark_session)

    # affichage du titre -> fin du projet 
    data_a_afficher = data.where(col('titre') == str(input_file)) # selection de la ligne a afficher

    info = [ f"Titre : {data_a_afficher.select('titre').collect()[0][0]}",  f"Date de sortie : {data_a_afficher.select('date').collect()[0][0] }" ,\
    f"Durée : {data_a_afficher.select('duree').collect()[0][0]}",\
    f"Note : {data_a_afficher.select('note').collect()[0][0]}" ,f"Type : {data_a_afficher.select('type').collect()[0][0]}",\
    f"Nombre d\'avis {int (data_a_afficher.select('nombre avis').collect()[0][0])}" ]

    return "|".join(info)


if __name__ == '__main__' : 
    affichage_info(input_file)