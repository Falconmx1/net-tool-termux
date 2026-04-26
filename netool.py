#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import sys
import socket
import threading
from colorama import init, Fore, Style
import requests
import dns.resolver

init(autoreset=True)

# Configuración de colores
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
C = Fore.CYAN
M = Fore.MAGENTA
W = Fore.WHITE
S = Style.RESET_ALL

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(f"""{C}
    ╔═══════════════════════════════════════╗
    ║     {W}NetTool v1.0 - Termux{R}               {C}║
    ║     {Y}Herramienta de Red Profesional{R}      {C}║
    ╚═══════════════════════════════════════╝{S}
    """)

def menu():
    print(f"""{Y}[!] Selecciona una opción:{S}
    
    {G}[1]{W} Escaneo de puertos
    {G}[2]{W} Ping continuo
    {G}[3]{W} Traceroute
    {G}[4]{W} Consulta WHOIS
    {G}[5]{W} Consulta DNS
    {G}[6]{W} Información de IP
    {G}[7]{W} Ping rápido (4 paquetes)
    {G}[8]{W} Escaneo de red local
    {G}[0]{R} Salir{S}
    """)

def port_scan():
    target = input(f"{B}[?]{W} Ingresa IP o dominio: {S}")
    ports = input(f"{B}[?]{W} Puertos (ej: 20-100 o 22,80,443): {S}")
    
    print(f"{Y}[*] Escaneando {target}...{S}")
    
    if '-' in ports:
        start, end = map(int, ports.split('-'))
        port_range = range(start, end+1)
    else:
        port_range = [int(p.strip()) for p in ports.split(',')]
    
    def scan(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"{G}[+] Puerto {port} -> ABIERTO{S}")
            sock.close()
        except:
            pass
    
    threads = []
    for port in port_range:
        t = threading.Thread(target=scan, args=(port,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

def ping_continuous():
    target = input(f"{B}[?]{W} Ingresa IP o dominio: {S}")
    print(f"{Y}[*] Haciendo ping a {target} (Ctrl+C para detener){S}")
    os.system(f"ping {target}")

def traceroute_cmd():
    target = input(f"{B}[?]{W} Ingresa IP o dominio: {S}")
    print(f"{Y}[*] Traceroute a {target}{S}")
    os.system(f"traceroute {target}")

def whois_lookup():
    target = input(f"{B}[?]{W} Ingresa dominio: {S}")
    print(f"{Y}[*] Consultando WHOIS para {target}{S}")
    os.system(f"whois {target}")

def dns_lookup():
    target = input(f"{B}[?]{W} Ingresa dominio: {S}")
    print(f"{Y}[*] Consultando DNS para {target}{S}")
    
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
    
    for record in record_types:
        try:
            answers = dns.resolver.resolve(target, record)
            for rdata in answers:
                print(f"{G}[+] {record}: {rdata}{S}")
        except:
            print(f"{R}[-] {record}: No encontrado{S}")
    
    # Reverse DNS lookup
    try:
        ip = socket.gethostbyname(target)
        hostname = socket.gethostbyaddr(ip)
        print(f"{G}[+] Reverse DNS: {hostname[0]}{S}")
    except:
        pass

def ip_info():
    target = input(f"{B}[?]{W} Ingresa IP o dominio: {S}")
    
    # Obtener IP
    try:
        ip = socket.gethostbyname(target)
        print(f"{G}[+] IP: {ip}{S}")
    except:
        print(f"{R}[-] No se pudo resolver{S}")
        return
    
    # Consultar API pública
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data['status'] == 'success':
            print(f"{C}[+] Información detallada:{S}")
            print(f"  {Y}País:{W} {data['country']}")
            print(f"  {Y}Ciudad:{W} {data['city']}")
            print(f"  {Y}ISP:{W} {data['isp']}")
            print(f"  {Y}Organización:{W} {data['org']}")
            print(f"  {Y}Código postal:{W} {data['zip']}")
            print(f"  {Y}Coordenadas:{W} {data['lat']}, {data['lon']}")
        else:
            print(f"{R}[-] No se pudo obtener información{S}")
    except:
        print(f"{R}[-] Error al conectar con la API{S}")

def ping_fast():
    target = input(f"{B}[?]{W} Ingresa IP o dominio: {S}")
    print(f"{Y}[*] Ping rápido a {target}{S}")
    os.system(f"ping -c 4 {target}")

def network_scan():
    network = input(f"{B}[?]{W} Ingresa red (ej: 192.168.1.0/24): {S}")
    print(f"{Y}[*] Escaneando red {network}{S}")
    os.system(f"nmap -sn {network}")

def main():
    while True:
        clear()
        banner()
        menu()
        
        option = input(f"{B}[>]{W} Opción: {S}")
        
        if option == '1':
            port_scan()
        elif option == '2':
            ping_continuous()
        elif option == '3':
            traceroute_cmd()
        elif option == '4':
            whois_lookup()
        elif option == '5':
            dns_lookup()
        elif option == '6':
            ip_info()
        elif option == '7':
            ping_fast()
        elif option == '8':
            network_scan()
        elif option == '0':
            print(f"{G}[!] Gracias por usar NetTool!{S}")
            sys.exit(0)
        else:
            print(f"{R}[!] Opción inválida{S}")
        
        input(f"\n{Y}[*] Presiona Enter para continuar...{S}")

if __name__ == "__main__":
    main()
