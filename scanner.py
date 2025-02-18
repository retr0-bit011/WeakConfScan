import socket
import paramiko

def check_open_ports(host, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def check_ssh_root_login(host, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        print(f"Error checking SSH root login: {e}")
        return False

def scan_server(host):
    results = {}
    
    # Chequear puertos comunes
    common_ports = [21, 22, 80, 443, 3306]
    open_ports = check_open_ports(host, common_ports)
    results['open_ports'] = open_ports
    
    # Chequear SSH login root
    if 22 in open_ports:
        results['ssh_root_login'] = check_ssh_root_login(host, 22, 'root', 'password')
    
    return results

def scan_database(host, port):
    results = {}
    
    # Chequeo de puerto de la base de datos esta abierto
    if port in check_open_ports(host, [port]):
        results['port_open'] = True
       
    else:
        results['port_open'] = False
    
    return results