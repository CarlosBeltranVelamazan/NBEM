
# Canarias, no hay datos de los edificios (superficie, año, si es vivienda o local o ...), pero hay mucha información de cuánta energía y co2 emite y del vector energético
# tiene en algunos casos dos referencias catastrales unidas por una coma en la misma casilla

def CanariasDB(archivo):
    import pandas as pd
    import numpy as np
    import xlrd   
    try:
        df = (pd.read_excel(archivo, skiprows=0))
    except:
        df = (pd.read_csv(archivo, skiprows=0, sep= ';', encoding='ANSI'))
    df.insert(0, 'CCAA', "Canarias")
    second_column = df.pop('provincia') 
    df.insert(1, 'PROV', second_column) 
    df.insert(2, 'Fecha_registro', df ['fecha_registro'].str[-4:])
    df.insert(3, 'C_CCAA', 5) 
    df.insert(4, 'CPROV', df.PROV) 
    df.CPROV.replace({"SANTA CRUZ DE TENERIFE": 38, "PALMAS (LAS)": 35, "sin provincia": None}, inplace=True)
    df.insert(5, 'N_certif', 1) 
    eleventh_column = df.pop('calificacion_consumo_anual')
    df.insert(6, 'Calificación_consumo_energía', eleventh_column) 
    eleventh_column = df.pop('calificacion_emision_anual')
    df.insert(7, 'Calificación_emisiones', eleventh_column) 

    df = (df.assign(
          EP_A = np.where(df['Calificación_consumo_energía']=='A',1,0), 
          EP_B = np.where(df['Calificación_consumo_energía']=='B',1,0), 
          EP_C = np.where(df['Calificación_consumo_energía']=='C',1,0), 
          EP_D = np.where(df['Calificación_consumo_energía']=='D',1,0), 
          EP_E = np.where(df['Calificación_consumo_energía']=='E',1,0), 
          EP_F = np.where(df['Calificación_consumo_energía']=='F',1,0), 
          EP_G = np.where(df['Calificación_consumo_energía']=='G',1,0), 
          co2_A = np.where(df['Calificación_emisiones']=='A',1,0), 
          co2_B = np.where(df['Calificación_emisiones']=='B',1,0), 
          co2_C = np.where(df['Calificación_emisiones']=='C',1,0), 
          co2_D = np.where(df['Calificación_emisiones']=='D',1,0), 
          co2_E = np.where(df['Calificación_emisiones']=='E',1,0), 
          co2_F = np.where(df['Calificación_emisiones']=='F',1,0), 
          co2_G = np.where(df['Calificación_emisiones']=='G',1,0), 
          ).groupby(['Fecha_registro']).agg(
                        CCAA = ('CCAA', 'first'), \
                        PROV = ('PROV', 'first'), \
                        Fecha_registro = ('Fecha_registro', 'first'), \
                        C_CCAA = ('C_CCAA', 'first'), \
                        CPROV = ('CPROV', 'first'), \
                        N_certif = ('N_certif', 'sum'), \
                        EP_A = ('EP_A', 'sum'), \
                        EP_B = ('EP_B', 'sum'), \
                        EP_C = ('EP_C', 'sum'), \
                        EP_D = ('EP_D', 'sum'), \
                        EP_E = ('EP_E', 'sum'), \
                        EP_F = ('EP_F', 'sum'), \
                        EP_G = ('EP_G', 'sum'), \
                        co2_A = ('co2_A', 'sum'), \
                        co2_B = ('co2_B', 'sum'), \
                        co2_C = ('co2_C', 'sum'), \
                        co2_D = ('co2_D', 'sum'), \
                        co2_E = ('co2_E', 'sum'), \
                        co2_F = ('co2_F', 'sum'), \
                        co2_G = ('co2_G', 'sum'), \
                        ))

    return df
