# La consulta al catastro alfanumerico te devuelve un archivo .CAT con muchisima información se puede usar por plantillas de excel y tal, 
# pero Zaragoza por ejemplo tiene 1543424 líneas, más de las que excel puede soportar. 
# Nota: los archivos .CAT pequeños como el 44_235 (Torrecilla del Rebollar) se pueden visualizar directamente abriendolos en VSCode, más cómodo

import pandas as pd
#from time import time

def TratarCAT (fichero, Carpeta_archivos_guardar):

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
 #   inicio  = time()

    archivo = fichero
    #print(archivo)
    # Para tratar los datos cojo el .cat, lo troceo en las columnas que voy a necesitar, hay datos que están solapados, hay dos formas de hacerlo, cogerlos ahora troceados y luego concatenar valores o cogerlos varias veces y luego borrar columnas, por simplicidad voy a hacer el segundo
    colspecs = [(0,2),(23,25),(25,28),(28,30),(30,44),(44,48),(48,50),(50,54),(50,58),(52,77),
                (54,58),(70,73),(73,74),(74,78),(78,82),(80,83),(83,153),(82,83),(83,90),(90,97),
                (97,104),(104,109),(94,119),(122,125),(125,195),(240,245),(295,299),(299,300),(300,307),(307,312),
                (295,305),(305,312),(312,319),(319,326),(326,333),(333,342),(342,352),(371,375),(427,428),(441,451),
                (451,461),(461,470),(64,67),(251,254)]
    columns=['Tipo_de_registro', 'Provincia', 'CMunicipioDGC', 'Clase', 'ReferenciaCatastral_parcela', 'C2', 'Letras_control_ReferenciaCatastral','Numero_de_Cargo_BI','Numero_fijo_BI', 'NombreProvincia',
                'Cod_UC', 'Codigo_de_destino_DGC', 'Indicador_reforma_o_rehabilitacion', 'Fecha_reforma', 'Antiguedad_efectiva_en_catastro', 'CMunicipioINE', 'NombreMunicipio', 'Indicador_local_interior','Superficie_del_local','Sup_porches_y_terrazas',
                'Sup_en_otras_plantas','Tipologia_constructiva_Normas_Tecnicas_de_Valoracion', 'NombreProvincia_BI','CMunicipioINE_BI', 'NombreMunicipio_BI', 'CP', 'FechaConstruccion','ExactitudFechaConstruccion','Superficie_suelo_EC', 'Longitud_de_fachada', 
                'SupFinca', 'SupConstruida', 'Sup_sobre_rasante', 'Sup_bajo_rasante', 'Sup_cubierta', 'Coord_X', 'Coord_Y', 'FechaConstruccion_BI', 'Clavegrupo_BI', 'Sup_elementos_urbanos',
                'Sup_elementos_rusticos','Coef_propiedad_finca', 'Planta_C', 'Planta_BI']

    df = pd.read_fwf(archivo, skiprows=1, skipfooter=1, colspecs=colspecs, index_col=False, names=columns, engine='python',encoding='latin1', converters={h:str for h in columns})
    # El encoding utf-8 da problemas, tanto latin1 como unicode-escape funcionan bien por ahora
    # Salto la primera y última fila que son encabezado y pie de tabla, index col = False para que no me coja la primera fila como nombre de columnas


    # Los tipo de Registros que hay, nos quedamos con los que nos interesan:
            
    finca = df.loc[df.loc[:, 'Tipo_de_registro'] == '11']
    unidadconstructiva = df.loc[df.loc[:, 'Tipo_de_registro'] == '13']
    construccion = df.loc[df.loc[:, 'Tipo_de_registro'] == '14']
    inmueble = df.loc[df.loc[:, 'Tipo_de_registro'] == '15']
    # elementos_comunes = df.loc[df.loc[:, 'Tipo_de_registro'] == '16']
    # cultivos = df.loc[df.loc[:, 'Tipo_de_registro'] == '17']

    # Del dataframe me quedo con el siguiente listado de columnas para cada tipo de registro
    colsfinca=['Tipo_de_registro', 'Provincia', 'CMunicipioDGC', 'ReferenciaCatastral_parcela', 'NombreProvincia', 'CMunicipioINE', 'NombreMunicipio', 'CP', 'SupFinca', 'SupConstruida', 'Sup_sobre_rasante', 'Sup_bajo_rasante', 'Sup_cubierta', 'Coord_X', 'Coord_Y']
    finca = finca[finca.columns.intersection(colsfinca)]

    colsuc=['Tipo_de_registro', 'Clase', 'ReferenciaCatastral_parcela','C2','FechaConstruccion','ExactitudFechaConstruccion','Superficie_suelo_EC','Longitud_de_fachada']
    unidadconstructiva = unidadconstructiva[unidadconstructiva.columns.intersection(colsuc)]
    unidadconstructiva.rename(columns={'C2':'Codigo_Unidad_Constructiva'}, inplace=True)

    colsconstr=['Tipo_de_registro', 'ReferenciaCatastral_parcela', 'C2', 'Numero_de_Cargo_BI', 'Cod_UC', 'Codigo_de_destino_DGC', 'Indicador_reforma_o_rehabilitacion','Fecha_reforma','Antiguedad_efectiva_en_catastro','Indicador_local_interior','Superficie_del_local','Sup_porches_y_terrazas','Sup_en_otras_plantas','Tipologia_constructiva_Normas_Tecnicas_de_Valoracion', 'Planta_C']
    construccion = construccion[construccion.columns.intersection(colsconstr)]
    construccion.rename(columns={'C2':'Numero_de_orden_elemento_de-construccion'}, inplace=True)

    colsbi=['Tipo_de_registro', 'Clase', 'ReferenciaCatastral_parcela', 'C2', 'Letras_control_ReferenciaCatastral', 'Numero_fijo_BI', 'FechaConstruccion_BI', 'Clavegrupo_BI', 'Sup_elementos_urbanos','Sup_elementos_rusticos','Coef_propiedad_finca', 'Planta_BI']
    inmueble = inmueble[inmueble.columns.intersection(colsbi)]
    inmueble.rename(columns={'C2':'Numero_de_Cargo'}, inplace=True)

