#Funcion que conecta con google drive requiere una fecha para el titulo
#import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def googledrive(data):
    # PUJADA AL DRIVE DEL PNG OBTINGUT
    g_login = GoogleAuth()
    g_login.LoadCredentialsFile("mycreds.txt")
    if g_login.credentials is None:
        # Authenticate if they're not there
        g_login.LocalWebserverAuth()
    elif g_login.access_token_expired:
        # Refresh them if expired
        g_login.Refresh()
    else:
        # Initialize the saved creds
        g_login.Authorize()
    # Save the current credentials to a file
    g_login.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(g_login)
    print('si')
    file_drive = drive.CreateFile({'title': data})
    file_drive.SetContentFile(data)
    file_drive.Upload()
    print("L'arxiu ha pujat al drive","\n")
    #sys.exit()
