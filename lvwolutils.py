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

import logging
import sys


class Utils(object):
    logpath = '/var/log/libvirt/libvirtwakeonlan.log'

    @staticmethod
    def SetupLogging(logpath=None):
        returnValue = True
        logformat = "%(asctime)s|%(levelname)s|%(message)s"
        dateformat = "%Y-%m-%d %H:%M:%S"
        if logpath is None:
            logpath = Utils.logpath
        try:
            logging.basicConfig(
                filename=logpath,
                level=logging.INFO,
                format=logformat,
                datefmt=dateformat)
        except Exception:
            logging.basicConfig(
                level=logging.INFO,
                format=logformat,
                datefmt=dateformat)
            logging.error("Unable to write to log file " + logpath)
            returnValue = False
        return returnValue

    @staticmethod
    def ShowVersion(Version):
        if len(sys.argv) == 2 and sys.argv[1] == 'version':
            print "LibVirt Wake-On-Lan Version " + Version
            sys.exit(0)
        return False
