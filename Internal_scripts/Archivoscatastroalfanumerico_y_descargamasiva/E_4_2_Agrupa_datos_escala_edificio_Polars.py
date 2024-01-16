# Este archivo hace lo mismo que su homólogo E_4 pero agrupa a escala de Bienes Inmuebles, esto nos sirve para sacar el nº de viv certificadas y el nº de terciarios por uso certificados

# Este script coje los datos generados por el E_3 y los trata para obtener archivos con los datos por edificio, así tenemos una BBDD a escala edificio con la información que nos interesa para ahora unirla con los edificos del INSPIRE en gis y con los certificados energéticos
import pandas as pd
import numpy as np
import polars as pl

def AgruparCATporEdificio (construccion, inmueble, Carpeta_archivos_guardar, nombre_archivo):

     #print ("Empieza E_4 con " + str(nombre_archivo)) 

     carpeta_leer = Carpeta_archivos_guardar

     construccion = construccion.to_pandas()
     inmueble = inmueble.to_pandas()

     # NOTA:::           Esto convertirlo a formato parquet cuando veamos que los datos los da bien el catastro
     # NOTA:::           Hay dos formas de convertir los datos string a numeros, el astype y el pd.to_numeric, la ventaja del to_numeric es que tiene coerce que elimina los que no se pueden convertir, asegurando que no haya errores, el otro es interesante porque te da la variable en int o float según sea necesario
     # Fincas
    #  #nombre_archivo = r"\Fincas.csv"
    #  edificios_F = finca.replace(",", ".")
    #  edificios_F.SupFinca = pd.to_numeric(edificios_F.SupFinca, errors='coerce')    
    #  edificios_F.SupConstruida = pd.to_numeric(edificios_F.SupConstruida, errors='coerce')
    #  edificios_F.Sup_bajo_rasante = pd.to_numeric(edificios_F.Sup_bajo_rasante, errors='coerce')
    #  edificios_F.Sup_sobre_rasante = pd.to_numeric(edificios_F.Sup_sobre_rasante, errors='coerce')
    #  edificios_F.Sup_cubierta = pd.to_numeric(edificios_F.Sup_cubierta, errors='coerce')
    #  edificios_F.insert(1, 'N_plantas_F', edificios_F['Sup_sobre_rasante'].div(edificios_F['Sup_cubierta']).replace(np.inf, 0))
    #  #edificios_F.to_csv(carpeta_leer + r"\Edificios_F" + ".csv", encoding='utf-8', index=False, decimal=",")

    #  # Unidad Constructiva
    #  #nombre_archivo = r"\UnidadesConstructivas.csv"
    #  df = unidadconstructiva.replace(",", ".")
    #  df.FechaConstruccion = pd.to_numeric(df.FechaConstruccion, errors='coerce')
    #  df.Superficie_suelo_EC = pd.to_numeric(df.Superficie_suelo_EC, errors='coerce')
    #  df.Longitud_de_fachada = pd.to_numeric(df.Longitud_de_fachada, errors='coerce')
    #  edificios_UC = df.groupby('ReferenciaCatastral_parcela') \
    #                 .agg(ReferenciaCatastral_parcela = ('ReferenciaCatastral_parcela', 'first'), \
    #                 FechaConstruccion = ('FechaConstruccion', 'mean'), \
    #                 ExactitudFechaConstruccion = ('ExactitudFechaConstruccion', 'first'), \
    #                 Superficie_suelo_EC = ('Superficie_suelo_EC', 'mean'), \
    #                 Longitud_de_fachada = ('Longitud_de_fachada', 'sum'), \
    #                 )
    #  #edificios_UC.to_csv(carpeta_leer + r"\Edificios_UC" + ".csv", encoding='utf-8', index=False)

     # Construcciones          WIP
     #nombre_archivo = r"\Construcciones.csv"
     df = construccion.replace(",", ".")
     df.Planta_C = pd.to_numeric(df.Planta_C, errors='coerce')                           # El número de plantas de la construcción, quito lo que no son números para poder sacar la altura máxima
     df.Fecha_reforma = pd.to_numeric(df.Fecha_reforma, errors='coerce')
     df.Antiguedad_efectiva_en_catastro = pd.to_numeric(df.Antiguedad_efectiva_en_catastro, errors='coerce')
     df.Superficie_del_local = pd.to_numeric(df.Superficie_del_local, errors='coerce')
     df.Sup_porches_y_terrazas = pd.to_numeric(df.Sup_porches_y_terrazas, errors='coerce')
     df.Sup_en_otras_plantas = pd.to_numeric(df.Sup_en_otras_plantas, errors='coerce')
     # Quito usos de la Y (Otros usos), y que en Bienes Inmuebles se considera Sanidad y Beneficiencia, aquí incluye porches, terrazas y silos y depósitos, los paso a la categoría L, para quitarlos
     df.Codigo_de_destino_DGC.replace ({"YCA":"L_OTROS", "YCB":"L_OTROS", 
                                        "YCE":"L_OTROS", "YDG":"L_OTROS", 
                                        "YDL":"L_OTROS", "YJD":"L_OTROS", 
                                        "YOU":"L_OTROS", "YPO":"L_OTROS", 
                                        "YSA":"L_OTROS", "YSL":"L_OTROS", 
                                        "YSO":"L_OTROS", "YSP":"L_OTROS", 
                                        "YTD":"L_OTROS", "YTZ":"L_OTROS", 
                                        }, inplace=True)
     df.insert(1, 'Uso_de_la_construcción', df['Codigo_de_destino_DGC'].str[:1])                # Del Código de destino nos quedamos con la primera letra, que da los mismos usos que la clasificación de los Bienes Inmuebles pero nos aporta más info al coger ahora los m2 de las construcciones con esos usos (por ejemplo ya no incluye los m2 de aparcamiento, trastero y zonas comunes como m2 de vivienda que si pasa en el BI)

     df.insert(1, 'Calidad_de_la_edificacion', df['Tipologia_constructiva_Normas_Tecnicas_de_Valoracion'].str[-1:])
     df.insert(1, 'Tipologia_constructiva', df['Tipologia_constructiva_Normas_Tecnicas_de_Valoracion'].str[:-1])
     df.Calidad_de_la_edificacion = pd.to_numeric(df.Calidad_de_la_edificacion, errors='coerce')

     # En este caso, elimino de la columna Tipologia_constructiva porque son los trasteros y garajes y me resulta en datos con algunos errores si hay más que viviendas
     df['Tipologia_constructiva'] = df['Tipologia_constructiva'].replace(['0113', '0123'], pd.NA)

   #  print(df['Numero_de_Cargo_BI'].map("{:04n}".format))       # Esto es para darle el formato de 0001 en vez de 1, pero ya viene así de serie
     df.insert(1, 'Referencia_BI', df['ReferenciaCatastral_parcela'] + df['Numero_de_Cargo_BI'])
    # print(df.Referencia_BI)

       # En la línea siguiente si pongo entre el df y el .groupby esto: .query("Codigo_de_destino_DGC == 'V'") me quedo sólo con los datos de vivienda, por si me resulta más útli
     edificios_C = df.assign(
                    S_Viv = np.where(df['Uso_de_la_construcción']=='V',df['Superficie_del_local'],0),            # Superficie de las construcciones en la parcela con uso Residencial
                    S_Almacen = np.where(df['Uso_de_la_construcción']=='A',df['Superficie_del_local'],0),
                    S_Ind = np.where(df['Uso_de_la_construcción']=='I',df['Superficie_del_local'],0),
                    S_Of = np.where(df['Uso_de_la_construcción']=='O',df['Superficie_del_local'],0),
                    S_Com = np.where(df['Uso_de_la_construcción']=='C',df['Superficie_del_local'],0),
                    S_Dep = np.where(df['Uso_de_la_construcción']=='K',df['Superficie_del_local'],0),
                    S_Esp = np.where(df['Uso_de_la_construcción']=='T',df['Superficie_del_local'],0),
                    S_Host = np.where(df['Uso_de_la_construcción']=='G',df['Superficie_del_local'],0),
                    S_San = np.where(df['Uso_de_la_construcción']=='Y',df['Superficie_del_local'],0),
                    S_Cult = np.where(df['Uso_de_la_construcción']=='E',df['Superficie_del_local'],0),
                    S_Rel = np.where(df['Uso_de_la_construcción']=='R',df['Superficie_del_local'],0),
                    S_Sin = np.where(df['Uso_de_la_construcción']=='P',df['Superficie_del_local'],0),
                    S_IAg = np.where(df['Uso_de_la_construcción']=='J',df['Superficie_del_local'],0),
                    S_Ag = np.where(df['Uso_de_la_construcción']=='Z',df['Superficie_del_local'],0),
                    ).groupby(['Referencia_BI']) \
                    .agg(Referencia_BI = ('Referencia_BI', 'first'), \
                         Indicador_reforma_o_rehabilitacion = ('Indicador_reforma_o_rehabilitacion', lambda x: x.mode().iat[0] if not x.mode().empty else None), \
                         Fecha_reforma = ('Fecha_reforma', 'mean'), \
                         Antiguedad_efectiva_en_catastro = ('Antiguedad_efectiva_en_catastro', 'mean'), \
                         Planta_C = ('Planta_C', 'max'), \
                        # Superficie_del_local = ('Superficie_del_local', 'sum'), \
                         Sup_porches_y_terrazas = ('Sup_porches_y_terrazas', 'sum'), \
                         Sup_en_otras_plantas = ('Sup_en_otras_plantas', 'sum'), \
                         Calidad_de_la_edificacion = ('Calidad_de_la_edificacion', 'mean'), \
                         Tipologia_constructiva = ('Tipologia_constructiva', lambda x: x.mode().iat[0] if not x.mode().empty else None), \
                         S_Viv = ('S_Viv', 'sum'), \
                         S_Almacen = ('S_Almacen', 'sum'), \
                         S_Ind = ('S_Ind', 'sum'), \
                         S_Of = ('S_Of', 'sum'), \
                         S_Com = ('S_Com', 'sum'), \
                         S_Dep = ('S_Dep', 'sum'), \
                         S_Esp = ('S_Esp', 'sum'), \
                         S_Host = ('S_Host', 'sum'), \
                         S_San = ('S_San', 'sum'), \
                         S_Cult = ('S_Cult', 'sum'), \
                         S_Rel = ('S_Rel', 'sum'), \
                         S_Sin = ('S_Sin', 'sum'), \
                         S_IAg = ('S_IAg', 'sum'), \
                         S_Ag = ('S_Ag', 'sum'), \
                    )
     #edificios_C.to_csv(carpeta_leer + r"\Edificios_C" + ".csv", encoding='utf-8', index=False)
     #print(edificios_C.dtypes)
     # Faltaría aportar esta información
     # Codigo_de_destino_DGC = ('Codigo_de_destino_DGC', 'first'), \
     # N_Codigo_de_destino_DGC = ('Codigo_de_destino_DGC', 'size'), \
     # Tipología_constructiva_Normas_Técnicas_de_Valoracion = ('Tipología_constructiva_Normas_Técnicas_de_Valoracion', 'first'), \
     # N_Tipología_constructiva_Normas_Técnicas_de_Valoracion = ('Tipología_constructiva_Normas_Técnicas_de_Valoracion', 'size'), \


     # Bienes Inmuebles
     #nombre_archivo = r"\BienesInmueble.csv"
     df = inmueble.replace(",", ".")
     df.Planta_BI = pd.to_numeric(df.Planta_BI, errors='coerce')                           # El número de plantas del inmueble, quito lo que no son números para poder sacar la altura máxima
     df.Sup_elementos_urbanos = pd.to_numeric(df.Sup_elementos_urbanos, errors='coerce')
     df.FechaConstruccion_BI = pd.to_numeric(df.FechaConstruccion_BI, errors='coerce')  
     df.insert(1, 'Referencia_BI', df['ReferenciaCatastral_parcela'] + df['Numero_de_Cargo'])
    # print(df.Referencia_BI)
     edificios_BI = df.assign(
     N_BI = np.where(df['Clavegrupo_BI'],1,0),                                            # Número de Bienes Inmuebles en la parcela
     Viv = np.where(df['Clavegrupo_BI']=='V',1,0),                                        # Número de Bienes Inmuebles en la parcela con uso Residencial
     Almacen = np.where(df['Clavegrupo_BI']=='A',1,0),                                    # Número de Bienes Inmuebles en la parcela con uso Almacén -Estacionamiento
     Ind = np.where(df['Clavegrupo_BI']=='I',1,0),                                        # Industrial
     Of = np.where(df['Clavegrupo_BI']=='O',1,0),                                         # Oficinas
     Com = np.where(df['Clavegrupo_BI']=='C',1,0),                                        # Comercial
     Dep = np.where(df['Clavegrupo_BI']=='K',1,0),                                        # Deportivo
     Esp = np.where(df['Clavegrupo_BI']=='T',1,0),                                        # Espectáculos
     Host = np.where(df['Clavegrupo_BI']=='G',1,0),                                       # Ocio y Hostelería
     San = np.where(df['Clavegrupo_BI']=='Y',1,0),                                        # Sanidad y Beneficencia
     Cult = np.where(df['Clavegrupo_BI']=='E',1,0),                                       # Cultural
     Rel = np.where(df['Clavegrupo_BI']=='R',1,0),                                        # Religioso
     Sin = np.where(df['Clavegrupo_BI']=='P',1,0),                                        # Edificio singular
     IAg = np.where(df['Clavegrupo_BI']=='J',1,0),                                        # Industrial agrario
     Ag = np.where(df['Clavegrupo_BI']=='Z',1,0),                                         # Agrario, quedan más usos posibles no incluidos porque no nos interesa añadir en este estudio
     Plantas = np.where(df['Planta_BI']>=0,df['Planta_BI'],0),                            # El número de plantas del inmueble, quito los negativos pra quedarme solo con las plantas sobre rasante
     ).groupby('Referencia_BI').agg({'ReferenciaCatastral_parcela':'first', 'Referencia_BI':'first', 
                                                  'Tipo_de_registro':'first', 'Provincia':'first',
                                                  'CMunicipioINE_BI':'first', 'CMunicipioDGC':'first', 
                                                  'NombreProvincia_BI':'first', 'Clavegrupo_BI':'first', 
                                                  'FechaConstruccion_BI':'mean', 'Plantas':'max', 
                                                  'N_BI':'sum', 'Sup_elementos_urbanos':'sum',
                                                  'Viv':'sum', 'Almacen':'sum',
                                                  'Ind':'sum', 'Of':'sum',
                                                  'Com':'sum', 'Dep':'sum',
                                                  'Esp':'sum', 'Host':'sum',
                                                  'San':'sum', 'Cult':'sum',
                                                  'Rel':'sum', 'Sin':'sum',
                                                  'IAg':'sum', 'Ag':'sum',
                                                  })

     #edificios_BI.to_csv(carpeta_leer + r"\Edificios_BI" + ".csv", encoding='utf-8', index=False)

     # Reiniciamos los índices de los dataframes porque el merge da error si ReferenciaCatastral_parcela es indice en unos y en otros no
    #  edificios_F.reset_index(inplace=True, drop=True)
    #  edificios_UC.reset_index(inplace=True, drop=True)
     edificios_C.reset_index(inplace=True, drop=True)
     edificios_BI.reset_index(inplace=True, drop=True)

     # Unimos los datos en un archivo por provincia con todos los datos por edificio
     #  edificios_F = edificios_F.merge(edificios_UC, how='left', on='ReferenciaCatastral_parcela').merge(edificios_C, how='left', on='ReferenciaCatastral_parcela').merge(edificios_BI, how='left', on='ReferenciaCatastral_parcela')
     edificios_F = edificios_BI.merge(edificios_C, how='left', on='Referencia_BI')

     # En el catastro las plantas bajas se catalogan con letras con lo que las ha quitado, las plantas altas las numera como 1 a la B+1, 2 a la B+2, le sumo 1 a las plantas. Lo aplico a las plantas de la construcciones y de los Bienes inmuebles
     edificios_F['Planta_C'] = np.where(
     (edificios_F['S_Viv'] >= 1) | (edificios_F['S_Ind'] >= 1) | (edificios_F['S_Of'] >= 1) |
     (edificios_F['S_Com'] >= 1) | (edificios_F['S_Dep'] >= 1) | (edificios_F['S_Esp'] >= 1) |
     (edificios_F['S_Host'] >= 1) | (edificios_F['S_San'] >= 1) | (edificios_F['S_Cult'] >= 1) |
     (edificios_F['S_Rel'] >= 1) | (edificios_F['S_Sin'] >= 1) | (edificios_F['S_IAg'] >= 1) |
     (edificios_F['S_Ag'] >= 1),
     edificios_F['Planta_C'] + 1, edificios_F['Planta_C'])

     edificios_F['Plantas'] = np.where(
     (edificios_F['Viv'] >= 1) | (edificios_F['Ind'] >= 1) | (edificios_F['Of'] >= 1) |
     (edificios_F['Com'] >= 1) | (edificios_F['Dep'] >= 1) | (edificios_F['Esp'] >= 1) |
     (edificios_F['Host'] >= 1) | (edificios_F['San'] >= 1) | (edificios_F['Cult'] >= 1) |
     (edificios_F['Rel'] >= 1) | (edificios_F['Sin'] >= 1) | (edificios_F['IAg'] >= 1) |
     (edificios_F['Ag'] >= 1),
     edificios_F['Plantas'] + 1, edificios_F['Plantas'])

     edificios_F['Plantas_DEF'] = edificios_F[['Planta_C', 'Plantas']].max(axis=1)

     # Le damos la tipología de la ERESEE (Nota la vamos aplicando, y  podríamos darle un valor extra: Aa edificio plurifamilar mayor de 5 alturas, y edificios anteriores al 1900, para que nos encaje luego con los datos de TABULA)
     edificios_F['Periodo_Construccion'] = np.where(edificios_F['FechaConstruccion_BI']<=1940,'<40',                     # Los rangos de años son los de la ERESEE, el ultimo es del 2011 que acaba hasta ahora
                                           np.where(edificios_F['FechaConstruccion_BI']<=1960,'41-60',
                                           np.where(edificios_F['FechaConstruccion_BI']<=1980,'61-80',
                                           np.where(edificios_F['FechaConstruccion_BI']<=2007,'81-07',
                                           np.where(edificios_F['FechaConstruccion_BI']<=2011,'08-11',
                                           np.where(edificios_F['FechaConstruccion_BI']>2011,'12-23','No_data'
                                                    ))))))
     edificios_F['Cluster_ERESEE'] = np.where(edificios_F['Viv']<1,'Tt ' + edificios_F['Periodo_Construccion'],           # Uu - Unifamiliar, Cc - Edificio de hasta 3 alturas, Bb - Edificio de entre 3 y 5 alturas, Tt - Terciario
                                     np.where(edificios_F['Viv']==1,'Uu ' + edificios_F['Periodo_Construccion'], 
                                     np.where((edificios_F['Viv']>1) & (edificios_F['Plantas_DEF']>3),'Bb ' + edificios_F['Periodo_Construccion'], 'Cc ' + edificios_F['Periodo_Construccion']
                                     )))
     

     #edificios_F.to_csv(carpeta_leer + r"\Edificios_Completos_" + str(nombre_archivo) + ".csv", encoding='utf-8', index=False)
     #print (edificios_F.dtypes)
     #print ('Terminado E_4 con ' + str(nombre_archivo))
     return edificios_F

     # Algunas ideas:

     # Clavegrupo_DGC = ['1','2','3','4','A','V','I','O','C','K','T','G','Y','E','R','M','P','B','J','Z']

     # Código para contar el numero de usos que hay en un archivo
     # df2 = (df.groupby(['Codigo_de_destino_DGC'])
     #             .size()
     #             .reset_index()
     #             )


     # Clusters de la ERESEE + detallados, por ejemplo para cuadrarlos con el proyecto TABULA, con dos cambios estaría adaptado
          # Darle un tipo extra Aa para edificios mayores a 5 plantas
          # Darle el periodo anteriores a 1900 


     # Idea para hacerlo: O como en el código que es más ligero o así, damos más datos, por ahorrar tiempo de cálculo y reducir tamaño de archivo no lo añado, pero siempre está bien como opción
