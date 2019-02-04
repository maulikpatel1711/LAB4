import calc
for a in ipcalc.network('192.168.0.1/24'):
    print str(a)
192.168.0.0
192.168.0.254
    subnet = ipcalc.Network('255.255.255.0/24')
    print str(subnet.network())
print str(subnet.netmask())
    '192.168.0.1' in Network('192.168.0.1/24')


