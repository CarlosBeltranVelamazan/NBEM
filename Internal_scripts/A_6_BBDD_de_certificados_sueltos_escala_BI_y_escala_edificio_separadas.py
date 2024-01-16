# Separo la BBDD en certificados a escala edificio y a escala de bien inmueble (14 y 20 dígitos de referencia catastral)
# Nota: Esto se hace para unirlo con la BBDD del catastro alfanumérico y darle a los edificios su superficie certificada y los BI la suya
# para poder conocer la superficie y el nº de viviendas y locales certificados (edificios todos y bi uno por certificado)

def Separar_14_y_20_difitos_RefCat (Carpeta_archivos_leer, Carpeta_archivos_guardar, file, Certificados_uso):

        import os
        import pandas as pd
        import numpy as np
        import xlrd 
        print ("Empieza el proceso de separar la BBDD nacional en datos por BI (Referencia catastral de 20 dígitos) y datos por edificio (Referencia catastral de 14 dígitos)") 

        TipoEdificio = Certificados_uso
        os.makedirs('BBDD_Unidas por Referencia Catastral', exist_ok=True)

        switch_BBDD = {
                0: Carpeta_archivos_leer,
                1: Carpeta_archivos_leer,
                2: Carpeta_archivos_leer}

        archivo = switch_BBDD.get(TipoEdificio) + file
        df = (pd.read_csv(archivo))
        df.insert(1, 'Digitos_RefCat', df['ReferenciaCatastral'].str.len())

        # Nota importante: El criterio para separar es este, edificios son 14 dígitos, los separo. Bienes inmuebles son 20 dígitos siempre (en realidad 18 + 2 letras de control), sin embargo hay casos que certifican varias viviendas para salvar el certificado en BI dejo todos y las referencias las corto a 20 dígitos. De esta manera el certificado se unirá con esa vivienda (al menos el certificado sigue siendo válido, se podría crear un certificado para cada BI pero hay mucha casuística de errores y saldrían más certificados finales que iniciales y eso es raro)
        # Corto por los 18 caracteres para unirlo con el catastro alfanumérico. Con este criterio empleado no hay un filtrado de errores de referencias catastrales, el filtrado se hace al unirlo con el catastro alfanumérico, si no se une es una referencia catastral incorrecta.

        edif = df.loc[df.loc[:, 'Digitos_RefCat'] == 14]        # Referencias catastrales de edificios
        df = df.loc[df.loc[:, 'Digitos_RefCat'] != 14]          # El resto de Referencias catastrales (ver nota importante)
        # inmuebles = df.loc[df.loc[:, 'Digitos_RefCat'] == 20] # Referencias catastrales de bienes inmuebles
        # df = df.loc[df.loc[:, 'Digitos_RefCat'] != 20]        # Referencias catastrales no válidas (ver nota importante)
        df.ReferenciaCatastral = df['ReferenciaCatastral'].str[:18]     # Ver nota importante

        # edif.to_parquet(Carpeta_archivos_guardar + file + '_14DigitRefCat' + ".gzip", compression='gzip', index=False)
        # inmuebles.to_parquet(Carpeta_archivos_guardar + file + '_20DigitRefCat' + ".gzip", compression='gzip', index=False)
        # df.to_parquet(Carpeta_archivos_guardar + file + '_ErroresRefCat' + ".gzip", compression='gzip', index=False)
        nombre = file.split('.', 1)

        edif.to_csv(Carpeta_archivos_guardar + nombre[0] + '_14DigitRefCat' + ".csv", index=False)
        df.to_csv(Carpeta_archivos_guardar + nombre[0] + '_20DigitRefCat' + ".csv", index=False)

        with open(Carpeta_archivos_guardar + nombre[0] + '_InformeErroresRefCat' + ".txt", 'w') as f:
                f.write('La BBDD completa tiene ' + str(edif.shape[0]) + ' certificados de edificios (Referencia Catastral de 14 dígitos) \n'
                         + str(df.shape[0]) + ' certificados de bienes inmuebles (Referencia Catastral de 20 dígitos)'
                        )


        print ('Terminado de separar por 14 y 20 dígitos')

