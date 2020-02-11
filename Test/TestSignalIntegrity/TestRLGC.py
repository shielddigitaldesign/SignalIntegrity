"""
TestRLGC.py
"""

# Copyright (c) 2018 Teledyne LeCroy, Inc.
# All rights reserved worldwide.
#
# This file is part of SignalIntegrity.
#
# SignalIntegrity is free software: You can redistribute it and/or modify it under the terms
# of the GNU General Public License as published by the Free Software Foundation, either
# version 3 of the License, or any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>
import unittest

import SignalIntegrity.Lib as si
import os

class TestRLGC(unittest.TestCase):            
    def testRLGC(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        spf=si.sp.SParameterFile('cable.s2p')
        rlgc = si.sp.RLGC(spf,si.fd.FrequencyList(spf.m_f).TimeDescriptor())
        pass
    def testRLGCFitFromFile(self):
        fd=si.fd.EvenlySpacedFrequencyList(20e9,400)
        rlgc=si.fit.RLGCFitFromFile(fd,'../../SignalIntegrity/App/Examples/HDMICable/HDMIThruPortsPeeled.si').Fit()
        pass
    def testRLGCFitFromFileUnCached(self):
        fd=si.fd.EvenlySpacedFrequencyList(20e9,400)
        rlgc=si.fit.RLGCFitFromFile(fd,'../../SignalIntegrity/App/Examples/HDMICable/HDMIThruPortsPeeled.si').Fit()
        pass

if __name__ == '__main__':
    unittest.main()
