from pyspark.sql import functions as F

def preproces_for_machine_learning(data, spark_session) :  

    """cette fonction permet de nettoyer les données afin de pouvoir faire des stats desc et des modeles ML"""

    # traitment variable avis 
    data = data.withColumn("avis", F.regexp_replace(F.col("avis"), "[\['\"0-9]" , ""))

    # traitment de la variable type
    data = data.withColumn("type", F.regexp_replace(F.col("type"), "[\[\]',]", ""))
 
    # encoder la variable date afin de passer du format francais a un format usuel  
    data = data.withColumn("date", F.regexp_replace('date','août', "08"))
    data = data.withColumn("date", F.regexp_replace('date','avril', "04"))
    data = data.withColumn("date", F.regexp_replace('date','décembre', "12"))
    data = data.withColumn("date", F.regexp_replace('date','février', "02"))
    data = data.withColumn("date", F.regexp_replace('date','janvier', "01"))
    data = data.withColumn("date", F.regexp_replace('date','juillet', "07"))
    data = data.withColumn("date", F.regexp_replace('date','mars', "03"))
    data = data.withColumn("date", F.regexp_replace('date','juin', "06"))
    data = data.withColumn("date", F.regexp_replace('date','mai', "05"))
    data = data.withColumn("date", F.regexp_replace('date','novembre', "11"))
    data = data.withColumn("date", F.regexp_replace('date','octobre', "10"))
    data = data.withColumn("date", F.regexp_replace('date','septembre', "09"))

    # changer le format des dates  
    spark_session.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY") # car ne veut pas reconnaitre le format de base 
    data = data.withColumn("date", F.to_date("date", "dd MM yyyy")) 

    ################### caster le format des colonnes
    # for col in ['note','nombre avis'] : 
    #     data = data.withColumn(col ,F.col(col).cast('float')) 

    return data 
  




