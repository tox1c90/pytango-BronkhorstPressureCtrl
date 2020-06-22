# -*- coding: utf-8 -*-
#
# This file is part of the BronkhorstPressureCtrl project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" BronkhorstPressureCtrl PyTango Class (Serial connection)

Class for controlling Bronkhorst Pressure/Flow controller via serial connection
"""

# PyTango imports
import tango
from tango import DebugIt
from tango.server import run
from tango.server import Device
from tango.server import attribute, command
from tango.server import device_property
from tango import AttrQuality, DispLevel, DevState
from tango import AttrWriteType, PipeWriteType
# Additional import
import propar


__all__ = ["BronkhorstPressureCtrl", "main"]


class BronkhorstPressureCtrl(Device):
    # -----------------
    # Device Properties
    # -----------------

    Port = device_property(
        dtype='DevString',
        doc='e.g., /dev/ttyBronkhorst'
    )


    # ----------
    # Attributes
    # ----------

    Position = attribute(
        dtype='DevDouble',
        access=AttrWriteType.READ_WRITE,
        unit="units",
        memorized=True,
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        """Initialises the attributes and properties of the BronkhorstPressureCtrl."""
        self.info_stream("init_device()")
        Device.init_device(self)
        self.set_state(DevState.INIT)
              
        self.info_stream("port: {:s}".format(self.Port))
        
        # connect to device
        self.__el_flow = propar.instrument(self.Port)
        
        self.set_status("The device is in ON state")
        self.set_state(DevState.ON)


    def always_executed_hook(self):
        """Method always executed before any TANGO command is executed."""

    def delete_device(self):
        self.set_status("The device is in OFF state")
        self.set_state(DevState.OFF)
        

    # ------------------
    # Attributes methods
    # ------------------

    def read_Position(self):
        return self.__el_flow.measure


    def write_Position(self, value):
        el_flow.setpoint = value
        pass        

    # --------
    # Commands
    # --------

    def dev_state(self):
        self.set_status("The device is in ON state")
        self.debug_stream("device state: ON")
        return DevState.ON


# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    return run((BronkhorstPressureCtrl,), args=args, **kwargs)


if __name__ == '__main__':
    main()
