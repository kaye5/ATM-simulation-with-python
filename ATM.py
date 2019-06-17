import os,Login,Menu,json,time,admin_menu,record
''' Cliff Bernado
	Mario Chandra
	Kevin Yuslianto
	CGK
'''
os.system("color 0f")
os.system("mode con: lines=50 cols=80")
while True : 
	#load json
	with open("user.json","r") as data : 
		user_data = json.load(data,encoding="utf-8")
	with open("admin.json","r") as data:
		admin_data = json.load(data,encoding="utf-8")
	with open("history.json","r") as data :
		hdata = json.load(data,encoding="utf-8")
	admin = [i for i in admin_data]
	rekening = [i for i in user_data]
	stats=''
	#check user and pass
	c = 0
	while c<5 :
		os.system("cls")
		#login no rekenening
		Login.loginrek()
		i_rekening = Login.loginrek.i_rekening
		if i_rekening == "" :
			continue
		#user
		elif i_rekening in rekening :
			for i in rekening : 
				if i == i_rekening :
					user_rekening = i
					auth = user_data[user_rekening]["auth"]
		#admin
		elif i_rekening in admin : 
			for i in admin :
				if i == i_rekening :
					admin_id = i 
					auth = admin_data[admin_id]["auth"]
		else :
			c += 1
			os.system("color 47")
			print("Tidak terdapat nomor rekening".center(80))
			print(f"Attempt : {c}".center(80))
			time.sleep(3)
			os.system("pause")
			os.system("cls")
			continue
		#login password
		cp = 0
		while cp<5 :
			os.system("color 0f")
			#user
			if auth == "user" :
				Login.loginpass()
				i_pass = Login.loginpass.i_pass 
				if i_pass == user_data[user_rekening]["pass"] :
					print("sucess")
					#work
				elif i_pass == "" :
					continue
				elif i_pass == "0" : 
					break
				else :
					cp += 1
					os.system("color 47")
					print("WRONG PASSWORD".center(80))
					print(f"Attempt : {cp}".center(80))
					time.sleep(3)
					os.system("pause")
					os.system("cls")
					if cp == 5 : 
						user_data[user_rekening]['status'] = "block"
						with open("user.json","w") as out :
							json.dump(user_data,out,indent=4)
					continue
			#admin
			elif auth == "admin" :
				Login.loginpass_admin()
				i_pass = Login.loginpass_admin.i_pass  
				if i_pass == admin_data[admin_id]["pass"] :
					print("sucess")
					#work
				elif i_pass == "" :
					continue
				elif i_pass == "0" : 
					break
				else :
					cp += 1
					os.system("color 47")
					print("WRONG PASSWORD".center(80))
					print(f"Attempt : {cp}".center(80))
					time.sleep(3)
					os.system("pause")
					os.system("cls")
					if cp == 5 : 
						admin_data[admin_id]['status'] = "block"
						with open("admin.json","w") as out :
							json.dump(admin_data,out,indent=4)
					continue

			if cp == 5 :
				break

			os.system("cls")
			if auth == "user" : 
				if user_data[user_rekening]["status"] == "active" :
					record.login_history_user(user_rekening,hdata)
					Menu.main(user_data,user_rekening,hdata)
				else :
					record.login_history_user(user_rekening,hdata)
					Menu.block()
					stats = "block"
			elif auth == "admin" : 
				if admin_data[admin_id]["status"] == "active" :
					record.login_history_admin(admin_id,hdata)
					with open("history.json","w") as out : 
						json.dump(hdata,out,indent=4)
					admin_menu.admin_menu(admin_data,admin_id,user_data,hdata)
				else :
					record.login_history_admin(admin_id,hdata)
					Menu.block()
					stats = "block"
			
			break
		break		#delet break while needed
	