class Disassembler(object):
    def __init__(self,program,name=None):
        """
         program: this is the blob of binary data that represents the
                  program to be disassembled
         name:    a human-readable name for this disassembler
        """
        self.program = program
        self.name = name
        self.baseaddress = 0
    def getInstructionSizeAtOffset(self,offset):
        pass
    def getInstructionAtOffset(self,offset):
        pass
