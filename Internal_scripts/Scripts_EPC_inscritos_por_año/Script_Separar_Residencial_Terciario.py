def Separar(archivo, ccaa):
    import pandas as pd
    import numpy as np
    import xlrd 
    try:
        df = (pd.read_excel(archivo, skiprows=0))
    except:
        df = (pd.read_csv(archivo, skiprows=0))
    df_residencial = pd.DataFrame()
    df_terciario = pd.DataFrame()

    # Errores en la referencia catastral
    a = df.shape[0] # Nos da el número de filas, total de los certificados
    df_VivUnifamiliar = df.loc[df.loc[:, 'TipoEdificio'] == 'Residencial - Vivienda unifamiliar'] # Copia los valores que son Residencial - Vivienda unifamiliar
    df_VivIndividual = df.loc[df.loc[:, 'TipoEdificio'] == 'Residencial - Vivienda individual'] # Copia los valores que son Residencial - Vivienda individual
    df_BloqueCompleto = df.loc[df.loc[:, 'TipoEdificio'] == 'Residencial - Bloque completo'] # Copia los valores que son Residencial - Bloque completo
    b = df_VivUnifamiliar.shape[0]
    c = df_VivIndividual.shape[0]
    d = df_BloqueCompleto.shape[0]
    df_Local = df.loc[df.loc[:, 'TipoEdificio'] == 'Terciario - Local'] # Copia los valores que son Terciario - Local
    df_EdificioCompleto = df.loc[df.loc[:, 'TipoEdificio'] == 'Terciario - Edificio completo'] # Copia los valores que son Terciario - Edificio completo
    e = df_Local.shape[0]
    f = df_EdificioCompleto.shape[0]
    df_residencial = pd.concat([df_VivUnifamiliar, df_VivIndividual, df_BloqueCompleto], axis=0)
    df_terciario = df.loc[df.loc[:, 'TipoEdificio'] != 'Residencial - Vivienda unifamiliar']
    df_terciario = df_terciario.loc[df.loc[:, 'TipoEdificio'] != 'Residencial - Vivienda individual']
    df_terciario = df_terciario.loc[df.loc[:, 'TipoEdificio'] != 'Residencial - Bloque completo']
    g = df_residencial.shape[0]
    h = df_terciario.shape[0]
    i = h-e-f
    informe = pd.DataFrame({'Comunidad autónoma':[ccaa], 'Total de certificados':[a], 'Total de certificados residencial':[g],
                'Total de certificados terciario':[h],'Total de certificados Residencial - Vivienda unifamiliar':[b],'Residencial - Vivienda individual':[c],'Residencial - Bloque completo':[d],
                'Terciario - Local':[e], 'Terciario - Edificio completo':[f],'Terciario - Otros':[i]})
    return df_residencial, df_terciario, informe
