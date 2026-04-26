# 🌐 NetTool - Herramienta de Red para Termux

[![Version](https://img.shields.io/badge/version-1.0-blue)](https://github.com/Falconmx1/net-tool-termux)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Termux](https://img.shields.io/badge/Termux-Compatible-red)](https://termux.com)

## 📱 Características

- ✅ Escaneo de puertos TCP multi-hilo
- ✅ Ping continuo y rápido
- ✅ Traceroute completo
- ✅ Consultas WHOIS
- ✅ DNS lookup (A, AAAA, MX, NS, TXT, CNAME)
- ✅ Geolocalización de IPs
- ✅ Escaneo de red local con Nmap
- ✅ Interfaz colorida y fácil de usar

## 🛠️ Instalación

```bash
pkg update && pkg upgrade
pkg install git python
git clone https://github.com/TU-USUARIO/net-tool-termux
cd net-tool-termux
bash install.sh

🚀 Uso
python netool.py

👨‍💻 Comandos disponibles
Comando	Descripción
scan [IP]	Escanea puertos
ping [IP]	Prueba de conectividad
trace [IP]	Traceroute
whois [domain]	Información WHOIS
dns [domain]	Consulta DNS
