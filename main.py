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

To handle the model, some python libraries are needed, see requirements.txt file. To install the libraries execute "pip install -r requirements.txt".
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
        # Folders for the Step A.1 Energy Performance Certificates (EPC)
folder_read_EPC = r'Downloaded_EPC_databases'                             # The folder where the files of the EPCs will be read from and if the download option is chosen the EPCs files will be saved 
folder_save_EPC_modificed = r'Modified_EPC_Databases'                     # The folder where the generated files will be saved
        # Folders for the Step A.2 Alphanumeric cadastre
folder_read_Alphanumeric_cadastre = r'Alphanumeric_cadastre'              # The folder to store the zip files from the Alphanumeric Cadastre
        # Folders for the Step A.3 INSPIRE cadastre
folder_INSPIRE = r'INSPIRE_cadastre'                                      # The folder with all the data and models from the INSPIRE Cadastre
folder_txt_INSPIRE = r'INSPIRE_cadastre\Original_txt_links'               # Additional feature: It allows updating the download links for the Inspire cadastre that will be used by the algorithm, contains the raw text of the webs with the links.
folder_INSPIRE_links = r'INSPIRE_cadastre\Automated_links'                # Contains the txt with the links to the INSPIRE Cadastre ready to download
folder_download_INSPIRE_zips = r'INSPIRE_cadastre\INSPIRE_files'          # Contains the downloaded INSPIRE Cadastre zips
        # Folders for the Step A.4 Others
folder_Additional_Information = r'Additional_Information'                 # Includes supplementary data to enhance the model, including climate zones map or the population residing in each municipality.
        # Folders for the Step B.1 Energy performance model
b1_output = r'Energy_performance_model'                                   # Contains the B.1 step outputs
        # Folders for the Step B.2 National enhanced building stock GIS model
b2_output = r'National_enhanced_building_stock_GIS_model'                 # Contains the B.2 step outputs
        # Folders for the Step B.3 National enhanced building stock GIS model
b3_output = r'National-scale_EPC-based_Building_Energy_Model'             # Contains the B.3 step outputs (the final file of the entire process)

Step_A_0 = True     # Create folders to store the data
if Step_A_0:
    import os
    os.makedirs(folder_read_EPC, exist_ok=True)
    os.makedirs(folder_save_EPC_modificed, exist_ok=True)
    os.makedirs(folder_read_Alphanumeric_cadastre, exist_ok=True)
    os.makedirs(folder_txt_INSPIRE, exist_ok=True)
    os.makedirs(folder_INSPIRE_links, exist_ok=True)
    os.makedirs(folder_download_INSPIRE_zips, exist_ok=True)
    os.makedirs(folder_Additional_Information, exist_ok=True)

