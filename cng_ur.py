# Coded by Cracker 
# CRACKER911181
 

<<<<<<< HEAD
import os,time,sys



#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest

def hide():

	vicurl=str(input(rosy+"\n\nEnter Your URL: "))
	doman=str(input("Enter A Domain (eg: 'https://google.com'): "))

	print(pest+"\n\n\t\tGenarating Your Link\n")

	os.system("curl -s https://is.gd/create.php\?format\=simple\&url\="+vicurl+" >> ln.test")
	oo=open("ln.test","r").read()

	oo1=oo.find("://")
	ox=str(oo[oo1+3:])
	real=str(yellow+"\n\nYour Link:	"+doman+"-@"+ox)

	print(real)
	os.system("rm ln.test")
	time.sleep(7)


while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] URL Changer [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.Change URL\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		hide()
	elif chose=="00":
		break
=======
import base64, codecs
magic = 'aW1wb3J0IG9zLHRpbWUsc3lzCgoKCiNUZXh0IGNvbG91cgojY3JlYXRlZCBCeSBDcmFja2VyOTExMTgxCmNvbG91cm9mZj0iXHgxYlswMG0iICNjb2xvdXIgb2ZmCgpyZWQ9Ilx4MWJbOTFtIiAjcmVkCmdyZWVuPSJceDFiWzkybSIgI2dyZWVuCnllbGxvdz0iXHgxYls5M20iICN5ZWxsb3cKYmx1ZT0iXHgxYls5NG0iICNibHVlCnJvc3k9Ilx4MWJbOTVtIiAjcm9zeQpwZXN0PSJceDFiWzk2bSIgI3Blc3QKCmRlZiBoaWRlKCk6CgoJdmljdXJsPXN0cihpbnB1dChyb3N5KyJcblxuRW50ZXIgWW91ciBVUkw6ICIpKQoJZG9tYW49c3RyKGlucHV0KCJFbnRlciBBIERvbWFpbiAoZWc6ICdodHRwczovL2dvb2dsZS5jb20n'
love = 'XGbtVvxcPtbWpUWcoaDbpTImqPfvKT5poyk0KUEUMJ5upzS0nJ5aVSyiqKVtGTyhn1khVvxXPtyipl5mrKA0MJ0bVzA1pzjtYKZtnUE0pUZ6Yl9cpl5aMP9wpzIuqTHhpTujKQ9zo3WgLKEpCKAcoKOfMIjzqKWfKQ0vX3McL3IloPfvVQ4+VTkhYaEyp3DvXDbWo289o3OyovtvoT4hqTImqPVfVaVvXF5lMJSxXPxXPtyiomR9o28hMzyhMPtvBv8iVvxXPJ94CKA0pvuio1giomReZmcqXDbWpzIuoQ1mqUVbrJIfoT93XlWpoykhJJ91pvOZnJ5eBtxvX2EioJShXlVgDPVeo3tcPtbWpUWcoaDbpzIuoPxXPJ9mYaA5p3EyoFtvpz0toT4hqTImqPVcPty0nJ1yYaAfMJIjXQpcPtbXq2ucoTHtIUW1MGbXPJ9mYaA5p3EyoFtaL2ky'
god = 'YXInKQoJcHJpbnQoYmx1ZStmIiIiCiAgIF9fX18gICAgICAgICAgICAgICAgXyAgICAgICAgICAgICAgICBfX19fXyAgICAgICAgICAgXwogIC8gX19ffF8gX18gX18gXyAgX19ffCB8IF9fX19fIF8gX18gICB8XyAgIF98X18gICBfX18gfCB8CiAiIiIrYmx1ZSsiIiJ8IHwgICB8ICdfXy8gX2AgfC8gX198IHwvIC8gXyBcICdfX3xfX19ffCB8LyBfIFwgLyBfIFx8IHwKICIiIitwZXN0KyIiInwgfF9fX3wgfCB8IChffCB8IChfX3wgICA8ICBfXy8gfCB8X19fX198IHwgKF8pIHwgKF8pIHwgfAogIFxfX19ffF98ICBcX18sX3xcX19ffF98XF9cX19ffF98ICAgICAgIHxffFxfX18vIFxfX18vfF98XG5cbiAiIiIrZ3Jl'
destiny = 'MJ4eVvVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPNtVvVvX2WfqJHeVvVvJ+XLuI0tIIWZVRAbLJ5aMKVtJ+XLuI0tKT4vVvVeM3WyMJ4eVvVvVQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CFVvVvgwo2kiqKWiMzLcPtxXPJAbo3AyCKA0pvucoaO1qPujMKA0XlWpoykhKUEpqQRhD2uuozqyVSIFGSkhKUEpqPVepzIxXlVjZP5PLJAeVSEiVRuioJIpoykhVvglo3A5XlWSoaEypvOMo3IlVR9jqTyiowbtVvxcPtxXPJyzVTAbo3AyCG0vZFV6PtxWnTyxMFtcPtyyoTyzVTAbo3AyCG0vZQNvBtbWPJWlMJSePt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969
