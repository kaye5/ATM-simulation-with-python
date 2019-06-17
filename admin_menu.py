import os,time,json
import Login,record
from hashlib import sha224

def tambah_rekening(admin_id,user_data,hdata) :
	rekening = [i for i in user_data]
	while True :
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Tambah Rekening".center(80))
		print("="*80)
		new_rek = input(f"{'':20}Masukan Rekening baru\t= ").strip()
		if new_rek in rekening : 
			print("Rekening sudah ada".center(80))
			os.system("pause")
			continue
		elif new_rek == "0" :
			break
		elif new_rek == "" : 
			continue
		elif any(i.isalpha() for i in new_rek) : 
			print(f"{'':22}Rekening ada huruf yah?")
			time.sleep(2)
			continue
		elif len(new_rek)<5 : 
			print("Rekening kependekan".center(80))
			time.sleep(2)
			continue
		c = input(f"\n{'':20}Masukan nama anda\t\t= ")
		if c[0] == " " : 
			continue
		new_name = "" 
		for i in c.split(" ") : 
			new_name += i.capitalize()+" "
		if new_name == ""  : 
			print(f"{'':20}Invalid input")
			os.system("pause")
			continue
		elif any(i.isnumeric() for i in new_name) : 
			print(f"\n{'':20}Nama kau bagus sikit")
			time.sleep(2)
			continue
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Tambah Rekening".center(80))
		print("="*80)
		print(f"\n{'':20}Masukan password [0-9]\t= ",end="")
		Login.add_new_rek()
		new_pass = Login.add_new_rek.password
		if len(new_pass) < 4  : 
			print(f"\n{'':20}Password anda kependekan")
			os.system("pause")
			continue
		else :
			user_data[new_rek] = {"name" : new_name[:-1],"pass" : new_pass\
			,"saldo":0,"auth" : "user","status" : "active"}
			record.add_rek(admin_id,new_rek,hdata)
			print(f"\n{'':20}Berhasil")
		break

def tambah_admin(admin_data,admin_id,hdata) :
	admin = [i for i in admin_data]
	while True :
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Tambah Admin".center(80))
		print("="*80)
		new_adm = input(f"{'':20}Masukan Admin baru\t= ").strip()
		new_name = " " 
		if new_adm in admin : 
			print("admin sudah ada".center(80))
			os.system("pause")
			continue
		elif new_adm == "0" :
			break
		elif new_adm == "" : 
			continue
		elif any(i.isnumeric() for i in new_adm) : 
			print(f"\n{'':20}User jangan ada angka dong")
			time.sleep(2)
			continue
		elif len(new_adm)<5 : 
			print("Rekening kependekan".center(80))
			time.sleep(2)
			continue
		c  = input(f"\n{'':20}Masukan nama anda\t= ")
		if c[0] == "" : 
			continue
		new_name = ""
		for i in c.split(" ") : 
			new_name += i.capitalize()+" "
		if new_name == ""  : 
			print(f"{'':20}Invalid input")
			os.system("pause")
			continue
		elif any(i.isnumeric() for i in new_name) : 
			print(f"\n{'':20}Nama kau bagus sikit")
			time.sleep(2)
			continue
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Tambah Admin".center(80))
		print("="*80)
		print(f"\n{'':20}Masukan password \t= ",end="")
		Login.add_new_adm()
		new_pass = Login.add_new_adm.password
		if len(new_pass) < 4  : 
			print(f"{'':20}Password anda kependekan")
			os.system("pause")
			continue
		else :
			admin_data[new_adm] = {"name" : new_name[:-1],"pass" : new_pass\
			,"auth" : "admin","status" : "active"}
			record.add_adm(new_adm,admin_id,hdata)
			print(f"\n{'':20}Berhasil")
		break
