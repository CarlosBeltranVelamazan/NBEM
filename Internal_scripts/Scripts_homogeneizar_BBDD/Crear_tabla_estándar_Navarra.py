 # Navarra
def NavarraDB(archivo):
    import pandas as pd
    import numpy as np
    import xlrd 
    try:
        df = (pd.read_excel(archivo, skiprows=0))
    except:
        df = (pd.read_csv(archivo, skiprows=0))
    second_column = df.pop('ReferenciaCatastral').str.strip()
    df.insert(0, 'ReferenciaCatastral', second_column) 
    second_column = df.pop('CP')
    df.insert(1, 'CP', second_column) 
    df.insert(2, 'CCAA', "Navarra") 
    df.insert(3, 'PROV', "Navarra") 
    df.insert(4, 'CMUN', "") 
    third_column = df.pop('Localidad')
    df.insert(5, 'Municipio', third_column) 
    df.insert(6, 'Coordenadas_latitud', "") 
    df.insert(7, 'Coordenadas_longitud', "") 
    third_column = df.pop('Zona')
    df.insert(8, 'ZonaClimatica', third_column) 
    fifth_column = df.pop('CodRegistroComAutonoma')
    df.insert(9, 'NumeroCertificado', fifth_column) 
    df.insert(10, 'TipoEdificio', "") 
    seventh_column = df.pop('Tipo')
    df.insert(11, 'Edificio_existente_o_nuevo', seventh_column) 
    seventh_column = df.pop('AnioConstruccion')
    df.insert(12, 'FechaConstrucción', seventh_column) 
    df.insert(13, 'SuperficieUtil', "") 
    tenth_column = df.pop('Dirección')
    df.insert(14, 'Direccion', tenth_column) 

    sepcol = df["EnergiaPrimNoRenovable"].str.split(';', expand=True)
    sepcol.columns = ['Global', 'Calefacción', 'Refrigeración', 'ACS', 'Iluminación']
    sepcol2 = sepcol['Global'].str.split(': ', expand=True)
    sepcol2.columns = ['Texto', 'ValorEPnorenovable']
    eleventh_column = sepcol2.pop('ValorEPnorenovable')
    df.insert(15, 'Consumo_energía_primaria', eleventh_column) # Consumo_energía_primaria (kWh/m2año)

    eleventh_column = df.pop('CalificacionEnePrinNoRenovGlobal')
    df.insert(16, 'Calificación_consumo_energía', eleventh_column) 

    sepcol5 = df["EmisionesCO2"].str.split(';', expand=True)
    sepcol5.columns = ['Global', 'Calefacción', 'Refrigeración', 'ACS', 'Iluminación', 'Cons.Eléctrico', 'Cons.Otros', 'Tot.Cons.Electrico', 'Tot.Cons.Otros']
    sepcol6 = sepcol5['Global'].str.split(': ', expand=True)
    sepcol6.columns = ['Texto', 'Emisiones']
    eleventh_column = sepcol6.pop('Emisiones')
    df.insert(17, 'Emisiones_CO2', eleventh_column) # Emisiones CO2 (kgCO2/m2año)

    eleventh_column = df.pop('CalificacionEmiCO2Global')
    df.insert(18, 'Calificación_emisiones', eleventh_column) 

    #df.insert(19, 'Calificación_general_del_edificio', "") 

    sepcol6 = sepcol5['Calefacción'].str.split(':', expand=True)
    sepcol6.columns = ['Texto', 'Emisiones']
    eleventh_column = sepcol6.pop('Emisiones')
    df.insert(19, 'Emisiones_calefacción', eleventh_column) 

    eleventh_column = df.pop('CalificacionEmiCO2Calefaccion')
    df.insert(20, 'Calificación_emisiones_calefacción', eleventh_column) 

    sepcol2 = sepcol['Calefacción'].str.split(':', expand=True)
    sepcol2.columns = ['Texto', 'ValorEPnorenovable']
    eleventh_column = sepcol2.pop('ValorEPnorenovable')
    df.insert(21, 'Consumo_calefacción', eleventh_column) 

    eleventh_column = df.pop('CalificacionEnePrinNoRenovCalefaccion') 
    df.insert(22, 'Calificación_consumo_calefacción', eleventh_column) 

    sepcol6 = sepcol5['Refrigeración'].str.split(':', expand=True)
    sepcol6.columns = ['Texto', 'Emisiones']
    eleventh_column = sepcol6.pop('Emisiones')
    df.insert(23, 'Emisiones_refrigeración', eleventh_column) 

    eleventh_column = df.pop('CalificacionEmiCO2Refrigeracion')
    df.insert(24, 'Calificación_emisiones_refrigeración', eleventh_column) 

    sepcol2 = sepcol['Refrigeración'].str.split(':', expand=True)
    sepcol2.columns = ['Texto', 'ValorEPnorenovable']
    eleventh_column = sepcol2.pop('ValorEPnorenovable')
    df.insert(25, 'Consumo_refrigeración', eleventh_column) 

    eleventh_column = df.pop('CalificacionEnePrinNoRenovRefrigeracion') 
    df.insert(26, 'Calificación_consumo_refrigeración', eleventh_column) 

    sepcol6 = sepcol5['ACS'].str.split(':', expand=True)
    sepcol6.columns = ['Texto', 'Emisiones']
    eleventh_column = sepcol6.pop('Emisiones')
    df.insert(27, 'Emisiones_ACS', eleventh_column) 

    eleventh_column = df.pop('CalificacionEmiCO2ACS')
    df.insert(28, 'Calificación_emisiones_ACS', eleventh_column) 

    sepcol2 = sepcol['ACS'].str.split(':', expand=True)
    sepcol2.columns = ['Texto', 'ValorEPnorenovable']
    eleventh_column = sepcol2.pop('ValorEPnorenovable')
    df.insert(29, 'Consumo_ACS', eleventh_column) 

    eleventh_column = df.pop('CalificacionEnePrinNoRenovACS') 
    df.insert(30, 'Calificación_consumo_ACS', eleventh_column) 

    sepcol6 = sepcol5['Iluminación'].str.split(':', expand=True)
    sepcol6.columns = ['Texto', 'Emisiones']
    eleventh_column = sepcol6.pop('Emisiones')
    df.insert(31, 'Emisiones_iluminación', eleventh_column) 

    eleventh_column = df.pop('CalificacionEmiCO2Iluminacion')
    df.insert(32, 'Calificación_emisiones_iluminación', eleventh_column) 

    sepcol2 = sepcol['Iluminación'].str.split(':', expand=True)
    sepcol2.columns = ['Texto', 'ValorEPnorenovable']
    eleventh_column = sepcol2.pop('ValorEPnorenovable') 
    df.insert(33, 'Consumo_iluminación', eleventh_column) 

    eleventh_column = df.pop('CalificacionEnePrinNoRenovIluminacion')   
    df.insert(34, 'Calificación_consumo_iluminación', eleventh_column) 

    eleventh_column = df.pop('NormativaVigente')
    df.insert(35, 'Normativa_edificación', eleventh_column) 
    df.insert(36, 'Normativa_instalaciones', "") 
    eleventh_column = df.pop('Procedimiento')
    df.insert(37, 'Programa_informático', eleventh_column) 
    df.insert(38, 'Fecha_registro', df ['Fecha'].str[-4:])
    df.insert(39, 'Dispone_de_solar_térmica',"") 
    df.insert(40, 'Dispone_de_solar_fotovoltaica', "") 
    df.insert(41, 'Dispone_de_geotérmica', "") 
    df.insert(42, 'Dispone_de_biomasa', "") 
    eleventh_column = df.pop('GeneradoresCalefaccion')
    df.insert(43, 'Generador_instalación', eleventh_column) 
    df.insert(44, 'Tipo_de_generador', "") 
    df.insert(45, 'Vector_energético', "") 
    df.insert(46, 'C_CCAA', 15) 
    df.insert(47, 'CPROV', 31) 

    # Antes de eliminar los EPC duplicados debo resolver problemas de las referencias catastrales como que tengan espacios, comas, ...
    df.ReferenciaCatastral.replace(to_replace=r',', value='-', regex=True,inplace=True)
    df.ReferenciaCatastral.replace(to_replace=r';', value='-', regex=True,inplace=True)
    df.ReferenciaCatastral.replace(to_replace=r' ', value='', regex=True,inplace=True)

    # De paso me evito problemas con las comas en la direción
    df.Direccion.replace(to_replace=r',', value='-', regex=True,inplace=True)
    df.Direccion.replace(to_replace=r';', value='-', regex=True,inplace=True)

    # En cuanto a las referencias catastrales sucede que a veces ponen varias seguidas de comas, para salvar al menos la primera me quedo con los primeros 18 caracteres sobre los que haremos la unión más adelante (por 14 caracteres - parcela (edificio) y por 18 caracteres (bien inmueble 18 + 2 caracteres de control))
    # Nota importante: El criterio para separar es este, edificios son 14 dígitos, los separo. Bienes inmuebles son 20 dígitos siempre (en realidad 18 + 2 letras de control), sin embargo hay casos que certifican varias viviendas para salvar el certificado en BI dejo todos y las referencias las corto a 20 dígitos. De esta manera el certificado se unirá con esa vivienda (al menos el certificado sigue siendo válido, se podría crear un certificado para cada BI pero hay mucha casuística de errores y saldrían más certificados finales que iniciales y eso es raro)
    # Corto por los 18 caracteres para unirlo con el catastro alfanumérico. Con este criterio empleado no hay un filtrado de errores de referencias catastrales, el filtrado se hace al unirlo con el catastro alfanumérico, si no se une es una referencia catastral incorrecta.
    df.ReferenciaCatastral = df['ReferenciaCatastral'].str[:18]     # Ver nota importante

    # Elimino los certificados duplicados quedandome con el más reciente
    EPC_antes_de_duplicados = df.shape[0]
    df['Fecha'] = pd.to_datetime(df['Fecha'].str.strip(), dayfirst=True, errors = 'coerce')
    df.sort_values(by='Fecha',ascending=False, inplace=True)
    df = (df.groupby(['ReferenciaCatastral']).agg(
                #         ReferenciaCatastral = ('ReferenciaCatastral', 'first'), \
                        CP = ('CP', 'first'), \
                        CCAA = ('CCAA', 'first'), \
                        PROV = ('PROV', 'first'), \
                        CMUN = ('CMUN', 'first'), \
                        Municipio = ('Municipio', 'first'), \
                        Coordenadas_latitud = ('Coordenadas_latitud', 'first'), \
                        Coordenadas_longitud = ('Coordenadas_longitud', 'first'), \
                        ZonaClimatica = ('ZonaClimatica', 'first'), \
                        NumeroCertificado = ('NumeroCertificado', 'first'), \
                        TipoEdificio = ('TipoEdificio', 'first'), \
                        Edificio_existente_o_nuevo = ('Edificio_existente_o_nuevo', 'first'), \
                        FechaConstrucción = ('FechaConstrucción', 'first'), \
                        SuperficieUtil = ('SuperficieUtil', 'first'), \
                        Direccion = ('Direccion', 'first'), \
                        Consumo_energía_primaria = ('Consumo_energía_primaria', 'first'), \
                        Calificación_consumo_energía = ('Calificación_consumo_energía', 'first'), \
                        Emisiones_CO2 = ('Emisiones_CO2', 'first'), \
                        Calificación_emisiones = ('Calificación_emisiones', 'first'), \
                        Emisiones_calefacción = ('Emisiones_calefacción', 'first'), \
                        Calificación_emisiones_calefacción = ('Calificación_emisiones_calefacción', 'first'), \
                        Consumo_calefacción = ('Consumo_calefacción', 'first'), \
                        Calificación_consumo_calefacción = ('Calificación_consumo_calefacción', 'first'), \
                        Emisiones_refrigeración = ('Emisiones_refrigeración', 'first'), \
                        Calificación_emisiones_refrigeración = ('Calificación_emisiones_refrigeración', 'first'), \
                        Consumo_refrigeración = ('Consumo_refrigeración', 'first'), \
                        Calificación_consumo_refrigeración = ('Calificación_consumo_refrigeración', 'first'), \
                        Emisiones_ACS = ('Emisiones_ACS', 'first'), \
                        Calificación_emisiones_ACS = ('Calificación_emisiones_ACS', 'first'), \
                        Consumo_ACS = ('Consumo_ACS', 'first'), \
                        Calificación_consumo_ACS = ('Calificación_consumo_ACS', 'first'), \
                        Emisiones_iluminación = ('Emisiones_iluminación', 'first'), \
                        Calificación_emisiones_iluminación = ('Calificación_emisiones_iluminación', 'first'), \
                        Consumo_iluminación = ('Consumo_iluminación', 'first'), \
                        Calificación_consumo_iluminación = ('Calificación_consumo_iluminación', 'first'), \
                        Normativa_edificación = ('Normativa_edificación', 'first'), \
                        Normativa_instalaciones = ('Normativa_instalaciones', 'first'), \
                        Programa_informático = ('Programa_informático', 'first'), \
                        Fecha_registro = ('Fecha_registro', 'first'), \
                        Dispone_de_solar_térmica = ('Dispone_de_solar_térmica', 'first'), \
                        Dispone_de_solar_fotovoltaica = ('Dispone_de_solar_fotovoltaica', 'first'), \
                        Dispone_de_geotérmica = ('Dispone_de_geotérmica', 'first'), \
                        Dispone_de_biomasa = ('Dispone_de_biomasa', 'first'), \
                        Generador_instalación = ('Generador_instalación', 'first'), \
                        Tipo_de_generador = ('Tipo_de_generador', 'first'), \
                        Vector_energético = ('Vector_energético', 'first'), \
                        C_CCAA = ('C_CCAA', 'first'), \
                        CPROV = ('CPROV', 'first'), \
                        ))

    return df, EPC_antes_de_duplicados