# Step A.1, Management of EPC in python - To use this step mark the variable Step_A_1 as True and provide the rest of the information required. Please see notes below.
Step_A_1 = True
if Step_A_1:
    from Internal_scripts import A_Script_clave

    Download_EPCs_DDBB = True                               # Step A.1.1. Download the data from the public EPCs Databases (True or False) (see notes below)
    Homogenize_DDBB = True                                  # Step A.1.2. Homogenize the databases (True or False) (necessary for the following steps)
    Filter_by_date = True                                   # Step A.1.3. Filter by certificate registration date (True or False)
    Filter_date = 2024                                      # Step A.1.3. Date included in the range that we want to filter (must be a year), also filter the EPCs registered before 2010 as errors. If we put 2019, we will use all certificates prior to 1/1/2020, (integer)
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

        
        2 - (*) In the final version of the cbc-NBEM these steps are not used, however, as they may be useful, the option of generating the data using these functionalities has been maintained. 
            To generate the cbc-NBEM it is recommended to set the values marked with (*) to False or 0 as appropriate.
        
        3 - During the execution of the code, several print commands have been written that will appear, they are written in Spanish, in general they offer information about the process or some minor notes about what is being generated.
        
        4 - Step A.1.1. Download the data from the public EPCs Databases:
            The script to download the databases of the EPCs cannot download all of them, this is the list of exceptions:
                - Over time, those responsible for providing this data change the formats, encodings, and methods of obtaining the information. 
                This step is automated but carries the highest risk of quickly becoming outdated. 
                It is recommended to supervise that all the desired data is downloaded or manually download the information and proceed with the rest of the code automatically.
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
Step_A_2 = True
if Step_A_2:
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
    drop_unused_columns = True                                # Result Step A.2. Eliminate from the alphanumeric cadastre result files the columns that are not necessary to reduce the file size

    # Drop unused columns is recommended as it greatly reduces the calculation time and the size of the resulting file. Depending on the output scale, building or building units, there are different columns to use. 
    # It is recommended to leave the default list of the code but you can see section 5 of the notes to select the desired columns.
    columns_to_use_buildings= ['Provincia', 'CMunicipioDGC', 'ReferenciaCatastral_parcela', 'CMunicipioINE', 'CP', 'SupFinca', 'SupConstruida', 'Sup_sobre_rasante', 'Sup_bajo_rasante', 'Sup_cubierta',
        'FechaConstruccion', 'ExactitudFechaConstruccion', 'Longitud_de_fachada', 'Indicador_reforma_o_rehabilitacion', 'Fecha_reforma', 'Antiguedad_efectiva_en_catastro', 'Superficie_del_local',
        'Calidad_de_la_edificacion', 'FechaConstruccion_BI', 'Plantas', 'N_BI', 'Sup_elementos_urbanos', 'Viv', 'S_Viv', 'Almacen', 'S_Almacen', 'Ind', 'S_Ind', 'Of', 'S_Of', 'Com', 'S_Com', 'Dep', 'S_Dep', 'Esp', 'S_Esp',
        'Host', 'S_Host', 'San', 'S_San', 'Cult', 'S_Cult', 'Rel', 'S_Rel', 'Sin', 'S_Sin', 'IAg', 'S_IAg', 'Ag', 'S_Ag', 
        'Periodo_Construccion', 'Cluster_ERESEE', 'Tipologia_constructiva', 'Plantas_DEF']
    columns_to_use_building_units= ['Provincia', 'CMunicipioDGC', 'ReferenciaCatastral_parcela', 'Referencia_BI', 'CMunicipioINE_BI', 'NombreProvincia_BI', 'Clavegrupo_BI',
        'CMunicipioINE', 'CP', 'SupFinca', 'SupConstruida', 'Sup_sobre_rasante', 'Sup_bajo_rasante', 'Sup_cubierta', 'FechaConstruccion', 'ExactitudFechaConstruccion',
        'Longitud_de_fachada', 'Indicador_reforma_o_rehabilitacion', 'Fecha_reforma', 'Antiguedad_efectiva_en_catastro', 'Superficie_del_local',
        'Calidad_de_la_edificacion', 'FechaConstruccion_BI', 'Plantas', 'N_BI', 'Sup_elementos_urbanos', 
        'Viv', 'S_Viv', 'Almacen', 'S_Almacen', 'Ind', 'S_Ind', 'Of', 'S_Of', 'Com', 'S_Com', 'Dep', 'S_Dep', 'Esp', 'S_Esp',
        'Host', 'S_Host', 'San', 'S_San', 'Cult', 'S_Cult', 'Rel', 'S_Rel', 'Sin', 'S_Sin', 'IAg', 'S_IAg', 'Ag', 'S_Ag', 
        'Periodo_Construccion', 'Cluster_ERESEE', 'Tipologia_constructiva', 'Plantas_DEF']

    # Step A.2.3. Done automatically

    E_Script_clave.Alphanumeric_cadastre (PROV, folder_read_Alphanumeric_cadastre, Extract_ZIP_files, building_scale_cadastre, building_unit_scale_cadastre, drop_unused_columns, columns_to_use_buildings, columns_to_use_building_units)

    """ 
    Notes about the Step A.2:

        1 - To generate the cbc-NBEM the recommended configuration is:
                PROV = 0
                folder_read_Alphanumeric_cadastre = 'Alphanumeric_cadastre'
                Extract_ZIP_files = True           # (just once)          # This script automatically unzips the zip files and sorts the documents it contains
                building_scale_cadastre = True                            # Process the CAT files to obtain the information by building at the province scale
                building_unit_scale_cadastre = True                       # Process the CAT files to obtain the information by building unit at the province scale

        2 - During the execution of the code, several print commands have been written that will appear, they are written in Spanish, in general they offer information about the process or some minor notes about what is being generated.
        
        3 - At times, the cadastral data may include duplicated buildings; it is advisable to treat them as errors and remove them. This process will eliminate all buildings with two or more different entries sharing the same cadastral reference (14 or 20 digits).
        
        4 - Intermediate files: Step A.2 consumes a large amount of space on the hard drive due to the large size of the files generated. 
            It is highly recommended that once the process is generated, the intermediate files used are deleted.
            The intermediate files that can be deleted are the downloaded zip files and the files located in the folders 'Archivos_descomprimidos' ('Unzipped files'), 'Datos por Provincia' ('Data by province'), Datos por Provincia_escala_BI ('Data by province building unit scale') and the txt reports.
            
        5 -Drop unused columns: It is recommended that only the columns that are going to be useful be selected from the list, this speeds up the process time and eliminates a lot of information that is not relevant.
           It is recommended to leave the default list of the code. This is the list of all the columns removed from the cadastre: ReferenciaCatastral_parcela and Referencia_BI are mandatory to keep it to be able to join the cadastres and the EPCs
           Columns dropped at building scale: 'Tipo_de_registro', 'N_plantas_F', 'Superficie_suelo_EC', 'Planta_C', 'Sup_porches_y_terrazas', 'Sup_en_otras_plantas', 
           Columns dropped at building unit scale: 'Tipo_de_registro', 'N_plantas_F', 'Superficie_suelo_EC', 'Planta_C', 'Sup_porches_y_terrazas', 'Sup_en_otras_plantas', 


        6 - Output: Two final files are generated, one with the information at the building scale and the other with the information at the real estate scale.
            Both are found in the folder: "Datos del Catastro alfanumerico por edificio" ("Data from the alphanumeric cadastre by building") and the files are named 
            "Edificios_España_Completos" ("Buildings in Spain completed") and "Edificios_España_Completos_escala_BI" ("Buildings units in Spain completed").

        7 - Output: If you mark the option to delete unused columns as True, it eliminates the columns from the previous result file that will not be used later, 
            generating lighter additional files with all the main information with the previous name accompanied by "_Reduced".
    """

