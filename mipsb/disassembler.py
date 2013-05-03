from instruction import BigEndianMipsInstruction
from common.disassembler import Disassembler


class BigEndianMipsDisassembler(Disassembler):
    def __init__(self,program):
        super(BigEndianMipsDisassembler,self).__init__(program,'BigEndianMipsDisassembler')
    def getInstructionSizeAtOffset(self,offset):
        return 4
    def getInstructionDataAtOffset(self,offset):
        idata = self.program[offset:offset+self.getInstructionSizeAtOffset(offset)]
        return idata
    def getInstructionAtOffset(self,offset):
        idata = self.getInstructionDataAtOffset(offset)
        mipsi = BigEndianMipsInstruction(idata)
        return mipsi
    def disassemble(self):
        offset = self.baseaddress
        while offset < len(self.program):
            increment = self.getInstructionSizeAtOffset(offset)
            instruction = BigEndianMipsInstruction(
                    self.getInstructionDataAtOffset(offset),
                    offset)
            offset += increment
            yield instruction


