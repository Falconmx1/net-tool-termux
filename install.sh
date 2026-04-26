#!/bin/bash

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}[+] NetTool - Herramienta de Red para Termux${NC}"
echo -e "${BLUE}[+] Instalando dependencias...${NC}"

# Actualizar repositorios
pkg update -y && pkg upgrade -y

# Instalar Python y pip
pkg install python -y
pkg install python-pip -y

# Instalar dependencias de red
pkg install nmap -y
pkg install traceroute -y
pkg install whois -y
pkg install dnsutils -y

# Instalar módulos de Python
pip install colorama
pip install requests
pip install dnspython

# Dar permisos de ejecución
chmod +x netool.py

echo -e "${GREEN}[✔] Instalación completada exitosamente!${NC}"
echo -e "${GREEN}[*] Para ejecutar: python netool.py${NC}"
