class Power() :
    def __init__ (self, CPU, RAMtotal, RAMinuse, timestamp, _id = None) :
        if (_id is not None):
            self._id = _id
        if (timestamp is None):
            self.timestamp = timestamp
        self.CPU = CPU
        self.RAMtotal = RAMtotal
        self.RAMinuse = RAMinuse
        self.timestamp = timestamp