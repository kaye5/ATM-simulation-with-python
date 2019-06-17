import os,Login,time,record,json
def check_saldo(user_data,user_rekening):
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Check Saldo".center(79))
		print()
		print("="*80)
		print(f"sisa saldo anda = Rp. {user_data[user_rekening]['saldo']:,} ".center(80))
		print()
def tarek(user_data,user_rekening,hdata) :
	value = ""
	while True :
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Tarik Uang".center(79))
		print("="*80)	
		print("1.Rp 100.000",end="")
		print("Rp 200.000.2".rjust(68))
		print("3.Rp 500.000",end="")
		print("Rp 1.000.000.4".rjust(68))
		print("0.Tidak jadi");print("")
		user_i=input(f"{'':^22}MAU TARIK BERAPA DUIT [0-4]? ");print()
		if user_i == "1":
		    if  user_data[user_rekening]["saldo"] < 100000  :
		        print("MAAF,SALDO ANDA TIDAK CUKUP")
		    else:
		        user_data[user_rekening]["saldo"] -= 100000
		        print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
		        print(f"{'':^22}TERIMA KASIH".center(80))
		        record.his_tarek(user_rekening,user_i,hdata)
		elif user_i == "2":
		    if user_data[user_rekening]["saldo"] < 200000 :
		        print("MAAF,SALDO ANDA TIDAK CUKUP")
		    else:
		        user_data[user_rekening]["saldo"] -= 200000
		        print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
		        print(f"{'':^22}TERIMA KASIH".center(80))
		        record.his_tarek(user_rekening,user_i,hdata)
		elif user_i== "3":
		    if user_data[user_rekening]["saldo"]< 500000 :
		        print("MAAF,SALDO ANDA TIDAK CUKUP")
		    else:
		        user_data[user_rekening]["saldo"] -= 500000
		        print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
		        print(f"{'':^22}TERIMA KASIH".center(80))
		        record.his_tarek(user_rekening,user_i,hdata)
		elif user_i == "4":
		    if user_data[user_rekening]["saldo"] < 1000000 :
		        print(f"{'':^22}MAAF,SALDO ANDA TIDAK CUKUP")
		    else:
		        user_data[user_rekening]["saldo"] -= 1000000
		        print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
		        print(f"{'':^22}TERIMA KASIH")
		        record.his_tarek(user_rekening,user_i,hdata)

		elif user_i == "0":
			print(f"{'':^22}TERIMA KASIH")
			break
		else:
		    print(f"{'':^22}MAAF INPUT TIDAK DIKENALI")
		    os.system("pause")
		    continue
		break		

def setor(user_data,user_rekening,hdata) : 
	while True :
		value = "" 
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Setor".center(79))
		print("="*80)	
		print("1.Rp 100.000",end="")
		print("Rp 200.000.2".rjust(68))
		print("3.Rp 500.000",end="")
		print("Rp 1.000.000.4".rjust(68))
		print("5. Lainnya");print("")
		print("0.Tidak jadi");print("")
		print("Ciee gajian".center(80))
		user_i=input(f"{'':^22}MAU SETOR BERAPA DUIT [0-5] = ");print("")
		if user_i== "1":
		    user_data[user_rekening]["saldo"] += 100000
		    print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
		    record.his_setor(user_rekening,user_i,hdata,value)
		elif user_i == "2":
		    user_data[user_rekening]["saldo"] += 200000
		    print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
		    record.his_setor(user_rekening,user_i,hdata,value) 
		elif user_i == "3":
		    user_data[user_rekening]["saldo"] += 500000
		    print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
		    record.his_setor(user_rekening,user_i,hdata,value) 
		elif user_i== "4":
		    user_data[user_rekening]["saldo"] += 1000000
		    print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
		    record.his_setor(user_rekening,user_i,hdata,value) 
		elif user_i == "5":
			while True :
				try : 
					value = int(input(f"{'':22}Masukan nominal setoran anda= "))
					if value == "" or value%5000!=0 or value<10000:
						print(f"{'':22}Input tidak memungkinkan")
						os.system("pause")
						continue
					elif value == 0 :
						break
					user_data[user_rekening]["saldo"] += value
					print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
					record.his_setor(user_rekening,user_i,hdata,value) 
					break
				except : 
					print(f"{'':22}Input tidak dikenali")
					os.system("pause")
					continue
		elif user_i == "0" :
			break
		else:
		    print(f"{'':^22}MAAF INPUT TIDAK DIKENALI");print("")
		    os.system("pause")
		    continue
		break
	print(f"{'':^22}TERIMA KASIH")

