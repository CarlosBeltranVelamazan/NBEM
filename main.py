"""                                         National-scale Building Energy Model based on Energy Performance Certificates in European countries

This script handles the entire automate process in python to generate the national-scale Building Energy Model based on Energy Performance Certificates in European countries shown in:

The code in this repository (https://github.com/CarlosBeltranVelamazan/NBEM) generates the UBEM model on a national scale following the methodology published in:
"A new approach for national-scale Building Energy Models based on Energy Performance Certificates in European countries: the case of Spain", doi: https://doi.org/10.1016/j.heliyon.2024.e25473.
The paper is published in Heliyon, at the following link https://www.sciencedirect.com/science/article/pii/S2405844024015044?via%3Dihub.

The authorship of this code belongs to Carlos Beltrán-Velamazán, Marta Monzón-Chavarrías and Belinda López-Mesa from the University of Zaragoza (Spain). 
Additional info: This is an open access paper distributed under the Creative Commons Attribution License which permits unrestricted use, distribution, 
and reproduction in any medium, provided the original work is properly cited. For any use of the model or code, the paper from Heliyon must be cited.
For any questions, problems or suggestions write an email to: cbeltran@unizar.es

If you use this tool please cite the paper: Carlos Beltrán-Velamazán, Marta Monzón-Chavarrías, Belinda López-Mesa, 
A new approach for national-scale Building Energy Models based on Energy Performance Certificates in European countries: The case of Spain, 
Heliyon, Volume 10, Issue 3, 2024, e25473, ISSN 2405-8440, https://doi.org/10.1016/j.heliyon.2024.e25473.

This script controls all the steps as shown in the aforementioned paper. To generate each step, its main variable must be marked as True 
and the internal steps that we want to perform must be defined. Please pay attention to the notes indicated in each step to generate the model. 
As the process is executed, folders will be created with the information generated.

 Data management and Model generation steps:
      - A.1: Management of EPCs in python
      - A.2: Alphanumeric cadastre
      - A.3: INSPIRE cadastre

                                                        HOW TO MANAGE THE MODEL

The model is controlled directly from this script, it is not necessary to enter or modify the rest of the internal scripts to generate the model.
Each step and substep can be executed separately independently and contains True or False variables to control each step and substep of the process and numerical variables to choose between different options to generate the model.
Please read the notes of each step carefully as they contain important information to be able to generate the model, step B require have the information from steps A that they need.
In each step, the notes include the recommended configuration to generate the model and the expected results at each step with the recommended configuration.
"""

 # Step 0 - Select the scale of the model
 # First of all, we must choose the scale of the model, national scale (Spain) or a single Autonomous Community (AC).
 # A value to the variable called CCAA must be givben, that value corresponds to the following switch switch_CCAA to select the country scale (Spain is the value 0)
 # or a single Autonomous Community (values 1 to 19). All the Autonomous Communities and autonomous cities are included to provide the data,
 # but currently the Autonomous Communities of Murcia, Extremadura, Madrid, the Basque Country, Ceuta and Melilla are not providing the EPCs in open acess.

CCAA = 0                             # Autonomous Community (select a value from the switch_CCAA)

switch_CCAA = {
    0: 'España',    # Spain: the entire country (refer to the paper in Heliyon where data availability is explained according to the autonomous community and data type)
	1: 'Andalucía',
	2: 'Aragón',
	3: 'Asturias, Principado de',
 	4: 'Balears, Illes',
	5: 'Canarias',
	6: 'Cantabria',
    7: 'Castilla y León',
	8: 'Castilla - La Mancha',
	9: 'Cataluña',
 	10: 'Comunitat Valenciana',  
	11: 'Extremadura',
	12: 'Galicia',    
 	13: 'Madrid, Comunidad de',
	14: 'Murcia, Región de',
 	15: 'Navarra, Comunidad Foral de',
	16: 'País Vasco',
	17: 'Rioja, La',
    18: 'Ceuta',
    19: 'Melilla',
    }

# Step A.0, Create folders to store the data - Just the first time, will create the structure of folders to or contain the input data or the steps or the output
                                                                          # The neccesary folders are:
                                                                          # Internal scripts: Contains the code to generate the model
