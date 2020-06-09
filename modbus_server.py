#!/usr/bin/env python
"""
Pymodbus Server With Callbacks
--------------------------------------------------------------------------

This is an example of adding callbacks to a running modbus server
when a value is written to it. In order for this to work, it needs
a device-mapping file.
"""
# --------------------------------------------------------------------------- #
# import the modbus libraries we need
# --------------------------------------------------------------------------- #
from pymodbus.server.asynchronous import StartTcpServer, StopServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer


# --------------------------------------------------------------------------- #
# import the python libraries we need
# --------------------------------------------------------------------------- #
from PySide2 import QtCore
from multiprocessing import SimpleQueue, Process
from time import sleep


# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #
'''
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)
'''
# --------------------------------------------------------------------------- #
# create your custom data block with callbacks
# --------------------------------------------------------------------------- #

class CallbackDataBlock(ModbusSparseDataBlock):
    """ A datablock that stores the new value in memory
    and passes the operation to a message queue for further
    processing.
    """

    def __init__(self, devices, queue):
        self.devices = devices
        self.queue = queue

        values = {k: 0 for k in devices.keys()}
        values[0xbeef] = len(values)  # the number of devices
        super(CallbackDataBlock, self).__init__(values)

    def setValues(self, address, value):
        """ Sets the requested values of the datastore

        :param address: The starting address
        :param values: The new values to be set
        """
        super(CallbackDataBlock, self).setValues(address, value)
        self.queue.put((self.devices.get(address, None), value))

    def getValues(self, address, count=1):
        ''' Returns the requested values of the datastore

        :param address: The starting address
        :param count: The number of values to retrieve
        :returns: The requested values from a:a+c
        '''
        value = super(CallbackDataBlock, self).getValues(address, count)
        self.queue.put((self.devices.get(address, None), value))
        return value


# --------------------------------------------------------------------------- #
# initialize your device map
# --------------------------------------------------------------------------- #
def di_map():
    devices = {
        0x0001: "di1",
        0x0002: "di2",   
        0x0003: "di3",  
        0x0004: "di4",
        0x0005: "di5",
        0x0006: "di6",
        0x0007: "di7", 
        0x0008: "di8",
    }
    return devices

def co_map():
    devices = {
        0x0001: "co1",
        0x0002: "co2",   
        0x0003: "co3",  
        0x0004: "co4",
        0x0005: "co5",
        0x0006: "co6",
        0x0007: "co7", 
        0x0008: "co8",
    }
    return devices

def hr_map():
    devices = {
        0x0001: "hr1",
        0x0002: "hr2",   
        0x0003: "hr3",  
        0x0004: "hr4",
        0x0005: "hr5",
        0x0006: "hr6",
        0x0007: "hr7", 
        0x0008: "hr8",
    }
    return devices

def ir_map():
    devices = {
        0x0001: "ir1",
        0x0002: "ir2",   
        0x0003: "ir3",  
        0x0004: "ir4",
        0x0005: "ir5",
        0x0006: "ir6",
        0x0007: "ir7", 
        0x0008: "ir8",
    }
    return devices

def run_callback_server(ip, porta, queue):
    # ----------------------------------------------------------------------- #
    # initialize your data store
    # ----------------------------------------------------------------------- #

    diDataBlock = CallbackDataBlock(di_map(), queue)
    coDataBlock = CallbackDataBlock(co_map(), queue)
    hrDataBlock = CallbackDataBlock(hr_map(), queue)
    irDataBlock = CallbackDataBlock(ir_map(), queue)
    
    store = ModbusSlaveContext(di=diDataBlock, co=coDataBlock, hr=hrDataBlock, ir=irDataBlock)
    context = ModbusServerContext(slaves=store, single=True)

    # ----------------------------------------------------------------------- #
    # initialize the server information
    # ----------------------------------------------------------------------- #
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'LHF Instrumentacao'
    identity.ProductCode = 'mOHM 1.0'
    identity.VendorUrl = 'lhf.ind.br'
    identity.ProductName = 'Miliohmimetro'
    identity.MajorMinorRevision = '1.0'

    # ----------------------------------------------------------------------- #
    # run the server you want
    # ----------------------------------------------------------------------- #
    StartTcpServer(context, identity=identity, address=(ip, porta))


def stop_callback_server():
    StopServer()
