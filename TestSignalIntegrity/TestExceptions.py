import unittest

import SignalIntegrity as si

class TestExceptions(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self,methodName)
    def testSystemDescriptionCheckConnections(self):
        sdp=si.p.SystemDescriptionParser()
        sdp.AddLines(['device DV 4','device ZI 2','device ZO 2',
            'port 1 ZI 1 2 ZI 2 3 ZO 2 4 DV 3',
            'connect ZI 1 DV 2','connect ZI 2 DV 1'])
        sdp.SystemDescription().Print()
        ssps=si.sd.SystemSParametersSymbolic(sdp.SystemDescription())
        try:
            ssps.LaTeXSolution().Emit()
        except si.PySIException as e:
            if e == si.PySIExceptionCheckConnections:
                pass
    def testSystemDescriptionCheckConnections2(self):
        sdp=si.p.SystemDescriptionParser()
        sdp.AddLines(['device DV 4','device ZI 2','device ZO 2',
            'port 1 ZI 1 2 ZI 2 3 ZO 2 4 DV 3',
            'connect ZI 1 DV 2','connect ZI 2 DV 1'])
        sdp.SystemDescription().Print()
        ssps=si.sd.SystemSParametersSymbolic(sdp.SystemDescription())
        with self.assertRaises(si.PySIException) as cm:
            ssps.LaTeXSolution().Emit()
        self.assertEqual(cm.exception.parameter,'CheckConnections')
    def testSystemDescriptionWrongDevice(self):
        sdp=si.p.SystemDescriptionParser()
        sdp.AddLines(['device DV 4','device ZI 2','device ZO 2',
            'port 1 ZI 1 2 ZI 2 3 ZO 2 4 DV 3',
            'connect Z 1 DV 2','connect ZI 2 DV 1'])
        with self.assertRaises(si.PySIException) as cm:
            sdp.SystemDescription().Print()
        self.assertEqual(cm.exception.parameter,'SystemDescriptionBuildError')
    def testSystemDescriptionWrongConnection(self):
        sdp=si.p.SystemDescriptionParser()
        sdp.AddLines(['device DV 4','device ZI 2','device ZO 2',
            'port 1 ZI 1 2 ZI 2 3 ZO 2 4 DV 3',
            'connect ZI 3 DV 2','connect ZI 2 DV 1'])
        with self.assertRaises(si.PySIException) as cm:
            sdp.SystemDescription().Print()
        self.assertEqual(cm.exception.parameter,'SystemDescriptionBuildError')
    def testSimulatorNoOutputProbes(self):
        sp=si.p.SimulatorParser()
        sp.AddLines(['voltagesource VS1 1','device G1 1 ground','connect G1 1 VS1 1'])
        ss=si.sd.SimulatorSymbolic(sp.SystemDescription(),size='small')
        with self.assertRaises(si.PySIException) as cm:
            ss.LaTeXTransferMatrix()
        self.assertEqual(cm.exception.parameter,'Simulator')
    def testSimulatorNoSources(self):
        sp=si.p.SimulatorParser()
        sp.AddLines(['device R1 1 R 50.0','device R2 1 R 50.0','output R2 1','connect R2 1 R1 1'])
        ss=si.sd.SimulatorSymbolic(sp.SystemDescription(),size='small')
        with self.assertRaises(si.PySIException) as cm:
            ss.LaTeXTransferMatrix()
        self.assertEqual(cm.exception.parameter,'Simulator')
    def testSimulatorNumericalError(self):
        sp=si.p.SimulatorParser()
        sp.AddLines(['voltagesource VS1 1','device G1 1 ground','output G1 1','connect G1 1 VS1 1'])
        sn=si.sd.SimulatorNumeric(sp.SystemDescription())
        with self.assertRaises(si.PySIException) as cm:
            sn.TransferMatrix()
        self.assertEqual(cm.exception.parameter,'Simulator')
if __name__ == '__main__':
    unittest.main()

