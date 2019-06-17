import time 
def login_history_user(user_rekening,hdata) :
	try : 
		hdata[user_rekening]=hdata[user_rekening].append(time.strftime("%a %d %b %Y %H:%M:%S || Login"))
	except : 
		hdata = {user_rekening : time.strftime("%a %d %b %Y %H:%M:%S || Login")}
	hdata[user_rekening] += "1"
def login_history_admin(admin_id,hdata) :
	try : 
		hdata[user_admin]=hdata[admin_id].append(time.strftime("%a %d %b %Y %H:%M:%S || Login"))
	except : 
		hdata = {admin_id : time.strftime("%a %d %b %Y %H:%M:%S || Login")}
