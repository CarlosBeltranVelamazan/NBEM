 # Andalucía
 # Nota: La información base es un xml y este script contiene la homogeneización de las tablas como en todos los casos, y una solución puntual a un problema al tratar el xml
 # el problema en cuestión se debe al convertirlo en un xlsx para tratarlo de la misma manera que el resto las etiquetas al estar en varios niveles (por ejeplo datos del edificio y como subetiqueta dirección, ref. catastral...)
 # al pasarlo a xlsx toma el nombre de la subetiqueta, esto nos crea un problema en los datos de la calefacción, refrigeración,... ya que la etiqueta es GeneradoresDeCalefaccion por ejemplo y la subetiqueta es Emisiiones de CO2, y es el mismo nombre de subetiquetas para todas las etiquetas de Calef, refrigeración, ACS e iluminación
 # esto cuadruplica los certificados que se crean, en esta tabla los agrupo primero por referencia catastral para volver a unir los datos.
 # Nota2: Lo más óptimo de cara al tiempo consumido es primero juntar por referencia catastral los valores cuadruplicados y luego crear la tabla estándar

import pandas as pd
import numpy as np

def AndaluciaDB(archivo):
        try:
                df = pd.read_excel(archivo, skiprows=0).dropna(how='all', axis=1)
        except:
                df = pd.read_csv(archivo, skiprows=0).dropna(how='all', axis=1)

        first_column = df.pop('ReferenciaCatastral').str.strip()
        df.insert(0, 'ReferenciaCatastral', first_column) 

        # Antes de eliminar los EPC duplicados debo resolver problemas de las referencias catastrales como que tengan espacios, comas, ...
        df.ReferenciaCatastral.replace(to_replace=r',', value='-', regex=True,inplace=True)
        df.ReferenciaCatastral.replace(to_replace=r';', value='-', regex=True,inplace=True)
        df.ReferenciaCatastral.replace(to_replace=r' ', value='', regex=True,inplace=True)

        # En cuanto a las referencias catastrales sucede que a veces ponen varias seguidas de comas, para salvar al menos la primera me quedo con los primeros 18 caracteres sobre los que haremos la unión más adelante (por 14 caracteres - parcela (edificio) y por 18 caracteres (bien inmueble 18 + 2 caracteres de control))
        # Nota importante: El criterio para separar es este, edificios son 14 dígitos, los separo. Bienes inmuebles son 20 dígitos siempre (en realidad 18 + 2 letras de control), sin embargo hay casos que certifican varias viviendas para salvar el certificado en BI dejo todos y las referencias las corto a 20 dígitos. De esta manera el certificado se unirá con esa vivienda (al menos el certificado sigue siendo válido, se podría crear un certificado para cada BI pero hay mucha casuística de errores y saldrían más certificados finales que iniciales y eso es raro)
        # Corto por los 18 caracteres para unirlo con el catastro alfanumérico. Con este criterio empleado no hay un filtrado de errores de referencias catastrales, el filtrado se hace al unirlo con el catastro alfanumérico, si no se une es una referencia catastral incorrecta.
        df.ReferenciaCatastral = df['ReferenciaCatastral'].str[:18]     # Ver nota importante

        # Uno por referencia catastral de las viviendas
        df2 = df.groupby('ReferenciaCatastral') \
                .agg(CP = ('CodigoPostal', 'first'), \
                CCAA = ('ComunidadAutonoma', 'first'), \
                PROV = ('Provincia', 'first'), \
                Municipio = ('Municipio', 'first'), \
                ZonaClimatica = ('ZonaClimatica', 'first'), \
                TipoEdificio = ('TipoDeEdificio', 'first'), \
                Edificio_existente_o_nuevo = ('AlcanceInformacionXML', 'first'), \
                FechaConstrucción = ('AnoConstruccion', 'first'), 
                SuperficieUtil = ('SuperficieHabitable', 'first'), 
                Direccion = ('Direccion', 'first'), 
                Normativa_edificación = ('NormativaVigente', 'first'), 
                Programa_informático = ('Procedimiento', 'first'), 
                Fecha_registro = ('Fecha', 'first'), 
                Compacidad = ('Compacidad', 'first'), 
                PorcentajeSuperficieHabitableCalefactada = ('PorcentajeSuperficieHabitableCalefactada', 'first'), 
                PorcentajeSuperficieHabitableRefrigerada = ('PorcentajeSuperficieHabitableRefrigerada', 'first'), 
                PorcentajeSuperficieAcristaladaNorte = ('N', 'first'), 
                PorcentajeSuperficieAcristaladaNoreste = ('NE', 'first'), 
                PorcentajeSuperficieAcristaladaEste = ('E', 'first'), 
                PorcentajeSuperficieAcristaladaSureste = ('SE', 'first'),
                PorcentajeSuperficieAcristaladaSur = ('S', 'first'),
                PorcentajeSuperficieAcristaladaSuroeste = ('SO', 'first'),
                PorcentajeSuperficieAcristaladaOeste = ('O', 'first'),
                PorcentajeSuperficieAcristaladaNoroeste = ('NO', 'first'),
                DemandaDiariaACS = ('DemandaDiariaACS', 'first'),
                InstalacionesTermicas_GeneradoresDeCalefaccion_Generador_Nombre = ('Nombre', 'first'),
                InstalacionesTermicas_GeneradoresDeCalefaccion_Generador_Tipo = ('Tipo', 'first'),
                InstalacionesTermicas_GeneradoresDeCalefaccion_Generador_PotenciaNominal = ('PotenciaNominal', 'first'),
                InstalacionesTermicas_GeneradoresDeCalefaccion_Generador_RendimientoEstacional = ('RendimientoEstacional', 'first'),
                InstalacionesTermicas_GeneradoresDeCalefaccion_Generador_VectorEnergetico = ('VectorEnergetico', 'first'),
                InstalacionesTermicas_GeneradoresDeCalefaccion_Generador_ModoDeObtencion = ('ModoDeObtencion', 'first'),
                InstalacionesTermicas_GeneradoresDeRefrigeracion_Generador_Nombre = ('Nombre2', 'first'),
                InstalacionesTermicas_GeneradoresDeRefrigeracion_Generador_Tipo = ('Tipo3', 'first'),
                InstalacionesTermicas_GeneradoresDeRefrigeracion_Generador_PotenciaNominal = ('PotenciaNominal4', 'first'),
                InstalacionesTermicas_GeneradoresDeRefrigeracion_Generador_RendimientoEstacional = ('RendimientoEstacional5', 'first'),
                InstalacionesTermicas_GeneradoresDeRefrigeracion_Generador_VectorEnergetico = ('VectorEnergetico6', 'first'),
                InstalacionesTermicas_GeneradoresDeRefrigeracion_Generador_ModoDeObtencion = ('ModoDeObtencion7', 'first'),
                InstalacionesTermicas_InstalacionesACS_Nombre = ('Nombre8', 'first'),
                InstalacionesTermicas_InstalacionesACS_Tipo = ('Tipo9', 'first'),
                InstalacionesTermicas_InstalacionesACS_PotenciaNominal = ('PotenciaNominal10', 'first'),
                InstalacionesTermicas_InstalacionesACS_RendimientoEstacional = ('RendimientoEstacional11', 'first'),
                InstalacionesTermicas_InstalacionesACS_VectorEnergetico = ('VectorEnergetico12', 'first'),
                InstalacionesTermicas_InstalacionesACS_ModoDeObtencion = ('ModoDeObtencion13', 'first'),
                InstalacionesIluminacion_PotenciaTotalInstalada = ('PotenciaTotalInstalada', 'first'),
                EnergiasRenovables_Termica_Nombre = ('Nombre14', 'first'),
                EnergiasRenovables_Termica_ConsumoFinalCalefaccion = ('ConsumoFinalCalefaccion', 'first'),
                EnergiasRenovables_Termica_ConsumoFinalRefrigeracion = ('ConsumoFinalRefrigeracion', 'first'),
                EnergiasRenovables_Termica_ConsumoFinalACS = ('ConsumoFinalACS', 'first'),
                EnergiasRenovables_Termica_DemandaACS = ('DemandaACS', 'first'),
                EnergiasRenovables_Electrica_Nombre = ('Nombre15', 'first'),
                EnergiasRenovables_Electrica_EnergiaGeneradaAutoconsumida = ('EnergiaGeneradaAutoconsumida', 'first'),
                EnergiasRenovables_Electrica_ReduccionGlobalEmisionesCO2 = ('ReduccionGlobalEmisionesCO2', 'first'),
                Demanda_EdificioObjeto_Global = ('Global', 'first'),
                Demanda_EdificioObjeto_Calefaccion = ('Calefaccion', 'first'),
                Demanda_EdificioObjeto_Refrigeracion = ('Refrigeracion', 'first'),
                Demanda_EdificioObjeto_ACS = ('ACS', 'first'),
                Consumo_EnergiaFinalVectores_GasNatural_Global = ('Global16', 'first'),
                Consumo_EnergiaFinalVectores_GasNatural_Calefaccion = ('Calefaccion17', 'first'),
                Consumo_EnergiaFinalVectores_GasNatural_Refrigeracion = ('Refrigeracion18', 'first'),
                Consumo_EnergiaFinalVectores_GasNatural_ACS = ('CS', 'first'),
                Consumo_EnergiaFinalVectores_GasNatural_Iluminacion = ('Iluminacion', 'first'),
                Consumo_EnergiaFinalVectores_GasoleoC_Global = ('Global19', 'first'),
                Consumo_EnergiaFinalVectores_GasoleoC_Calefaccion = ('Calefaccion20', 'first'),
                Consumo_EnergiaFinalVectores_GasoleoC_Refrigeracion = ('Refrigeracion21', 'first'),
                Consumo_EnergiaFinalVectores_GasoleoC_ACS = ('CS22', 'first'),
                Consumo_EnergiaFinalVectores_GasoleoC_Iluminacion = ('Iluminacion23', 'first'),
                Consumo_EnergiaFinalVectores_GLP_Global = ('Global24', 'first'),
                Consumo_EnergiaFinalVectores_GLP_Calefaccion = ('Calefaccion25', 'first'),
                Consumo_EnergiaFinalVectores_GLP_Refrigeracion = ('Refrigeracion26', 'first'),
                Consumo_EnergiaFinalVectores_GLP_ACS = ('CS27', 'first'),
                Consumo_EnergiaFinalVectores_GLP_Iluminacion = ('Iluminacion28', 'first'),
                Consumo_EnergiaFinalVectores_Carbon_Global = ('Global29', 'first'),
                Consumo_EnergiaFinalVectores_Carbon_Calefaccion = ('Calefaccion30', 'first'),
                Consumo_EnergiaFinalVectores_Carbon_Refrigeracion = ('Refrigeracion31', 'first'),
                Consumo_EnergiaFinalVectores_Carbon_ACS = ('CS32', 'first'),
                Consumo_EnergiaFinalVectores_Carbon_Iluminacion = ('Iluminacion33', 'first'),
                Consumo_EnergiaFinalVectores_BiomasaPellet_Global = ('Global34', 'first'),
                Consumo_EnergiaFinalVectores_BiomasaPellet_Calefaccion = ('Calefaccion35', 'first'),
                Consumo_EnergiaFinalVectores_BiomasaPellet_Refrigeracion = ('Refrigeracion36', 'first'),
                Consumo_EnergiaFinalVectores_BiomasaPellet_ACS = ('CS37', 'first'),
                Consumo_EnergiaFinalVectores_BiomasaPellet_Iluminacion = ('Iluminacion38', 'first'),
                Consumo_EnergiaFinalVectores_BiomasaOtros_Global = ('Global39', 'first'),
                Consumo_EnergiaFinalVectores_BiomasaOtros_Calefaccion = ('Calefaccion40', 'first'),
                Consumo_EnergiaFinalVectores_BiomasaOtros_Refrigeracion = ('Refrigeracion41', 'first'),
                Consumo_EnergiaFinalVectores_BiomasaOtros_ACS = ('CS42', 'first'),
                Consumo_EnergiaFinalVectores_BiomasaOtros_Iluminacion = ('Iluminacion43', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadPeninsular_Global = ('Global44', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadPeninsular_Calefaccion = ('Calefaccion45', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadPeninsular_Refrigeracion = ('Refrigeracion46', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadPeninsular_ACS = ('CS47', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadPeninsular_Iluminacion = ('Iluminacion48', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadBaleares_Global = ('Global49', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadBaleares_Calefaccion = ('Calefaccion50', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadBaleares_Refrigeracion = ('Refrigeracion51', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadBaleares_ACS = ('CS52', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadBaleares_Iluminacion = ('Iluminacion53', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadCanarias_Global = ('Global54', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadCanarias_Calefaccion = ('Calefaccion55', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadCanarias_Refrigeracion = ('Refrigeracion56', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadCanarias_ACS = ('CS57', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadCanarias_Iluminacion = ('Iluminacion58', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadCeutayMelilla_Global = ('Global59', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadCeutayMelilla_Calefaccion = ('Calefaccion60', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadCeutayMelilla_Refrigeracion = ('Refrigeracion61', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadCeutayMelilla_ACS = ('CS62', 'first'),
                Consumo_EnergiaFinalVectores_ElectricidadCeutayMelilla_Iluminacion = ('Iluminacion63', 'first'),
                Consumo_EnergiaFinalVectores_Biocarburante_Global = ('Global64', 'first'),
                Consumo_EnergiaFinalVectores_Biocarburante_Calefaccion = ('Calefaccion65', 'first'),
                Consumo_EnergiaFinalVectores_Biocarburante_Refrigeracion = ('Refrigeracion66', 'first'),
                Consumo_EnergiaFinalVectores_Biocarburante_ACS = ('CS67', 'first'),
                Consumo_EnergiaFinalVectores_Biocarburante_Iluminacion = ('Iluminacion68', 'first'),
                Consumo_EnergiaPrimariaNoRenovable_Global = ('Global69', 'first'),
                Consumo_EnergiaPrimariaNoRenovable_Calefaccion = ('Calefaccion70', 'first'),
                Consumo_EnergiaPrimariaNoRenovable_Refrigeracion = ('Refrigeracion71', 'first'),
                Consumo_EnergiaPrimariaNoRenovable_ACS = ('CS72', 'first'),
                Consumo_EnergiaPrimariaNoRenovable_Iluminacion = ('Iluminacion73', 'first'),
                EmisionesCO2_Global = ('Global74', 'first'),
                EmisionesCO2_Calefaccion = ('Calefaccion75', 'first'),
                EmisionesCO2_Refrigeracion = ('Refrigeracion76', 'first'),
                EmisionesCO2_ACS = ('ACS77', 'first'),
                EmisionesCO2_Iluminacion = ('Iluminacion78', 'first'),
                EmisionesCO2_ConsumoElectrico = ('ConsumoElectrico', 'first'),
                EmisionesCO2_ConsumoOtros = ('ConsumoOtros', 'first'),
                EmisionesCO2_TotalConsumoElectrico = ('TotalConsumoElectrico', 'first'),
                EmisionesCO2_TotalConsumoOtros = ('TotalConsumoOtros', 'first'),
                Calificacion_Demanda_EscalaCalefaccion_A = ('A', 'first'),
                Calificacion_Demanda_EscalaCalefaccion_B = ('B', 'first'),
                Calificacion_Demanda_EscalaCalefaccion_C = ('C', 'first'),
                Calificacion_Demanda_EscalaCalefaccion_D = ('D', 'first'),
                Calificacion_Demanda_EscalaCalefaccion_E = ('E79', 'first'),
                Calificacion_Demanda_EscalaCalefaccion_F = ('F', 'first'),
                Calificacion_Demanda_EscalaRefrigeracion_A = ('A80', 'first'),
                Calificacion_Demanda_EscalaRefrigeracion_B = ('B81', 'first'),
                Calificacion_Demanda_EscalaRefrigeracion_C = ('C82', 'first'),
                Calificacion_Demanda_EscalaRefrigeracion_D = ('D83', 'first'),
                Calificacion_Demanda_EscalaRefrigeracion_E = ('E84', 'first'),
                Calificacion_Demanda_EscalaRefrigeracion_F = ('F85', 'first'),
                Calificacion_Demanda_Letra_Calefaccion = ('Calefaccion86', 'first'),
                Calificacion_Demanda_Letra_Refrigeracion = ('Refrigeracion87', 'first'),
                Calificacion_EnergiaPrimariaNoRenovable_EscalaGlobal_A = ('A88', 'first'),
                Calificacion_EnergiaPrimariaNoRenovable_EscalaGlobal_B = ('B89', 'first'),
                Calificacion_EnergiaPrimariaNoRenovable_EscalaGlobal_C = ('C90', 'first'),
                Calificacion_EnergiaPrimariaNoRenovable_EscalaGlobal_D = ('D91', 'first'),
                Calificacion_EnergiaPrimariaNoRenovable_EscalaGlobal_E = ('E92', 'first'),
                Calificacion_EnergiaPrimariaNoRenovable_EscalaGlobal_F = ('F93', 'first'),
                Calificacion_EnergiaPrimariaNoRenovable_Letra_Global = ('Global94', 'first'),
                Calificacion_EnergiaPrimariaNoRenovable_Letra_Calefaccion = ('Calefaccion95', 'first'),
                Calificacion_EnergiaPrimariaNoRenovable_Letra_Refrigeracion = ('Refrigeracion96', 'first'),
                Calificacion_EnergiaPrimariaNoRenovable_Letra_ACS = ('ACS97', 'first'),
                Calificacion_EnergiaPrimariaNoRenovable_Letra_Iluminacion = ('Iluminacion98', 'first'),
                Calificacion_EmisionesCO2_EscalaGlobal_A = ('A99', 'first'),
                Calificacion_EmisionesCO2_EscalaGlobal_B = ('B100', 'first'),                
                Calificacion_EmisionesCO2_EscalaGlobal_C = ('C101', 'first'),               
                Calificacion_EmisionesCO2_EscalaGlobal_D = ('D102', 'first'),                
                Calificacion_EmisionesCO2_EscalaGlobal_E = ('E103', 'first'),                
                Calificacion_EmisionesCO2_EscalaGlobal_F = ('F104', 'first'),                
                Calificacion_EmisionesCO2_Letra_Global = ('Global105', 'first'),
                Calificacion_EmisionesCO2_Letra_Calefaccion = ('Calefaccion106', 'first'),
                Calificacion_EmisionesCO2_Letra_Refrigeracion = ('Refrigeracion107', 'first'),
                Calificacion_EmisionesCO2_Letra_ACS = ('ACS108', 'first'),
                Calificacion_EmisionesCO2_Letra_Iluminacion = ('Iluminacion109', 'first'),
                )
# df.TipoEdificio.replace ({"VIVIENDA UNIFAMILIAR":"Residencial - Vivienda unifamiliar", "VIVIENDA INDIVIDUAL":"Residencial - Vivienda individual", "BLOQUE COMPLETO":"Residencial - Bloque completo", "LOCAL":"Terciario - Local", "BLOQUE COMPLETO TERCIARIO":"Terciario - Edificio completo"}, inplace=True)
 # df.insert(4, 'CMUN', "")        df.insert(6, 'Coordenadas_latitud', "")        df.insert(7, 'Coordenadas_longitud', "") 
 #df.insert(9, 'NumeroCertificado', '') df.insert(37, 'Normativa_instalaciones', '')
        df = df2
        eleventh_column = df.pop('Fecha_registro')
        df.insert(37, 'Fecha_registro_completa', eleventh_column)
        df.insert(37, 'Fecha_registro', eleventh_column.str[-4:])
        df.insert(45, 'C_CCAA', 1) 
        sepcol = archivo.split('\\')            # Para dar la provincia como para andalucía es el mismo script saco qué provincia es por el nombre del archivo de entrada, le quito la ruta y me quedo con el nombre para ver qué provincia es cada caso
        nombre = sepcol[-1]
        if nombre == 'Almería.xlsx':
                df.insert(46, 'CPROV', 4) 
        elif nombre == 'Cádiz.xlsx':
                df.insert(46, 'CPROV', 11) 
        elif nombre == 'Córdoba.xlsx':
                df.insert(46, 'CPROV', 14) 
        elif nombre == 'Granada.xlsx':
                df.insert(46, 'CPROV', 18) 
        elif nombre == 'Huelva.xlsx':
                df.insert(46, 'CPROV', 21) 
        elif nombre == 'Jaén.xlsx':
                df.insert(46, 'CPROV', 23) 
        elif nombre == 'Malaga.xlsx':
                df.insert(46, 'CPROV', 29) 
        elif nombre == 'Sevilla.xlsx':
                df.insert(46, 'CPROV', 41) 
        df.insert(5, 'N_certif', 1) 
        df.insert(6, 'Calificación_consumo_energía', df.Calificacion_EnergiaPrimariaNoRenovable_Letra_Global) 
        df.insert(7, 'Calificación_emisiones', df.Calificacion_EmisionesCO2_Letra_Global) 

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


