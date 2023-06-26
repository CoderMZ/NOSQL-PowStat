class Power:
    def __init__(self, cpu_percent, virtual_memory, swap_memory, timestamp):
        self.cpu_percent = cpu_percent
        self.virtual_memory = virtual_memory
        self.swap_memory = swap_memory
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'cpu_percent': self.cpu_percent,
            'virtual_memory': self.virtual_memory,
            'swap_memory': self.swap_memory,
            'timestamp': self.timestamp
        }
