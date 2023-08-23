
send(IP(src="192.168.1.107",dst="192.168.1.107")/ICMP()/"ok")
sendp(L1/L2/L3)
#--------------------------------------------------------------------
#defining layer , showing , changing:

L1 = TCP()
L2 = IP()
L1 = Ether()

L2 = IP(port = 80,dport = 123)
L1.src = ""
L1.show()
#--------------------------------------------------------------------

sniff(iface="lo",prn=lambda x:x.show()) #listening for ping lo ip
sniff(filter="src 192.168.1.107",count=3) #listening for ping lo ip and 3 packs
#nsummarys()

