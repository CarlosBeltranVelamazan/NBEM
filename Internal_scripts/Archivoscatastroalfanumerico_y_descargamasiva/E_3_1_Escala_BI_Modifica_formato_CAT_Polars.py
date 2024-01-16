# Este archivo hace lo mismo que su homólogo E_3 pero sólo con los Bienes Inmuebles, esto nos sirve para sacar el nº de viv certificadas y el nº de terciarios por uso certificados

# La consulta al catastro alfanumerico te devuelve un archivo .CAT con muchisima información se puede usar por plantillas de excel y tal, 
# pero Zaragoza por ejemplo tiene 1543424 líneas, más de las que excel puede soportar. 
# Nota: los archivos .CAT pequeños como el 44_235 (Torrecilla del Rebollar) se pueden visualizar directamente abriendolos en VSCode, más cómodo

import pandas as pd
import numpy as np
import polars as pl
#from time import time

def TratarCAT (Carpeta_archivos_descargas_CA, carpeta, fichero, Carpeta_archivos_guardar):

    # El primer paso es leer el archivo, separar por tipo de registro, el cat contiene mucha información variada y no puede tratarse de golpe toda por que el esquema de los datos no es homogéneo
    #print ("Empieza el proceso de tratar el .cat " + fichero.name) 

    # Datos a extraer de los archivos .cat: # No lo usamos, son necesarios los 4 tipos de datos para el código implementado.
    #Datos_finca = True
    #Datos_unidadconstructiva = True
    #Datos_construccion = True
    #Datos_inmueble = True
    #Datos_elementos_comunes = True          # No implementado
    #Datos_cultivos = False                  # No implementado

    # Para saber cuánto tarda este proceso
    #inicio  = time()
    #print(fichero)
    archivo = Carpeta_archivos_descargas_CA  + '\\' + 'Archivos_descomprimidos' + '\\' + carpeta.name + '\\' + fichero.name

    # Versión polars para tratar el .cat
    df = pl.read_csv(
        archivo,
        has_header=False,
        skip_rows=1,
        sep = '$',
        encoding='latin-1',
        new_columns=["All"], truncate_ragged_lines=True
    )

    column_names = ['Tipo_de_registro', 'Provincia', 'CMunicipioDGC', 'Clase', 'ReferenciaCatastral_parcela', 'C2', 'Letras_control_ReferenciaCatastral','Numero_de_Cargo_BI','Numero_fijo_BI', 'NombreProvincia',
                    'Cod_UC', 'Codigo_de_destino_DGC', 'Indicador_reforma_o_rehabilitacion', 'Fecha_reforma', 'Antiguedad_efectiva_en_catastro', 'CMunicipioINE', 'NombreMunicipio', 'Indicador_local_interior','Superficie_del_local','Sup_porches_y_terrazas',
                    'Sup_en_otras_plantas','Tipologia_constructiva_Normas_Tecnicas_de_Valoracion', 'NombreProvincia_BI','CMunicipioINE_BI', 'NombreMunicipio_BI', 'CP', 'FechaConstruccion','ExactitudFechaConstruccion','Superficie_suelo_EC', 'Longitud_de_fachada', 
                    'SupFinca', 'SupConstruida', 'Sup_sobre_rasante', 'Sup_bajo_rasante', 'Sup_cubierta', 'Coord_X', 'Coord_Y', 'FechaConstruccion_BI', 'Clavegrupo_BI', 'Sup_elementos_urbanos',
                    'Sup_elementos_rusticos','Coef_propiedad_finca', 'Planta_C', 'Planta_BI']

    slice_tuples = [(0,2),(23,25),(25,28),(28,30),(30,44),(44,48),(48,50),(50,54),(50,58),(52,77),
                    (54,58),(70,73),(73,74),(74,78),(78,82),(80,83),(83,153),(82,83),(83,90),(90,97),
                    (97,104),(104,109),(94,119),(122,125),(125,195),(240,245),(295,299),(299,300),(300,307),(307,312),
                    (295,305),(305,312),(312,319),(319,326),(326,333),(333,342),(342,352),(371,375),(427,428),(441,451),
                    (451,461),(461,470),(64,67),(251,254)]

    df = df.with_columns(
        [
        pl.col("All").str.slice(slice_tuple[0], slice_tuple[1]- slice_tuple[0]).str.strip().alias(col)
        for slice_tuple, col in zip(slice_tuples, column_names)
        ]
        ).drop("All")

    # Los tipo de Registros que hay, nos quedamos con los que nos interesan:
  #  finca = df.filter(pl.col('Tipo_de_registro') == '11')
  #  unidadconstructiva = df.filter(pl.col('Tipo_de_registro') == '13')
    construccion = df.filter(pl.col('Tipo_de_registro') == '14')
    inmueble = df.filter(pl.col('Tipo_de_registro') == '15')
    # elementos_comunes = df.filter(pl.col('Tipo_de_registro') == '16')
    # cultivos = df.filter(pl.col('Tipo_de_registro') == '17')

    # Del dataframe me quedo con el siguiente listado de columnas para cada tipo de registro

    colsconstr=['Tipo_de_registro', 'Provincia', 'CMunicipioDGC', 'ReferenciaCatastral_parcela', 'C2', 'Numero_de_Cargo_BI', 'Cod_UC', 'Codigo_de_destino_DGC', 'Indicador_reforma_o_rehabilitacion','Fecha_reforma','Antiguedad_efectiva_en_catastro','Indicador_local_interior','Superficie_del_local','Sup_porches_y_terrazas','Sup_en_otras_plantas','Tipologia_constructiva_Normas_Tecnicas_de_Valoracion', 'Planta_C']
    cols_borrar = list(set(column_names) ^ set(colsconstr))
    construccion = construccion.drop(cols_borrar)
    construccion = construccion.rename({'C2':'Numero_de_orden_elemento_de-construccion'})

    colsbi=['Tipo_de_registro', 'Provincia', 'CMunicipioDGC', 'Clase', 'ReferenciaCatastral_parcela', 'C2', 'Letras_control_ReferenciaCatastral', 'Numero_fijo_BI', 'NombreProvincia_BI','CMunicipioINE_BI', 'NombreMunicipio_BI', 'FechaConstruccion_BI', 'Clavegrupo_BI', 'Sup_elementos_urbanos','Sup_elementos_rusticos','Coef_propiedad_finca', 'Planta_BI']
    cols_borrar = list(set(column_names) ^ set(colsbi))
    inmueble = inmueble.drop(cols_borrar)
    inmueble = inmueble.rename({'C2':'Numero_de_Cargo'})

    # finca.write_csv(r"Archivoscatastroalfanumerico_y_descargamasiva\Cat alfanumerico\Fincas.csv")
    # unidadconstructiva.write_csv(r"Archivoscatastroalfanumerico_y_descargamasiva\Cat alfanumerico\UnidadesConstructivas.csv")
    # construccion.write_csv(r"Archivoscatastroalfanumerico_y_descargamasiva\Cat alfanumerico\Construcciones.csv")
    # inmueble.write_csv(r"Archivoscatastroalfanumerico_y_descargamasiva\Cat alfanumerico\BienesInmueble.csv")

    a = df.shape[0]
  #  b = finca.shape[0]
  #  c = unidadconstructiva.shape[0]
    d = construccion.shape[0]
    e = inmueble.shape[0]

    # Para saber cuánto tarda este proceso
    #duracion = time() - inicio

    #with open(Carpeta_archivos_guardar + '\\' + r"Datos_archivo_cat_" + fichero.name + ".txt", 'w') as f:
    #                f.write('En el archivo ' + fichero.name + '\nEn total hay: ' + str(a) + ' datos \nFincas: ' + str (b) + '\nUnidades Constructivas: ' + str(c) + '\nConstrucciones: ' + str(d) + '\nBienes inmuebles: ' + str(e) + '\nY ha tardado: ' + str(duracion) + ' segundos' )

    #print ('Terminado el paso E_3')
    return construccion, inmueble, a, d, e
    

    #                                                           NOTAS E INFORMACIÓN IMPORTANTE

    # El formato .cat el catastro lo define aqui:
    # https://www.catastro.minhap.es/documentos/formatos_intercambio/catastro_fin_cat_2006.pdf
    # Preguntas frecuentes
    # https://www.catastro.minhap.es/documentos/preguntas_frecuentes_formato_cat.pdf

    # Hay 8 Tipos de registro en el .cat definido por los 2 primeros dígitos: 
    # 01 - Encabezado. La primera línea
    # 11 - Finca: La parcela catastral
    # 13 - Unidad Constructiva. Existirá uno por cada unidad constructiva en cada parcela catastral
    # 14 - Construcción. Existirá uno por cada construcción de cada unidad constructiva en cada parcela catastral
    # 15 - Inmueble. Existirá uno por cada bien inmueble en cada parcela catastral
    # 16 - Reparto de elementos comunes. 
    # 17 - Registro de cultivos
    # 90 -  Registro de cola. La ultima línea

    """ 
    Los elementos que componen la base de datos catastral, y que pueden encontrarse en el formato CAT, son los siguientes:
    Finca. Identifica y localiza a la parcela catastral.
    Unidad Constructiva. Representa un edificio o un conjunto de construcciones particularizadas dentro de un edificio.
    Construcción. Identifica cada uno de los locales existentes en un bien inmueble, con su descripción física: superficie, antigüedad, tipología.
    Inmueble. Identifica cada uno de los bienes inmuebles dentro de una parcela catastral.
    Reparto de elementos comunes. Identifica el elemento constructivo cuyo valor se reparte entre los demás elementos de construcción.
    Cultivos. Identifica cada subparcela de cultivo existente dentro de la parcela catastral.
    """

