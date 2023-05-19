# !/usr/bin/python3
# BackTrack

from os import system 

try:
    
    from colorama import Fore as f 
    from pyfiglet import figlet_format as fig 
    import socket 
    import requests
    import time
    from subprocess import  getoutput
    
except ModuleNotFoundError:
    system("pip install colorama && pip install pyfiglet && pip install socket && pip install requests")
    
system("")    

# Need Functions

def telegram(text:str):
    if text.startswith("send post"):
        site = text.replace("send post ", "")
        try:
            site_payload = {
                "UrlBox" : site,
                "AgentList" : "Google Chrome",
                "VersionList" : "HTTP/1.1",
                "MethodList" : "GET"
            }
            start = time.time()
            req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", site_payload)
            end = time.time()
            print(f"\n{f.RED}Url {f.YELLOW}: {f.WHITE}{site}\n{f.RED}Send {f.YELLOW}: {f.WHITE}True\n{f.RED}Mission end in {f.YELLOW}: {f.WHITE}{end-start:.2f}\n")
        except:
            print(f"{f.RED}Faild ! Please Try Again")

    elif text == "cls" or text == "clear":
        system("clear")
        
    elif text == "time" or text == "date" or text == "t" or text == "d":
        times = time.strftime(f"{f.YELLOW}%H{f.BLUE}:{f.YELLOW}%M{f.BLUE}:{f.YELLOW}%S {f.RED}|| {f.YELLOW}%y{f.BLUE}-{f.YELLOW}%m{f.BLUE}-{f.YELLOW}%d")
        print(f"\n{times}\n")

    elif text == "help" or text == "?":
        help_file = open("help.txt", "r")
        print(help_file.read()) 
    
    elif text == "cd ..":
        main()
        
        
def network(text: str):
    if text.startswith("get site -html"):
        site = text.replace("get site -html ", "")
        try:
            start = time.time()
            html = requests.get(site).text
            end = time.time()
            print(f.WHITE,html+"\n\n"+f"{f.RED}mission end in {f.YELLOW}: {f.WHITE}{end-start:.2f}")

        except:
            print(f"{f.RED}Faild ! Please Try Again")

    elif text.startswith("get site -ip"):
        site = text.replace("get site -ip ", "")
        try:
            start = time.time()
            s = socket.gethostbyname(site)
            end = time.time()
            print(f"\n{f.RED}site {f.YELLOW}: {f.WHITE}{site}\n{f.RED}host {f.YELLOW}: {f.WHITE}{s}\n{f.RED}mission end in {f.YELLOW}: {f.WHITE}{end-start:.2f}\n")

        except:
            print(f"\n{f.RED}Faild ! Please Try Again")

    elif text.startswith("get site -s"):
            site = text.replace("get site -s ", "")
            try:
                start = time.time()
                req = requests.get(site).status_code
                end = time.time()
                print("\n"+str(req)+f"{f.RED}\nmission end in {f.YELLOW}: {f.WHITE}{end-start:.2f}\n")

            except:
                print(f"{f.RED}Faild ! Please Try Again")

    elif text.startswith("font"):
        string = text.replace("font ", "")
        def font(txt : str):
            txt = txt.lower()
            t_1 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "Qᴡᴇʀᴛʏᴜɪᴏᴘᴀꜱᴅꜰɢʜᴊᴋʟᴢxᴄᴠʙɴᴍ"))
            t_2 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒"))
            t_3 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪"))
            t_4 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶"))
            t_5 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼"))
            t_6 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝐪𝐰𝐞𝐫𝐭𝐲𝐮𝐢𝐨𝐩𝐚𝐬𝐝𝐟𝐠𝐡𝐣𝐤𝐥𝐳𝐱𝐜𝐯𝐛𝐧𝐦"))
            t_7 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝗾𝘄𝗲𝗿𝘁𝘆𝘂𝗶𝗼𝗽𝗮𝘀𝗱𝗳𝗴𝗵𝗷𝗸𝗹𝘇𝘅𝗰𝘃𝗯𝗻𝗺"))
            t_8 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝚚𝚠𝚎𝚛𝚝𝚢𝚞𝚒𝚘𝚙𝚊𝚜𝚍𝚏𝚐𝚑𝚓𝚔𝚕𝚣𝚡𝚌𝚟𝚋𝚗𝚖"))
            t_9 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "QЩΣЯƬYЦIӨPΛƧDFGΉJKᄂZXᄃVBПM"))
            print(t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8, t_9)
        print("")
        font(txt=string)
        print("")
        
    elif text == "time" or text == "date" or text == "t" or text == "d":
        times = time.strftime(f"{f.YELLOW}%H{f.BLUE}:{f.YELLOW}%M{f.BLUE}:{f.YELLOW}%S {f.RED}|| {f.YELLOW}%y{f.BLUE}-{f.YELLOW}%m{f.BLUE}-{f.YELLOW}%d")
        print(f"\n{times}\n")

    elif text == "cls" or text == "clear":
        system("clear")
        
    elif text == "help" or text == "?":
        help_file = open("help.txt", "r")
        print(help_file.read()) 

    
    elif text == "cd ..":
        main()
      


