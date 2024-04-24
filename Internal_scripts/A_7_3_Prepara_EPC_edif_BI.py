def prepare_EPCs (EPC_database_14_digits, EPC_database_20_digits):
    import os
    import pandas as pd
    import numpy as np
    from simpledbf import Dbf5
    from time import time

    inicio  = time()

    # Building scale. 14 digits cadastral reference
    try: 
        df = (pd.read_parquet(EPC_database_14_digits))
    except:
        df = (pd.read_csv(EPC_database_14_digits, skiprows=0))

    # Para poder guardar en formato parquet hay que quitar las columnas que no aportan nada (y que son problemáticas si no se han filtrado antes), para eso es este código

    # Columnas que queremos conservar en el df, las que no estén aquí se borrarán
    colsusar = ['ReferenciaCatastral', 'TipoEdificio',
        'Consumo_energía_primaria', 'Calificación_consumo_energía',
        'Emisiones_CO2', 'Calificación_emisiones', 'Fecha_registro',
        'C_CCAA', 'CPROV']
    df = df[df.columns.intersection(colsusar)]


    # Columnas finales que deben estar en el dataframe para que tenga los datos como si estuvieran agrupados por edificio:
    # (va a ser lo más fácil para automatizar el proceso)

    # ReferenciaCatastral_edificio, ReferenciaCatastral_BI, Consumo_energia_primaria_medio, Consumo_energia_primaria_mediano, 
    # Emisiones_CO2_medio, Emisiones_CO2_mediano, C_CCAA, CPROV, Numero_de_EPC, A_EP, B_EP, C_EP, D_EP, E_EP, F_EP, G_EP, A_CO2, 
    # B_CO2, C_CO2, D_CO2, E_CO2, F_CO2, G_CO2

    first_column = df.pop('CPROV')
    df.insert(0, 'CPROV', first_column)

    first_column = df.pop('C_CCAA')
    df.insert(0, 'C_CCAA', first_column)

    df.insert(0, 'G_CO2', np.where(df['Calificación_emisiones']=='G',1,0))
    df.insert(0, 'F_CO2', np.where(df['Calificación_emisiones']=='F',1,0))
    df.insert(0, 'E_CO2', np.where(df['Calificación_emisiones']=='E',1,0))
    df.insert(0, 'D_CO2', np.where(df['Calificación_emisiones']=='D',1,0))
    df.insert(0, 'C_CO2', np.where(df['Calificación_emisiones']=='C',1,0))
    df.insert(0, 'B_CO2', np.where(df['Calificación_emisiones']=='B',1,0))
    df.insert(0, 'A_CO2', np.where(df['Calificación_emisiones']=='A',1,0))

    df.insert(0, 'G_EP', np.where(df['Calificación_consumo_energía']=='G',1,0))
    df.insert(0, 'F_EP', np.where(df['Calificación_consumo_energía']=='F',1,0))
    df.insert(0, 'E_EP', np.where(df['Calificación_consumo_energía']=='E',1,0))
    df.insert(0, 'D_EP', np.where(df['Calificación_consumo_energía']=='D',1,0))
    df.insert(0, 'C_EP', np.where(df['Calificación_consumo_energía']=='C',1,0))
    df.insert(0, 'B_EP', np.where(df['Calificación_consumo_energía']=='B',1,0))
    df.insert(0, 'A_EP', np.where(df['Calificación_consumo_energía']=='A',1,0))

    df.insert(0, 'Numero_de_EPC', 1)

    first_column = df.pop('Emisiones_CO2')
    df.insert(0, 'Emisiones_CO2_mediano', first_column)
    df.insert(0, 'Emisiones_CO2_medio', first_column)

    first_column = df.pop('Consumo_energía_primaria')
    df.insert(0, 'Consumo_energia_primaria_mediano', first_column)
    df.insert(0, 'Consumo_energia_primaria_medio', first_column)

    first_column = df.pop('ReferenciaCatastral')

    df.insert(0, 'ReferenciaCatastral_BI', "")
    df.insert(0, 'ReferenciaCatastral_edificio', first_column.str[:14])

    first_column = df.pop('Calificación_consumo_energía')
    first_column = df.pop('Calificación_emisiones')

    # df.to_csv(Carpeta_archivos_guardar + nombre14[0] + "prueba" + ".csv", index=False)
    df_14 = df

    # Building unit scale. 20 digit cadastral reference
    try: 
        df = (pd.read_parquet(EPC_database_20_digits))
    except:
        df = (pd.read_csv(EPC_database_20_digits, skiprows=0))

    # Para poder guardar en formato parquet hay que quitar las columnas que no aportan nada (y que son problemáticas si no se han filtrado antes), para eso es este código
    # Columnas que queremos conservar en el df, las que no estén aquí se borrarán
    colsusar = ['ReferenciaCatastral', 'TipoEdificio',
        'Consumo_energía_primaria', 'Calificación_consumo_energía',
        'Emisiones_CO2', 'Calificación_emisiones', 'Fecha_registro',
        'C_CCAA', 'CPROV']
    df = df[df.columns.intersection(colsusar)]

    first_column = df.pop('CPROV')
    df.insert(0, 'CPROV', first_column)

    first_column = df.pop('C_CCAA')
    df.insert(0, 'C_CCAA', first_column)

    df.insert(0, 'G_CO2', np.where(df['Calificación_emisiones']=='G',1,0))
    df.insert(0, 'F_CO2', np.where(df['Calificación_emisiones']=='F',1,0))
    df.insert(0, 'E_CO2', np.where(df['Calificación_emisiones']=='E',1,0))
    df.insert(0, 'D_CO2', np.where(df['Calificación_emisiones']=='D',1,0))
    df.insert(0, 'C_CO2', np.where(df['Calificación_emisiones']=='C',1,0))
    df.insert(0, 'B_CO2', np.where(df['Calificación_emisiones']=='B',1,0))
    df.insert(0, 'A_CO2', np.where(df['Calificación_emisiones']=='A',1,0))

    df.insert(0, 'G_EP', np.where(df['Calificación_consumo_energía']=='G',1,0))
    df.insert(0, 'F_EP', np.where(df['Calificación_consumo_energía']=='F',1,0))
    df.insert(0, 'E_EP', np.where(df['Calificación_consumo_energía']=='E',1,0))
    df.insert(0, 'D_EP', np.where(df['Calificación_consumo_energía']=='D',1,0))
    df.insert(0, 'C_EP', np.where(df['Calificación_consumo_energía']=='C',1,0))
    df.insert(0, 'B_EP', np.where(df['Calificación_consumo_energía']=='B',1,0))
    df.insert(0, 'A_EP', np.where(df['Calificación_consumo_energía']=='A',1,0))

    df.insert(0, 'Numero_de_EPC', 1)


    first_column = df.pop('Emisiones_CO2')
    df.insert(0, 'Emisiones_CO2_mediano', first_column)
    df.insert(0, 'Emisiones_CO2_medio', first_column)

    first_column = df.pop('Consumo_energía_primaria')
    df.insert(0, 'Consumo_energia_primaria_mediano', first_column)
    df.insert(0, 'Consumo_energia_primaria_medio', first_column)

    first_column = df.pop('ReferenciaCatastral')

    df.insert(0, 'ReferenciaCatastral_BI', first_column)
    df.insert(0, 'ReferenciaCatastral_edificio', first_column.str[:14])

    first_column = df.pop('Calificación_consumo_energía')
    first_column = df.pop('Calificación_emisiones')

    # df.to_csv(Carpeta_archivos_guardar + nombre20[0] + "prueba" + ".csv", index=False)

    # df.to_parquet(Carpeta_archivos_guardar + nombre20[0] + ".gzip", compression='gzip', index=False)

    duracion_A = time() - inicio
    print('En total ha tardado: ' + str(duracion_A) + ' segundos')

    return df_14, df
