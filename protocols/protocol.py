'''
            GDP - The Generic Device Programmer.

    By Dean Camera (dean [at] fourwalledcubicle [dot] com)
'''

from abc import ABCMeta, abstractmethod


class ProtocolError(Exception):
    pass


class Protocol(object):
    __metaclass__ = ABCMeta


    @abstractmethod
    def get_vtarget(self):
        pass


    @abstractmethod
    def set_interface_frequency(self, target_frequency):
        pass


    @abstractmethod
    def enter_session(self):
        pass


    @abstractmethod
    def exit_session(self):
        pass


    @abstractmethod
    def erase_memory(self, memory_space, offset):
        pass


    @abstractmethod
    def read_memory(self, memory_space, offset, length):
        pass


    @abstractmethod
    def write_memory(self, memory_space, offset, data):
        pass


    @abstractmethod
    def open(self):
        pass


    @abstractmethod
    def close(self):
        pass