# Banner

print(f"""{f.RED}
 ___ _   _ _ __  _ __ __ _
/ __| | | | '_ \| '__/ _` |
\__ \ |_| | |_) | | | (_| |
|___/\__,_| .__/|_|  \__,_|
          |_|
          
    {f.RED}+----------------------+
{f.RED}    |   {f.YELLOW}Supra {f.CYAN}FrameWork{f.RED}    |   
{f.RED}    +----------------------+

""")

# Main Function
def main():
    app = str(input(f"{f.WHITE}home{f.YELLOW}/{f.WHITE}terminal{f.YELLOW}/{f.WHITE}Supra {f.YELLOW}> {f.WHITE}"))

    
    if app == "help" or app == "?":
        help_file = open("help.txt", "r")
        print(help_file.read()) 
        main() 
    
    elif app == "cls" or app == "clear":
        system("clear")
        main()
    
    elif app == "cd network":
        net_app = str(input(f"{f.WHITE}home{f.YELLOW}/{f.WHITE}terminal{f.YELLOW}/{f.WHITE}Supra{f.YELLOW}/{f.WHITE}network {f.YELLOW}> {f.WHITE}"))
        network(text=net_app)
        main()
        

        
            
    elif app.startswith("font"):
        text = app.replace("font ", "")
        def font(text : str):
            text = text.lower()
            t_1 = text.translate(text.maketrans("qwertyuiopasdfghjklzxcvbnm", "Qᴡᴇʀᴛʏᴜɪᴏᴘᴀꜱᴅꜰɢʜᴊᴋʟᴢxᴄᴠʙɴᴍ"))
            t_2 = text.translate(text.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒"))
            t_3 = text.translate(text.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪"))
            t_4 = text.translate(text.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶"))
            t_5 = text.translate(text.maketrans("qwertyuiopasdfghjklzxcvbnm", "🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼"))
            t_6 = text.translate(text.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝐪𝐰𝐞𝐫𝐭𝐲𝐮𝐢𝐨𝐩𝐚𝐬𝐝𝐟𝐠𝐡𝐣𝐤𝐥𝐳𝐱𝐜𝐯𝐛𝐧𝐦"))
            t_7 = text.translate(text.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝗾𝘄𝗲𝗿𝘁𝘆𝘂𝗶𝗼𝗽𝗮𝘀𝗱𝗳𝗴𝗵𝗷𝗸𝗹𝘇𝘅𝗰𝘃𝗯𝗻𝗺"))
            t_8 = text.translate(text.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝚚𝚠𝚎𝚛𝚝𝚢𝚞𝚒𝚘𝚙𝚊𝚜𝚍𝚏𝚐𝚑𝚓𝚔𝚕𝚣𝚡𝚌𝚟𝚋𝚗𝚖"))
            t_9 = text.translate(text.maketrans("qwertyuiopasdfghjklzxcvbnm", "QЩΣЯƬYЦIӨPΛƧDFGΉJKᄂZXᄃVBПM"))
            print(t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8, t_9)
        print("")
        font(text=text)
        print("")
        main()
        
    elif app == "time" or app == "date" or app == "t" or app == "d":
        times = time.strftime(f"{f.YELLOW}%H{f.BLUE}:{f.YELLOW}%M{f.BLUE}:{f.YELLOW}%S {f.RED}|| {f.YELLOW}%y{f.BLUE}-{f.YELLOW}%m{f.BLUE}-{f.YELLOW}%d")
        print(f"\n{times}\n")
        main()
        
    elif app == "cd telegram" or app == "cd tel":
        tel_app = str(input(f"{f.WHITE}home{f.YELLOW}/{f.WHITE}terminal{f.YELLOW}/{f.WHITE}Supra{f.YELLOW}/{f.WHITE}telegram {f.YELLOW}> {f.WHITE}"))
        telegram(text=tel_app)
        main()

            
    elif app.startswith("send post"):
        site = app.replace("send post ", "")
        try:
            site_payload = {
                "UrlBox" : site,
                "AgentList" : "Google Chrome",
                "VersionList" : "HTTP/1.1",
                "MethodList" : "GET"
            }
            start = time.time()
            req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", site_payload)
            end = time.time()
            print(f"\n{f.RED}Url {f.YELLOW}: {f.WHITE}{site}\n{f.RED}Send {f.YELLOW}: {f.WHITE}True\n{f.RED}Mission end in {f.YELLOW}: {f.WHITE}{end-start:.2f}\n")
            main()
        except:
            print(f"{f.RED}Faild ! Please Try Again")
            main()
            
    else:
        print(f"\n{f.RED}faild\n")
        main()


# Start Function
main()