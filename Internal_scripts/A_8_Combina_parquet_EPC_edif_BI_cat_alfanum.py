def combine_with_cadastre (EPC_database_14_digits, EPC_database_20_digits, 
                           alphanumeric_cadastre_database_buildings, alphanumeric_cadastre_database_building_units, b1_output):

    import pandas as pd
    import numpy as np
    from time import time
    inicio  = time()

    # Building scale. 14 digits cadastral reference

    df = EPC_database_14_digits
    try: 
        cat = (pd.read_parquet(alphanumeric_cadastre_database_buildings))
    except:
        cat = (pd.read_csv(alphanumeric_cadastre_database_buildings, skiprows=0))
    # Columnas que queremos conservar en el df, las que no estén aquí se borrarán
    colsusar = ['ReferenciaCatastral_parcela', 'Provincia', 'Viv', 'S_Viv', 'Ind', 'S_Ind', 'Of', 'S_Of', 'Com', 'S_Com', 'Dep', 'S_Dep', 'Esp', 'S_Esp',
        'Host', 'S_Host', 'San', 'S_San', 'Cult', 'S_Cult', 'Rel', 'S_Rel',
        'Sin', 'S_Sin', 'Uso_princial']
    cat = cat[cat.columns.intersection(colsusar)]

    # Al valor de la provincia del catastro le asigno su CCAA correspondiente
    cat.insert(1, 'CAutonoma', cat.Provincia) 
    cat.CAutonoma.replace ({'04':1, '11':1, '14':1, '18':1, '21':1, '23':1, '29':1, '41':1,
                            '22':2, '44':2, '50':2, '33':3, '07':4, '35':5, '38':5, '39':6,
                            '05':7, '09':7, '24':7, '34':7, '37':7, '40':7, '42':7, '47':7, '49':7,
                            '02':8, '13':8, '16':8, '19':8, '45':8, 
                            '08':9, '17':9, '25':9, '43':9, '03':10, '12':10, '46':10, 
                            '06':11, '10':11, '15':12, '27':12, '32':12, '36':12, 
                            '28':13, '30':14, '31':15, '01':16, '48':16, '20':16,
                            '26':17, '51':18, '52':19
                            }, inplace=True)
    # cat.CAutonoma.replace ({4:1, 11:1, 14:1, 18:1, 21:1, 23:1, 29:1, 41:1,
    #                         22:2, 44:2, 50:2, 33:3, 7:4, 35:5, 38:5, 39:6,
    #                         5:7, 9:7, 24:7, 34:7, 37:7, 40:7, 42:7, 47:7, 49:7,
    #                         2:8, 13:8, 16:8, 19:8, 45:8, 
    #                         8:9, 17:9, 25:9, 43:9, 3:10, 12:10, 46:10, 
    #                         6:11, 10:11, 15:12, 27:12, 32:12, 36:12, 
    #                         28:13, 30:14, 31:15, 1:16, 48:16, 20:16,
    #                         26:17, 51:18, 52:19
    #                         }, inplace=True)
    # Numero de EPC antes de la unión
    a = df.shape[0]

    df = pd.merge(df, cat, how='inner', left_on='ReferenciaCatastral_edificio', right_on='ReferenciaCatastral_parcela')
    # El uso industrial finalmente lo elimino: df['S_Ind']+
    df.insert(0, 'm2_certificados', np.where(df['S_Viv']!=0,df['S_Viv'],(df['S_Of']+df['S_Com']+df['S_Dep']+df['S_Esp']+df['S_Host']+df['S_San']
                                                                        +df['S_Cult']+df['S_Rel']+df['S_Sin'])))
    # El uso industrial finalmente lo elimino: df['S_Ind']+
    df.insert(0, 'Numero_de_BI_certificados', np.where(df['S_Viv']!=0,df['Viv'],(df['Of']+df['Com']+df['Dep']+df['Esp']+df['Host']+df['San']
                                                                        +df['Cult']+df['Rel']+df['Sin'])))

    df.insert(0, 'Uso_certificado', np.where(df['S_Viv']!=0,"Residencial - Bloque completo o unifamiliar","Terciario - Edificio completo"))

    b = df.shape[0]

    print(df.shape[0])

    pre_borrar = df.shape[0]
    # Esto son errores de que han certificado bienes inmuebles con elementos constructivos de uso almacén-estacionamiento y similares y estos no puede ser certificados, se eliminan por tanto.
    df ['m2_certificados'] = df ['m2_certificados']. fillna('None')
    df['Coincide'] = np.where((df['m2_certificados']!= 'None'), 'Si','Bien')
    df = df.loc[(df['Coincide'] == 'Si')]
    duplicados = df.shape[0] - pre_borrar
    if duplicados != 0:
        print ('Se han borrado por none ' + str(duplicados) + ' edif')

    df['Coincide'] = np.where((df['m2_certificados']!= 0), 'Si','Bien')
    df = df.loc[(df['Coincide'] == 'Si')]
    df = df.drop(['Coincide'], axis=1)

    edifcertif = df.shape[0]

    print(df.shape[0])
    df['Coincide'] = np.where((df['C_CCAA']== df['CAutonoma']), 'Si','No_data')
    df = df.loc[(df['Coincide'] == 'Si')]
    df = df.drop(['Coincide'], axis=1)
    print(df.shape[0])

    g = df.shape[0]

    # Les doy los m2 certificados por letra que tienen
    df.insert(0, 'G_CO2_m2', np.where(df['G_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'F_CO2_m2', np.where(df['F_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'E_CO2_m2', np.where(df['E_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'D_CO2_m2', np.where(df['D_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'C_CO2_m2', np.where(df['C_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'B_CO2_m2', np.where(df['B_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'A_CO2_m2', np.where(df['A_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'G_EP_m2', np.where(df['G_EP']>0, df['m2_certificados'],0))
    df.insert(0, 'F_EP_m2', np.where(df['F_EP']>0, df['m2_certificados'],0))
    df.insert(0, 'E_EP_m2', np.where(df['E_EP']>0, df['m2_certificados'],0))
    df.insert(0, 'D_EP_m2', np.where(df['D_EP']>0, df['m2_certificados'],0))
    df.insert(0, 'C_EP_m2', np.where(df['C_EP']>0, df['m2_certificados'],0))
    df.insert(0, 'B_EP_m2', np.where(df['B_EP']>0, df['m2_certificados'],0))
    df.insert(0, 'A_EP_m2', np.where(df['A_EP']>0, df['m2_certificados'],0))

    # Les doy los Bienes Inmuebles certificados por letra que tienen
    df.insert(0, 'G_CO2_BI', np.where(df['G_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'F_CO2_BI', np.where(df['F_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'E_CO2_BI', np.where(df['E_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'D_CO2_BI', np.where(df['D_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'C_CO2_BI', np.where(df['C_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'B_CO2_BI', np.where(df['B_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'A_CO2_BI', np.where(df['A_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'G_EP_BI', np.where(df['G_EP']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'F_EP_BI', np.where(df['F_EP']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'E_EP_BI', np.where(df['E_EP']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'D_EP_BI', np.where(df['D_EP']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'C_EP_BI', np.where(df['C_EP']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'B_EP_BI', np.where(df['B_EP']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'A_EP_BI', np.where(df['A_EP']>0, df['Numero_de_BI_certificados'],0))

    num_edif_resid = df.loc[df.loc[:, 'Uso_certificado'] == 'Residencial - Bloque completo o unifamiliar'].shape[0]
    num_edif_terc = df.loc[df.loc[:, 'Uso_certificado'] == 'Terciario - Edificio completo'].shape[0]

    #df.to_csv(b1_output + r"\Datosalfanum_14_digit" + "prueba" + ".csv", index=False)
    df.to_parquet(b1_output + r"\Datosalfanum_14_digit" + ".gzip", compression='gzip', index=False)
    df_14_digits = df

    # Building unit scale. 20 digit cadastral reference
    df = EPC_database_20_digits
    try: 
        cat = (pd.read_parquet(alphanumeric_cadastre_database_building_units))
    except:
        cat = (pd.read_csv(alphanumeric_cadastre_database_building_units, skiprows=0))

    # Columnas que queremos conservar en el df, las que no estén aquí se borrarán
    colsusar = ['Referencia_BI', 'Provincia', 'S_Viv', 'S_Ind', 'S_Of', 
        'S_Com', 'S_Dep', 'S_Esp', 'S_Host', 
        'S_San', 'S_Cult', 'S_Rel', 'S_Sin',
        'Uso_princial']
    cat = cat[cat.columns.intersection(colsusar)]

    # Al valor de la provincia del catastro le asigno su CCAA correspondiente
    cat.insert(1, 'CAutonoma', cat.Provincia) 
    cat.CAutonoma.replace ({'04':1, '11':1, '14':1, '18':1, '21':1, '23':1, '29':1, '41':1,
                            '22':2, '44':2, '50':2, '33':3, '07':4, '35':5, '38':5, '39':6,
                            '05':7, '09':7, '24':7, '34':7, '37':7, '40':7, '42':7, '47':7, '49':7,
                            '02':8, '13':8, '16':8, '19':8, '45':8, 
                            '08':9, '17':9, '25':9, '43':9, '03':10, '12':10, '46':10, 
                            '06':11, '10':11, '15':12, '27':12, '32':12, '36':12, 
                            '28':13, '30':14, '31':15, '01':16, '48':16, '20':16,
                            '26':17, '51':18, '52':19
                            }, inplace=True)

    # Numero de EPC antes de la unión
    c = df.shape[0]

    df = pd.merge(df, cat, left_on='ReferenciaCatastral_BI', right_on='Referencia_BI')
    # El uso industrial finalmente lo elimino: df['S_Ind']+
    df.insert(0, 'm2_certificados', np.where(df['S_Viv']!=0,df['S_Viv'],(df['S_Of']+df['S_Com']+df['S_Dep']+df['S_Esp']+df['S_Host']+df['S_San']
                                                                        +df['S_Cult']+df['S_Rel']+df['S_Sin'])))

    df.insert(0, 'Numero_de_BI_certificados', 1)

    df.insert(0, 'Uso_certificado', np.where(df['S_Viv']!=0,"Residencial - Vivienda invidual o unifamiliar","Terciario - Local"))

    d = df.shape[0]

    print(df.shape[0])

    pre_borrar = df.shape[0]
    # Esto son errores de que han certificado bienes inmuebles con elementos constructivos de uso almacén-estacionamiento y similares y estos no puede ser certificados, se eliminan por tanto.
    df ['m2_certificados'] = df ['m2_certificados']. fillna('None')
    df['Coincide'] = np.where((df['m2_certificados']!= 'None'), 'Si','Bien')
    df = df.loc[(df['Coincide'] == 'Si')]
    duplicados = df.shape[0] - pre_borrar
    if duplicados != 0:
        print ('Se han borrado por none ' + str(duplicados) + ' bi')

    df['Coincide'] = np.where((df['m2_certificados']!= 0), 'Si','Bien')
    df = df.loc[(df['Coincide'] == 'Si')]
    df = df.drop(['Coincide'], axis=1)

    bicertif = df.shape[0]

    print(df.shape[0])
    df['Coincide'] = np.where((df['C_CCAA']== df['CAutonoma']), 'Si','No_data')
    df = df.loc[(df['Coincide'] == 'Si')]
    df = df.drop(['Coincide'], axis=1)
    print(df.shape[0])

    h = df.shape[0]

    # Les doy los m2 certificados por letra que tienen
    df.insert(0, 'G_CO2_m2', np.where(df['G_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'F_CO2_m2', np.where(df['F_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'E_CO2_m2', np.where(df['E_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'D_CO2_m2', np.where(df['D_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'C_CO2_m2', np.where(df['C_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'B_CO2_m2', np.where(df['B_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'A_CO2_m2', np.where(df['A_CO2']>0, df['m2_certificados'],0))
    df.insert(0, 'G_EP_m2', np.where(df['G_EP']>0, df['m2_certificados'],0))
    df.insert(0, 'F_EP_m2', np.where(df['F_EP']>0, df['m2_certificados'],0))
    df.insert(0, 'E_EP_m2', np.where(df['E_EP']>0, df['m2_certificados'],0))
    df.insert(0, 'D_EP_m2', np.where(df['D_EP']>0, df['m2_certificados'],0))
    df.insert(0, 'C_EP_m2', np.where(df['C_EP']>0, df['m2_certificados'],0))
    df.insert(0, 'B_EP_m2', np.where(df['B_EP']>0, df['m2_certificados'],0))
    df.insert(0, 'A_EP_m2', np.where(df['A_EP']>0, df['m2_certificados'],0))

    # Les doy los Bienes Inmuebles certificados por letra que tienen
    df.insert(0, 'G_CO2_BI', np.where(df['G_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'F_CO2_BI', np.where(df['F_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'E_CO2_BI', np.where(df['E_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'D_CO2_BI', np.where(df['D_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'C_CO2_BI', np.where(df['C_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'B_CO2_BI', np.where(df['B_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'A_CO2_BI', np.where(df['A_CO2']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'G_EP_BI', np.where(df['G_EP']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'F_EP_BI', np.where(df['F_EP']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'E_EP_BI', np.where(df['E_EP']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'D_EP_BI', np.where(df['D_EP']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'C_EP_BI', np.where(df['C_EP']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'B_EP_BI', np.where(df['B_EP']>0, df['Numero_de_BI_certificados'],0))
    df.insert(0, 'A_EP_BI', np.where(df['A_EP']>0, df['Numero_de_BI_certificados'],0))

    num_BI_resid = df.loc[df.loc[:, 'Uso_certificado'] == 'Residencial - Vivienda invidual o unifamiliar'].shape[0]
    num_BI_terc = df.loc[df.loc[:, 'Uso_certificado'] == 'Terciario - Local'].shape[0]

    #df.to_csv(b1_output + r"\Datosalfanum_20_digit" + "prueba" + ".csv", index=False)
    df.to_parquet(b1_output + r"\Datosalfanum_20_digit" + ".gzip", compression='gzip', index=False)

    print(df.columns)

    with open(b1_output + r'\InformeUnionesEPCyAlfanumerico' + ".txt", 'w') as f:
            f.write('De la BBDD de EPC con 14 dígitos hay ' + str(a) + ' certificados de edificios (Referencia Catastral de 14 dígitos) \n'
                    + 'Tras la unión con el cat alfanumerico hay ' + str(b) + ' certificados de edificios (Referencia Catastral de 14 dígitos) \n'
                    + 'Tras eliminar los EPC los que tienen 0 m2 certificables hay ' + str(edifcertif) + ' certificados de bienes inmuebles (Referencia Catastral de 14 dígitos) \n'            
                    + 'Y tras eliminar los EPC registrados en CCAA que no son la del edificio quedan: ' + str(g) + ' certificados de edificios (Referencia Catastral de 14 dígitos) \n'
                    + 'De la BBDD de EPC con 18 dígitos hay ' + str(c) + ' certificados de bienes inmuebles (Referencia Catastral de 18 + 2 dígitos) \n'
                    + 'Tras la unión con el cat alfanumerico hay ' + str(d) + ' certificados de bienes inmuebles (Referencia Catastral de 18 + 2 dígitos) \n'
                    + 'Tras eliminar los EPC los que tienen 0 m2 certificables hay ' + str(bicertif) + ' certificados de bienes inmuebles (Referencia Catastral de 18 + 2 dígitos) \n'            
                    + 'Y tras eliminar los EPC registrados en CCAA que no son la del edificio quedan: ' + str(h) + ' certificados de bienes inmuebles (Referencia Catastral de 18 + 2 dígitos) \n'
                    + 'De edificios han fallado ' + str(a-g) + ' certificados de edificios, un ' + str((a-g)*100/a) + ' porciento han fallado \n'
                    + 'De BI han fallado ' + str(c-h) + ' certificados de BI, un ' + str((c-h)*100/c) + ' porciento han fallado \n'
                    + 'En total hay: ' + str(num_edif_resid) + ' certificados de edificios residenciales (Referencia Catastral de 14 dígitos) \n' 
                    + 'En total hay: ' + str(num_BI_resid) + ' certificados de bienes inmuebles residenciales (Referencia Catastral de 18 + 2 dígitos) \n' 
                    + 'En total hay: ' + str(num_edif_terc) + ' certificados de edificios no residenciales (Referencia Catastral de 14 dígitos) \n' 
                    + 'En total hay: ' + str(num_BI_terc) + ' certificados de bienes inmuebles no residenciales (Referencia Catastral de 18 + 2 dígitos) \n' 
                    )
    print ('De la BBDD de EPC con 14 dígitos hay ' + str(a) + ' certificados de edificios (Referencia Catastral de 14 dígitos) \n'
                    + 'Tras la unión con el cat alfanumerico hay ' + str(b) + ' certificados de edificios (Referencia Catastral de 14 dígitos) \n'
                    + 'Tras eliminar los EPC los que tienen 0 m2 certificables hay ' + str(edifcertif) + ' certificados de bienes inmuebles (Referencia Catastral de 14 dígitos) \n'            
                    + 'Y tras eliminar los EPC registrados en CCAA que no son la del edificio quedan: ' + str(g) + ' certificados de edificios (Referencia Catastral de 14 dígitos) \n'
                    + 'De la BBDD de EPC con 18 dígitos hay ' + str(c) + ' certificados de bienes inmuebles (Referencia Catastral de 18 + 2 dígitos) \n'
                    + 'Tras la unión con el cat alfanumerico hay ' + str(d) + ' certificados de bienes inmuebles (Referencia Catastral de 18 + 2 dígitos) \n'
                    + 'Tras eliminar los EPC los que tienen 0 m2 certificables hay ' + str(bicertif) + ' certificados de bienes inmuebles (Referencia Catastral de 18 + 2 dígitos) \n'   
                    + 'Y tras eliminar los EPC registrados en CCAA que no son la del edificio quedan: ' + str(h) + ' certificados de bienes inmuebles (Referencia Catastral de 18 + 2 dígitos) \n'
                    + 'De edificios han fallado ' + str(a-g) + ' certificados de edificios, un ' + str((a-g)*100/a) + ' porciento han fallado \n'
                    + 'De BI han fallado ' + str(c-h) + ' certificados de BI, un ' + str((c-h)*100/c) + ' porciento han fallado \n'
                    + 'En total hay: ' + str(num_edif_resid) + ' certificados de edificios residenciales (Referencia Catastral de 14 dígitos) \n' 
                    + 'En total hay: ' + str(num_BI_resid) + ' certificados de bienes inmuebles residenciales (Referencia Catastral de 18 + 2 dígitos) \n' 
                    + 'En total hay: ' + str(num_edif_terc) + ' certificados de edificios no residenciales (Referencia Catastral de 14 dígitos) \n' 
                    + 'En total hay: ' + str(num_BI_terc) + ' certificados de bienes inmuebles no residenciales (Referencia Catastral de 18 + 2 dígitos) \n' 
                    )

    duracion_A = time() - inicio
    # print('En total ha tardado: ' + str(duracion_A) + ' segundos')

    # print ('Terminado')

    return df_14_digits, df
