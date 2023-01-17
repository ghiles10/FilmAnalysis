def preprocess_to_csv() :

    '''nettoie la base de données et enregistre un fichier csv'''
    
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col
    import preprocess_linux 
    import warnings
    warnings.filterwarnings("ignore")
   
    # spark session 
    spark_session = SparkSession.builder.appName('data_film').getOrCreate()

    # base de données
    raw_data = spark_session.read.option("delimiter", "\t").csv(r'./src/data/data_film.txt', header=False).cache()
    raw_data = raw_data.toDF('titre', 'date', 'duree', 'type', 'note', 'nombre avis', 'avis')

    # PREPROCESS
    data = preprocess_linux.preproces_for_machine_learning(raw_data, spark_session)

    #enregistrer la base nettoyee
    data.write.format("csv").mode("overwrite").save("./src/data/base_nettoye.csv")

if __name__ == '__main__' : 
    preprocess_to_csv()
