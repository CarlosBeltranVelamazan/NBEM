 # Galicia, el csv no entrecomilla los campos y en algunas direcciones hay texto con comas entre medio, esto no permite leerlo como un archivo normal porque crea columnas que no son correctas al enternder que las comas de las direcciones son separadores de columnas
 # Además, no sólo hay comas en la dirección sino en el tipo de edificio, porque ponen Vivienda Unifamiliar (Calle..., ...,....) complicando el asunto. 
 # Para solucionarlo, como va siempre entre paréntesis primero divido por paréntesis, quito esa parte y sigo con la información buena, sin embargo como también hay paréntesis en la dirección a veces debo comprobar que no esté borrando desde ahí
import pandas as pd
import numpy as np
import re
def GaliciaDB(archivo):
        df2 = (pd.read_csv(archivo, skiprows=0, sep='__', engine='python',encoding='latin1')
                .dropna(how='all', axis=1))
        print(df2.shape [0])
        df = pd.DataFrame ()
        df1 = pd.DataFrame ()
        c = 1
      #  print (df2.iloc[:, 0])
        for i in df2.index:
                linea2 = df2.iloc[i, 0]
                linea3 = re.sub(r'\([^)]*\)', '', linea2)
                linea = linea3.split(',')
                try:
                        nueva_fila = {'numSol':linea[0] ,'numeroRegistro':linea[1] ,'tipoCEE':linea[2],'enderezo':linea[3:-12],'normativa':linea[-12],'refCatastral':linea[-11],'municipio':linea[-10],'cpCat':linea[-9],'provincia':linea[-8],'consumo':linea[-7],'letraConsumo':linea[-6],'emisions':linea[-5],'letraEmisions':linea[-4],'anoSolicitude':linea[-3],'fechaCaducidade':linea[-2],'descViv':linea[-1]}
                        df1 = pd.concat([df1, pd.DataFrame(nueva_fila.values()).T], ignore_index=True, axis=0)
                        if i == 5000*c:
                                c = c+1
                                df = pd.concat([df, df1], ignore_index=True, axis=0)
                                df1 = pd.DataFrame ()
                                print(i)
                except:
                        print('error en ' + str(i))
                        pass
        df = pd.concat([df, df1], ignore_index=True, axis=0)
        df.columns = ['numSol','numeroRegistro','tipoCEE','enderezo','normativa','refCatastral','municipio','cpCat','provincia','consumo','letraConsumo','emisions','letraEmisions','anoSolicitude','fechaCaducidade','descViv']
        first_column = df.pop('refCatastral').str.strip()
        df.insert(0, 'ReferenciaCatastral', first_column) 
        second_column = df.pop('cpCat')
        df.insert(1, 'CP', second_column) 
        df.insert(2, 'CCAA', "Galicia") 
        third_column = df.pop('provincia')
        df.insert(3, 'PROV', third_column) 
        eleventh_column = df.pop('normativa')
        df.insert(4, 'Normativa_edificación', eleventh_column) 
        df.insert(5, 'Normativa_instalaciones', "") 
        df.insert(6, 'Programa_informático', "") 
        eleventh_column = df.pop('anoSolicitude')
        df.insert(7, 'Fecha_registro', eleventh_column) 
        df.insert(8, 'C_CCAA', 12) 
        df.insert(9, 'CPROV', df.PROV) 
        df.CPROV.replace({"A CORUÑA": 15, "LUGO": 27, "OURENSE": 32, "PONTEVEDRA": 36}, inplace=True)
        df.insert(10, 'N_certif', 1) 
        eleventh_column = df.pop('letraConsumo')
        df.insert(11, 'Calificación_consumo_energía', eleventh_column) 
        eleventh_column = df.pop('letraEmisions')
        df.insert(12, 'Calificación_emisiones', eleventh_column) 

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


