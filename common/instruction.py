class Instruction(object):
    def __init__(self,idata,baseaddress=0,offset=0):
        self.baseaddress = baseaddress
        self.offset = offset
        self.mnemonic = 'undef'
        self.rdest = 'unk'
        self.rsrc = 'unk'
        self.immval = 0
        self.comment = ''
        self.idata = idata
        self._disassemble()
    def _disassemble(self):
        pass
    def _address(self):
        return self.baseaddress + self.offset
    def __str__(self):
        return '%08x %s %s, %s, %s # %s' % (self._address(),
                self.mnemonic, self.rdest, self.rsrc, self.immval,
                self.comment)
