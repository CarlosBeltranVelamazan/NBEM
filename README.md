# NBEM
Code to generate National-scale Building Energy Models based on Energy Performance Certificates

## Description:
The code in this repository is designed to generate a National-scale Urban Building Energy Model for Spain. The model includes all buildings in Spain, with georeferenced data from the INSPIRE Cadastre and alphanumeric data from the Spanish Cadastre, as well as all energy data obtained from publicly available Energy Performance Certificates (EPCs) in Spain.

<p align="center">
  <img src="https://ars.els-cdn.com/content/image/1-s2.0-S2405844024015044-gr2.jpg" width="350" title="General methodology flowchart to build a national-scale EPC-based UBEM in European countries">
  <img src="https://ars.els-cdn.com/content/image/1-s2.0-S2405844024015044-gr3.jpg" width="350" title="Flowchart of the specific methodology to build the national-scale EPC-based UBEM for the case of Spain">
  <img src="https://ars.els-cdn.com/content/image/1-s2.0-S2405844024015044-gr6.jpg" width="350" title="Georeferenced buildings in Spain with their Climate zone">
</p>

The code in this repository is part of the paper “A new approach for national-scale Building Energy Models based on Energy Performance Certificates in European countries: the case of Spain”, published in Heliyon in 2023 and written by Carlos Beltran-Velamazan, Marta Monzón-Chavarrías and Belinda López-Mesa from the Built4Life Lab, University of Zaragoza (Spain), doi: https://doi.org/10.1016/j.heliyon.2024.e25473.
There the methodology is explained and developed and the results obtained are shown. The article can be found in the following link https: https://www.sciencedirect.com/science/article/pii/S2405844024015044?via%3Dihub.
If you use this tool please cite the paper: Carlos Beltrán-Velamazán, Marta Monzón-Chavarrías, Belinda López-Mesa, A new approach for national-scale Building Energy Models based on Energy Performance Certificates in European countries: The case of Spain, Heliyon, Volume 10, Issue 3, 2024, e25473, ISSN 2405-8440, https://doi.org/10.1016/j.heliyon.2024.e25473.

## Project Status:
Released, development ongoing. Currently, we are fine-tuning the code for better comprehension, and we will be releasing the complete updated code as soon as possible.
For any suggestions, questions, or inquiries about the code, its usage, or the model, please feel free to send a mail to cbeltran@unizar.es

## Data input needed:
Energy Performance Certificates (EPCs), INSPIRE Cadastre files, and Alphanumeric Cadastre files. EPC data and INSPIRE Cadastre files can be downloaded automatically by the repository code, while alphanumeric cadastral data must be manually downloaded from the cadastral electronic headquarters province by province (see the notes in the main.py file for the respective sections).

## How to install: 
The code contains Python scripts to generate the model; no specific files need to be installed. Certain libraries such as Pandas, Geopandas, Polars, and Geopolars are required. See requirements.txt for the listing and versions.

## How to use: 
A script named main.py has been created to handle the entire automated process in Python for generating the national-scale Building Energy Model based on Energy Performance Certificates in European countries. The main.py script contains the parameters and a recommended configuration for generating the model. Internal scripts can be modified to obtain different results if desired.

# Project info
This tool was developed at the **Built4Life Lab**, research group from the **University of Zaragoza-I3A**, within the research project named **LocalRegen**, funded by the Ministry of Science and Innovation of Spain, grant number PID2019-104871RB-C21/AEI/10.13039/501100011033 and by GOBIERNO DE ARAGÓN, grant number T37_23R: Built4Life Lab.
Website: http://www.localregen.net/

* Main Contact: Belinda López-Mesa, Built4Life Lab, University of Zaragoza-I3A, 50108 Zaragoza, Spain (belinda@unizar.es)

<p align="center">
  <img src="https://proyectolocalregen.files.wordpress.com/2021/04/logo-localregen-color.png?w=848" width="350" title="LocalRegen">
  <img src="https://iphunizar.com/wp-content/uploads/2022/03/Perez_Moreno_Lucia_LOGO_B4L_gris.png" width="350" title="Built4Life Lab">
</p>

## Additional info: 
The code is available under the terms of the MIT License. Permitted with proper citation: Unrestricted use, distribution, and reproduction in any medium.