"""  edificios_F['Tipo_Edi'] = edificios_F['Viv'].apply(lambda x: 'Pp' if x>1 else 'Tt' if x<1 else 'Uu')              # Uu - Unifamiliar, Pp - Plurifamiliar, Tt - Terciario
     edificios_F['Tipo_Cluster'] = edificios_F['Plantas'].apply(lambda x: 'Cc' if x<=3 else 'Aa' if x>5 else 'Bb')         # Cc - Edificio de hasta 3 alturas, Bb - Edificio de entre 3 y 5 alturas, Aa - Edificio mayor de 5 alturas
     edificios_F['Periodo_Construccion'] = np.where(edificios_F['FechaConstruccion_BI']<=1900,'<1900',                     # Los rangos de años son los de la ERESEE, el ultimo es del 2011 que acaba hasta ahora
                                           np.where(edificios_F['FechaConstruccion_BI']<=1940,'00-40',
                                           np.where(edificios_F['FechaConstruccion_BI']<=1960,'41-60',
                                           np.where(edificios_F['FechaConstruccion_BI']<=1980,'61-80',
                                           np.where(edificios_F['FechaConstruccion_BI']<=2007,'81-07',
                                           np.where(edificios_F['FechaConstruccion_BI']<=2011,'08-11',
                                           np.where(edificios_F['FechaConstruccion_BI']>2011,'12-23','No_data'
                                                    )))))))
     edificios_F['Cluster_ERESEE'] = np.where(edificios_F['Tipo_Edi']=='Uu','Uu' + edificios_F['Periodo_Construccion'],                     # Los rangos de años son los de la ERESEE, el ultimo es del 2011 que acaba hasta ahora
                                     np.where(edificios_F['Tipo_Edi']=='Tt','Tt' + edificios_F['Periodo_Construccion'],
                                     np.where((edificios_F['Tipo_Edi']=='Pp') & (edificios_F['Tipo_Cluster']=='Cc'),'Cc' + edificios_F['Periodo_Construccion'],
                                     np.where((edificios_F['Tipo_Edi']=='Pp') & (edificios_F['Tipo_Cluster']=='Bb'),'Bb' + edificios_F['Periodo_Construccion'],
                                     np.where((edificios_F['Tipo_Edi']=='Pp') & (edificios_F['Tipo_Cluster']=='Aa'),'Aa' + edificios_F['Periodo_Construccion'],
                                                    )))))
     
 """



     