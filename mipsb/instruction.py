from struct import unpack
from common.instruction import Instruction

class BigEndianMipsInstruction(Instruction):
    mnemonics = {}
    functs = {}
    registers = ['zero','at','v0','v1','a0','a1','a2','a3',
            't0','t1','t2','t3','t4','t5','t6','t7',
            's0','s1','s2','s3','s4','s5','s6','s7',
            't8','t9','k0','k1','gp','sp','fp','ra']
    mnemonics[0x08] = 'addi'
    mnemonics[0x09] = 'addiu'
    mnemonics[0x0c] = 'andi'
    mnemonics[0x04] = 'beq'
    mnemonics[0x05] = 'bne'
    mnemonics[0x02] = 'j'
    mnemonics[0x03] = 'jal'
    mnemonics[0x24] = 'lbu'
    mnemonics[0x25] = 'lhu'
    mnemonics[0x0f] = 'lui'
    mnemonics[0x23] = 'lw'
    mnemonics[0x0d] = 'ori'
    mnemonics[0x28] = 'sb'
    mnemonics[0x29] = 'sh'
    mnemonics[0x0a] = 'slti'
    mnemonics[0x0b] = 'sltiu'
    mnemonics[0x2b] = 'sw'
    functs[0x20] = 'add'
    functs[0x21] = 'addu'
    functs[0x24] = 'and'
    functs[0x1a] = 'div'
    functs[0x1b] = 'divu'
    functs[0x08] = 'jr'
    functs[0x10] = 'mfhi'
    functs[0x12] = 'mflo'
    functs[0x18] = 'mult'
    functs[0x19] = 'multu'
    functs[0x27] = 'nor'
    functs[0x26] = 'xor'
    functs[0x25] = 'or'
    functs[0x2a] = 'slt'
    functs[0x2b] = 'sltu'
    functs[0x00] = 'sll'
    functs[0x02] = 'srl'
    functs[0x22] = 'sub'
    functs[0x23] = 'subu'
    functs[0x0c] = 'syscall'
    def __init__(self,idata,offset=0):
        self.dword, = unpack('>L',idata)
        super(BigEndianMipsInstruction,self).__init__(idata,offset=offset)
    def _get_opcode(self):
        opcode = self.dword >> (32-6)
        return opcode
    def _get_funct(self):
        funct = self.dword & 0x63
        return funct
    def _get_rs(self):
        rs = (self.dword >> 21) & 31
        return rs
    def _get_rt(self):
        rt = (self.dword >> 16) & 31
        return rt
    def _get_rd(self):
        rd = (self.dword >> 11) & 31
        return rd
    def _get_shift(self):
        shift = (self.dword >> 6) & 31
        return shift
    def _get_immediate(self):
        imm = (self.dword & 0xffff)
        return imm
    def _get_address(self):
        addr = (self.dword & 0x3ffffff)
        return addr
    def _get_mnemonic(self):
        if self._isR():
            return self.functs[self._get_funct()]
        return self.mnemonics[self._get_opcode()]
    def _disassemble(self):
        self.opcode = self._get_opcode()
        self.mnemonic = self._get_mnemonic()
        if self._isJ():
            self.address = self._get_address()
            self.string = str(self)
            return
        self.rs = self._get_rs()
        self.rt = self._get_rt()
        if self._isI():
            self.immediate = self._get_immediate()
            self.string = str(self)
        if self._isR():
            self.rd = self._get_rd()
            self.shift = self._get_shift()
        self.string = str(self)
    def _isR(self):
        opcode = self._get_opcode()
        return opcode in [0,0x10]
    def _isI(self):
        opcode = self._get_opcode()
        return opcode in [0x8,0x9,0xc,0x4,0x5,0x24,0x25,0xf,0x23,0xd,0x28,0x29,
            0xa,0xb,0x2b]
    def _isJ(self):
        opcode = self._get_opcode()
        return opcode in [2,3]
    def __str__(self):
        if self.__dict__.has_key('string'):
            return self.string
        retstring = '%08x ' % self.offset
        if self._isJ():
            return '%s%s %x' % (retstring,self.mnemonic,self.address)
        if self._isI():
            return '%s%s %s, %s, 0x%x' % (retstring,
                    self.mnemonic,
                    self.registers[self.rt],
                    self.registers[self.rs],
                    self.immediate)
        if self._isR():
            return '%s%s %s, %s, %s' % (retstring,
                    self.mnemonic,
                    self.registers[self.rd],
                    self.registers[self.rs],
                    self.registers[self.rt])
        return '%sinvalid instruction' % (retstring)