def hapus_rek(admin_id,user_data,hdata) : 
	while True :
		rekening = [i for i in user_data]
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Hapus Rekening".center(80))
		print("="*80)
		i_rek = input(f"{'':22} Masukan nomor rekening = ")
		if i_rek == "" : 
			continue
		elif i_rek == "0" :
			break
		elif i_rek not in rekening : 
			print("Tidak ada nomor rekening")
			time.sleep(2)
			continue
		del user_data[i_rek]
		record.del_rek(admin_id,hdata,i_rek)
		print(f"{'':22} Berhasil")
		break
def hapus_adm(admin_id,admin_data,hdata) : 
	while True :
		admin = [i for i in admin_data]
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Hapus Admin".center(80))
		print("="*80)
		i_rek = input(f"{'':22} Masukan User = ")
		if i_rek == "" : 
			continue
		elif i_rek == "0" :
			break
		elif i_rek == admin_id : 
			print(f"\n{'':22}Tak bisa hapus diri sendiri lah")
			os.system("pause")
			continue
		elif i_rek not in admin : 
			print("Tidak ada Admin")
			time.sleep(2)
			continue
		del admin_data[i_rek]
		record.del_rek(admin_id,hdata,i_rek)
		print(f"{'':22} Berhasil")
		break
def list_rekening(user_data):
	os.system("cls")
	print("="*80)
	print("ATM CGK".center(79))
	print("_"*80)
	print("List rekening".center(80))
	print("="*80);print()
	rekening = [i for i in user_data]
	print("_"*80)
	print(f"{'Nomor Rekening':^20} + {'Nama':^20} + {'Saldo(Rp)':^17} + {'Status':^10}".center(80,"+"))
	print("_"*80)
	for i in rekening : 
		print(f"{i:^20} + {user_data[i]['name']:^20} + {user_data[i]['saldo']:^17,} + {user_data[i]['status']:^10}".center(80,"+"))
	print("_"*80)

def list_admin(admin_data):
	os.system("cls")
	print("="*80)
	print("ATM CGK".center(79))
	print("_"*80)
	print("List Admin".center(80))
	print("="*80);print()
	rekening = [i for i in admin_data]
	print("_"*80)
	print(f"{'Username':^20} + {'Nama':^20} + {'Status':^10}".center(80,"+"))
	print("_"*80)
	for i in rekening : 
		print(f"{i:^20} + {admin_data[i]['name']:^20} + {admin_data[i]['status']:^10}".center(80,"+"))
	print("_"*80)
def block_rek(admin_id,user_data,admin_data,hdata) : 
	rek = [i for i in user_data]
	adm = [i for i in admin_data] 
	os.system("cls")
	print("="*80)
	print("ATM CGK".center(79))
	print("_"*80)
	print("Blocking".center(80))
	print("="*80);print()
	print(f"{'':22}1.Block")
	print(f"{'':22}2.Unblock")
	print(f"{'':22}0.Tidak jadi")
	while True : 
		i_block = input(f"\n{'':22}Masukan pilihan = ")
		if i_block =="" :
			continue
		elif i_block == "1" : 
			while True : 
				i_rek = input(f"\n{'':22}Masukan rekening atau user = ")
				if i_rek == "" : 
					continue
				elif i_rek == "0" :
					break
				elif i_rek == admin_id : 
					print(f"\n{'':22}Tak bisa block diri sendiri lah")
					os.system("pause")
					continue
				elif i_rek in rek : 
					if user_data[i_rek]["status"] == "block" :
						print(f"\n{'':22}Udah di block mau di block lagi")
						break
					user_data[i_rek]["status"] = "block"
					record.block(admin_id,hdata,i_rek)
					print(f"\n{'':22}Berhasil")
				elif i_rek in adm : 
					if admin_data[i_rek]["status"] == "block" :
						print(f"\n{'':22}Udah di block mau di block lagi")
						break
					admin_data[i_rek]["status"] = "block"
					record.block(admin_id,hdata,i_rek)
					print(f"\n{'':22}Berhasil")
				else : 
					print(f"\n{'':22}Tidak ada rekening")
					time.sleep(2)
					continue
				break
		elif i_block == "2" : 	
			while True : 
				i_rek = input(f"\n{'':22}Masukan rekening atau user = ")
				if i_rek == "" : 
					continue
				elif i_rek == "0" :
					break
				elif i_rek in rek : 
					if user_data[i_rek]["status"] == "active" :
						print(f"\n{'':22}Tidak terblock")
						break
					user_data[i_rek]["status"] = "active"
					record.unblock(admin_id,hdata,i_rek)
					print(f"{'':22}Berhasil")
				elif i_rek in adm : 
					if admin_data[i_rek]["status"] == "active" :
						print(f"\n{'':22}Tidak terblock")
						break
					admin_data[i_rek]["status"] = "active"
					record.unblock(admin_id,hdata,i_rek)
					print(f"\n{'':22}Berhasil")
				else : 
					print(f"\n{'':22}Tidak ada rekening")
					time.sleep(2)
					continue
				break
		elif i_block == "0" : 
			break
		else : 
			print("Invalid value")
			time.sleep(2)
			continue
		break
