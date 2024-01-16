 # Internal script, downloads the INSPIRE zip files from the web, is based on the links in txt extracted from https://www.catastro.minhafp.es/INSPIRE/buildings/ES.SDGC.BU.atom.xml?_gl=1*1uznbac*_ga*MTI0MTg5ODY0OC4xNjc2OTc0NTg0*_ga_JG5LDK2LGX*MTY5MzU1NjU5NS4xMC4xLjE2OTM1NTY2NDMuMC4wLjA

import os
import wget

def download_files_from_urls(url_list, save_folder):
    for url in url_list:
        try:
            print(f"Downloading {url}")
            
            wget.download(url, out=save_folder)
            print(" Download complete")
        except Exception as e:
            print(f"Failed to download {url} Error: {str(e)}")

def process_text_file(file_path, save_folder, encoding_txt):
    with open(file_path, 'r', encoding=encoding_txt) as file:
        lines = file.readlines()
        urls = [line.strip() for line in lines]
        download_files_from_urls(urls, save_folder)

def Download_files(folder_txt_INSPIRE, folder_download_INSPIRE_zips, encoding_txt):
    os.makedirs(folder_download_INSPIRE_zips, exist_ok=True)
    with os.scandir(folder_txt_INSPIRE) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith('.txt'):
                print(f"Processing file: {entry.name}")
                save_folder = os.path.join(folder_download_INSPIRE_zips, os.path.splitext(os.path.basename(entry.name))[0]) # The folder with the region's files will be inside the folder_download_INSPIRE_zips and will have the name of the txt file with the links
                os.makedirs(save_folder, exist_ok=True)
                process_text_file(entry.path, save_folder, encoding_txt)

if __name__ == "__main__":
    # Replace the following URLs with your list of URLs
    folder_links_INSPIRE = r'INSPIRE_cadastre\Automated_links'              # Contains the txt with the links to the INSPIRE Cadastre
    folder_download_INSPIRE_zips = r'INSPIRE_cadastre\INSPIRE_files'        # Contains the downloaded INSPIRE Cadastre zips
    Download_files(folder_links_INSPIRE, folder_download_INSPIRE_zips)