#    finca.to_csv(Carpeta_archivos_guardar + r"\Fincas_" + fichero.name + ".csv", index=False)
#    unidadconstructiva.to_csv(Carpeta_archivos_guardar + r"\UnidadesConstructivas_" + fichero.name + ".csv", index=False)
#    construccion.to_csv(Carpeta_archivos_guardar + r"\Construcciones_" + fichero.name + ".csv", index=False)
#    inmueble.to_csv(Carpeta_archivos_guardar + r"\BienesInmueble_" + fichero.name + ".csv", index=False)

    a = df.shape[0]
    b = finca.shape[0]
    c = unidadconstructiva.shape[0]
    d = construccion.shape[0]
    e = inmueble.shape[0]

    # Para saber cuánto tarda este proceso
 #   duracion = time() - inicio

#    with open(Carpeta_archivos_guardar + '\\' + r"Datos_archivo_cat_" + fichero.name + ".txt", 'w') as f:
#                    f.write('En el archivo ' + fichero.name + '\nEn total hay: ' + str(a) + ' datos \nFincas: ' + str (b) + '\nUnidades Constructivas: ' + str(c) + '\nConstrucciones: ' + str(d) + '\nBienes inmuebles: ' + str(e) + '\nY ha tardado: ' + str(duracion) + ' segundos' )

    #print ('Terminado el paso E_3')
    return finca, unidadconstructiva, construccion, inmueble, a, b, c, d, e
    

    #                                                           NOTAS E INFORMACIÓN IMPORTANTE

    # Para leerlo y que separe el texto de los cat por longitudes de caracteres de las columnas. Idea de internet con varios conceptos: (fuente: https://towardsdatascience.com/parsing-fixed-width-text-files-with-pandas-f1db8f737276)
    # pandas.read_fwf('humchr01.txt', skiprows=36, skipfooter=5, colspecs=colspecs, names=['gene_name', 'chromosomal_position', 'uniprot', 'entry_name', 'mtm_code', 'description'])
    # (archivo, encabezado a saltar, pie de página a saltar, la lista de cada cuanto cortar el texto en columnas, nombres de columnas)
    # Si pones colspecs defines el ancho de las columnas, si lo dejas por defecto con las primeras 100 columnas detecta las anchuras automáticas


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

