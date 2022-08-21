#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random, json, ctypes
try:
    import requests
    from bit import *
    from bit.format import bytes_to_wif
    from rich import print

except ImportError:
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'bit']) # https://pypi.org/project/bit/
    subprocess.check_call(["python", '-m', 'pip', 'install', 'requests']) # https://pypi.org/project/requests/
    subprocess.check_call(["python", '-m', 'pip', 'install', 'rich']) # https://pypi.org/project/rich/
    import requests
    from bit import *
    from bit.format import bytes_to_wif
    from rich import print
    
ctypes.windll.kernel32.SetConsoleTitleW('Mizogg Corp.BTC_API.py')

Mizogg = '''[red]
                ╔═╗╔═╗                   
                ║║╚╝║║                   
                ║╔╗╔╗║╔╗╔═══╗╔══╗╔══╗╔══╗
                ║║║║║║╠╣╠══║║║╔╗║║╔╗║║╔╗║
                ║║║║║║║║║║══╣║╚╝║║╚╝║║╚╝║
                ╚╝╚╝╚╝╚╝╚═══╝╚══╝╚═╗║╚═╗║
                                 ╔═╝║╔═╝║
                                 ╚══╝╚══╝
                  ___            ___  
                 (o o)          (o o) 
                (  V  ) MIZOGG (  V  )
                --m-m------------m-m--
[/red]'''

def get_balance1(caddr):
    request = requests.get('http://127.0.0.1:5000/balance?active=' + caddr, timeout=20)
    request = request.json()
    jdumps = json.dumps(request)
    jloads = json.loads(jdumps)
    balance1 = jloads[caddr]['final_balance']
    return balance1

def get_balance2(uaddr):
    request = requests.get('http://127.0.0.1:5000/balance?active=' + uaddr, timeout=20)
    request = request.json()
    jdumps = json.dumps(request)
    jloads = json.loads(jdumps)
    balance2 = jloads[uaddr]['final_balance']
    return balance2

def get_balance3(saddr):
    request = requests.get('http://127.0.0.1:5000/balance?active=' + saddr, timeout=20)
    request = request.json()
    jdumps = json.dumps(request)
    jloads = json.loads(jdumps)
    balance3 = jloads[saddr]['final_balance']
    return balance3

def random_scan():
    count=0
    total=0
    while True:
        dec =int(random.randrange(1073741823, 115792089237316195423570985008687907852837564279074904382605163141518161494336))
        HEX = "%064x" % dec  
        key = Key.from_int(dec)
        wifu = bytes_to_wif(key.to_bytes(), compressed=False)
        wifc = bytes_to_wif(key.to_bytes(), compressed=True)
        key1 = Key(wifu)
        caddr = key.address
        uaddr = key1.address
        saddr = key.segwit_address
        balance1 = get_balance1(caddr)
        balance2 = get_balance2(uaddr)
        balance3 = get_balance3(saddr)
        count+=1
        total+=3
        ctypes.windll.kernel32.SetConsoleTitleW('Count=' + str(count) + ' Total=' + str(total))
        if (balance1 > 0):
            print('Balance Found! Address COMPRESSED : ',caddr, ' Balance : ',balance1, '\n WIF COMPRESSED   = ', wifc)
            f=open("winner.txt","a")
            f.write('\nPrivatekey (dec): ' + str(dec))
            f.write('\nPrivatekey (hex): ' + HEX)
            f.write('\nPrivatekey compressed: ' + wifc)
            f.write('\nPublic Address 1 Compressed: ' + caddr)
            f.close()
        if (balance2 > 0):
            print('Balance Found! Address UNCOMPRESSED : ',uaddr, ' Balance : ',balance2, '\n WIF COMPRESSED   = ', wifu)
            f=open("winner.txt","a")
            f.write('\nPrivatekey (dec): ' + str(dec))
            f.write('\nPrivatekey (hex): ' + HEX)
            f.write('\nPrivatekey Uncompressed: ' + wifu)
            f.write('\nPublic Address 1 Uncompressed: ' + uaddr)
            f.close()    
        if (balance3 > 0):
            print('Balance Found! Address 3 P2SH : ',saddr, ' Balance : ',balance3,)
            f=open("winner.txt","a")
            f.write('\nPrivatekey (dec): ' + str(dec))
            f.write('\nPrivatekey (hex): ' + HEX)
            f.write('\nPublic Address 3 P2SH: ' + saddr)
            f.close()
        else:
            print('\n', '='*30, '[ BALANCE CHECK ]', '='*30)
            print('\nAddress COMPRESSED   = ', caddr, " Balance : ",balance1)
            print('Address UnCOMPRESSED = ', uaddr, " Balance : ",balance2)
            print('Address 3 Segwit     = ', saddr, " Balance : ",balance3)
            print('WIF COMPRESSED   = ', wifc)
            print('WIF UnCOMPRESSED = ', wifu)
            print('Private Key HEX  = ', HEX)
            print('Private Key DEC = ', dec)
            

        
