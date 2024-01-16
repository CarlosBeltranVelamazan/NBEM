# Para aligerar el peso de los archivos (todos los edificios de España comprimidos en .zip son 5 gb, descomprimidos son 150 gb incluyendo capa buildings, buildingsparts y other constructions)
# eliminamos las capas que no vamos a usar: buildingsparts y other constructions. Así es más sencillo trabajar y el peso es mucho menor. Quitando esas capas el peso es de 59 gb.
import os
import pandas as pd
import polars as pl
import geopandas as gpd
import geopolars as gpl
import numpy as np
from time import time

def list_gml_files(folder_path):
    gml_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.gml'):
                gml_files.append(os.path.join(root, file))
    return gml_files

def combine_gml_files_to_geoparquet(folder_path, output_file, Coordinate_Reference_System, drop_duplicates):
    gml_files = list_gml_files(folder_path)

    # Initialize an empty GeoDataFrame
    combined_gdf = gpd.GeoDataFrame()

    # Read each GML file, transform to a common CRS, and append it to the GeoDataFrame
    for gml_file in gml_files:
        print('Merging:' + gml_file)
        gdf = gpd.read_file(gml_file)
        
        # Check if the GeoDataFrame has a CRS, and transform to the common CRS if needed
        if gdf.crs and gdf.crs != Coordinate_Reference_System:
            gdf = gdf.to_crs(Coordinate_Reference_System)

        combined_gdf = combined_gdf._append(gdf)
    
    if drop_duplicates == True: # Drop duplicates based on the "reference" column. 14 digits cadastral reference.
        before_duplicates_count = len(combined_gdf)
        combined_gdf = combined_gdf.drop_duplicates(subset='reference')
        after_duplicates_count = len(combined_gdf)
        deleted_buildings_count = before_duplicates_count - after_duplicates_count
        print(f'Deleted {deleted_buildings_count} duplicate buildings.')

    # Save the combined GeoDataFrame to GeoParquet
    combined_gdf.to_parquet(output_file, index=False)

def Merge_files (folder_download_INSPIRE_zips, folder_INSPIRE, Coordinate_Reference_System, drop_duplicates):
    print('Merging building files')
    output_file = folder_INSPIRE + '\\' + r'GIS_INSPIRE_Buildings' + r'.parquet'
    combine_gml_files_to_geoparquet(folder_download_INSPIRE_zips, output_file, Coordinate_Reference_System, drop_duplicates)
    print(f'Combined GML files into {output_file}')
    print ('GIS map with all the buildings from the Spanish INSPIRE Cadastre created')


