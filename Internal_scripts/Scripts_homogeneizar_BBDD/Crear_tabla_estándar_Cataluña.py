 # Cataluña

def CataluñaDB(archivo):
        import pandas as pd
        import numpy as np
        import xlrd 
        df = (pd.read_csv(archivo, skiprows=0, sep= ';')
                .dropna(how='all', axis=1))
        first_column = df.pop('REFERENCIA CADASTRAL').str.strip()
        second_column = df.pop('CODI_POSTAL')
        df.insert(0, 'ReferenciaCatastral', first_column)
        df.insert(1, 'CP', second_column) 
        df.insert(2, 'CCAA', "Cataluña") 
        second_column = df.pop('NOM_PROVINCIA')
        df.insert(3, 'PROV', second_column)
        second_column = df.pop('CODI_POBLACIO') 
        df.insert(4, 'CMUN', second_column) 
        third_column = df.pop('POBLACIO')
        df.insert(5, 'Municipio', third_column) 
        third_column = df.pop('UTM_X')
        df.insert(6, 'Coordenadas_latitud', third_column) 
        third_column = df.pop('UTM_Y')
        df.insert(7, 'Coordenadas_longitud', third_column) 
        fourth_column = df.pop('ZONA CLIMATICA')
        df.insert(8, 'ZonaClimatica', fourth_column) 
        fifth_column = df.pop('NUM_CAS')
        df.insert(9, 'NumeroCertificado', fifth_column) 
        sixth_column = df.pop('US_EDIFICI')
        df.insert(10, 'TipoEdificio', sixth_column) 
        df.TipoEdificio.replace ({"Vivienda unifamiliar":"Residencial - Vivienda unifamiliar", "Habitatge unifamiliar":"Residencial - Vivienda unifamiliar", "Vivienda individual en bloque de viviendas":"Residencial - Vivienda individual", "Habitatge individual en bloc d'habitatges":"Residencial - Vivienda individual", "Habitatge individual":"Residencial - Vivienda individual", "Bloc d'habitatges":"Residencial - Bloque completo", "Bloc d'habitatges plurifamiliar":"Residencial - Bloque completo", "Bloque de viviendas":"Residencial - Bloque completo", "Bloque de viviendas plurifamiliar":"Residencial - Bloque completo", "Local":"Terciario - Local", "Terciari":"Terciario - Edificio completo", "Terciario":"Terciario - Edificio completo"}, inplace=True)
        seventh_column = df.pop('Tipus Tramit')
        df.insert(11, 'Edificio_existente_o_nuevo', seventh_column) 
        eighth_column = df.pop('ANY_CONSTRUCCIO')
        df.insert(12, 'FechaConstrucción', eighth_column) 
        nineth_column = df.pop('METRES_CADASTRE')
        df.insert(13, 'SuperficieUtil', nineth_column) 
        tenth_column = df.pop('ADREÇA')
        df.insert(14, 'Direccion', tenth_column) 
        eleventh_column = df.pop('Energia primària no renovable')
        df.insert(15, 'Consumo_energía_primaria', eleventh_column) # Consumo_energía_primaria (kWh/m2año)
        eleventh_column = df.pop("Qualificació de consum d'energia primaria no renovable")
        df.insert(16, 'Calificación_consumo_energía', eleventh_column) 
        eleventh_column = df.pop('Emissions de CO2')
        df.insert(17, 'Emisiones_CO2', eleventh_column) # Emisiones CO2 (kgCO2/m2año)
        eleventh_column = df.pop("Qualificacio d'emissions de CO2")
        df.insert(18, 'Calificación_emisiones', eleventh_column) 
        eleventh_column = df.pop('Emissions calefacció')
        df.insert(19, 'Emisiones_calefacción', eleventh_column) 
        eleventh_column = df.pop('Qualificació emissions calefacció')
        df.insert(20, 'Calificación_emisiones_calefacción', eleventh_column) 
        eleventh_column = df.pop('Energia calefacció demanda')
        df.insert(21, 'Consumo_calefacción', eleventh_column) 
        eleventh_column = df.pop('Qualificació energia calefacció demanda')
        df.insert(22, 'Calificación_consumo_calefacción', eleventh_column) 
        eleventh_column = df.pop('Emissions refrigeració')
        df.insert(23, 'Emisiones_refrigeración', eleventh_column) 
        eleventh_column = df.pop('Qualificació emissions refrigeració')
        df.insert(24, 'Calificación_emisiones_refrigeración', eleventh_column) 
        eleventh_column = df.pop('Energia refrigeració demanda')
        df.insert(25, 'Consumo_refrigeración', eleventh_column) 
        eleventh_column = df.pop('Qualificació energia refrigeració demanda')
        df.insert(26, 'Calificación_consumo_refrigeración', eleventh_column) 
        eleventh_column = df.pop('Emissions ACS')
        df.insert(27, 'Emisiones_ACS', eleventh_column) 
        eleventh_column = df.pop('Qualificació emissions ACS')
        df.insert(28, 'Calificación_emisiones_ACS', eleventh_column) 
        eleventh_column = df.pop('Energia ACS')
        df.insert(29, 'Consumo_ACS', eleventh_column) 
        eleventh_column = df.pop('Qualificació energia ACS')
        df.insert(30, 'Calificación_consumo_ACS', eleventh_column) 
        eleventh_column = df.pop('Emissions enllumenament')
        df.insert(31, 'Emisiones_iluminación', eleventh_column) 
        eleventh_column = df.pop('Qualificació emissions enllumenament')
        df.insert(32, 'Calificación_emisiones_iluminación', eleventh_column) 
        eleventh_column = df.pop('Energia enllumenament')
        df.insert(33, 'Consumo_iluminación', eleventh_column) 
        eleventh_column = df.pop('Qualificació energia enllumenament')
        df.insert(34, 'Calificación_consumo_iluminación', eleventh_column) 
        eleventh_column = df.pop('Normativa construcció')
        df.insert(35, 'Normativa_edificación', eleventh_column) 
        df.insert(36, 'Normativa_instalaciones', "") 
        eleventh_column = df.pop('Eina de certificacio')
        df.insert(37, 'Programa_informático', eleventh_column) 
        df.insert(38, 'Fecha_registro', df ['DATA_ENTRADA'].str[-4:])
        eleventh_column = df.pop('SOLAR TERMICA')
        df.insert(39, 'Dispone_de_solar_térmica', eleventh_column) 
        eleventh_column = df.pop('SOLAR FOTOVOLTAICA')
        df.insert(40, 'Dispone_de_solar_fotovoltaica', eleventh_column) 
        eleventh_column = df.pop('ENERGIA GEOTERMICA')
        df.insert(41, 'Dispone_de_geotérmica', eleventh_column) 
        eleventh_column = df.pop('SISTEMA BIOMASSA')
        df.insert(42, 'Dispone_de_biomasa', eleventh_column) 
        df.insert(43, 'Generador_instalación', "") 
        df.insert(44, 'Tipo_de_generador', "") 
        df.insert(45, 'Vector_energético', "") 
        df.insert(46, 'C_CCAA', 9) 
        df.insert(47, 'CPROV', df.PROV) 
        df.CPROV.replace({"BARCELONA": 8, "Barcelona": 8, "GIRONA": 17, "Girona": 17, "LLEIDA": 25, "Lleida": 25, "TARRAGONA": 43, "Tarragona": 43}, inplace=True)

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
        df.DATA_ENTRADA = pd.to_datetime(df.DATA_ENTRADA.str.strip(), dayfirst=True)
        df.sort_values(by='DATA_ENTRADA',ascending=False, inplace=True)
        df = (df.groupby(['ReferenciaCatastral']).agg(
                          #      ReferenciaCatastral = ('ReferenciaCatastral', 'first'), \
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

