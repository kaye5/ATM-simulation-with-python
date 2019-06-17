import time 
def login_history_user(user_rekening,hdata) : 
	try:
		hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || Login "))
	except : 
		hdata[user_rekening] = [time.strftime("%a %d %b %Y %H:%M:%S || Login ")]
def login_history_admin(admin_id,hdata) : 
	try :
		hdata[admin_id].append(time.strftime("%a %d %b %Y %H:%M:%S || Login "))
	except :
		hdata[admin_id] = [time.strftime("%a %d %b %Y %H:%M:%S || Login ")]	
def his_tarek(user_rekening,user_i,hdata) :
	if user_i== "1":
	    hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || Tarek Rp. 100.000 "))
	elif user_i == "2":
	    hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || Tarek Rp. 200.000 "))
	elif user_i == "3":
	    hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || Tarek Rp. 500.000 "))
	elif user_i== "4":
	    hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || Tarek Rp. 1.000.000 "))
def his_setor(user_rekening,user_i,hdata,value) :
	if user_i== "1":
	    hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || Setor Rp. 100.000 "))
	elif user_i == "2":
	    hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || Setor Rp. 200.000 "))
	elif user_i == "3":
	    hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || Setor Rp. 500.000 "))
	elif user_i== "4":
	    hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || Setor Rp. 1.000.000 "))
	elif user_i== "5":
		hdata[user_rekening].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Setor Rp. {value:,} "))
def his_cpass(user_rekening,hdata) :
	hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || Ubah password "))
def his_cname(user_rekening,hdata) :	
	hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || Ubah nama "))
def his_cf(user_rekening,user_d,user_i,hdata,value) :
	try :
		if user_i== "1":
		    hdata[user_rekening].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer ke {user_d} Rp. 100.000 "))
		    hdata[user_d].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer dari {user_rekening} Rp. 100.000 "))
		elif user_i == "2":
		    hdata[user_rekening].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer ke {user_d} Rp. 200.000 "))
		    hdata[user_d].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer dari {user_rekening} Rp. 200.000 "))
		elif user_i == "3":
		    hdata[user_rekening].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer ke {user_d} Rp. 500.000 "))
		    hdata[user_d].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer dari {user_rekening} Rp. 500.000 "))
		elif user_i== "4":
		    hdata[user_rekening].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer ke {user_d} Rp. 1.000.000 "))
		    hdata[user_d].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer dari {user_rekening} Rp. 1.000.000 "))
		elif user_i== "5":
			hdata[user_rekening].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer ke {user_d} Rp. {value:,} "))
			hdata[user_d].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer dari {user_rekening} Rp. {value:,} "))
	except :
		if user_i== "1":
		    hdata[user_rekening].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer ke {user_d} Rp. 100.000 "))
		    hdata[user_d] = [time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer dari {user_rekening} Rp. 100.000 ")]
		elif user_i == "2":
		    hdata[user_rekening].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer ke {user_d} Rp. 200.000 "))
		    hdata[user_d] = [time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer dari {user_rekening} Rp. 200.000 ")]
		elif user_i == "3":
		    hdata[user_rekening].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer ke {user_d} Rp. 500.000 "))
		    hdata[user_d] = [time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer dari {user_rekening} Rp. 500.000 ")]
		elif user_i== "5":
		    hdata[user_rekening].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer ke {user_d} Rp. 1.000.000 "))
		    hdata[user_d] = [time.strftime(f"%a %d %b %Y %H:%M:%S || Transfer dari {user_rekening} Rp. 1.000.000 ")]				   

def his_buang(user_rekening,user_i,hdata,value) :
	if user_i== "1":
	    hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || buang Rp. 100.000 "))
	elif user_i == "2":
	    hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || buang Rp. 200.000 "))
	elif user_i == "3":
	    hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || buang Rp. 500.000 "))
	elif user_i== "4":
	    hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || buang Rp. 1.000.000 "))
	elif user_i == "5" :     
		hdata[user_rekening].append(time.strftime(f"%a %d %b %Y %H:%M:%S || buang Rp. {value:,}"))	  
def add_rek(admin_id,new_rek,hdata) :
	hdata[admin_id].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Add Rekening : {new_rek} "))
def add_adm(new_adm,admin_id,hdata) :
	hdata[admin_id].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Add Admin : {new_adm} "))
def del_rek(admin_id,hdata,i_rek) : 
	hdata[admin_id].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Deleted : {i_rek} "))
def block(admin_id,hdata,i_rek) : 
	hdata[admin_id].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Blocked : {i_rek} "))
def unblock(admin_id,hdata,i_rek) : 
	hdata[admin_id].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Unblocked : {i_rek} "))
def edit_rek(admin_id,user_data,hdata,edit_rek_i,i_rek) : 
	if edit_rek_i == "1" :
		hdata[admin_id].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Ubah nama : {i_rek} "))	
	elif edit_rek_i == "2" : 
		hdata[admin_id].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Ubah rekening: {i_rek} "))	
	elif edit_rek_i == "3" : 
		hdata[admin_id].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Ubah password: {i_rek} "))

def edit_adm(admin_id,admin_data,hdata,edit_rek_i,i_rek) : 
	if edit_rek_i == "1" :
		hdata[admin_id].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Ubah nama : {i_rek} "))	
	elif edit_rek_i == "2" : 
		hdata[admin_id].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Ubah User: {i_rek} "))	
	elif edit_rek_i == "3" : 
		hdata[admin_id].append(time.strftime(f"%a %d %b %Y %H:%M:%S || Ubah password: {i_rek} "))
