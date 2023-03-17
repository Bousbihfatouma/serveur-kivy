# pip install kivy
# pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import pathlib
import os


myFolderpath= pathlib.Path(__file__).parent.resolve()
strFolderpath = str(myFolderpath)
class SayHello(App):
	def build(self):
		self.window = GridLayout()
		self.window.cols=1
		self.window.size_hint = (0.8, 0.8)
		self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		#on augmente la taille de l'image
		self.image = Image(source="2133.JPG", size_hint = (2, 2))
		#self.image = Image(source="2133.JPG")
		# on créer l'objet Label
		self.window.add_widget(self.image)
  
		self.message = Label(text="Bonjour de Malte")
		# on ajoute le label à la fenêtre
		self.window.add_widget(self.message)
		self.user = TextInput(text="", size_hint = (1, 1), multiline = True)
		self.window.add_widget(self.user)
		# création de la zone des boutons
		self.buttonArea = GridLayout(cols=3, size_hint = (1,0.2))
		# création du premier bouton	
		button = Button(text="Say Hello", 
				size_hint = (1,0.2),
				on_press=self.buttonHello
		)
		# creation du second bouton
		buttonQuit = Button(text="Quit", 
				size_hint = (1,0.2),
				on_press=self.buttonQuit
		)

		buttonSave = Button(text="SaveFile", 
				size_hint = (1,0.2),
				on_press=self.buttonSave
		)


		# ajout des boutons à la zone des boutons
		self.buttonArea.add_widget(button)
		self.buttonArea.add_widget(buttonSave)
		self.buttonArea.add_widget(buttonQuit)
		# ajout de la zone des boutons à la fenêtre
		self.window.add_widget(self.buttonArea)
		# affiche la fenetre construite	
		return self.window

	def buttonHello(self, instance):
		self.message.text = "Bonjour " + self.user.text

	def buttonSave(self, instance):
		# on enregistre le contenu de la zone de texte dans un fichier
		with open(strFolderpath+os.sep+"test.txt", "w") as f:
			f.write(self.user.text)
			f.close()

	def buttonQuit(self, instance):
		self.stop()

if __name__ == "__main__":
	SayHello().run()
	