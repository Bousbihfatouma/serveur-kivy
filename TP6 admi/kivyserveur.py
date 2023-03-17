# pip install kivy
# pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/

from kivy.app import App
from tkinter.tix import ButtonBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
	def build(self):
		self.window = GridLayout()
		self.window.cols=1
		self.window.size_hint = (0.5, 0.5)
		self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

		self.lblLogin = Label(text="login")
		self.window.add_widget(self.lblLogin)
		self.login= TextInput(text="",size_hint =(1,1),multiline= False)
		self.window.add_widget(self.login)
		self.lblpass = Label(text="Password")
		self.window.add_widget(self.lblpass)
		self.Password= TextInput(text="",size_hint =(1,1),multiline= False)
		self.window.add_widget(self.Password)
		self.lblEmail = Label(text="Email")
		self.window.add_widget(self.lblEmail)
		self.Email= TextInput(text="",size_hint =(1,1),multiline= False)
		self.window.add_widget(self.Email)
		self.lblIp = Label(text="Ip")
		self.window.add_widget(self.lblIp)
		self.Ip= TextInput(text="",size_hint =(1,1),multiline= False)
		self.window.add_widget(self.Ip)
	    
	

       # création de la zone des boutons
		self.buttonArea = GridLayout(cols=2, size_hint = (1,0.2))
		# création du premier bouton	
		buttonGo = Button(text="Go", 
				size_hint = (1,0.2),
				on_press=self.buttonGo
		)
		# creation du second bouton
		buttonStop = Button(text="Stop", 
				size_hint = (1,0.2),
				on_press=self.buttonStop
		)
		 
	
		# ajout des boutons à la zone des boutons
		self.buttonArea.add_widget(buttonGo)
		self.buttonArea.add_widget(buttonStop)
		# ajout de la zone des boutons à la fenêtre
		self.window.add_widget(self.buttonArea)
		# affiche la fenetre construite	
		return self.window

	def buttonGo(self, instance):
		self.message.text = "Go " + self.login.text

	def buttonStop(self, instance):
		self.Stop()
		

if __name__ == "__main__":
	SayHello().run()

    
