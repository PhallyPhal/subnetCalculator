#Author:   Justin Oberg
#Date:     2019-04-24
#Network Attributes (with GUI!)
#This program allows you to put in an IP address and it will tell you
#Helpful information about the network.

import tkinter
import re
def networkCalculator(event=None):
    
    def ipToBin(input):
        """Converts an IPv4 address to binary string."""
        
        a, b, c, d = input.split('.')
        a = format(int(a), '08b')
        b = format(int(b), '08b')
        c = format(int(c), '08b')
        d = format(int(d), '08b')
        return a, b, c, d
        
    def subInvert(input):
        """Takes four segments of an already binary subnet mask and inverts them."""
        input = entSubnet.get()
        a, b, c, d = input.split('.')
        a = format(int(a), '08b')
        b = format(int(b), '08b')
        c = format(int(c), '08b')
        d = format(int(d), '08b')
        e = str(a).replace('1','2').replace('0','1').replace('2','0')
        f = str(b).replace('1','2').replace('0','1').replace('2','0')
        g = str(c).replace('1','2').replace('0','1').replace('2','0')
        h = str(d).replace('1','2').replace('0','1').replace('2','0')
        return a, b, c, d, e, f, g, h

    def netAddress(sA,sB,sC,sD,ipA,ipB,ipC,ipD):
        """Calculates the network address for the program."""
        netAddPlaceHolder = '00000000'
        netAd1,netAd2,netAd3,netAd4 = '','','',''
        for i in range(0,8):
            if str(sA[i]) == '1' and str(ipA[i]) == '1':
                netAd1 = str(netAd1[:i]) + '1' + netAddPlaceHolder[(i+1):]
            else: netAd1 = str(netAd1[:i]) + '0' + netAddPlaceHolder[(i+1):]

        for i in range(0,8):
            if str(sB[i]) == '1' and str(ipB[i]) == '1':
                netAd2 = str(netAd2[:i]) + '1' + netAddPlaceHolder[(i+1):]
            else: netAd2 = str(netAd2[:i]) + '0' + netAddPlaceHolder[(i+1):]

        for i in range(0,8):
            if str(sC[i]) == '1' and str(ipC[i]) == '1':
                netAd3 = str(netAd3[:i]) + '1' + netAddPlaceHolder[(i+1):]
            else: netAd3 = str(netAd3[:i]) + '0' + netAddPlaceHolder[(i+1):]

        for i in range(0,8):
            if str(sD[i]) == '1' and str(ipD[i]) == '1':
                netAd4 = str(netAd4[:i]) + '1' + netAddPlaceHolder[(i+1):]
            else: netAd4 = str(netAd4[:i]) + '0' + netAddPlaceHolder[(i+1):]
        return netAd1, netAd2, netAd3, netAd4

    def broadcastAddress(is1, is2, is3, is4, n1, n2, n3, n4):
        """Finds the broadcast address for the network for the program."""
        new1, new2, new3, new4 = '','','',''
        for i in range(0,8):
            if str(is1[i]) != str(n1[i]):
                new1 = new1 + '1'
            else:
                new1 = new1 + '0'
        for i in range(0,8):
            if str(is2[i]) != str(n2[i]):
                new2 = new2 + '1'
            else:
                new2 = new2 + '0'
        for i in range(0,8):
            if str(is3[i]) != str(n3[i]):
                new3 = new3 + '1'
            else:
                new3 = new3 + '0'
        for i in range(0,8):
            if str(is4[i]) != str(n4[i]):
                new4 = new4 + '1'
            else:
                new4 = new4 + '0'
        return new1, new2, new3, new4

    def maxDevices(a, b, c, d):
        """Finds the maximum amount of device numbers on the given network
        provided the subnet mask (in binary string)"""
        onBits = len(re.findall('1', a)) + len(re.findall('1', b)) \
                     + len(re.findall('1', c)) + len(re.findall('1', d))
        maxDevices = 2**(32-onBits) - 2
        return maxDevices
            
    
    ipInput = entIp.get()
    subInput = entSubnet.get()
    ipBin1, ipBin2, ipBin3, ipBin4 = ipToBin(ipInput)
    subBin1, subBin2, subBin3, subBin4, subInv1, subInv2, subInv3, subInv4 = subInvert(subInput)
    net1, net2, net3, net4 = netAddress(subBin1, subBin2, subBin3, subBin4,
                                        ipBin1, ipBin2, ipBin3, ipBin4)

    networkAddress = (str(int(net1, base=2)) + '.' +
          str(int(net2, base=2)) + '.' + str(int(net3, base=2)) + '.' +
          str(int(net4, base=2)))

    broad1, broad2, broad3, broad4 = broadcastAddress(subInv1, subInv2, subInv3,
                                                      subInv4, net1, net2, net3,
                                                      net4)
    broadcastAddress = (str(int(broad1, base=2)) + '.' + str(int(broad2, base=2))
                        + '.' + str(int(broad3, base=2)) + '.' +
                        str(int(broad4, base=2)))
    maximumNetDevices = maxDevices(subBin1, subBin2, subBin3, subBin4)

    entNetwork.config(state='normal')
    entNetwork.delete(0, tkinter.END)
    entNetwork.insert(0, networkAddress)
    entNetwork.config(state='disabled')
    entBroadcast.config(state='normal')
    entBroadcast.delete(0, tkinter.END)
    entBroadcast.insert(0, broadcastAddress)
    entBroadcast.config(state='disabled')
    entDevice.config(state='normal')
    entDevice.delete(0, tkinter.END)
    entDevice.insert(0, maximumNetDevices)
    entDevice.config(state='disabled')
    
    
    
    



    
