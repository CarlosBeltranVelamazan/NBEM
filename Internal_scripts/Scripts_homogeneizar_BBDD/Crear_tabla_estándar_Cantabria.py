 # Cantabria, el C.P. y el municpio están en la dirección, el script los separa, algunos datos pueden salir erróneos si les falta el código postal o no está bien. Hasta ahora ningún dato correcto se pierde en el proceso, unicamente los datos ya erróneos obtienen salidas erróneas.

def CantabriaDB(archivo):
        import pandas as pd
        import numpy as np
        import xlrd 
        df = (pd.read_excel(archivo, skiprows=0)
                .dropna(how='all', axis=1))
        first_column = df.pop('REFERENCIA CATASTRAL').str.strip()
        df.insert(0, 'ReferenciaCatastral', first_column)
        sepcol = df["ED. MUNICIPIO"].str.split(' - ', expand=True)
        sepcol.columns = ['CMUN', 'municip']
        df.insert(1, 'CP', "")
        df.insert(2, 'CCAA', "Cantabria")
        df.insert(3, 'PROV', "Cantabria") 
        df.insert(4, 'CMUN', sepcol['CMUN']) 
        # eleventh_column = sepcol['municip']
        df.insert(5, 'Municipio', sepcol['municip'])
        df.insert(6, 'Coordenadas_latitud', "") 
        df.insert(7, 'Coordenadas_longitud', "") 
        df.insert(8, 'ZonaClimatica', "") 
        fifth_column = df.pop('CERTIFICADO')
        df.insert(9, 'NumeroCertificado', fifth_column) 
        fifth_column = df.pop('USO EDIFICIO')
        df.insert(10, 'TipoEdificio', fifth_column)
        fifth_column = df.pop('TIPO CERTIFICADO')
        df.insert(11, 'Edificio_existente_o_nuevo', fifth_column) 
        df.insert(12, 'FechaConstrucción', "") 
        df.insert(13, 'SuperficieUtil', "") 
        tenth_column = df.pop('ED. VÍA')
        df.insert(14, 'Direccion', tenth_column) 
        eleventh_column = df.pop('kWh/m2*año')
        df.insert(15, 'Consumo_energía_primaria', eleventh_column) # Consumo_energía_primaria (kWh/m2año)
        eleventh_column = df.pop('CALIF. CONSUMO')
        df.insert(16, 'Calificación_consumo_energía', eleventh_column) 
        df.Calificación_consumo_energía.replace ({"A - Calificación A":"A", "B - Calificación B":"B", "C - Calificación C":"C", "D - Calificación D":"D", "E - Calificación E":"E", "F - Calificación F":"F", "G - Calificación G":"G", "N/D":""}, inplace=True)
        eleventh_column = df.pop('kgCO2/m2*año')
        df.insert(17, 'Emisiones_CO2', eleventh_column) # Emisiones CO2 (kgCO2/m2año)
        eleventh_column = df.pop('CALIF.EMI.GLOBALES')
        df.insert(18, 'Calificación_emisiones',  eleventh_column) 
        df.Calificación_emisiones.replace ({"A - Calificación A":"A", "B - Calificación B":"B", "C - Calificación C":"C", "D - Calificación D":"D", "E - Calificación E":"E", "F - Calificación F":"F", "G - Calificación G":"G", "N/D":""}, inplace=True)
        df.insert(19, 'Emisiones_calefacción', "") 
        eleventh_column = df.pop('CALIF.CALEFACCIÓN')
        df.insert(20, 'Calificación_emisiones_calefacción', eleventh_column)
        df.Calificación_emisiones_calefacción.replace ({"A - Calificación A":"A", "B - Calificación B":"B", "C - Calificación C":"C", "D - Calificación D":"D", "E - Calificación E":"E", "F - Calificación F":"F", "G - Calificación G":"G", "N/D":""}, inplace=True)
        df.insert(21, 'Consumo_calefacción', "") 
        df.insert(22, 'Calificación_consumo_calefacción', "") 
        df.insert(23, 'Emisiones_refrigeración', "") 
        eleventh_column = df.pop('CALIF.REFRIGERACIÓN')
        df.insert(24, 'Calificación_emisiones_refrigeración', eleventh_column) 
        df.Calificación_emisiones_refrigeración.replace ({"A - Calificación A":"A", "B - Calificación B":"B", "C - Calificación C":"C", "D - Calificación D":"D", "E - Calificación E":"E", "F - Calificación F":"F", "G - Calificación G":"G", "N/D":""}, inplace=True)
        df.insert(25, 'Consumo_refrigeración', "") 
        df.insert(26, 'Calificación_consumo_refrigeración', "") 
        df.insert(27, 'Emisiones_ACS', "") 
        eleventh_column = df.pop('CALIF.ACS')
        df.insert(28, 'Calificación_emisiones_ACS', eleventh_column)
        df.Calificación_emisiones_ACS.replace ({"A - Calificación A":"A", "B - Calificación B":"B", "C - Calificación C":"C", "D - Calificación D":"D", "E - Calificación E":"E", "F - Calificación F":"F", "G - Calificación G":"G", "N/D":""}, inplace=True)
        df.insert(29, 'Consumo_ACS', "") 
        df.insert(30, 'Calificación_consumo_ACS', "") 
        df.insert(31, 'Emisiones_iluminación', "") 
        eleventh_column = df.pop('CALIF.ILUMINACIÓN')
        df.insert(32, 'Calificación_emisiones_iluminación', eleventh_column) 
        df.Calificación_emisiones_iluminación.replace ({"A - Calificación A":"A", "B - Calificación B":"B", "C - Calificación C":"C", "D - Calificación D":"D", "E - Calificación E":"E", "F - Calificación F":"F", "G - Calificación G":"G", "N/D":""}, inplace=True)
        df.insert(33, 'Consumo_iluminación', "") 
        df.insert(34, 'Calificación_consumo_iluminación', "") 
        eleventh_column = df.pop('NORMA CONSTRUCCIÓN')
        df.insert(35, 'Normativa_edificación', eleventh_column) 
        eleventh_column = df.pop('NORMA ENERGÉTICA')
        df.insert(36, 'Normativa_instalaciones', eleventh_column) 
        eleventh_column = df.pop('DOC. RECONOCIDO')
        df.insert(37, 'Programa_informático', eleventh_column) 
        df['VIGENCIA DESDE'] = df['VIGENCIA DESDE'].astype(str)
        df.insert(38, 'Fecha_registro', df ['VIGENCIA DESDE'].str[:4])
        df.insert(39, 'Dispone_de_solar_térmica',"") 
        df.insert(40, 'Dispone_de_solar_fotovoltaica', "") 
        df.insert(41, 'Dispone_de_geotérmica', "") 
        df.insert(42, 'Dispone_de_biomasa', "") 
        df.insert(43, 'Generador_instalación', "") 
        df.insert(44, 'Tipo_de_generador', "") 
        df.insert(45, 'Vector_energético', "") 
        df.insert(46, 'C_CCAA', 6) 
        df.insert(47, 'CPROV', 39) 

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
        df['VIGENCIA DESDE'] = pd.to_datetime(df['VIGENCIA DESDE'].str.strip(), dayfirst=True)
        df.sort_values(by='VIGENCIA DESDE',ascending=False, inplace=True)
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
