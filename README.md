# WeakConfScan

Herramienta en Python para escanear servidores y bases de datos en busca de configuraciones inseguras, como puertos abiertos, acceso root permitido y contraseñas débiles. Genera un informe en formato TXT con los hallazgos.

---

## Funcionalidades
- Escaneo de puertos comunes (SSH, MySQL, etc.).
- Detección de acceso root permitido en SSH.
- Verificación de contraseñas débiles o predeterminadas.
- Generación de un informe en formato TXT.

---

## Requisitos
- Python 3.x
- Bibliotecas: `paramiko`, `socket`

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/retr0-bit011/WeakConfScan.git
   cd WeakConfScan
   pip install -r requirements.txt
   ```
2. Modificar archivo config.py
   En el archivo config.py colocar la ip del servidor que vamos a auditar, al igual que la base de datos
3. Ejecutar el script
   ```bash
   python3 main.py