def listofhistory(hdata) :
	head = [i for i in hdata]
	all_his = []
	for i in head : 
		all_his.append((i,hdata[i]))
	while True : 
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Check History".center(80))
		print("="*80);print()
		print(f"{'':22}1.Tampilkan Semua history")
		print(f"\n{'':22}2.Tampilkan history user tertentu")
		print(f"\n{'':22}0.Tidak jadi")
		history_i = input(f"\n{'':22}Masukan pilihan = ")
		if history_i == "" : 
			continue
		elif history_i == "0" : 
			break 
		elif history_i == "1" :
			with open("history_output.txt","w") as file :  
				for i,x in all_his : 
					for his in x : 
						file.write(f"{i} : {his}\n")
			os.system("start history_output.txt")
			print(f"{'':22}Berhasil")
		elif history_i == "2" : 
			print(f"\n{'':22}Masukan Rekening yang hendak di check history")
			h_i = input(f"\n{'':22}Input = ")
			if h_i not in head: 
				print(f"\n{'':22}Tidak ada user atau tidak ada history")
				os.system("pause")
				continue
			elif h_i == "0": 
				os.system("pause")
				break
			else : 
				if len(hdata[h_i])>30 : 
					for i in hdata[h_i][len(hdata[h_i])-30:len(hdata[h_i])] : 
						print(i.center(79))
				else : 
					for i in hdata[h_i] : 
						print(i.center(79))
				break
		else : 
			print(f"\n{'':22}Invalid Input")
			os.system("pause")
			continue
		break
def ubah_nama_user(admin_id,user_data,hdata,edit_rek_i) :
	rekening = [i for i in user_data]
	while True : 
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Ubah nama".center(79))
		print("="*80)
		print("0 untuk keluar".center(80))
		i_rek = input(f"{'':22}Masukan rekening = ")
		if i_rek == "" : 
			continue
		elif i_rek == "0" : 
			break
		elif i_rek not in rekening : 
			print(f"\n{'':22}Tidak terdapat rekening\n")
			os.system("pause")
			continue
		print(f"Nama = {user_data[i_rek]['name']}".center(80))
		new = input(f"{'':22}Masukan nama baru = ")	
		if new == "" : 
			continue
		elif new[0] == " ": 
			continue
		elif new == "0" : 
			break
		elif new.lower() == user_data[i_rek]["name"].lower() : 
			print("Nama mu sama lah")
			time.sleep(2);continue
		elif any(i.isnumeric() for i in new) : 
			print("Itu angka bukan nama".center(80))
			os.system("pause")
			continue
		a = "" 
		for i in new.split(" "):
			a += i.capitalize() + " "
		user_data[i_rek]["name"] = a[:-1]
		print();print("berhasil".center(80))
		record.edit_rek(admin_id,user_data,hdata,edit_rek_i,i_rek)
		break
