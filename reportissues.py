#! /bin/sh
"true" '''\'
if command -v python2 > /dev/null; then
  exec python2 "$0" "$@"
else
  exec python "$0" "$@"
fi
exit $?
'''

#    LibVirt Wake On Lan - Print via Google Cloud Print
#    Copyright (C) 2013 Simon Cadman
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

if __name__ == '__main__':  # pragma: no cover

    from lvwolutils import Utils
    from libvirtwol import LibVirtWakeOnLan
    import libvirt
    import sys
    from xml.dom import minidom
    Utils.SetupLogging()

    # line below is replaced on commit
    LVWOLVersion = "20140807 221108"
    Utils.ShowVersion(LVWOLVersion)
    
    # add debug output here
    print "LibVirt Wake-On-Lan Version " + LVWOLVersion
    conn = libvirt.open(None)
    if conn is None:
        print 'Failed to open connection to the hypervisor'
        sys.exit(1)

    domains = conn.listDefinedDomains()
    print "%i VMs found" % len(domains)
    for domainName in domains:
        domain = conn.lookupByName(domainName)
        params = []
        # TODO - replace with api calls to fetch network interfaces
        xml = minidom.parseString(domain.XMLDesc(0))
        devices = xml.documentElement.getElementsByTagName("devices")
        foundcards = []
        for device in devices:
            for interface in device.getElementsByTagName("interface"):
                foundcards.append(interface)
        print "%s - %i network card(s):" % (domainName, len(foundcards))
        for foundcard in foundcards:
            macadd = interface.getElementsByTagName("mac")
            foundmac = macadd[0].getAttribute("address")
            source = interface.getElementsByTagName("source")
            sourcebridge = source[0].getAttribute("bridge")
            model = interface.getElementsByTagName("model")
            modeltype = model[0].getAttribute("type")
            address = interface.getElementsByTagName("address")
            addresstype = address[0].getAttribute("type")
            print "MAC address '%s', source bridge '%s', model type '%s', address type '%s'" % ( foundmac, sourcebridge, modeltype, addresstype )
        if len(sys.argv) == 2 and sys.argv[1] == "xml":
            print domain.XMLDesc(0)
        print ""