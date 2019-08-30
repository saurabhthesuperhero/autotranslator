from translate import Translator
import notify2
import pyperclip
def kamkarbro():
	txt=pyperclip.paste()
	translator= Translator(to_lang="marathi")
	ans=translator.translate(txt)
	notify2.init('Translator')
	n = notify2.Notification("Translator",
	                         ans,
	               # Icon name
	                        )
	n.show()


kamkarbro()