folder_read_EPC = r'Downloaded_EPC_databases'                             # The folder where the files of the EPCs will be read from and if the download option is chosen the EPCs files will be saved 
folder_save_EPC_modificed = r'Modified_EPC_Databases'                     # The folder where the generated files will be saved
folder_read_Alphanumeric_cadastre = r'Alphanumeric_cadastre'              # The folder to store the zip files from the Alphanumeric Cadastre
folder_INSPIRE = r'INSPIRE_cadastre'                                      # The folder with all the data and models from the INSPIRE Cadastre
folder_txt_INSPIRE = r'INSPIRE_cadastre\Original_txt_links'               # Additional feature: It allows updating the download links for the Inspire cadastre that will be used by the algorithm, contains the raw text of the webs with the links.
folder_INSPIRE_links = r'INSPIRE_cadastre\Automated_links'                # Contains the txt with the links to the INSPIRE Cadastre ready to download
folder_download_INSPIRE_zips = r'INSPIRE_cadastre\INSPIRE_files'          # Contains the downloaded INSPIRE Cadastre zips


Step_A_0 = True     # Create folders to store the data
if Step_A_0 == True:
    import os
    os.makedirs(folder_read_EPC, exist_ok=True)
    os.makedirs(folder_save_EPC_modificed, exist_ok=True)
    os.makedirs(folder_read_Alphanumeric_cadastre, exist_ok=True)
    os.makedirs(folder_txt_INSPIRE, exist_ok=True)
    os.makedirs(folder_INSPIRE_links, exist_ok=True)
    os.makedirs(folder_download_INSPIRE_zips, exist_ok=True)

