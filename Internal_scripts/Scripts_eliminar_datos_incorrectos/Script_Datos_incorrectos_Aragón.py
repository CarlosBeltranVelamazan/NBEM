def Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa):
    import pandas as pd
    import numpy as np
    import xlrd 
    df = (pd.read_excel(archivo, skiprows=0))
    fallos = pd.DataFrame()
    # Errores en la referencia catastral
    a = df.shape[0] # Nos da el número de filas antes de eliminar los valores erróneos

    # Nota importante: Para evitar problemas con las referencias catastrales que tienen comas las sustituyo por guiones
    df.ReferenciaCatastral.replace(to_replace=r',', value='.', regex=True,inplace=True)
    df.ReferenciaCatastral.replace(to_replace=r';', value='.', regex=True,inplace=True)
    df.ReferenciaCatastral.replace(to_replace=r' ', value='', regex=True,inplace=True)


    if eliminar_errores_ReferenciaCatastral == 1:
        # Nota importante: El filtrado de las referencias catastrales da problemas porque hay referencias catastrales reales que no siguen esos patrones
        # Nota importante: Para poder filtrar los certificados con errores en las referencias catastrales empleo esta solución, que comprueba que los primeros 14 dígitos de las referencias catastrales coincidan con edificios, ya que puede certificarse edificios o partes de edificios, debe tenerse en cuenta que a veces hay varias referencias de 20 dígitos seguidas en el mismo campo, este script comprueba los primeros 14 dígitos pero como finalmente el objetivo de usar la referencia catastral como dato será agrupar por edificio esta solución nos es la más apta para este caso.     

        # Algunas indicaciónes que he desarrollado para filtrar Referencias Catastrales que podrían ser útiles
        # Esto sería para comprobar que las referencias catastrales de edificio  están bien, es el código de re para los 14 carácteres de una referencia catastral.
        # df = df[df['ReferenciaCatastral_edificio'].str.contains(r"^[0-9]{7}[A-Z]{2}[0-9]{4}[A-Z]{1}$", regex=True)].reset_index()
        # Esto sería para comprobar que las referencias catastrales de edificio  están bien, es el código de re para los 20 carácteres de una referencia catastral.
        # df = df[df['ReferenciaCatastral'].str.contains(r"^[0-9]{7}[A-Z]{2}[0-9]{4}[A-Z]{1}[0-9]{4}[A-Z]{2}", regex=True)].reset_index()
        # Para re se usa match para que toda la cadena sea así, search para que parte de la cadena cumpla la condición y se pone lo que queremos que comprueba y la condición
        # En la condición ^ significa el principio y $ el final de los carácteres, [0-9]{7} es que los siguientes 7 carácteres tienen que ser números, [A-Z]{2} dos carácteres tienen que ser letras
        # [0-9]{4} ahora 4 carácteres números y [A-Z]{1} y una letra (hasta aqui la referencia catastral del edificio) y ahora [0-9]{4}[A-Z]{2} son 4 numeros y dos letras (la referencia catastral de la parte del edificio)
        # La expresión regular acaba en .* para marcar que continúa con cualquier otro caracter 0 o más veces, referencias de 14 dígitos o más largas con lo que continue
        
        df ['ReferenciaCatastral'] = df ['ReferenciaCatastral']. fillna('None') # Cambia los valores vacíos por otros en los que literalmente pone vacío
        fallos2 = df.loc[df.loc[:, 'ReferenciaCatastral'] == 'None']
        df = df.loc[df.loc[:, 'ReferenciaCatastral'] != 'None']
        # Para poder guardar los valores que no cumplen la expresión regurlar de las referencias catastrales empleo esta solución df = df[df['ReferenciaCatastral'].str.contains(r"^[0-9]{7}[A-Z]{2}[0-9]{4}[A-Z]{1}.*", regex=True)].reset_index()
        bien = df[df['ReferenciaCatastral'].str.contains(r"^[0-9]{7}[A-Z]{2}[0-9]{4}[A-Z]{1}.*", regex=True)]
        fallos3 = df[~df.index.isin(bien.index)]      
        df = bien

        fallos = pd.concat([fallos2, fallos3], axis=0)
    b = df.shape[0] # Nos da el número de filas después de eliminar los valores erróneos
    c = a-b # Nos da el número de certificados que hemos eliminado por erróneos

    # Errores en el Código Postal
    if eliminar_errores_CP == 1:
        df ['CP'] = df ['CP']. fillna('None')
        fallos2 = df.loc[df.loc[:, 'CP'] == 'None']
        df = df.loc[df.loc[:, 'CP'] != 'None']
        fallos = pd.concat([fallos, fallos2], axis=0)
    d = df.shape[0]
    e = b-d

    # Errores en el FechaConstrucción
    if eliminar_errores_FechaConstrucción == 1:
        first_column = df.pop('FechaConstrucción')
        first_column = pd.to_numeric(first_column, errors='coerce')
        df.insert(13, 'FechaConstrucción', first_column)
        df ['FechaConstrucción'] = df ['FechaConstrucción'].fillna('None')
        fallos2 = df.loc[df.loc[:, 'FechaConstrucción'] == 'None']
        df = df.loc[df.loc[:, 'FechaConstrucción'] != 'None']
        fallos10 = df.loc[df.loc[:, 'FechaConstrucción'] < 1500]
        df = df.loc[df.loc[:, 'FechaConstrucción'] >= 1500]
        fallos11 = df.loc[df.loc[:, 'FechaConstrucción'] > 2022]
        df = df.loc[df.loc[:, 'FechaConstrucción'] <= 2022]
        fallos = pd.concat([fallos, fallos2, fallos10, fallos11], axis=0)
    f = df.shape[0]
    g = d-f

    # Errores en el SuperficieUtil
    if eliminar_errores_SuperficieUtil == 1:
        first_column = df.pop('SuperficieUtil')
     #   first_column = first_column.replace(",", ".").astype(float,errors='ignore')        # Debería funcionar pero me ha dado problemas, mejor la línea de debajo
        first_column.replace(to_replace=r',', value='.', regex=True,inplace=True)
        first_column = pd.to_numeric(first_column, errors='coerce')
        first_column = first_column.astype({'SuperficieUtil':'float64'})
        df.insert(14, 'SuperficieUtil', first_column)
        df ['SuperficieUtil'] = df ['SuperficieUtil']. fillna('None')
        fallos2 = df.loc[df.loc[:, 'SuperficieUtil'] == 'None']
        df = df.loc[df.loc[:, 'SuperficieUtil'] != 'None']
        fallos10 = df.loc[df.loc[:, 'SuperficieUtil'] < 10]
        df = df.loc[df.loc[:, 'SuperficieUtil'] >= 10]
        fallos = pd.concat([fallos, fallos2, fallos10], axis=0)
    h = df.shape[0]
    i = f-h

    # Errores en el Consumo_energía_primaria
    if eliminar_errores_Consumo_energía_primaria == 1:
        first_column = df.pop('Consumo_energía_primaria')
        #first_column = first_column.str.replace(",", ".").astype(float,errors='ignore')
        first_column.replace(to_replace=r',', value='.', regex=True,inplace=True)
        first_column = pd.to_numeric(first_column, errors='coerce')
        df.insert(16, 'Consumo_energía_primaria', first_column)
        df ['Consumo_energía_primaria'] = df ['Consumo_energía_primaria'].fillna('None')
        fallos2 = df.loc[df.loc[:, 'Consumo_energía_primaria'] == 'None']
        df = df.loc[df.loc[:, 'Consumo_energía_primaria'] != 'None']
        fallos10 = df.loc[df.loc[:, 'Consumo_energía_primaria'] < 0.01]
        df = df.loc[df.loc[:, 'Consumo_energía_primaria'] >= 0.01]
        fallos11 = df.loc[df.loc[:, 'Consumo_energía_primaria'] > 629.7]         # La referencia 1 (2020 Gangolells Office representatives for cost-optimal energy retrofitting analysis) eran 1000, el paper 2 usa 629,7 (2018 Las Heras Casas A tool for verifying energy performance certificates a Aragon)
        df = df.loc[df.loc[:, 'Consumo_energía_primaria'] <= 629.7]
        fallos = pd.concat([fallos, fallos2, fallos10, fallos11], axis=0)
    j = df.shape[0]
    k = h-j

    # Errores en Calificación_consumo_energía
    if eliminar_errores_Calificación_consumo_energía == 1:
        fallos3 = df.loc[df.loc[:, 'Calificación_consumo_energía'] == '-']
        df = df.loc[df.loc[:, 'Calificación_consumo_energía'] != '-']
        fallos = pd.concat([fallos, fallos3], axis=0)
    l = df.shape[0]
    m = j-l

    # Errores en Emisiones_CO2
    if eliminar_errores_Emisiones_CO2 == 1:
        first_column = df.pop('Emisiones_CO2')
        # first_column = first_column.str.replace(",", ".").astype(float,errors='ignore')
        first_column.replace(to_replace=r',', value='.', regex=True,inplace=True)
        first_column = pd.to_numeric(first_column, errors='coerce')
        df.insert(18, 'Emisiones_CO2', first_column)
        df ['Emisiones_CO2'] = df ['Emisiones_CO2']. fillna('None')
        fallos2 = df.loc[df.loc[:, 'Emisiones_CO2'] == 'None']
        df = df.loc[df.loc[:, 'Emisiones_CO2'] != 'None']
        fallos10 = df.loc[df.loc[:, 'Emisiones_CO2'] < 0.01]
        df = df.loc[df.loc[:, 'Emisiones_CO2'] >= 0.01]
        fallos11 = df.loc[df.loc[:, 'Emisiones_CO2'] > 333.1]                     # La referencia 1 (2020 Gangolells Office representatives for cost-optimal energy retrofitting analysis) usando el peor vector energético eran 529 (1000*peor vector), el paper 2 serían 333.1 (2018 Las Heras Casas A tool for verifying energy performance certificates a Aragon)
        df = df.loc[df.loc[:, 'Emisiones_CO2'] <= 333.1]
        fallos = pd.concat([fallos, fallos2, fallos10, fallos11], axis=0)
    n = df.shape[0]
    o = l-n

    # Errores en Calificación_emisiones
    if eliminar_errores_Calificación_emisiones == 1:
        fallos3 = df.loc[df.loc[:, 'Calificación_emisiones'] == '-']
        df = df.loc[df.loc[:, 'Calificación_emisiones'] != '-']
        fallos = pd.concat([fallos, fallos3], axis=0)
    p = df.shape[0]
    q = n-p

    # Generación de los informes de errores y certificados descartados
    #df = df.drop(df.columns[[0]], axis='columns') # Quito el índice de los certificados que sale repetido
    #fallos = fallos.drop(df.columns[[0]], axis='columns') # Quito el índice de los certificados que sale repetido
    errores = pd.DataFrame({'Comunidad autónoma':[ccaa], 'Total de certificados':[a], 'Total de certificados correctos':[p], 'Total de certificados borrados':[c+e+g+i+k+m+o+q],
                'Certificados borrados por errores en ReferenciaCatastral':[c],'Certificados borrados por errores en CP':[e],'Certificados borrados por errores en FechaConstrucción':[g],'Certificados borrados por errores en SuperficieUtil':[i],
                'Certificados borrados por errores en Consumo_energía_primaria':[k], 'Certificados borrados por errores en Calificación_consumo_energía':[m],
                 'Certificados borrados por errores en Emisiones_CO2':[o], 'Certificados borrados por errores en Calificación_emisiones':[q], 'Porcentaje EPC correctos':[p*100/(a)], 'Porcentaje EPC con errores':[(c+e+g+i+k+m+o+q)*100/(a)]})
    print ('Se han borrado: ', c+e+g+i+k+m+o+q, 'certificados energéticos')
    return df, errores, fallos
