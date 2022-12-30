def affichage_info(input_file) : 
    
    
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col
    import preprocess_linux 
    import warnings
    warnings.filterwarnings("ignore")
   

    # spark session 
    spark_session = SparkSession.builder.appName('affichage_film').getOrCreate()

    # base de données
    data = spark_session.read.csv(r'./data/base_nettoye.csv', header=True)
    data = data.toDF('titre', 'date', 'duree', 'type', 'note', 'nombre avis', 'avis')

    # affichage du titre -> fin du projet 
    data_a_afficher = data.where(col('titre') == str(input_file)) # selection de la ligne a afficher

    info = [ f"Titre : {data_a_afficher.select('titre').collect()[0][0]}",  f"Date de sortie : {data_a_afficher.select('date').collect()[0][0] }" ,\
    f"Durée : {data_a_afficher.select('duree').collect()[0][0]}",\
    f"Note : {data_a_afficher.select('note').collect()[0][0]}" ,f"Type : {data_a_afficher.select('type').collect()[0][0]}",\
    f"Nombre d\'avis {int (data_a_afficher.select('nombre avis').collect()[0][0])}" ]

    return " | ".join(info)


if __name__ == '__main__' : 
    affichage_info(input_file)
