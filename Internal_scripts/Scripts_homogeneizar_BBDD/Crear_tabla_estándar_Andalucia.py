 # Andalucía
 # Nota: La información base es un xml, en otro script se convierte a xlsx y este script contiene la homogeneización de las tablas como en todos los casos

import pandas as pd
import numpy as np

def AndaluciaDB(df, archivo_xml):
        first_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/IdentificacionEdificio/ReferenciaCatastral')
        df.insert(0, 'ReferenciaCatastral', first_column)
        second_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/IdentificacionEdificio/CodigoPostal')
        df.insert(1, 'CP', second_column) 
        df.insert(2, 'CCAA', "Andalucía")
        df.insert(3, 'PROV', "") 
        df.insert(4, 'CMUN', "")
        second_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/IdentificacionEdificio/Municipio') 
        df.insert(5, 'Municipio', second_column) 
        df.insert(6, 'Coordenadas_latitud', "") 
        df.insert(7, 'Coordenadas_longitud', "") 
        second_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/IdentificacionEdificio/ZonaClimatica') 
        df.insert(8, 'ZonaClimatica', second_column) 
        df.insert(9, 'NumeroCertificado', "") 
        sixth_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/IdentificacionEdificio/TipoDeEdificio')
        df.insert(10, 'TipoEdificio', sixth_column) 
        df.TipoEdificio.replace ({"ViviendaUnifamiliar":"Residencial - Vivienda unifamiliar", "ViviendaIndividualEnBloque":"Residencial - Vivienda individual", "BloqueDeViviendaCompleto":"Residencial - Bloque completo", "LocalUsoTerciario":"Terciario - Local", "EdificioUsoTerciario":"Terciario - Edificio completo"}, inplace=True)
        seventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/IdentificacionEdificio/AlcanceInformacionXML')
        df.insert(11, 'Edificio_existente_o_nuevo', seventh_column) 
        seventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/IdentificacionEdificio/AnoConstruccion')
        df.insert(12, 'FechaConstrucción', seventh_column) 
        seventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/DatosGeneralesyGeometria/SuperficieHabitable')
        df.insert(13, 'SuperficieUtil', seventh_column) 
        tenth_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/IdentificacionEdificio/Direccion')
        df.insert(14, 'Direccion', tenth_column) 
        tenth_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Consumo/EnergiaPrimariaNoRenovable/Global')
        df.insert(15, 'Consumo_energía_primaria', tenth_column) # Consumo_energía_primaria (kWh/m2año) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Calificacion/EnergiaPrimariaNoRenovable/Global')
        df.insert(16, 'Calificación_consumo_energía', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/EmisionesCO2/Global')
        df.insert(17, 'Emisiones_CO2', eleventh_column) # Emisiones CO2 (kgCO2/m2año)
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Calificacion/EmisionesCO2/Global')
        df.insert(18, 'Calificación_emisiones',  eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/EmisionesCO2/Calefaccion')
        df.insert(19, 'Emisiones_calefacción', eleventh_column)
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Calificacion/EmisionesCO2/Calefaccion')
        df.insert(20, 'Calificación_emisiones_calefacción', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Consumo/EnergiaPrimariaNoRenovable/Calefaccion')
        df.insert(21, 'Consumo_calefacción', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Calificacion/EnergiaPrimariaNoRenovable/Calefaccion')
        df.insert(22, 'Calificación_consumo_calefacción', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/EmisionesCO2/Refrigeracion')
        df.insert(23, 'Emisiones_refrigeración', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Calificacion/EmisionesCO2/Refrigeracion')
        df.insert(24, 'Calificación_emisiones_refrigeración', eleventh_column)
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Consumo/EnergiaPrimariaNoRenovable/Refrigeracion') 
        df.insert(25, 'Consumo_refrigeración', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Calificacion/EnergiaPrimariaNoRenovable/Refrigeracion')
        df.insert(26, 'Calificación_consumo_refrigeración', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/EmisionesCO2/ACS')
        df.insert(27, 'Emisiones_ACS', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Calificacion/EmisionesCO2/ACS')
        df.insert(28, 'Calificación_emisiones_ACS', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Consumo/EnergiaPrimariaNoRenovable/CS')
        df.insert(29, 'Consumo_ACS', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Calificacion/EnergiaPrimariaNoRenovable/ACS')
        df.insert(30, 'Calificación_consumo_ACS', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/EmisionesCO2/Iluminacion')
        df.insert(31, 'Emisiones_iluminación', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Calificacion/EmisionesCO2/Iluminacion')
        df.insert(32, 'Calificación_emisiones_iluminación', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Consumo/EnergiaPrimariaNoRenovable/Iluminacion')
        df.insert(33, 'Consumo_iluminación', eleventh_column) 
        eleventh_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/Calificacion/EnergiaPrimariaNoRenovable/Iluminacion')
        df.insert(34, 'Calificación_consumo_iluminación', eleventh_column) 
        sixth_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/IdentificacionEdificio/NormativaVigente')
        df.insert(35, 'Normativa_edificación', sixth_column) 
        df.insert(36, 'Normativa_instalaciones', "") 
        sixth_column = df.pop('DatosEnergeticos/DatosEnergeticosDelEdificio/IdentificacionEdificio/Procedimiento')
        df.insert(37, 'Programa_informático', sixth_column) 
        df.insert(38, 'Fecha_registro', df ['DatosEnergeticos/DatosEnergeticosDelEdificio/DatosDelCertificador/Fecha'].str[-4:])
        df.insert(39, 'Dispone_de_solar_térmica',"") 
        df.insert(40, 'Dispone_de_solar_fotovoltaica', "") 
        df.insert(41, 'Dispone_de_geotérmica', "") 
        df.insert(42, 'Dispone_de_biomasa', "") 
        df.insert(43, 'Generador_instalación', "") 
        df.insert(44, 'Tipo_de_generador', "") 
        df.insert(45, 'Vector_energético', "") 
        df.insert(46, 'C_CCAA', 1) 
        sepcol = archivo_xml.split('\\')            # Para dar la provincia como para andalucía es el mismo script saco qué provincia es por el nombre del archivo de entrada, le quito la ruta y me quedo con el nombre para ver qué provincia es cada caso
        nombre = sepcol[-1]
        if nombre == 'ALMERIA.xml':
                df.insert(46, 'CPROV', 4) 
                second_column = df.pop('PROV')
                df.insert(3, 'PROV', 'Almería') 
        elif nombre == 'CADIZ.xml':
                df.insert(46, 'CPROV', 11) 
                second_column = df.pop('PROV')
                df.insert(3, 'PROV', 'Cádiz') 
        elif nombre == 'CORDOBA.xml':
                df.insert(46, 'CPROV', 14) 
                second_column = df.pop('PROV')
                df.insert(3, 'PROV', 'Córdoba') 
        elif nombre == 'GRANADA.xml':
                df.insert(46, 'CPROV', 18) 
                second_column = df.pop('PROV')
                df.insert(3, 'PROV', 'Granada') 
        elif nombre == 'HUELVA.xml':
                df.insert(46, 'CPROV', 21) 
                second_column = df.pop('PROV')
                df.insert(3, 'PROV', 'Huelva') 
        elif nombre == 'JAEN.xml':
                df.insert(46, 'CPROV', 23) 
                second_column = df.pop('PROV')
                df.insert(3, 'PROV', 'Jaén') 
        elif nombre == 'MALAGA.xml':
                df.insert(46, 'CPROV', 29) 
                second_column = df.pop('PROV')
                df.insert(3, 'PROV', 'Malaga') 
        elif nombre == 'SEVILLA.xml':
                df.insert(46, 'CPROV', 41) 
                second_column = df.pop('PROV')
                df.insert(3, 'PROV', 'Sevilla') 

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
        df['DatosEnergeticos/DatosEnergeticosDelEdificio/DatosDelCertificador/Fecha'] = pd.to_datetime(df['DatosEnergeticos/DatosEnergeticosDelEdificio/DatosDelCertificador/Fecha'].str.strip(), dayfirst=True, errors = 'coerce')
        df.sort_values(by='DatosEnergeticos/DatosEnergeticosDelEdificio/DatosDelCertificador/Fecha',ascending=False, inplace=True)
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