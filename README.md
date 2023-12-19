# NBEM
Code to generate National-scale Building Energy Models based on Energy Performance Certificates

Description:
The code in this repository is designed to generate a National-scale Urban Building Energy Model for Spain. The model includes all buildings in Spain, with georeferenced data from the INSPIRE Cadastre and alphanumeric data from the Spanish Cadastre, as well as all energy data obtained from publicly available Energy Performance Certificates (EPCs) in Spain.

The code in this repository is part of the paper “A new approach for national-scale Building Energy Models based on Energy Performance Certificates in European countries: the case of Spain”, published in Heliyon in 2023 and written by Carlos Beltran-Velamazan, Marta Monzón-Chavarrías and Belinda López-Mesa from the University of Zaragoza (Spain).
There the methodology is explained and developed and the results obtained are shown. The article can be found in the following link https:

For any suggestions, questions, or inquiries about the code, its usage, or the model, please feel free to send a mail to cbeltran@unizar.es

Data input needed: Energy Performance Certificates (EPCs), INSPIRE Cadastre files, and Alphanumeric Cadastre files. EPC data and INSPIRE Cadastre files can be downloaded automatically by the repository code, while alphanumeric cadastral data must be manually downloaded from the cadastral electronic headquarters province by province (see the notes in the MAIN file for the respective sections).

How to install: The code contains Python scripts to generate the model; no specific files need to be installed. Certain libraries such as Pandas, Geopandas, Polars, and Geopolars are required. See the details in the MAIN file of the code.

How to use: A script named MAIN has been created to handle the entire automated process in Python for generating the national-scale Building Energy Model based on Energy Performance Certificates in European countries. The MAIN script contains the parameters and a recommended configuration for generating the model. Internal scripts can be modified to obtain different results if desired.

Additional info: This is an open access article distributed under the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.


