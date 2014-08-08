#    LibVirt Wake On Lan
#    Copyright (C) 2014 Simon Cadman
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
import os
import sys
import pytest
import base64
sys.path.insert(0, ".")

from libvirtwol import LibVirtWakeOnLan


def test_StartServerByMACAddress():
    pass

def test_GetMACAddress():
    testdata = "7ZMABwBuwov////////erb7vsz/erb7vsz/erb7vsz/erb7vsz/erb7vsz/erb7vsz/erb7vsz/erb7vsz/erb7vsz/erb7vsz/erb7vsz/erb7vsz/erb7vsz/erb7vsz/erb7vsz/erb7vsz8="
    assert LibVirtWakeOnLan.GetMACAddress(base64.b64decode(testdata)) == "de:ad:be:ef:b3:3f"

def test_DecodeIPPacket():
    pass

def test_InspectIPPacketNoMAC():
    pass
    
def test_InspectIPPacketWithMAC():
    pass