# Step A.1, Management of EPC in python - To use this step mark the variable Step_A_1 as True and provide the rest of the information required. Please see notes below.
Step_A_1 = False
if Step_A_1 == True:
    from Internal_scripts import A_Script_clave

    Download_EPCs_DDBB = True                               # Step A.1.1. Download the data from the public EPCs Databases (True or False) (see notes below)
    Homogenize_DDBB = True                                  # Step A.1.2. Homogenize the databases (True or False) (necessary for the following steps)
    Filter_by_date = True                                   # Step A.1.3. Filter by certificate registration date (True or False)
    Filter_date = 2023                                      # Step A.1.3. Date included in the range that we want to filter (must be a year), also filter the EPCs registered before 2010 as errors. If we put 2019, we will use all certificates prior to 1/1/2020, (integer)
    Certificates_date_used = 1                              # Step A.1.3. To use all the data (0), those before the date of filtering (1) or those after the date of filtering (2)
    Divide_by_use_EPCs = False                              # To divide the dataset by the use of the EPC into residential or non-residential (True or False) (*)
    Use_EPCs = 0                                            # To use all the data (0), those for residential use (1) or those for tertiary use (2) (*)
    Detect_errors = True                                    # Step A.1.3. Detect errors and outlier values (True o False) (necessary for the following steps)
    Join_by_RefCat = False                                  # To join the EPCs by cadastral reference (group by building) (True or False) (*)
    EPCs_joined_by_RefCat = 0                               # To use the single EPCs data (0), or the data grouped by building (grouped by Cadastral Reference) (1) (*)
    Join_DDBB_Spain = True                                  # Join all the EPCs DDBB in a single database at national level (True or False) (necessary for the following steps)
    Divide_into_buildings_and_buildings_units = True        # Result Step A.1. Divide the dataset into building or real estate certificates (14 or 20 digits of cadastral reference) (True or False)



    A_Script_clave.EPCs (folder_read_EPC, folder_save_EPC_modificed, CCAA, Download_EPCs_DDBB, Homogenize_DDBB, Filter_by_date, Filter_date, Certificates_date_used, Divide_by_use_EPCs, Use_EPCs, Detect_errors, 
                  Join_by_RefCat, EPCs_joined_by_RefCat, Join_DDBB_Spain, Divide_into_buildings_and_buildings_units)

    """ 
    Notes about the Step A.1:

        1 - To generate the cbc-NBEM the recommended configuration is:
                Download_EPCs_DDBB = True       # (just once)           # Step A.1.1. Download the data from the public EPCs Databases (True or False) (see notes below)
                Homogenize_DDBB = True                                  # Step A.1.2. Homogenize the databases (True or False) (necessary for the following steps)
                Filter_by_date = True                                   # Step A.1.3. Filter by certificate registration date (True or False)
                Filter_date = 2023                                      # Step A.1.3. Date included in the range that we want to filter (must be a year), also filter the EPCs registered before 2010 as errors. If we put 2019, we will use all certificates prior to 1/1/2020, (integer)
                Certificates_date_used = 1                              # Step A.1.3. To use all the data (0), those before the date of filtering (1) or those after the date of filtering (2)
                Divide_by_use_EPCs = False                              # To divide the dataset by the use of the EPC into residential or non-residential (True or False) (*)
                Use_EPCs = 0                                            # To use all the data (0), those for residential use (1) or those for tertiary use (2) (*)
                Detect_errors = True                                    # Step A.1.3. Detect errors and outlier values (True o False) (necessary for the following steps)
                Join_by_RefCat = False                                  # To join the EPCs by cadastral reference (group by building) (True or False) (*)
                EPCs_joined_by_RefCat = 0                               # To use the single EPCs data (0), or the data grouped by building (grouped by Cadastral Reference) (1) (*)
                Join_DDBB_Spain = True                                  # Join all the EPCs DDBB in a single database at national level (True or False) (necessary for the following steps)
                Divide_into_buildings_and_buildings_units = True        # Result Step A.1. Divide the dataset into building or real estate certificates (14 or 20 digits of cadastral reference) (True or False)
                folder_read_EPC = 'Downloaded_EPC_databases'                    # The folder where the files of the EPCs will be read from and if the download option is chosen the EPCs files will be saved 
                folder_save_EPC_modificed = 'Modified_EPC_Databases'          # The folder where the generated files will be saved
        
        2 - (*) In the final version of the cbc-NBEM these steps are not used, however, as they may be useful, the option of generating the data using these functionalities has been maintained. 
            To generate the cbc-NBEM it is recommended to set the values marked with (*) to False or 0 as appropriate.
        
        3 - During the execution of the code, several print commands have been written that will appear, they are written in Spanish, in general they offer information about the process or some minor notes about what is being generated.
        
        4 - Step A.1.1. Download the data from the public EPCs Databases:
            The script to download the databases of the EPCs cannot download all of them, this is the list of exceptions:
                - In the AC (Autonomous Community) of Asturias there is a problem with a protocol because the website is old, you have to use Internet explorer to download the file.
                To download the Asturias Database go to: https://datos.gob.es/es/catalogo/a03002951-eficiencia-energetica-edif-viv
                - The AC of Galicia has a capcha of I am not a robot and as I am a robot prefer to not automate it.
                To download the Galicia Database go to: https://datos.gob.es/es/catalogo/a12002994-registro-de-certificados-de-eficiencia-energetica-de-edificios-de-galicia
            Additional notes: It has already happened that file formats and encodings change over time, it can happen and might involve adapt the code, just indicate that:
                - The Castellón database from 2014 has a character that is not valid and causes problems, it is best to delete it by hand, open it
                with notepad, it is at the address of the certificate with cadastral ref E2014VB017159, you must open the file and delete it from the address.
                It is the character that is just behind the PT8 in the direction, removing it works fine.
                - Navarra is in the process of reforming the DB, which will surely have changes.
                - Castilla y León gives a complex to read xls, it is best to open it with excel or similar and save it in xlsx (check that the values of primary energy, CO2 and such are read as dates of the xls, and put it in number format)
                - Castilla la Mancha and the Canary Islands give a zip, it must be extracted
                - Galicia gives a csv with problems due to the address (the text is without quotes), that is already resolved in the code itself, you don't have to do anything
                - Andalusia gives an xml that causes problems, you have to open it and save it in excel, this causes the certificates to quadruple due to a problem with
                the labels but the code already implemented solves it and all the information is fine.
        
        5 - Step A.1.3. Outlier detection. Currently this step filters the EPCs data with the criteria indicated in the paper, 
            this criteria can be modified internally by modifying the script 'A_3_Eliminar_datos_incorrectos' and the scripts in the "Scripts_eliminar_incorrect_data" folder.
            If you wish to modify the filtering criteria, a careful study of the data is recommended for this modification due to the wide range of errors and anomalous data that the EPCs present.
        
        6 - Output: Following the recommended configuration for the cbc-NBEM the main results of all step A.1 
            are found in the folder: "BBDD_Unidas por Referencia Cadastral" and the file is named 'Todos_los_certificados_España_Pre_2024' ('All the EPCs in Spain before the data selected'),
            this file contains all the EPCs registered in the databases that we have used as input, already in a homogeneous format and with filtered errors. 
            And within the same folder there is a folder called "Parquet" where we have the same file dividing the certificates into 14-digit (building EPCs) 
            and 20-digit (real estate EPCs), these two files will be the input that will be used in step B.1 to generate the model.
        
        7 - Intermediate files: Once step A.1 is completed, the intermediate results obtained as well as the reports that are generated in the process are not necessary and 
            can be deleted to reduce the consumption of space on the hard drive. These files are not automatically deleted since they allow working by substeps and 
            being able to identify and resolve problems during the execution of this step, but upon successful completion they can be deleted.
            The folders that contains those intermediate files that can be deleted are: 'BBDD_Descargadas' ('Downloaded DDBB'), 'BBDD_Modificadas' ('Standarized DDBB'), 'Separados_por_fecha' ('Divided by the data selected'), 'BBDD_ErroresEliminados' ('Errors filtered'). (depending on the configuration chosen, other folders may appear that are also temporary files)
    """

