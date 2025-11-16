'''
    API: Application Programming Interface
    Nasa API: https://api.nasa.gov/
    API_KEY_NASA: YOUR NASA API_Key
    Developer: Michael A.Botina
    Date 09112025
    Script description: Get an read data from NASA API about comets and others
    https://

'''
import requests
import os

os.system('clear')

def nasa_data(api_key):
    print("::: COMET INFORMATION :::")
    url = f"asd{api_key}"

    #Realizar la solicitud de la API
    response = requests.get(url)
    response.raise_for_status() #=> valida si se presenta algun error en la peticion 
    data = response.json() #Convertir la respuesta a formato JSON

    print(data)

API_KEY_NASA = tu llave
get_nasa_data(API_KEY_NASA)