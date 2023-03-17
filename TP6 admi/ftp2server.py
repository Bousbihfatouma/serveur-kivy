# pip install pyftpdlib
#Tout d'abord, vous importez les modules nécessaires pour créer le serveur FTP:
from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
import os
#Ensuite, vous créez un objet DummyAuthorizer, qui permettra de gérer les utilisateurs et les autorisations:
authorizer = DummyAuthorizer()
#Vous ajoutez un utilisateur avec le nom d'utilisateur "user" et le mot de passe "12345". Cet utilisateur aura les autorisations suivantes: lecture, écriture, suppression, renommage, création de répertoires, suppression de répertoires, listage de fichiers et modification des horodatages.
authorizer.add_user("user", "12345", os.getcwd()+"/ftpserver/logged", perm="elradfmwMT")
#Vous ajoutez également un accès anonyme pour les utilisateurs qui ne fournissent pas de nom d'utilisateur et de mot de passe. Ces utilisateurs ne seront autorisés qu'à lire les fichiers.
authorizer.add_anonymous(os.getcwd()+"/ftpserver/nobody")
#Vous spécifiez l'adresse et le port sur lequel le serveur FTP écoutera les connexions entrantes:
address = ("0.0.0.0", 21)  # listen on every IP on my machine on port 21
#Dans ce cas, le serveur écoutera toutes les adresses IP disponibles sur la machine sur le port 21.
#Vous créez un objet FTPHandler, qui traitera les connexions entrantes:
handler = FTPHandler
#ous attribuez l'objet authorizer que vous avez créé précédemment à l'objet handler, afin que le serveur FTP puisse utiliser les autorisations que vous avez spécifiées:
handler.authorizer = authorizer
#ous créez enfin un objet FTPServer en lui passant l'adresse et l'objet handler que vous avez créé précédemment:
server = servers.FTPServer(address, handler)
#vous lancez le serveur en appelant la méthode serve_forever() sur l'objet server:
server.serve_forever()