def sequential_scan():
    z=int(input("'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
    y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))

    P = z
    count=0
    total=0
    while P<y:
        P+=1
        dec = P
        HEX = "%064x" % dec  
        key = Key.from_int(dec)
        wifu = bytes_to_wif(key.to_bytes(), compressed=False)
        wifc = bytes_to_wif(key.to_bytes(), compressed=True)
        key1 = Key(wifu)
        caddr = key.address
        uaddr = key1.address
        saddr = key.segwit_address
        balance1 = get_balance1(caddr)
        balance2 = get_balance2(uaddr)
        balance3 = get_balance3(saddr)
        count+=1
        total+=3
        ctypes.windll.kernel32.SetConsoleTitleW('Count=' + str(count) + ' Total=' + str(total))
        if (balance1 > 0):
            print('Balance Found! Address COMPRESSED : ',caddr, ' Balance : ',balance1, '\n WIF COMPRESSED   = ', wifc)
            f=open("winner.txt","a")
            f.write('\nPrivatekey (dec): ' + str(dec))
            f.write('\nPrivatekey (hex): ' + HEX)
            f.write('\nPrivatekey compressed: ' + wifc)
            f.write('\nPublic Address 1 Compressed: ' + caddr)
            f.close()
        if (balance2 > 0):
            print('Balance Found! Address UNCOMPRESSED : ',uaddr, ' Balance : ',balance2, '\n WIF COMPRESSED   = ', wifu)
            f=open("winner.txt","a")
            f.write('\nPrivatekey (dec): ' + str(dec))
            f.write('\nPrivatekey (hex): ' + HEX)
            f.write('\nPrivatekey Uncompressed: ' + wifu)
            f.write('\nPublic Address 1 Uncompressed: ' + uaddr)
            f.close()    
        if (balance3 > 0):
            print('Balance Found! Address 3 P2SH : ',saddr, ' Balance : ',balance3,)
            f=open("winner.txt","a")
            f.write('\nPrivatekey (dec): ' + str(dec))
            f.write('\nPrivatekey (hex): ' + HEX)
            f.write('\nPublic Address 3 P2SH: ' + saddr)
            f.close()
        else:
            print('\n', '='*30, '[ BALANCE CHECK ]', '='*30)
            print('\nAddress COMPRESSED   = ', caddr, " Balance : ",balance1)
            print('Address UnCOMPRESSED = ', uaddr, " Balance : ",balance2)
            print('Address 3 Segwit     = ', saddr, " Balance : ",balance3)
            print('WIF COMPRESSED   = ', wifc)
            print('WIF UnCOMPRESSED = ', wifu)
            print('Private Key HEX  = ', HEX)
            print('Private Key DEC = ', dec)

print(Mizogg)
print ("[green]\n 1 for Random Scan [/green]\n [blue]2 for Sequential Scan [/blue]")
method_input = input("\n : Type 1-2 to begin :")
if method_input=="1":
    random_scan()
elif method_input=="2":
    sequential_scan()