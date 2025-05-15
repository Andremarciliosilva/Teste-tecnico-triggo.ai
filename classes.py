# Imports das bibliotecas
import pandas as pd

# Classe pra converter os arquivos csvs's pra DataFrame
class CsvToDataFrame:
    def __init__(self, csv_file: str):
        self.csv_file = csv_file

    def read_csv(self):
        df = pd.read_csv(self.csv_file)
        return df
    
# Classe com métodos pra remover e substituir os valores nulos e duplicados
class CleaningDatasets:
    def __init__(self, df: pd.DataFrame) -> pd.DataFrame:
        self.df:pd.DataFrame = df

    def fill_and_report_nulls(self):
        self.df.fillna("Campo vazio/não preenchido", inplace=True)
    
    def remove_duplicate(self, df: pd.DataFrame):
        df:pd.DataFrame = df
        df.drop_duplicates(inplace=True)

   
class NormalizeDataFrames:
     def __init__(self, csv_file: str, colunm):
        self.csv_file = csv_file
        self.colunm = colunm

     def unique_value(self):
        df_unique_value = self.csv_file[self.colunm].unique()
        return print(df_unique_value)
