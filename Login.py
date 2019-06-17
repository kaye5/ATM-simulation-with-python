import os,sys
if sys.platform[:3] == "win" :
	import msvcrt
else :
	import getpass

i_rekening="";i_pass=""
def loginrek() : 
	os.system("cls")
	os.system("color 0f")
	print("="*80,end="")
	print("++","++".rjust(77),end="")
	print("++","ATM CGK".center(74),"++",end="")
	print("++","++".rjust(77),end="")
	print("="*80,)
	print(" Login ".center(80,"_"))
	print(f"{'':20}No. Rekening\t: ",end=" ")
	loginrek.i_rekening = str(input())
	print()

def passhid() :
	print(f"{'':20}Password [0-9] \t: ",end=" ",flush=True)
	password = "" 
	while True : 
		press = msvcrt.getch()
		try :
			pressd = str(press.decode("utf-8"))
			if press == b'\r' : 
				break
			elif press == b'\x08':
				os.system("cls")
				print("="*80,end="")
				print("++","++".rjust(77),end="")
				print("++","ATM CGK".center(74),"++",end="")
				print("++","++".rjust(77),end="")
				print("="*80,)
				print(" Login ".center(80,"_"))
				print(f"{'':20}No. Rekening\t: ",loginrek.i_rekening)
				password = password[0:len(password)-1]
				
				hid = "*"*len(password)
				print(f"{'':20}Password [0-9] \t: ",hid,end="",flush=True)
			elif 48<=ord(pressd)<=57 :
				print("*",end="",flush=True)
				password += pressd
		except :
			continue
	
	passhid.password = password	

def loginpass() : 
	os.system("cls")
	print("="*80,end="")
	print("++","++".rjust(77),end="")
	print("++","ATM CGK".center(74),"++",end="")
	print("++","++".rjust(77),end="")
	print("="*80,)
	print(" Login ".center(80,"_"))
	print(f"{'':20}No. Rekening\t: ",loginrek.i_rekening)
	#check platform
	if sys.platform[:3] == "win" :
		passhid()
		loginpass.i_pass = passhid.password
	else :
		loginpass.i_pass = getpass.getpass()
	print()
	print("="*80)
	print("="*80)

def passhid_admin() :
	password = "" 
	while True : 
		press = msvcrt.getch()
		try :
			pressd = str(press.decode("utf-8"))
			if press == b'\r' : 
				break
			elif press == b'\x08':
				os.system("cls")
				print("="*80,end="")
				print("++","++".rjust(77),end="")
				print("++","ATM CGK".center(74),"++",end="")
				print("++","++".rjust(77),end="")
				print("="*80,)
				print(" Login ".center(80,"_"))
				print(f"{'':20}No. Rekening\t: ",loginrek.i_rekening)
				password = password[0:len(password)-1]
				hid = "*"*len(password)
				print(f"{'':20}Pass \t\t: ",hid,end="",flush=True)
			elif 33<=ord(pressd)<=126 :
				print("*",end="",flush=True)
				password += pressd
		except :
			continue
	passhid_admin.password = password

def loginpass_admin() : 
	os.system("cls")
	print("="*80,end="")
	print("++","++".rjust(77),end="")
	print("++","ATM CGK".center(74),"++",end="")
	print("++","++".rjust(77),end="")
	print("="*80,)
	print(" Login ".center(80,"_"))
	print(f"{'':20}No. Rekening\t: ",loginrek.i_rekening)
	print(f"{'':20}Pass\t\t: ",end=" ",flush=True)
	#check platform
	if sys.platform[:3] == "win" :
		passhid_admin()
		loginpass_admin.i_pass = passhid_admin.password
	else :
		loginpass_admin.i_pass = getpass.getpass()
	print()
	print("="*80)
	print("="*80)

def change_hid_old() :
	print(f"{'':29}Password [0-9] \t: ",end="",flush=True)
	if sys.platform[:3] == "win" :
		password = "" 
		while True : 
			press = msvcrt.getch()
			try :
				pressd = str(press.decode("utf-8"))
				if press == b'\r' : 
					break
				elif press == b'\x08':
					os.system("cls")
					print("="*80)
					print("ATM CGK".center(79))
					print("_"*80)
					print("Ubah Password".center(79))
					print("="*80)
					print("Masukan Password lama".center(80))
					password = password[0:len(password)-1]
					hid = "*"*len(password)
					print(f"{'':29}Password [0-9] \t: {hid}",end="",flush=True) 
				elif 48<=ord(pressd)<=57 :
					print("*",end="",flush=True)
					password += pressd
				else :
					continue
			except :
				continue
		
		change_hid_old.password = password	
	else : 
		change_hid_old.password= getpass.getpass()