# Step A.2, Alphanumeric cadastre - To use this step mark the variable Step_A_2 as True and provide the rest of the information required. Please see notes below.
Step_A_2 = False
if Step_A_2 == True:
    from Internal_scripts import E_Script_clave
    import os
    # This step will generate a database with all the buildings in Spain with the information contained in the alphanumeric cadastre.
    # This information is provided at the building scale (14-digit cadastral reference) (set building_scale_cadastre as True).
    # and at the real state scale (20-digit cadastral reference) (set building_unit_scale_cadastre as True).

    # As the alphanumeric cadastre provides information by province, we can select whether we want to work with all of Spain or to generate information from a single province. 
    # To do this, is possible to choose a value in the PROV variable based on the switch_PROV below:
    # All the provincies and autonomous cities are included in the list, but Navarra and the Basque Country are not in the Spanish cadastre so until now there is no information about them.
    PROV = 0                                              # Province (select a value from the switch_PROV)
    switch_PROV = {
        0: 'España',
        1: 'Araba/Álava',
        2: 'Albacete',
        3: 'Alicante/Alacant',
        4: 'Almería',
        5: 'Ávila',
        6: 'Badajoz',
        7: 'Balears, Illes',
        8: 'Barcelona',
        9: 'Burgos',
        10: 'Cáceres',  
        11: 'Cádiz',
        12: 'Castellón/Castelló',    
        13: 'Ciudad Real',
        14: 'Córdoba',
        15: 'Coruña, A',
        16: 'Cuenca',
        17: 'Girona',
        18: 'Granada',
        19: 'Guadalajara',
        20: 'Gipuzkoa',
        21: 'Huelva',
        22: 'Huesca',
        23: 'Jaén',
        24: 'León',
        25: 'Lleida',
        26: 'Rioja, La',
        27: 'Lugo',
        28: 'Madrid',
        29: 'Málaga',
        30: 'Murcia',
        31: 'Navarra',
        32: 'Ourense',
        33: 'Asturias',
        34: 'Palencia',
        35: 'Palmas, Las',
        36: 'Pontevedra',
        37: 'Salamanca',
        38: 'Santa Cruz de Tenerife',
        39: 'Cantabria',
        40: 'Segovia',
        41: 'Sevilla',
        42: 'Soria',
        43: 'Tarragona',
        44: 'Teruel',
        45: 'Toledo',
        46: 'Valencia/València',
        47: 'Valladolid',
        48: 'Bizkaia',
        49: 'Zamora',
        50: 'Zaragoza',
        51: 'Ceuta',
        52: 'Melilla',
        99: 'Error',
        }
    # The list follows the INE Province code: https://www.ine.es/daco/daco42/codmun/cod_provincia.htm (and I add the 0 (Spain))

    # Step A.2.1. 
    # The first step is to download the alphanumeric cadastre information from the Sede Electrónica del Catastro - Difusión de datos catastrales.
    # https://www.sedecatastro.gob.es/Accesos/SECAccDescargaDatos.aspx
    # This step is not automated but can be downloaded province by province from the website itself.
    # The alphanumeric cadastre files in zip format must be saved in the folder: Alphanumeric_cadastre (or define the path to the files)

    # After downloading the files to the folder, this script automatically unzips the zip files and sorts the documents it contains.  (necessary for the following steps)
    Extract_ZIP_files = True

    # Step A.2.2. 
    # The raw information from the alphanumeric cadastre is converted into information about the buildings. 
    # This step is subdivided into two substeps, generating the information at the building and real state scale.

    building_scale_cadastre = True                            # Process the CAT files to obtain the information by building at the province scale
    building_unit_scale_cadastre = True                       # Process the CAT files to obtain the information by building unit at the province scale

    # Step A.2.3. Done automatically

    E_Script_clave.Alphanumeric_cadastre (PROV, folder_read_Alphanumeric_cadastre, Extract_ZIP_files, building_scale_cadastre, building_unit_scale_cadastre)

    """ 
    Notes about the Step A.2:

        1 - To generate the cbc-NBEM the recommended configuration is:
                PROV = 0
                folder_read_Alphanumeric_cadastre = 'Alphanumeric_cadastre'
                Extract_ZIP_files = True           # (just once)          # This script automatically unzips the zip files and sorts the documents it contains
                building_scale_cadastre = True                            # Process the CAT files to obtain the information by building at the province scale
                building_unit_scale_cadastre = True                       # Process the CAT files to obtain the information by building unit at the province scale

        2 - During the execution of the code, several print commands have been written that will appear, they are written in Spanish, in general they offer information about the process or some minor notes about what is being generated.
        
        3 - Intermediate files: Step A.2 consumes a large amount of space on the hard drive due to the large size of the files generated. 
            It is highly recommended that once the process is generated, the intermediate files used are deleted.
            The intermediate files that can be deleted are the downloaded zip files and the files located in the folders 'Archivos_descomprimidos' ('Unzipped files'), 'Datos por Provincia' ('Data by province'), Datos por Provincia_escala_BI ('Data by province building unit scale') and the txt reports.
            
        4 - Output: Two final files are generated, one with the information at the building scale and the other with the information at the real estate scale.
            Both are found in the folder: "Datos del Catastro alfanumerico por edificio" ("Data from the alphanumeric cadastre by building") and the files are named 
            "Edificios_España_Completos" ("Buildings in Spain completed") and "Edificios_España_Completos_escala_BI" ("Buildings units in Spain completed").
    """