#GUI Resides below!

root = tkinter.Tk()
root.title("Network Calculator")
topFrame = tkinter.Frame(root)
topFrame.pack()
bottomFrame = tkinter.Frame(root)
bottomFrame.pack(side=tkinter.BOTTOM)
topFrame.pack()

lblTitle = tkinter.Label(topFrame, text="Subnetting Calculator")
lblIp = tkinter.Label(topFrame, text="Enter valid IPv4 address.")
entIp = tkinter.Entry(topFrame)
lblCopyright = tkinter.Label(bottomFrame, text="\u00a9Justin Oberg")
lblSubnet = tkinter.Label(topFrame, text="Enter valid IPv4 subnet mask.")
entSubnet = tkinter.Entry(topFrame)
btnCalculate = tkinter.Button(topFrame, text="Calculate!", command=networkCalculator)
lblNetwork = tkinter.Label(topFrame, text="Network Address")
entNetwork = tkinter.Entry(topFrame, bg="lightgray", state='disabled')
lblBroadcast = tkinter.Label(topFrame, text="Broadcast Address")
entBroadcast = tkinter.Entry(topFrame, bg="lightgray", state='disabled')
lblDevice = tkinter.Label(topFrame, text="Maximum Devices")
entDevice = tkinter.Entry(topFrame, bg='lightgray', state='disabled')
root.bind_all('<Return>', networkCalculator)
lblTitle.grid(row=0,column=0)
lblIp.grid()
entIp.grid(row=1, column = 1, padx=5, pady=5)
lblSubnet.grid(row=2, column =0, padx=5, pady=5)
entSubnet.grid(row=2, column=1, padx=5, pady=5)
lblNetwork.grid(row=1, column=2, padx=5, pady=5)
entNetwork.grid(row=1, column=3, padx=5, pady=5)
lblBroadcast.grid(row=2, column=2, padx=5, pady=5)
entBroadcast.grid(row=2, column=3, padx=5, pady=5)
lblDevice.grid(row=3, column=0, padx=5, pady=5)
entDevice.grid(row=3, column=1, padx=5, pady=5)

btnCalculate.grid(row=3, column=3)

lblCopyright.pack(pady=5)

root.mainloop()
