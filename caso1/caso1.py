#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='192.168.100.0/24')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone') # Switch r1 - r4
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='standalone') # Switch r1 - r5
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, failMode='standalone') # Switch r4 - h1
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch, failMode='standalone') # Switch r5 - h2

    r1 = net.addHost('r1', cls=Node, ip='192.168.100.6/29') # Router central
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')

    r4 = net.addHost('r4', cls=Node, ip='192.168.100.1/29') # Router sucursal 1
    r4.cmd('sysctl -w net.ipv4.ip_forward=1')

    r5 = net.addHost('r5', cls=Node, ip='192.168.100.9/29') # Router sucursal 2
    r5.cmd('sysctl -w net.ipv4.ip_forward=1')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.1.254', defaultRoute=None) # Host sucursal 1
    h2 = net.addHost('h2', cls=Host, ip='10.0.2.254', defaultRoute=None) # Host sucursal 2

    info( '*** Add links\n')
    net.addLink(r1, s2, intfName1='r1s2-eth0', params1={'ip':'192.168.100.6/29'})
    net.addLink(r1, s3, intfName1='r1s3-eth0', params1={'ip':'192.168.100.14/29'})
    net.addLink(s2, r4, intfName2='s2r4-eth0', params2={'ip':'192.168.100.1/29'})
    net.addLink(s3, r5, intfName2='s3r5-eth0', params2={'ip':'192.168.100.9/29'})
    net.addLink(r4, s6, intfName1='r4s6-eth0', params1={'ip':'10.0.1.1/24'})
    net.addLink(r5, s7, intfName1='r5s7-eth0', params1={'ip':'10.0.2.1/24'})
    net.addLink(s6, h1, intfName2='s6h1-eth0', params2={'ip':'10.0.1.254/24'})
    net.addLink(s7, h2, intfName2='s7h2-eth0', params2={'ip':'10.0.2.254/24'})

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s2').start([])
    net.get('s3').start([])
    net.get('s6').start([])
    net.get('s7').start([])

    info( '*** Post configure switches and hosts\n')

    # Configuración de enrutamiento
    r1.cmd('ip route add 10.0.1.0/24 via 192.168.100.1 dev r1s2-eth0')
    r1.cmd('ip route add 10.0.2.0/24 via 192.168.100.9 dev r1s3-eth0')

    r4.cmd('ip route add 10.0.2.0/24 via 192.168.100.6 dev s2r4-eth0')
    r4.cmd('ip route add 192.168.100.8/29 via 192.168.100.6 dev s2r4-eth0')

    r5.cmd('ip route add 10.0.1.0/24 via 192.168.100.14 dev s3r5-eth0')
    r5.cmd('ip route add 192.168.100.0/29 via 192.168.100.14 dev s3r5-eth0')

    h1.cmd('ip route add 192.168.100.0/29 via 10.0.1.1 dev s6h1-eth0')
    h1.cmd('ip route add 192.168.100.8/29 via 10.0.1.1 dev s6h1-eth0')
    h1.cmd('ip route add 10.0.2.0/24 via 10.0.1.1 dev s6h1-eth0')

    h2.cmd('ip route add 192.168.100.0/29 via 10.0.2.1 dev s7h2-eth0')
    h2.cmd('ip route add 192.168.100.8/29 via 10.0.2.1 dev s7h2-eth0')
    h2.cmd('ip route add 10.0.1.0/24 via 10.0.2.1 dev s7h2-eth0')


    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
                                                                                                                                                                   81,0-1        95%