def change_pass(user_data,user_rekening,hdata) : 
	os.system("cls")
	print("="*80)
	print("ATM CGK".center(79))
	print("_"*80)
	print("Tekan 'ya' untuk melanjutkan".center(80))
	user_i = input(f"{'':^26}masukan jawaban = ")
	if user_i.lower() == "ya" :
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
					elif Login.change_hid_old.password == Login.change_hid_new.password : 
						print("\npassword sama")
						time.sleep(2)
						continue
					else : 
						user_data[user_rekening]["pass"] = Login.change_hid_new.password
						record.his_cpass(user_rekening,hdata)
						print("\nberhasil")
						time.sleep(2)
						break
				break
			else :
				c+=1
				print("wrong pass".center(80))
				print(f"attempt {c}".center(80))
				os.system("pause")
				continue
		print("")
	else :
		print("TERIMA KASIH")

def ubah_nama(user_data,user_rekening,hdata) :
	while True : 
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Ubah nama".center(79))
		print("="*80)
		print("0 untuk keluar".center(80))
		print(f"Nama = {user_data[user_rekening]['name']}".center(80))
		new = input(f"{'':^30}Masukan nama baru = ").strip()
		if new == "" : 
			continue
		elif new == "0" : 
			break
		elif new[0] == " " :
			continue
		elif new.lower() == user_data[user_rekening]["name"].lower() : 
			print("Nama sama".center(80))
			time.sleep(2)
			continue
		elif any(i.isnumeric() for i in new ) : 
			print("Itu angka bukan nama".center(80))
			os.system("pause")
			continue
		a = "" 
		for i in new.split(" "):
			a += i.capitalize() + " "
		user_data[user_rekening]["name"] = a[:-1]
		print("berhasil".center(80))
		record.his_cname(user_rekening,hdata)
		break
def tf(user_data,user_rekening,hdata) : 
	value=""
	rek = [i for i in user_data]
	while True :
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Transfer".center(79))
		print("="*80)
		print("1.Rp 100.000",end="")
		print("Rp 200.000.2".rjust(68))
		print("3.Rp 500.000",end="")
		print("Rp 1.000.000.4".rjust(68))
		print("5.Lainnya\n")
		print("6.Tidak jadi");print("")
		user_d =input(f"{'':^22}MASUKAN REKENING TUJUAN = ");print("") 
		if user_d == user_rekening :
			print("Tidak bisa Transfer ke rekening sendiri")
			os.system("pause")
			continue
		elif user_d == ""  :
			continue
		elif user_d == "6" :
			break 
		elif user_d in rek : 
			user_i=input(f"{'':^22}MAU TRANSFER BERAPA [1-6] = ");print("")
			if user_i== "1":
				if user_data[user_rekening]["saldo"] >= 100000:
					user_data[user_rekening]["saldo"] -= 100000
					user_data[user_d]["saldo"] += 100000
					print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
					record.his_cf(user_rekening,user_d,user_i,hdata,value)
				else : 
					print(f"{'':^21} Saldo tak mecukupi")
					os.system("pause")
					continue
			elif user_i == "2":
				if user_data[user_rekening]["saldo"] >= 200000:
				    user_data[user_rekening]["saldo"] -= 200000
				    user_data[user_d]["saldo"] +=200000
				    print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
				    record.his_cf(user_rekening,user_d,user_i,hdata,value)
				else : 
					print(f"{'':^21} Saldo tak mecukupi")
					os.system("pause")
					continue
			elif user_i == "3":
				if user_data[user_rekening]["saldo"] >= 500000:
				    user_data[user_rekening]["saldo"] -= 500000
				    user_data[user_d]["saldo"] += 500000
				    print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
				    record.his_cf(user_rekening,user_d,user_i,hdata,value)
				else : 
					print(f"{'':^21}Saldo tak mencukupi")
					os.system("pause")
					continue
			elif user_i== "4":
				if user_data[user_rekening]["saldo"] >= 1000000:
					user_data[user_rekening]["saldo"] -= 1000000
					user_data[user_d]["saldo"] += 1000000
					print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
					record.his_cf(user_rekening,user_d,user_i,hdata,value)
				else : 
					print(f"{'':^21s}Saldo tak mencukupi")
					os.system("pause")
					continue

			elif user_i == "5" : 
				try : 
					value = int(input(f"{'':21} Masukan jumlah= "));print()
					if value == "" : 
						continue
					elif value == 6 :
						print(f"{'':^22}TERIMA KASIH")
						break
					elif value%50000 != 0 or value<10000:
						print(f"{'':^22}Jumlah tidak memungkinkan")
						os.system("pause")
						continue
					elif user_data[user_rekening]["saldo"]<value\
					or user_data[user_rekening]["saldo"]<=50000 : 
						print("Saldo anda tidak cukup".center(80))
						os.system("pause")
						break
					else : 
						print(f"jumlah Trasnfer {value:,}".center(80))
						user_data[user_rekening]["saldo"]-=value 
						user_data[user_d]["saldo"]+=value 
						print(f"Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}".center(80))
						record.his_cf(user_rekening,user_d,user_i,hdata,value)
				except : 
					print("invalid value".center(80))
					os.system("pause")
					continue
			elif user_i == "6" :
				break
			else:
			    print("MAAF INPUT TIDAK DIKENALI".rjust(22));print("")
			    os.system("pause")
			    continue
		else :
			print("Tidak terdapat no rekening".rjust(22))
			os.system("pause")
			continue
		break
	print("TERIMA KASIH".center(80))

