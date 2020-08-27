import requests
from bs4 import BeautifulSoup as bs
import json
import os
import time

#This URL will be the URL that your login form points to with the "action" tag.
POSTLOGINURL = 'https://www.hackerrank.com/auth/login'
LOGINREST = "https://www.hackerrank.com/rest/auth/login"
#This URL is the page you actually want to pull down with requests.
REQUESTURL = 'https://www.hackerrank.com/rest/contests/master/submissions/?offset=0&limit=500'

username= 'usr'
password= 'pass'

with requests.Session() as s:
	headers = requests.utils.default_headers()
	headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',})
	site = s.get(POSTLOGINURL,headers=headers)
	bs_content = bs(site.content, "html.parser")
	token = str()
	for link in bs_content.find_all('meta'):
		if str(link.get('name')) == 'csrf-token':
			token=(str(link.get('content')))
	login_data = {"fallback":"false","login":username,"password":password, "remember_me":"false"}
	headers=({"authority": "www.hackerrank.com",
		"method": "POST",
		"path": "/rest/auth/login",
		"scheme": "https",
		"accept": "application/json",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-US,en;q=0.9,ar;q=0.8",
		"content-length": "89",
		"content-type": "application/json",
		"cookie": "user_type=hacker; hackerrank_mixpanel_token=7d9b95fc-9617-4f31-bd20-94f072556788; show_cookie_banner=false; h_r=home; h_l=body_middle_left_button; h_v=1; hrc_l_i=F; _hrank_session=fc937d8fa51bc4fbd5578d011ee9fe67fd339cbbb4a28213bf4a7cfda39fc102a9afad2a19a9da496d47af7e3469d718888e30732bd84745f1d774e300bdd0ea",
		"origin": "https://www.hackerrank.com",
		"referer": "https://www.hackerrank.com/dashboard",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
		'x-csrf-token': token,})
	rh=s.post(LOGINREST,data=login_data,headers=headers)
	# print(rh.response)
	home_page = s.get(REQUESTURL,headers=headers)
	f=open("masa2el.json","w")
	f.write(home_page.content.decode("utf-8") )
	f.close()
	#print(home_page.content)
	# print(json.dumps(home_page.content))
	with open('masa2el.json') as json_file:
		data = json.load(json_file)
		if not os.path.exists('hackerrank_sol'):
			os.mkdir('hackerrank_sol')
		i=0
		for p in data['models']:
	        #print('Name: ' + str(p['challenge_id']))
	        #print('Website: ' + p['language'])
	        #print('From: ' + p['challenge']['slug'])
			
			if p['status'] == 'Accepted':
				i=i+1
				challenge_slug=p['challenge']['slug']
				sol_id=p['id']
				if not os.path.exists('hackerrank_sol/'+p['language']):
					os.mkdir('hackerrank_sol/'+p['language'])
				extension="py"
				if p['language'].find('py') == -1:
					extension=p['language']
				file_name='hackerrank_sol/'+p['language']+'/'+challenge_slug+"."+extension
				link='https://www.hackerrank.com/rest/contests/master/challenges/'+challenge_slug+'/submissions/'+str(sol_id)
				home_page = s.get(link,headers=headers)
				# home_page.config['keep_alive'] = False
				print(home_page)
				f=open(file_name,"w")
				f.write(home_page.content.decode("utf-8"))
				f.close()
				with open(file_name) as json_file:
					data = json.load(json_file)
					f=open(file_name,"w")
					print(file_name)
					f.write(data['model']['code'])
					f.close()
					#print('Name: ' + str(data['model']['code']))
					#print('')
				#time.sleep(5)
				if i==10:
					print("SLEEPING FOR 60 SECONDS!")
					time.sleep(60)
					i=0