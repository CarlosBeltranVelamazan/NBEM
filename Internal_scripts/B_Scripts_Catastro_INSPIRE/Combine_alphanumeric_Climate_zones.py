import pandas as pd
from time import time

def Assign_climate_zone(climate_zone_map, Inspire_buildings, b2_output, buildings_with_climate_zones_name):

   inicio = time()

   # Debo unir C_minicip de las tablas con los municipios y sus ZC y unirlo con Provincia + CMunicipioINE
   dtype_dict = {'C_minicip': str}
   climate_map = pd.read_csv(climate_zone_map, dtype=dtype_dict)

   #dtype_dict = {'Provincia': 'str', 'CMunicipioINE': 'str'}
   edificios = pd.read_parquet(Inspire_buildings)

   duracion = time() - inicio
   print('Ha leído el GIS en ' + str(duracion) + ' segundos')


   edificios['Provincia'] = edificios['Provincia'].astype(str)
   edificios['CMunicipioINE'] = edificios['CMunicipioINE'].astype(str)
   edificios['CMunicipioINE_completo'] = edificios['Provincia'] + edificios['CMunicipioINE']

   #print(edificios['Provincia'])
   #print(edificios['CMunicipioINE'])
   #print(edificios['CMunicipioINE_completo'])
   #print(edificios.dtypes)
   # Realizar la unión por las columnas especificadas
   resultado = pd.merge(edificios, climate_map[['C_minicip', 'Zona_Clima']], left_on='CMunicipioINE_completo', right_on='C_minicip')
   resultado.drop('C_minicip', axis=1, inplace=True)

   resultado.to_parquet(b2_output + buildings_with_climate_zones_name + ".gzip", compression='gzip', index=False)
   resultado.to_csv(b2_output + buildings_with_climate_zones_name + ".csv")

   duracion = time() - inicio
   print('Ha completado la asignación de zona clima a los edificios en ' + str(duracion) + ' segundos')