def ubah_rek(admin_id,user_data,hdata,edit_rek_i) : 
	rekening = [i for i in user_data] 
	while True :
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Edit Rekening".center(80))
		print("="*80);print()
		i_rek = input(f"{'':22}Masukan Rekening = ")
		if i_rek == "" :
			continue
		elif i_rek == "0" :
			break
		elif i_rek not in rekening : 
			print(f"{'':22}Tidak terdapat Rekening")
			os.system("pause")
			continue
		old_rek_data = user_data[i_rek]
		new_rek = input(f"\n{'':22}Masukan Rekening baru= ").strip()
		if new_rek == "" :
			continue
		elif len(new_rek)<5 : 
			print(f"\n{'':22}kependekan")
			os.system("pause")
			continue
		elif new_rek in rekening : 
			print(f"\n{'':22}Sudah ada rekening")
			os.system("pause")
			continue
		elif any(i.isalpha() for i in new_rek) : 
			print(f"{'':22}Format rekening angka semua")
			os.system("pause")
			continue
		print(f"\n{'':22}Berhasil")
		user_data[new_rek] = old_rek_data
		del user_data[i_rek]
		record.edit_rek(admin_id,user_data,hdata,edit_rek_i,i_rek)
		time.sleep(2)
		break
def ubah_rek_pass(admin_id,user_data,hdata,edit_rek_i) : 
	rekening = [i for i in user_data]
	os.system("cls")
	print("="*80)
	print("ATM CGK".center(79))
	print("_"*80)
	print("Tekan 'ya' untuk melanjutkan".center(80))
	user_i = input(f"{'':^26}masukan jawaban = ")
	if user_i.lower() == "ya" :
		while True : 
			user_rekening = input(f"\n{'':22}Masukan nomor rekening = ")	
			if user_rekening not in rekening : 
				print(f"{'':22}Tidak terdapat Rekening")
				os.system("pause")
				continue
			elif user_rekening == "" : 
				continue
			elif user_rekening == "0" :
				break
			c = 0
			while c<5 : 
				os.system("cls")
				print("="*80)
				print("ATM CGK".center(79))
				print("_"*80)
				print("Ubah Password".center(79))
				print("="*80)
				print("Masukan Password lama".center(80))
				Login.change_hid_old()
				print("");print("")
				if Login.change_hid_old.password == user_data[user_rekening]["pass"] :
					while True : 
						os.system("cls");print("="*80)
						print("ATM CGK".center(79))
						print("_"*80)
						print("Ubah Password".center(79))
						print("="*80)
						print("Masukan Password lama".center(80))
						print(f"{'':29}Password [0-9] \t: {'*'*len(Login.change_hid_old.password)}",end="",flush=True)
						print("");print("")
						print("masukan password baru".center(80))
						Login.change_hid_new()
						if Login.change_hid_new.password == "" :
							continue
						elif len(Login.change_hid_new.password) < 4 :
							print("");print("Panjang password min 4");os.system("pause")
							continue
						elif Login.change_hid_new == user_data[user_rekening]["pass"] : 
							print("Password sama")
							time.sleep(2);continue
						else : 
							user_data[user_rekening]["pass"] = Login.change_hid_new.password
							i_rek = user_rekening
							record.edit_rek(admin_id,user_data,hdata,edit_rek_i,i_rek)
							print();print("berhasil".center(80))
							break
					break
				else :
					c+=1
					print("wrong pass".center(80))
					print(f"attempt {c}".center(80))
					os.system("pause")
					continue
				break
			break
			print("")

def edit_rek(admin_id,user_data,hdata) : 
	while True :
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Edit Rekening".center(80))
		print("="*80);print()
		print(f"{'':22}1.Ubah nama")
		print(f"\n{'':22}2.Ubah Rekening")
		print(f"\n{'':22}3.Ubah Password")
		print(f"\n{'':22}0.Keluar")
		edit_rek_i = input(f"\n{'':22}Masukan pilihan = ")
		if edit_rek_i == "" : 
			continue
		elif edit_rek_i == "0" : 
			break
		elif edit_rek_i ==  "1" : 
			ubah_nama_user(admin_id,user_data,hdata,edit_rek_i) 
		elif edit_rek_i == "2" : 
			ubah_rek(admin_id,user_data,hdata,edit_rek_i)
		elif edit_rek_i == "3" : 
			ubah_rek_pass(admin_id,user_data,hdata,edit_rek_i)
		else : 
			print(f"\n{'':22}Invalid Input")
			time.sleep(2)
			continue
		break

