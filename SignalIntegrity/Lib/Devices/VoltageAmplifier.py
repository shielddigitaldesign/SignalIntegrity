"""
VoltageAmplifier.py
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

def VoltageAmplifier(P,G,Zi,Zo,Z0=50):
    """VoltageAmplifier
    2-4 Port Voltage Amplifiers
    @param P integer number of ports (2-4)
    @param G float voltage gain
    @param Zi float or complex input impedance
    @param Zo float or complex output impedance
    @param Z0 (optional) float reference impedance (defaults to 50 ohms)
    @return list of list s-parameter matrix for a voltage amplifier
    @remark
    The voltage amplifier can be two, three or four ports.\n
    @see VoltageAmplifierFourPort
    @see VoltageAmplifierThreePort
    @see VoltageAmplifierTwoPort
    """
    if P==2:
        return VoltageAmplifierTwoPort(G,Zi,Zo,Z0=50.)
    elif P==3:
        return VoltageAmplifierThreePort(G,Zi,Zo,Z0=50.)
    elif P==4:
        return VoltageAmplifierFourPort(G,Zi,Zo,Z0=50.)


def VoltageAmplifierFourPort(G,Zi,Zo,Z0=50.):
    """VoltageAmplifierFourPort
    Four port voltage amplifier
    @param G float voltage gain
    @param Zi float or complex input impedance
    @param Zo float or complex output impedance
    @param Z0 (optional) float reference impedance (defaults to 50 ohms)
    @return list of list s-parameter matrix for a voltage amplifier
    @remark
    The voltage sense element senses the voltage with the plus terminal at port 1
    and and the minus terminal at port 2 shunted with impedance of Zi.\n
    The voltage generated by the amplifier has the plus terminal at port 3 and 
    and the minus terminal at port 4 with Zo in series.\n
    """
    S11=Zi/(Zi+2.*Z0)
    S12=2.*Z0/(Zi+2.*Z0)
    S13=0
    S14=0
    S21=S12
    S22=S11
    S23=0
    S24=0
    S31=2.*Zi*Z0*G/((Zi+2.*Z0)*(Zo+2.*Z0))
    S32=-S31
    S33=Zo/(Zo+2.*Z0)
    S34=2.*Z0/(Zo+2.*Z0)
    S41=S32
    S42=S31
    S43=S34
    S44=S33
    return [[S11,S12,S13,S14],
            [S21,S22,S23,S24],
            [S31,S32,S33,S34],
            [S41,S42,S43,S44]]

def VoltageAmplifierThreePort(G,Zi,Zo,Z0=50.):
    """VoltageAmplifierThreePort
    Three port voltage amplifier
    @param G float voltage gain
    @param Zi float or complex input impedance
    @param Zo float or complex output impedance
    @param Z0 (optional) float reference impedance (defaults to 50 ohms)
    @return list of list s-parameter matrix for a voltage amplifier
    @remark
    The three port voltage amplifier is the same as the four port voltage amplifier with
    ports two and three connected together and exposed as a single port.\n
    The voltage sense element senses the voltage with the plus terminal at port 1
    and and the minus terminal at port 3 shunted with impedance of Zi.\n
    The voltage generated by the amplifier has the plus terminal at port 2 and 
    and the minus terminal at port 3 with Zo in series.\n
    """
    D=-Zo*Zi-2.*Zo*Z0-2.*Zi*Z0-3.*Z0*Z0+G*Zi*Z0
    S11=(-Zo*Zi-2.*Zi*Z0+Z0*Z0+G*Zi*Z0)/D
    S12=-2.*Z0*Z0/D
    S13=-2.*Z0*(Zo+Z0)/D
    S21=-2.*Z0*(G*Zi+Z0)/D
    S22=(Z0*Z0-2.*Zo*Z0+G*Zi*Z0-Zo*Zi)/D
    S23=2.*Z0*(G*Zi-Zi-Z0)/D
    S31=2.*Z0*(-Z0+G*Zi-Zo)/D
    S32=-2.*Z0*(Zi+Z0)/D
    S33=(-Zo*Zi+Z0*Z0-G*Zi*Z0)/D
    return [[S11,S12,S13],
            [S21,S22,S23],
            [S31,S32,S33]]

def VoltageAmplifierTwoPort(G,Zi,Zo,Z0=50.):
    """VoltageAmplifierTwoPort
    Two port voltage amplifier
    @param G float voltage gain
    @param Zi float or complex input impedance
    @param Zo float or complex output impedance
    @param Z0 (optional) float reference impedance (defaults to 50 ohms)
    @return list of list s-parameter matrix for a voltage amplifier
    @remark
    The two port voltage amplifier is the same as the three port voltage amplifier with
    port 3 grounded.\n
    The voltage sense element senses the voltage  to ground at port 1 shunted to ground
    with impedance of Zi.\n
    The voltage generated by the amplifier is at port 2 referenced to ground 
    with Zo in series with the output.\n
    """
    return [[(Zi-Z0)/(Zi+Z0),0.],[2.*G*Zi*Z0/((Zi+Z0)*(Zo+Z0)),(Zo-Z0)/(Zo+Z0)]]