# Step A.3, INSPIRE cadastre - To use this step mark the variable Step_A_3 as True and provide the rest of the information required. Please see notes below.
Step_A_3 = True
if Step_A_3:
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
    Step_A_3_1_Part_1 = True
    if Step_A_3_1_Part_1:
        from Internal_scripts.B_Scripts_Catastro_INSPIRE import Update_download_links
        Update_download_links.Automate_links (folder_txt_INSPIRE, folder_INSPIRE_links, encoding_txt)

        # Part 2: Bulk download of zips by province
            # This code will read the txt files with the url to the INSPIRE zip files and download them
            # This will start the bulk download of all the zip files linked in the txt
            # This step also generates one folder per txt file (one folder by province) so it's easier to organize files after bulk download
            # The preceding script will also produce a file indicating the expected number of files for each province's folder. Kindly verify that all downloads have been successful.
            # Additionally, in the console, it will display whether each link has been downloaded successfully or the download error.
        
    Step_A_3_1_Part_2 = True
    if Step_A_3_1_Part_2:
        from Internal_scripts.B_Scripts_Catastro_INSPIRE import Download_INSPIRE_files
        Download_INSPIRE_files.Download_files (folder_INSPIRE_links, folder_download_INSPIRE_zips, encoding_txt)

        # Part 3: Unzip the data. The ZIP files for each province are being decompressed.
    Step_A_3_1_Part_3 = True
    if Step_A_3_1_Part_3:
        from Internal_scripts.B_Scripts_Catastro_INSPIRE import Unzip_INSPIRE
        Unzip_INSPIRE.Unzip (folder_download_INSPIRE_zips)

        # Part 4: Delete the files we do not wish to keep.
            # The uncompressed information takes up a lot of space, that's why, since we are only going to use the 'building.gml' layer, it is recommended to delete the unused layers (buildingpart, otherconstruction, and the XML).
    Step_A_3_1_Part_4 = True
    if Step_A_3_1_Part_4:
        from Internal_scripts.B_Scripts_Catastro_INSPIRE import Delete_buildingpart_and_other_constructions
        Delete_buildingpart_and_other_constructions.Delete_non_used_files (folder_download_INSPIRE_zips)

    # Step A.3.2. Merge the files into a single geoparquet file
            # If preferred, this step can be done in QGIS using the Merge Vector Layers tool.
    Step_A_3_2 = True
    if Step_A_3_2:
        Coordinate_Reference_System = 'EPSG:25830'          # The standard crs in Spain is ETRS89 / UTM Zone 30N, EPSG:25830. Part of the info is on 'ETRS89 / UTM zone 31N', 'ETRS89 / UTM zone 29N' and REGCAN95 for the Cannary Islands and must be transformed into a common crs.
        drop_duplicates = True                              # At times, the cadastral data may include duplicated buildings; it is advisable to treat them as errors and remove them. This process will eliminate all buildings with two or more entries sharing the same cadastral reference (14 digits).
        drop_unused_columns = True                          # Result Step A.3. Eliminate from the INSPIRE cadastre result files the columns that are not necessary to reduce the file size
        columns_to_use = ['reference', 'beginning', 'conditionOfConstruction', 'currentUse', 'numberOfBuildingUnits', 'numberOfDwellings', 'value', 'geometry'] # See section 5 in the notes to select the columns you want to use.

        from Internal_scripts.B_Scripts_Catastro_INSPIRE import Create_GIS_buildings_map
        Create_GIS_buildings_map.Merge_files (folder_download_INSPIRE_zips, folder_INSPIRE, Coordinate_Reference_System, drop_duplicates, drop_unused_columns, columns_to_use)

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

        4 - Note: this step requires a lot of time (more than 24 hours for all the buildings of Spain).
        
        5 - Drop unused columns: It is recommended that only the columns that are going to be useful be selected from the list, this speeds up the process time and eliminates a lot of information that is not relevant.
            This is the list of all the columns contained in the basic INSPIRE cadastre: reference is mandatory to keep it to be able to join the cadastres and the EPCs
                ['gml_id', 'beginLifespanVersion', 'conditionOfConstruction', 'beginning', 'end', 'endLifespanVersion',
                 'informationSystem', 'reference', 'localId', 'namespace', 'horizontalGeometryEstimatedAccuracy',
                 'horizontalGeometryEstimatedAccuracy_uom', 'horizontalGeometryReference', 'referenceGeometry', 'currentUse', 'numberOfBuildingUnits',
                 'numberOfDwellings', 'documentLink', 'format', 'sourceStatus',
                 'officialAreaReference', 'value', 'value_uom', 'geometry']

        6 - Output: A final file is generated, with the GIS map with all the building in the INSPIRE Spanish Cadastre named GIS_INSPIRE_Buildings.parquet in the INSPIRE folder. This is a geoparquet file and can be opened and modified in QGIS or ArcGIS if desired.
        """

# Step A.4, Others - Please see notes below.
    # This step is divided into two independent parts: Part 1 involves creating the climate zones map, and Part 2 involves classifying the buildings as built in rural or urban municipalities.

    # Part 1: Climate zones map
            # The Climate zones map is generated using the official provinces map and the Digital Terrain Model from the CNIG, in particular de MDT 200. Available at the following link: https://centrodedescargas.cnig.es/CentroDescargas/index.jsp
            # As it is generated only once, automating the process has not been deemed relevant. This map can be created using QGIS through its tools or with geopandas.
            # To generate it, all files should be merged into a single coordinate reference system, and it is recommended to use ETRS89 / UTM Zone 30N, EPSG:25830, should be the same as the one crs used for the buildings in the INSPIRE Cadastre.
            # Using the criteria specified in the DB HE "Energy Savings," Annex B: Climatic Zones, contour lines defining the climatic zones can be generated. Subsequently, it is sufficient to intersect the province polygons with these lines and assign the climatic zone. For more information, refer to the Heliyon paper.
            # The climate zones map file should be stored in the "Additional_Information" folder.

    # Part 2: Municipalities sizes
            # The population data for municipalities throughout Spain is available from the INE (National Institute of Statistics) at https://www.ine.es/dynt3/inebase/es/index.htm?padre=525.
            # This step will be carried out later in step B.2.3, where each building will be assigned the type of municipality in which it was constructed. 
            # In this step, it is sufficient to download the INE population file and store it in the "Additional_Information" folder.

# Step B, Model generation
    
# Step B.1, Energy performance model
Step_B_1 = True
if Step_B_1:
    # In this section, the information from the EPCs (Energy Performance Certificates) is merged with the alphanumeric cadastre, filtered and analysed.
    from Internal_scripts import A_7_3_Prepara_EPC_edif_BI
    from Internal_scripts import A_8_Combina_parquet_EPC_edif_BI_cat_alfanum
    from Internal_scripts import A_9_Combina_EPC_edif_BI_agrupa_por_edificio

    EPC_database_14_digits = r'BBDD_Unidas por Referencia Catastral\Parquet\Todos_los_certificados_España_Pre_2025_14DigitRefCat.csv'                                   # The output files of the A.1 process (EPCs). 14 digits cadastral reference (buildings)
    EPC_database_20_digits = r'BBDD_Unidas por Referencia Catastral\Parquet\Todos_los_certificados_España_Pre_2025_20DigitRefCat.csv'                                   # The output files of the A.1 process (EPCs). 20 digits cadastral reference (building units)
    alphanumeric_cadastre_database_buildings = r'Alphanumeric_cadastre\Datos del Catastro alfanumerico por edificio\Edificios_España_Completos_Reducido.gzip'                     # The output files of the A.2 process (Alphanumeric cadastre). 14 digits cadastral reference (buildings) # It is recommended to use parquet files
    alphanumeric_cadastre_database_building_units = r'Alphanumeric_cadastre\Datos del Catastro alfanumerico por edificio\Edificios_España_Completos_escala_BI_Reducido.gzip'      # The output files of the A.2 process (Alphanumeric cadastre). 20 digits cadastral reference (building units) # It is recommended to use parquet files
    B_1_model_name = r'\Energy_performance_model' # The name of the output file of the B.1 step

    os.makedirs(b1_output, exist_ok=True)
    EPC_database_14_digits_prepared, EPC_database_20_digits_prepared = A_7_3_Prepara_EPC_edif_BI.prepare_EPCs (EPC_database_14_digits, EPC_database_20_digits)
    b1_14_digits, b1_20_digits = A_8_Combina_parquet_EPC_edif_BI_cat_alfanum.combine_with_cadastre (EPC_database_14_digits_prepared, EPC_database_20_digits_prepared, alphanumeric_cadastre_database_buildings, alphanumeric_cadastre_database_building_units, b1_output)
    b1_model = A_9_Combina_EPC_edif_BI_agrupa_por_edificio.group_by_building (b1_14_digits, b1_20_digits, b1_output, B_1_model_name)

    # from Internal_scripts import Z_5_Combina_EPC_edif_BI_sin_agrupar_por_edificio  # Optional, combines EPC and alphanumeic cadaster at building unit scale (without group by building)

# Step B.2, National enhanced building stock GIS model
Step_B_2 = True
if Step_B_2:
    # In this section, the information from the INSPIRE Cadastre is merged with the alphanumeric cadastre, the climate zones map and the type of municipality
    os.makedirs(b2_output, exist_ok=True)
    # Step B.2.1, Assign Climate zone to buildings
    Step_B_2_1 = True
    if Step_B_2_1:
      # Note: the assignment of climatic zones can be done building by building with a spatial union with the INSPIRE cadastre or if the climatic zones 
      # have been calculated by municipality, it can be joined by municipality code between the map of climatic zones and the alphanumeric cadastre.
        climate_zone_map = r'Additional_Information\Municipios de España con su Zonas climática.csv' # The path to the climate zones map (step A.4)
        Alphanumeric_buildings = r'Alphanumeric_cadastre\Datos del Catastro alfanumerico por edificio\Edificios_España_Completos_Reducido.gzip' # The path to the Alphanumeric cadastre (step A.2)
        buildings_with_climate_zones_name = r'\Buildings_with_climate_zones'

        from Internal_scripts.B_Scripts_Catastro_INSPIRE import Combine_alphanumeric_Climate_zones
        Combine_alphanumeric_Climate_zones.Assign_climate_zone (climate_zone_map, Alphanumeric_buildings, b2_output, buildings_with_climate_zones_name)

    # Step B.2.2, Assign type of municipality. Combine alphanumerical cadastre and the population census by municipality to know what type of municipality the building is located in (rural or urban)
    # This step updates the input file by adding the indicated column, interrupting this step may cause the file to be corrupted.
    Step_B_2_2 = True
    if Step_B_2_2:
        from Internal_scripts import G_1_2_Municipio_Rural_o_Urbano_Catastro_Alfanumerico_parquet
        population_census = r'Additional_Information\pobmun22.xlsx'
        Alphanumeric_buildings = r'National_enhanced_building_stock_GIS_model\Buildings_with_climate_zones.gzip'
        G_1_2_Municipio_Rural_o_Urbano_Catastro_Alfanumerico_parquet.assign_type_of_municipality(population_census, Alphanumeric_buildings)

    # Step B.2.3, Union of cadastres. Combine INSPIRE and alphanumerical cadastre
    Step_B_2_3 = True
    if Step_B_2_3:

        # The path to the INSPIRE and alphanumeric cadastres (step A.2 and A.3) (remember to use the data from the cadastre with the climatic zone from the previous step)
        INSPIRE_buildings = r'INSPIRE_cadastre\GIS_INSPIRE_Buildings_v2.parquet' # The path to the INSPIRE cadastre (step A.2) or the INSPIRE with climate zones (step B.2.1)
        Alphanumeric_buildings = r'National_enhanced_building_stock_GIS_model\Buildings_with_climate_zones.gzip' # The path to the Alphanumeric cadastre (step A.2) or the Alphanumeric with climate zones (step B.2.1)
        B_2_model_name = r'\National_enhanced_building_stock_GIS_model' # The name of the output file of the B.2 step

        from Internal_scripts import G_1_Uno_parquet_INSPIRE_y_Alfanumerico   

    # This step can be done in 2 ways, tabular data (non a GIS map), faster and less time and resources consuming or a GIS map which contains the geoespatial information
    # Part 1: Tabular data
        # If the desired objective is tabular information, it can be obtained in Parquet or CSV format with all the details. 
        # This outcome may be more practical depending on the use, as the reading time and file size are significantly reduced compared to a GIS map.
        Tabular_data = True
        if Tabular_data:
            G_1_Uno_parquet_INSPIRE_y_Alfanumerico.combine_cadastres (INSPIRE_buildings, Alphanumeric_buildings, b2_output, B_2_model_name)

    # Part 2: GIS map
        # If the desired objective is a GIS map at building by building scale, it is obtained by combining the geographical information from the INSPIRE cadastre with the alphanumeric data, resulting in a map. 
        # This step can be performed in two ways: "inner" (only buildings with EPCs will be generated) and "left" (a map with all buildings in Spain will be generated, and EPC information will be added for buildings with at least one certificate).
        # from Internal_scripts import G_12_Uno_geoparquet_Edif_España_y_CEE
        GIS_data = True
        if GIS_data:
            G_1_Uno_parquet_INSPIRE_y_Alfanumerico.combine_cadastres_GIS (INSPIRE_buildings, Alphanumeric_buildings, b2_output, B_2_model_name)

# Step B.3, National-scale EPC-based Building Energy Model
Step_B_3 = True
if Step_B_3:
    os.makedirs(b3_output, exist_ok=True)
    from Internal_scripts import G_2_Uno_parquet_INSPIRE_Alfanumerico_y_CEE

    # The path to the INSPIRE and alphanumeric cadastres (step A.2 and A.3) (remember to use the data from the cadastre with the climatic zone from the previous step)
    cadastres_files = r'National_enhanced_building_stock_GIS_model\National_enhanced_building_stock_GIS_model.parquet' # The path to the cadastres combined (step B.2)
    EPC_files = r'Energy_performance_model\Energy_performance_model.gzip' # The path to the EPCs files (step B.1)
    B_3_model_name = r'\National-scale_EPC-based_Building_Energy_Model' # The name of the output file of the B.3 step

    # Part 1: Tabular data
    Tabular_data = True
    if Tabular_data:
        G_2_Uno_parquet_INSPIRE_Alfanumerico_y_CEE.combine_cadastres_with_EPCs (cadastres_files, EPC_files, b3_output, B_3_model_name)

    # Part 2: GIS map
    GIS_data = True
    if GIS_data:
        G_2_Uno_parquet_INSPIRE_Alfanumerico_y_CEE.combine_cadastres_with_EPCs_GIS (cadastres_files, EPC_files, b3_output, B_3_model_name)


print ('All active steps have been completed.')