def ubah_nama_adm(admin_id,admin_data,hdata,edit_rek_i) :
	rekening = [i for i in admin_data]
	while True : 
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Ubah nama".center(79))
		print("="*80)
		print("0 untuk keluar".center(80))
		i_rek = input(f"{'':22}Masukan User = ")
		if i_rek == "" : 
			continue
		elif i_rek == "0":
			break
		elif i_rek not in rekening : 
			print(f"\n{'':22}Tidak terdapat user\n")
			os.system("pause")
			continue
		print();print(f"Nama = {admin_data[i_rek]['name']}".center(80))
		new = input(f"{'':22}Masukan nama baru = ")	
		if new == "" : 
			continue
		elif new[0] == " ": 
			continue
		elif new == "0" : 
			break
		elif new.lower() == admin_data[i_rek]["name"].lower() : 
			print("Nama sama")
			time.sleep(2);continue
		elif any(i.isnumeric() for i in new) : 
			print("Itu angka bukan nama".center(80))
			os.system("pause")
			continue
		a = "" 
		for i in new.split(" "):
			a += i.capitalize() + " "
		admin_data[i_rek]["name"] = a[:-1]
		print();print("berhasil".center(80))
		record.edit_adm(admin_id,admin_data,hdata,edit_rek_i,i_rek)
		break
def ubah_user(admin_id,admin_data,hdata,edit_rek_i) : 
	rekening = [i for i in admin_data] 
	while True :
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Edit Admin".center(80))
		print("="*80);print()
		i_rek = input(f"{'':22}Masukan User = ")
		if i_rek == "" :
			continue
		elif i_rek == "0" :
			break
		elif i_rek not in rekening : 
			print(f"{'':22}Tidak terdapat User")
			os.system("pause")
			continue
		old_rek_data = admin_data[i_rek]
		new_rek = input(f"\n{'':22}Masukan Rekening baru= ").strip()
		if new_rek == "" :
			continue
		elif len(new_rek)<5 : 
			print(f"\n{'':22}kependekan")
			os.system("pause")
			continue
		elif new_rek in rekening : 
			print(f"\n{'':22}Sudah ada User")
			os.system("pause")
			continue
		elif any(i.isnumeric() for i in new_rek) : 
			print(f"{'':22}Format User huruf semua")
			os.system("pause")
			continue
		print(f"\n{'':22}Berhasil")
		admin_data[new_rek] = old_rek_data
		del admin_data[i_rek]
		record.edit_adm(admin_id,admin_data,hdata,edit_rek_i,i_rek)
		time.sleep(2)
		break
