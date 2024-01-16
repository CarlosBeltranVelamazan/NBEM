 # Cataluña

def CataluñaDB(archivo):
        import pandas as pd
        import numpy as np
        import xlrd 
        df = (pd.read_csv(archivo, skiprows=0, sep= ';')
                .dropna(how='all', axis=1))
        df.insert(0, 'CCAA', "Cataluña") 
        second_column = df.pop('NOM_PROVINCIA')
        df.insert(1, 'PROV', second_column)
        df.insert(2, 'Fecha_registro', df ['DATA_ENTRADA'].str[-4:])
        df.insert(3, 'C_CCAA', 9) 
        df.insert(4, 'CPROV', df.PROV) 
        df.CPROV.replace({"BARCELONA": 8, "Barcelona": 8, "GIRONA": 17, "Girona": 17, "LLEIDA": 25, "Lleida": 25, "TARRAGONA": 43, "Tarragona": 43}, inplace=True)
        df.insert(5, 'N_certif', 1) 
        eleventh_column = df.pop("Qualificació de consum d'energia primaria no renovable")
        df.insert(6, 'Calificación_consumo_energía', eleventh_column) 
        eleventh_column = df.pop("Qualificacio d'emissions de CO2")
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


