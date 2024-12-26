from pytube import YouTube
from pytube import Playlist

def Que_quieres(): 
    print("Quieres descargar un video o una lista de reproducion")
    print("1. Un video unico")
    print("2. Una lista de reproducion")

    opcion = input("Elige un numero para iniciar la descarga de tu agrado: ")

    if opcion == "1" :
        video()
    elif opcion == "2":
        listadereproducion()


def video():
    print("Ingresa url")
    url = input()
    yt = YouTube(url)
    return yt


def listadereproducion():
    print("ingresa url")
    url = input()
    p = Playlist(url)
    return p

Que_quieres()