rom mininet.topo import Topo

class BinaryTreeTopo( Topo ):

    def __init__( self ):
        Topo.__init__( self )

        host = []
        host.append(self.addHost("h1"))
        host.append(self.addHost("h2"))
        host.append(self.addHost("h3"))
        host.append(self.addHost("h4"))
        host.append(self.addHost("h5"))
        host.append(self.addHost("h6"))
        host.append(self.addHost("h7"))
        host.append(self.addHost("h8"))
        

        switch = []
        switch.append(self.addSwitch("s1")
        switch.append(self.addSwitch("s2")
        switch.append(self.addSwitch("s3")
        switch.append(self.addSwitch("s4")
        switch.append(self.addSwitch("s5")
        switch.append(self.addSwitch("s6")
	switch.append(self.addSwitch("s7")
       
        self.addLink(switch[0], switch[1])
        self.addLink(switch[0], switch[4])
        self.addLink(switch[1], switch[2])
        self.addLink(switch[1], switch[3])
        self.addLink(switch[4], switch[5])
        self.addLink(switch[4], switch[6])
        self.addLink(switch[2], host[0])
        self.addLink(switch[2], host[1])
        self.addLink(switch[3], host[2])
        self.addLink(switch[3], host[3])
        self.addLink(switch[5], host[4])
        self.addLink(switch[5], host[5])
        self.addLink(switch[6], host[6])
        self.addLink(switch[6], host[7])

topos = { 'binary_tree' : ( lambda: BinaryTreeTopo() ) }

