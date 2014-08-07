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
import logging
import sys
import pytest
import struct
sys.path.insert(0, ".")

from lvwolutils import Utils


def teardown_function(function):
    logging.shutdown()
    reload(logging)


def test_SetupLogging():
    testLogFile = '/tmp/test.log'
    assert os.path.exists(testLogFile) is False
    assert Utils.SetupLogging(testLogFile) is True
    logging.error('test_setupLogging error test')
    assert os.path.exists(testLogFile) is True
    os.unlink(testLogFile)


def test_SetupLoggingDefault():
    testLogFile = '/tmp/test.log'
    assert os.path.exists(testLogFile) is False
    Utils.logpath = testLogFile
    assert Utils.SetupLogging() is True
    logging.error('test_setupLogging error test')
    assert os.path.exists(testLogFile) is True
    os.unlink(testLogFile)


def test_SetupLoggingFails():
    testLogFile = '/tmp/dirthatdoesntexist/test.log'
    assert os.path.exists(testLogFile) is False
    assert Utils.SetupLogging(testLogFile) is False
    assert os.path.exists(testLogFile) is False


def test_showVersion():
    assert Utils.ShowVersion("12345") is False
    sys.argv = ['testfile', 'version']
    with pytest.raises(SystemExit):
        Utils.ShowVersion("12345")