# Step A.3, INSPIRE cadastre - To use this step mark the variable Step_A_3 as True and provide the rest of the information required. Please see notes below.
Step_A_3 = True
if Step_A_3 == True:
    # This step will generate a GIS map with all the buildings in Spain with the information contained in the INSPIRE cadastre. This information is provided at the building scale (14-digit cadastral reference).

    # Step A.3.1. Download the INSPIRE cadastre data. This step is divided in four parts:

        # Create the download links that will be automated for the massive download of data
            # The INSPIRE cadastre files can be downloaded from the links of the ATOM download service (https://www.catastro.minhap.es/webinspire/index.html), 
            # which can be found at: https://www.catastro.minhafp.es/INSPIRE/buildings/ES.SDGC.BU.atom.xml?_gl=1*1uznbac*_ga*MTI0MTg5ODY0OC4xNjc2OTc0NTg0*_ga_JG5LDK2LGX*MTY5MzU1NjU5NS4xMC4xLjE2OTM1NTY2NDMuMC4wLjA.
            # This website contains a link to an xml of each province of Spain, which contains information on all the municipalities in the province in a zip file by municipality
            # and the link to download the zip file with the information about the buildings from the INSPIRE cadastre.

            # If you prefer, the links already generated for the download have been added to this file, folder 'INSPIRE_cadastre\Automated_links' so that it is not necessary to perform the part 1 and 2 in this step. (Links updated as of 2023).

        # Part 1: (Optional) Update the txt links
            # To generate the updated links if preferred just copy the content of the web of the province including the links with the .zip and the code will clean everything is not the url to download the files
            # As a recommendation, it is advisable to save each txt with the name of the province it contains for easier handle.
            # An additional file will be created containing the number of excepted files downloaded per region in the next step, to ensure that all files have been downloaded. 
    
    encoding_txt = 'utf-8'  # As a recommendation, use 'utf-8', in some cases also 'latin-1' is useful. There are some problems with spanish and catalan letters in the links.
    Step_A_3_1_Part_1 = False
    if Step_A_3_1_Part_1  == True:
        from Internal_scripts.B_Scripts_Catastro_INSPIRE import Update_download_links
        Update_download_links.Automate_links (folder_txt_INSPIRE, folder_INSPIRE_links, encoding_txt)

        # Part 2: Bulk download of zips by province
            # This code will read the txt files with the url to the INSPIRE zip files and download them
            # This will start the bulk download of all the zip files linked in the txt
            # This step also generates one folder per txt file (one folder by province) so it's easier to organize files after bulk download
            # The preceding script will also produce a file indicating the expected number of files for each province's folder. Kindly verify that all downloads have been successful.
            # Additionally, in the console, it will display whether each link has been downloaded successfully or the download error.
        
    Step_A_3_1_Part_2 = False
    if Step_A_3_1_Part_2  == True:
        from Internal_scripts.B_Scripts_Catastro_INSPIRE import Download_INSPIRE_files
        Download_INSPIRE_files.Download_files (folder_INSPIRE_links, folder_download_INSPIRE_zips, encoding_txt)

        # Part 3: Unzip the data. The ZIP files for each province are being decompressed.
    Step_A_3_1_Part_3 = False
    if Step_A_3_1_Part_3  == True:
        from Internal_scripts.B_Scripts_Catastro_INSPIRE import Unzip_INSPIRE
        Unzip_INSPIRE.Unzip (folder_download_INSPIRE_zips)

        # Part 4: Delete the files we do not wish to keep.
            # The uncompressed information takes up a lot of space, that's why, since we are only going to use the 'building.gml' layer, it is recommended to delete the unused layers (buildingpart, otherconstruction, and the XML).
    Step_A_3_1_Part_4 = False
    if Step_A_3_1_Part_4  == True:
        from Internal_scripts.B_Scripts_Catastro_INSPIRE import Delete_buildingpart_and_other_constructions
        Delete_buildingpart_and_other_constructions.Delete_non_used_files (folder_download_INSPIRE_zips)

    # Step A.3.2. Merge the files into a single geoparquet file
            # If preferred, this step can be done in QGIS using the Merge Vector Layers tool.
    Step_A_3_2 = True
    if Step_A_3_2  == True:
        Coordinate_Reference_System = 'EPSG:25830'          # The standard crs in Spain is ETRS89 / UTM Zone 30N, EPSG:25830. Part of the info is on 'ETRS89 / UTM zone 31N', 'ETRS89 / UTM zone 29N' and REGCAN95 for the Cannary Islands and must be transformed into a common crs.
        drop_duplicates = True                              # At times, the cadastral data may include duplicated buildings; it is advisable to treat them as errors and remove them. This process will eliminate all buildings with two or more entries sharing the same cadastral reference (14 digits).
        from Internal_scripts.B_Scripts_Catastro_INSPIRE import Create_GIS_buildings_map
        Create_GIS_buildings_map.Merge_files (folder_download_INSPIRE_zips, folder_INSPIRE, Coordinate_Reference_System, drop_duplicates)

    """ 
    Notes about the Step A.3:

        1 - To generate the model the recommended configuration is:
                encoding_txt = 'utf-8'
                Step_A_3_1_Part_1 = True
                Step_A_3_1_Part_2 = True
                Step_A_3_1_Part_3 = True
                Step_A_3_1_Part_4 = True
                Step_A_3_2 = True
                Coordinate_Reference_System = 'EPSG:25830'
                drop_duplicates = True

        2 - During the execution of the code, several print commands have been written that will appear, they offer information about the download process or some minor notes about what is being generated.

        3 - In case to prefer use a single or several provincies just move the rest of the txt links out of the folders.
        
        4 - Output: A final file is generated, with the GIS map with all the building in the INSPIRE Spanish Cadastre named GIS_INSPIRE_Buildings.parquet in the INSPIRE folder. This is a geoparquet file and can be opened and modified in QGIS or ArcGIS if desired.
        """

print ('All active steps have been completed.')
