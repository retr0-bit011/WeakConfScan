from scanner import scan_server, scan_database
from report_generator import generate_report
from config import SERVER_IP, DATABASE_IP, DATABASE_PORT

def main():
    server_results = scan_server(SERVER_IP)
    database_results = scan_database(DATABASE_IP, DATABASE_PORT)
    
    scan_results = {
        'server': server_results,
        'database': database_results
    }
    
    generate_report(scan_results)
    print("Escaneo completo. Informe Guardado.")

if __name__ == "__main__":
    main()