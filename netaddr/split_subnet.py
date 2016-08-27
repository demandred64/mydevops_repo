from netaddr import *
import pprint
pri_carriage_net = IPNetwork('10.20.4.0/23')


pri_carriage_list = list(pri_carriage_net.subnet(30));

# pprint.pprint(pri_carriage_list)


usable_addr = list(pri_carriage_list[0].iter_hosts())


#pprint.pprint(usable_addr)
print "SiteCode, PEAddress,CEAddress"
print "CBR,", usable_addr[0],",",usable_addr[1]