def change_hid_new() :
	print(f"{'':29}Password [0-9] \t: ",end="",flush=True)
	if sys.platform[:3] == "win" :
		password = "" 
		while True : 
			press = msvcrt.getch()
			try :
				pressd = str(press.decode("utf-8"))
				if press == b'\r' : 
					break
				elif press == b'\x08':
					os.system("cls")
					print("="*80)
					print("ATM CGK".center(79))
					print("_"*80)
					print("Ubah Password".center(79))
					print("="*80)
					print("Masukan Password lama".center(80))
					print(f"{'':29}Password [0-9] \t: {'*'*len(change_hid_old.password)}",end="",flush=True);print("")
					print("")
					print("Masukan password baru".center(80))
					password = password[0:len(password)-1]
					hid = "*"*len(password)
					print(f"{'':29}Password [0-9] \t: {hid}",end="",flush=True) 
					
				elif 48<=ord(pressd)<=57 :
					print("*",end="",flush=True)
					password += pressd
			except :
				continue
		
		change_hid_new.password = password	
	else :
		change_hid_new.password = getpass.getpass()
def add_new_rek() :
	if sys.platform[:3] == "win" :
		password = "" 
		while True : 
			press = msvcrt.getch()
			try :
				pressd = str(press.decode("utf-8"))
				if press == b'\r' : 
					break
				elif press == b'\x08':
					os.system("cls")
					print("="*80)
					print("ATM CGK".center(79))
					print("_"*80)
					print("Tmabah Rekening".center(80))
					print("="*80)
					password = password[0:len(password)-1]
					hid = "*"*len(password)
					print(f"\n{'':20}Masukan password [0-9]\t= {hid}",end="",flush=True) 
				elif 48<=ord(pressd)<=57 :
					print("*",end="",flush=True)
					password += pressd
				else :
					continue
			except :
				continue
		
		add_new_rek.password = password	
	else :
		add_new_rek.password = getpass.getpass

def add_new_adm() :
	if sys.platform[:3] == "win" :
		password = "" 
		while True : 
			press = msvcrt.getch()
			try :
				pressd = str(press.decode("utf-8"))
				if press == b'\r' : 
					break
				elif press == b'\x08':
					os.system("cls")
					print("="*80)
					print("ATM CGK".center(79))
					print("_"*80)
					print("Tambah Admin".center(80))
					print("="*80)
					password = password[0:len(password)-1]
					hid = "*"*len(password)
					print(f"\n{'':20}Masukan password \t= {hid}",end="",flush=True) 
				elif 33<=ord(pressd)<=126 :
					print("*",end="",flush=True)
					password += pressd
				else :
					continue
			except :
				continue
		
		add_new_adm.password = password	
	else :
		add_new_adm.password = getpass.getpass

def change_hid_old_adm() :
	print(f"{'':29}Password \t: ",end="",flush=True)
	if sys.platform[:3] == "win" :
		password = "" 
		while True : 
			press = msvcrt.getch()
			try :
				pressd = str(press.decode("utf-8"))
				if press == b'\r' : 
					break
				elif press == b'\x08':
					os.system("cls")
					print("="*80)
					print("ATM CGK".center(79))
					print("_"*80)
					print("Ubah Password".center(79))
					print("="*80)
					print("Masukan Password lama".center(80))
					password = password[0:len(password)-1]
					hid = "*"*len(password)
					print(f"{'':29}Password \t: {hid}",end="",flush=True) 
				elif 33<=ord(pressd)<=126 :
					print("*",end="",flush=True)
					password += pressd
				else :
					continue
			except :
				continue
		
		change_hid_old_adm.password = password	
	else : 
		change_hid_old_adm.password= getpass.getpass()
def change_hid_new_adm() :
	print(f"{'':29}Password \t: ",end="",flush=True)
	if sys.platform[:3] == "win" :
		password = "" 
		while True : 
			press = msvcrt.getch()
			try :
				pressd = str(press.decode("utf-8"))
				if press == b'\r' : 
					break
				elif press == b'\x08':
					os.system("cls")
					print("="*80)
					print("ATM CGK".center(79))
					print("_"*80)
					print("Ubah Password".center(79))
					print("="*80)
					print("Masukan Password lama".center(80))
					print(f"{'':29}Password \t: {'*'*len(change_hid_old_adm.password)}",end="",flush=True);print("")
					print("")
					print("Masukan password baru".center(80))
					password = password[0:len(password)-1]
					hid = "*"*len(password)
					print(f"{'':29}Password \t: {hid}",end="",flush=True) 
					
				elif 33<=ord(pressd)<=126 :
					print("*",end="",flush=True)
					password += pressd
			except :
				continue
		
		change_hid_new_adm.password = password	
	else :
		change_hid_new_adm.password = getpass.getpass()