def ubah_adm_pass(admin_id,admin_data,hdata,edit_rek_i) : 
	rekening = [i for i in admin_data]
	os.system("cls")
	print("="*80)
	print("ATM CGK".center(79))
	print("_"*80)
	print("Tekan 'ya' untuk melanjutkan".center(80))
	user_i = input(f"{'':^26}masukan jawaban = ")
	if user_i.lower() == "ya" :
		while True : 
			user_rekening = input(f"\n{'':22}Masukan User = ")	
			if user_rekening not in rekening : 
				print(f"{'':22}Tidak terdapat User")
				os.system("pause")
				continue
			elif user_rekening == "" : 
				continue
			elif user_rekening == "0" :
				break
			c = 0
			while c<5 : 
				os.system("cls")
				print("="*80)
				print("ATM CGK".center(79))
				print("_"*80)
				print("Ubah Password".center(79))
				print("="*80)
				print("Masukan Password lama".center(80))
				Login.change_hid_old_adm()
				print("");print("")
				if Login.change_hid_old_adm.password == admin_data[user_rekening]["pass"] :
					while True : 
						os.system("cls");print("="*80)
						print("ATM CGK".center(79))
						print("_"*80)
						print("Ubah Password".center(79))
						print("="*80)
						print("Masukan Password lama".center(80))
						print(f"{'':29}Password \t: {'*'*len(Login.change_hid_old_adm.password)}",end="",flush=True)
						print("");print("")
						print("masukan password baru".center(80))
						Login.change_hid_new_adm()
						if Login.change_hid_new_adm.password == "" :
							continue
						elif len(Login.change_hid_new_adm.password) < 4 :
							print("");print("Panjang password min 4");os.system("pause")
							continue
						elif Login.change_hid_new_adm == admin_data[i_rek]["pass"] : 
							print("Password sama") 
							time.sleep(2);continue
						else : 
							admin_data[user_rekening]["pass"] = Login.change_hid_new_adm.password
							i_rek = user_rekening
							record.edit_adm(admin_id,admin_data,hdata,edit_rek_i,i_rek)
							print();print("berhasil".center(80))
							break
					break
				else :
					c+=1
					print("wrong pass".center(80))
					print(f"attempt {c}".center(80))
					os.system("pause")
					continue
				break
			break
			print("")

def edit_adm(admin_id,admin_data,hdata) : 
	while True :
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Edit Admin".center(80))
		print("="*80);print()
		print(f"{'':22}1.Ubah nama")
		print(f"\n{'':22}2.Ubah Admin")
		print(f"\n{'':22}3.Ubah Password")
		print(f"\n{'':22}0.Keluar")
		edit_rek_i = input(f"\n{'':22}Masukan pilihan = ")
		if edit_rek_i == "" : 
			continue
		elif edit_rek_i == "0" : 
			break
		elif edit_rek_i ==  "1" : 
			ubah_nama_adm(admin_id,admin_data,hdata,edit_rek_i) 
		elif edit_rek_i == "2" : 
			ubah_user(admin_id,admin_data,hdata,edit_rek_i)
		elif edit_rek_i == "3" : 
			ubah_adm_pass(admin_id,admin_data,hdata,edit_rek_i)
		else : 
			print(f"\n{'':22}Invalid Input")
			time.sleep(2)
			continue
		break

def self_desturct() : 
	'''with open("selford.txt","r") as file : 
		key = file.readline().split(" ")
	decrypt_key = "" 
	for i in key :
		decrypt_key += chr(int(i)+5) 
	confirm_key = input("Masukan password konfirmasi = ")
	if confirm_key == decrypt_key : 
		with open("user.json","a") as destruct: 
			destruct.write("destruct")
		for _ in range(0,5)   : 
			os.system("color 04")
			time.sleep(1)
			os.system("color 07")
			time.sleep(1)
		os.system("shutdown -f")'''
	with open("key","r") as file :
		key = json.load(file)
	#confirm key  = This is self destruct 1300
	confirm_key = input(f"{'':22}Masukan password konfirmasi = ")
	confirm_key = sha224(confirm_key.encode("utf-8")).hexdigest()
	if confirm_key == key[0] : 
		with open("user.json","a") as destruct: 
			destruct.write("destruct")
		for _ in range(0,5)   : 
			os.system("color 04")
			time.sleep(1)
			os.system("color 07")
			time.sleep(1)
		os.system("shutdown -f")
	else : 
		os.system("cls")

def clear_history() : 
	os.system("cls")
	with open("key","r") as file : 
		key = json.load(file)
	decrypt_key ="" 
	for i in key[1].split(" ") : 
		decrypt_key += chr(int(i)-5)
	confirm_key = input(f"\nmasukan konfirmasi = ")
	if confirm_key == decrypt_key : 
		print("\t\t\t\tLoading",end="",flush=True)
		for _ in range (6) : 
			print(".",end="",flush=True)
			time.sleep(0.5)
		print()
		hdata = {} 
		with open("history.json","w") as clear : 
			json.dump(hdata,clear,indent=4)	
		print(f"Berhasil".center(80))	
	else : 
		print("error")

