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
        df.PROV.replace ({"A CORUÃA":"A CORUÑA"}, inplace=True)
        df.insert(4, 'CMUN', "") 
        third_column = df.pop('municipio')
        df.insert(5, 'Municipio', third_column) 
        df.Municipio.replace ({"A CORUÃA":"A CORUÑA"}, inplace=True)
        df.insert(6, 'Coordenadas_latitud', "") 
        df.insert(7, 'Coordenadas_longitud', "") 
        df.insert(8, 'ZonaClimatica', "") 
        fifth_column = df.pop('numeroRegistro')
        df.insert(9, 'NumeroCertificado', fifth_column) 
        sixth_column = df.pop('descViv')
        df.insert(10, 'TipoEdificio', sixth_column) 
        df.TipoEdificio.replace ({"VIVENDA UNIFAMILIAR":"Residencial - Vivienda unifamiliar", "VIVENDA UNIFAMILIAR ":"Residencial - Vivienda unifamiliar", "VIVENDA UNIFAMILIAR )":"Residencial - Vivienda unifamiliar", "VIVENDA INDIVIDUAL DENTRO DUN BLOQUE":"Residencial - Vivienda individual", "VIVENDA INDIVIDUAL DENTRO DUN BLOQUE ":"Residencial - Vivienda individual", "VIVENDA INDIVIDUAL DENTRO DUN BLOQUE )":"Residencial - Vivienda individual", "EDIFICIO DE VIVENDAS EN BLOQUE":"Residencial - Bloque completo", "EDIFICIO DE VIVENDAS EN BLOQUE ":"Residencial - Bloque completo", "EDIFICIO DE VIVENDAS EN BLOQUE )":"Residencial - Bloque completo", "TERCIARIO-LOCAL":"Terciario - Local", "TERCIARIO-LOCAL ":"Terciario - Local", "TERCIARIO-LOCAL )":"Terciario - Local", "TERCIARIO-EDIFICIO COMPLETO":"Terciario - Edificio completo", "TERCIARIO-EDIFICIO COMPLETO ":"Terciario - Edificio completo", "TERCIARIO-EDIFICIO COMPLETO )":"Terciario - Edificio completo"}, inplace=True)
        seventh_column = df.pop('tipoCEE')
        df.insert(11, 'Edificio_existente_o_nuevo', seventh_column) 
        df.insert(12, 'FechaConstrucción', "") 
        df.insert(13, 'SuperficieUtil', '') 
        tenth_column = df.pop('enderezo')
        df.insert(14, 'Direccion', tenth_column) 
        eleventh_column = df.pop('consumo')
        df.insert(15, 'Consumo_energía_primaria', eleventh_column) # Consumo_energía_primaria (kWh/m2año)
        eleventh_column = df.pop('letraConsumo')
        df.insert(16, 'Calificación_consumo_energía', eleventh_column) 
        eleventh_column = df.pop('emisions')
        df.insert(17, 'Emisiones_CO2', eleventh_column) # Emisiones CO2 (kgCO2/m2año)
        eleventh_column = df.pop('letraEmisions')
        df.insert(18, 'Calificación_emisiones', eleventh_column) 
        df.insert(19, 'Emisiones_calefacción', "") 
        df.insert(20, 'Calificación_emisiones_calefacción', "") 
        df.insert(21, 'Consumo_calefacción', "") 
        df.insert(22, 'Calificación_consumo_calefacción', "") 
        df.insert(23, 'Emisiones_refrigeración', "") 
        df.insert(24, 'Calificación_emisiones_refrigeración', "") 
        df.insert(25, 'Consumo_refrigeración', "") 
        df.insert(26, 'Calificación_consumo_refrigeración', "") 
        df.insert(27, 'Emisiones_ACS', "") 
        df.insert(28, 'Calificación_emisiones_ACS', "") 
        df.insert(29, 'Consumo_ACS', "") 
        df.insert(30, 'Calificación_consumo_ACS', "") 
        df.insert(31, 'Emisiones_iluminación', "") 
        df.insert(32, 'Calificación_emisiones_iluminación', "") 
        df.insert(33, 'Consumo_iluminación', "") 
        df.insert(34, 'Calificación_consumo_iluminación', "") 
        eleventh_column = df.pop('normativa')
        df.insert(35, 'Normativa_edificación', eleventh_column) 
        df.insert(36, 'Normativa_instalaciones', "") 
        df.insert(37, 'Programa_informático', "") 
        eleventh_column = df.pop('anoSolicitude')
        df.insert(38, 'Fecha_registro', eleventh_column) 
        df.insert(39, 'Dispone_de_solar_térmica',"") 
        df.insert(40, 'Dispone_de_solar_fotovoltaica', "") 
        df.insert(41, 'Dispone_de_geotérmica', "") 
        df.insert(42, 'Dispone_de_biomasa', "") 
        df.insert(43, 'Generador_instalación', "") 
        df.insert(44, 'Tipo_de_generador', "") 
        df.insert(45, 'Vector_energético', "") 
        df.insert(46, 'C_CCAA', 12) 
        df.insert(47, 'CPROV', df.PROV) 
        df.CPROV.replace({"A CORUÑA": 15, "LUGO": 27, "OURENSE": 32, "PONTEVEDRA": 36}, inplace=True)
        print (df.shape [0])

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
        df['fechaCaducidade'] = pd.to_datetime(df['fechaCaducidade'].str.strip(), dayfirst=True, errors = 'coerce')
        df.sort_values(by='fechaCaducidade',ascending=False, inplace=True)
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
