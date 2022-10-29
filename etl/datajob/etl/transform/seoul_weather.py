from infra.jdbc import DataMart, DataWarehouse, save_data
from pyspark.sql import Row
from infra.spark_session import get_spark_session
from pyspark.sql.functions import col
from pyspark.sql.types import *
import csv

class SeoulweatherTransformer:
    
    @classmethod
    def transform(cls):
        path = '/themapark/data/seoul_weather2.csv'
        dw = get_spark_session().read.csv(path, encoding='cp949',header=True)

        w_data = dw.select(
                col('지점명').cast(IntegerType()).alias('THEME_NUM')
                ,col('일시').cast(DateType()).alias('STD_DATE')
                ,col('최고기온').cast(FloatType()).alias('HIGH_TEMP')
                ,col('최저기온').cast(FloatType()).alias('LOW_TEMP')
                ,col('DIFF_TEMP').cast(FloatType())
                ,col('일강수량').cast(FloatType()).alias('RAIN_AMOUNT')
                ,col('평균풍속').cast(FloatType()).alias('AVG_WIND')
                ,col('최대순간풍속').cast(FloatType()).alias('HIGH_WIND')
            )


        save_data(DataWarehouse,w_data , 'DAILY_WEATHER')