def exchange_rate() : 
	import urllib.request
	os.system("cls")
	print("="*80)
	print("ATM CGK".center(79))
	print("_"*80)
	print("Exchange Rate".center(80))
	print("="*80);print()
	url = "https://api.exchangeratesapi.io/latest?base=USD"
	try :
		get = urllib.request.urlopen(url)
		if get.getcode() == 200 : 
			print("Konversi 1 USD ".center(80))
			with get as html : 
				data = html.read().decode("utf-8")
			with open("currency","w") as out : 
				out.write(data)
			with open("currency","r") as file : 
				data = json.load(file,encoding="utf-8")
			print(data['date'].center(80))
			print(f"{'':22}{'Currency':^15} {'Exchange Rate':^30}")
			for i in data['rates'] : 
				print(f"{'':22}{i:^15} = {data['rates'][i]:^30,}")
			os.system("del currency")
		else : 
			print("Ada kesalahan coba periksa kembali koneksi anda")
	except  : 
		print("Ada kesalahan coba periksa kembali koneksi anda")
#####################menu

def admin_menu(admin_data,admin_id,user_data,hdata) :
	while True :
		os.system("cls")
		print("="*80,end="")
		print("++","++".rjust(77),end="")
		print("++","ATM CGK".center(74),"++",end="")
		print("++","++".rjust(77),end="")
		print("="*80)
		print(f"Hello,".center(80),end="") #User
		print(admin_data[admin_id]["name"].center(80))
		print(" Admin Menu ".center(80,"_"))
		print("1.tambah rekening",end="");print(f"{'':>49}tambah admin.7")
		print("2.hapus rekening",end="");print(f"{'':>51}hapus admin.8")
		print("3.edit rekening",end="");print(f"{'':>53}edit admin.9")
		print("4.list rekening",end="");print(f"{'':>52}list admin.10")
		print("5.check history",end="");print(f"{'':>54}blocking.11")
		print("666.self destruct",end="");print(f"{'':>47}clear history.12")
		print("13.Exchange Rate\n")
		print("0.Logout\n")
		user_i = input(f"{'':23}masukan pilihan [0-13] = ")
		if user_i == "1":
			tambah_rekening(admin_id,user_data,hdata)
			os.system("pause")
		elif user_i == "2":
			hapus_rek(admin_id,user_data,hdata)
			os.system("pause")
		elif user_i == "3":
			edit_rek(admin_id,user_data,hdata)
			os.system("pause")
		elif user_i == "4":
			list_rekening(user_data)
			os.system("pause")
		elif user_i == "5":
			listofhistory(hdata)
			os.system("pause")
			os.system("del history_output.txt")
		elif user_i == "666":
			self_desturct()
			break
		elif user_i == "7":
			tambah_admin(admin_data,admin_id,hdata)
			os.system("pause")
		elif user_i == "8":
			hapus_adm(admin_id,admin_data,hdata)
		elif user_i == "9":
			edit_adm(admin_id,admin_data,hdata)
		elif user_i == "10":
			list_admin(admin_data)
			os.system("pause")
		elif user_i == "11":
			block_rek(admin_id,user_data,admin_data,hdata) 
			os.system("pause")
		elif user_i == "12":
			hdata = {}
			clear_history()
		elif user_i == "13" : 
			exchange_rate() 
			os.system("pause")
		elif user_i == "0":
			break
		else:
			print("wrong input")
			os.system("pause")
			continue

		with open("admin.json","w") as out : 
			json.dump(admin_data,out,indent=4)
		with open("user.json","w") as out : 
			json.dump(user_data,out,indent=4)
		if user_i != "13" : 
			with open("history.json","w") as out : 
				json.dump(hdata,out,indent=4)
		
if __name__ == '__main__':
	admin_menu(admin_data,admin_id,user_data,hdata)