def buang_duit(user_data,user_rekening,hdata):
	value = ""
	while True :
		os.system("cls")
		print("="*80)
		print("ATM CGK".center(79))
		print("_"*80)
		print("Buang Uang".center(79))
		print("="*80)	
		print("1.Rp 100.000",end="")
		print("Rp 200.000.2".rjust(68))
		print("3.Rp 500.000",end="")
		print("Rp 1.000.000.4".rjust(68))
		print("5.Lainnya");print()
		print("0.Tidak jadi");print("")
		user_i=input(f"{'':^22}MAU Buang BERAPA DUIT [0-5]? ");print()
		if user_i == "1":
		    if  user_data[user_rekening]["saldo"] < 100000  :
		        print("MAAF,SALDO ANDA TIDAK CUKUP")
		    else:
		        user_data[user_rekening]["saldo"] -= 100000
		        print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
		        print("TERIMA KASIH".center(80))
		        record.his_buang(user_rekening,user_i,hdata,value)
		elif user_i == "2":
		    if user_data[user_rekening]["saldo"] < 200000 :
		        print("MAAF,SALDO ANDA TIDAK CUKUP")
		    else:
		        user_data[user_rekening]["saldo"] -= 200000
		        print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
		        print("TERIMA KASIH".center(80))
		        record.his_buang(user_rekening,user_i,hdata,value)
		elif user_i== "3":
		    if user_data[user_rekening]["saldo"]< 500000 :
		        print("MAAF,SALDO ANDA TIDAK CUKUP")
		    else:
		        user_data[user_rekening]["saldo"] -= 500000
		        print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
		        print("TERIMA KASIH".center(80))
		        record.his_buang(user_rekening,user_i,hdata,value)
		elif user_i == "4":
		    if user_data[user_rekening]["saldo"] < 1000000 :
		        print("MAAF,SALDO ANDA TIDAK CUKUP")
		    else:
		        user_data[user_rekening]["saldo"] -= 1000000
		        print(f"{'':^22}Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}");print()
		        print("TERIMA KASIH")
		        record.his_buang(user_rekening,user_i,hdata,value)
		elif user_i == "5" : 
			try : 
				value = int(input(f"{'':21} Masukan jumlah= "));print()
				if value == "" : 
					continue
				elif value == 0 :
					print("TERIMA KASIH".center(80))
					break
				elif value%50000 != 0 or value<10000:
					print("Jumlah tidak memungkinkan".center(80))
					os.system("pause")
					continue
				elif user_data[user_rekening]["saldo"]<value : 
					print("Saldo anda tidak cukup".center(80))
					os.system("pause")
					continue
				else : 
					print(f"jumlah Buang {value:,}".center(80))
					user_data[user_rekening]["saldo"]-=value 
					print(f"Sisa saldo Rp. {user_data[user_rekening]['saldo']:,}".center(80))
					print("TERIMA KASIH".center(80))
					record.his_buang(user_rekening,user_i,hdata,value)
			except : 
				print("invalid value".center(80))
				os.system("pause")
				continue

		elif user_i == "0":
			print("TERIMA KASIH".center(80))
			break
		else:
		    print("MAAF INPUT TIDAK DIKENALI")
		    os.system("pause")
		    continue
		break	
