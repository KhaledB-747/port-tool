#!/usr/bin/python
import socket
import argparse 
import pandas as pa
from colorama import Fore,Style 
#this tools create by Khaled, Gmail: kh3bns@gmail.com 
def check_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex(("127.0.0.1", port))
        s.close()
        if result == 0:
            return ' Open'
        else:
            return ' Closed'
    except Exception:
        return 'Unknown'
arg = argparse.ArgumentParser()
arg.add_argument("-m","--number", type=int, help="Get service name by port number")
arg.add_argument("-n","--name", type=str, help="Get port number by service name")
arg.add_argument("-s", type=int, help="Start port range") #start port to search from
arg.add_argument("-e", type=int, help="end port range") #end port to stop search range
args = arg.parse_args()
prot_name = args.name
port_number = args.number
start_range = args.s
end_range = args.e
if not any(vars(args).values()):
    arg.print_help()
    exit()
try:
    if start_range and end_range:
        result = {"Port":[], "Name":[], "Status":[]}
        for i in range(start_range,end_range+1):
            try:
                name = socket.getservbyport(i)
                result["Port"].append(i)
                result["Name"].append(name)
                result["Status"].append(check_port(i))
            except (OSError, socket.error):
                pass
        pr = pa.DataFrame(result)
        print(Fore.YELLOW + pr.to_string(index=False) + Style.RESET_ALL)
    elif port_number:
        try:
            name = socket.getservbyport(port_number)
            style = {"Port":[port_number], "Name":[name], "Status":[check_port(port_number)]}
            pr = pa.DataFrame(style)
            print(pr.to_string(index=False))
        except (OSError, socket.error):
            print(f"Port with number '{port_number}' does not exist")
    elif prot_name:
        try:
            number = socket.getservbyname(prot_name)
            style = {"Port":[number], "Name":[prot_name], "Status":[check_port(number)]}
            pr = pa.DataFrame(style)
            print(pr.to_string(index=False))
        except Exception:
            print(f"Port with name '{prot_name}' does not exist")
except Exception as d:
    print(d)
    print(Fore.RED+"Unknown error!"+Style.RESET_ALL)
    print(Fore.RED+"Use --help to more information"+Style.RESET_ALL)