def konversi_uang(data) : 
	while  True :
		try : 
			os.system("cls")
			rp = int(input("Konversi Rp = "));print(f"\nRp. {rp:,} ")
			print(f"{'1':<19} USD ==> {round(data['rates']['IDR'],3):>20,} IDR")
			usd = rp/data['rates']['IDR']
			for i in data['rates'] : 
				print(f"{rp:<19,} IDR ==> {round(usd*data['rates'][i],3):>20,} {i}")
			break
		except : 
			print(f"{'':22}Invalid value")
			time.sleep(2);continue
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
				print(f"{'':22}{i:^15} = {round(data['rates'][i],5):^30,}")	
			while True : 
				print(f"\n{'':22}1.Konversi rupiah")
				print(f"{'':22}0.Keluar")
				confirm = input(f"{'':22}Pilihan = ")
				if confirm == "0" : 
					break
				elif confirm == "1" : 
					konversi_uang(data)
				else : 
					print(f"{'':22}Salah input")
					time.sleep(2)
					continue
			os.system("del currency")
		else : 
			print("Ada kesalahan coba periksa kembali koneksi anda")
	except  : 
		print("Ada kesalahan coba periksa kembali koneksi anda")

def check_history(user_rekening,hdata) : 
	os.system("cls")
	print("="*80)
	print("ATM CGK".center(79))
	print("_"*80)
	print("Check History".center(79))
	print("="*80)
	for i in hdata[user_rekening] : 
		print(i.center(79))
################MENU BOSS
def main(user_data,user_rekening,hdata) :
	while True:
		os.system("cls")
		print("="*80,end="")
		print("++","++".rjust(77),end="")
		print("++","ATM CGK".center(74),"++",end="")
		print("++","++".rjust(77),end="")
		print("="*80)
		print(f"Hello,".center(80),end="") #User
		print(user_data[user_rekening]["name"].center(80))
		print(" Main Menu ".center(80,"_"))
		print(f"1.Check Saldo"+f"{'':>60}Setor.2")
		print("3.Transfer"+f"{'':>57}Tarik Tunai.4")
		print("5.Buang Duit"+f"{'':>53}Ubah Password.6")
		print("7.History"+f"{'':>60}Ubah Nama.8")
		print("0.Logout"+f"{'':>57}Exchange Rate.9")
		print("-"*80)
		user_i = input(f"{'':23}Masukan pilihan anda [0-9] = ")
		if user_i == "1" :
			check_saldo(user_data,user_rekening)
		elif user_i == "2" :
			setor(user_data,user_rekening,hdata)
		elif user_i == "3" :
			tf(user_data,user_rekening,hdata)
		elif user_i == "4" :
			tarek(user_data,user_rekening,hdata)
		elif user_i == "5" :
			buang_duit(user_data,user_rekening,hdata)
		elif user_i == "6" : 
			change_pass(user_data,user_rekening,hdata)
		elif user_i =="7" : 
			check_history(user_rekening,hdata)
		elif user_i == "8" :
			ubah_nama(user_data,user_rekening,hdata)
		elif user_i == "9" : 
			exchange_rate()
		elif user_i == "0" :
			os.system("cls")
			print("="*80)
			print("ATM CGK".center(79))
			print()
			print("="*80)
			print(f"Goodbye {user_data[user_rekening]['name']}".center(80))
			time.sleep(3)

			break
		else :
			print("Input salah".center(80));time.sleep(2)
			continue
			os.system("pause")
		with open("user.json","w") as out :
				json.dump(user_data,out,indent=4)
		with open("history.json","w") as out :
 				json.dump(hdata,out,indent=4)
		os.system("pause")
def block() : 
	os.system("cls")
	print("="*80,end="")
	print("++","++".rjust(77),end="")
	print("++","ATM CGK".center(74),"++",end="")
	print("++","++".rjust(77),end="")
	print("="*80)
	print("Akun anda di blokir".center(80))
	os.system("pause")