import os
from struct import *
from cStringIO import StringIO
from common.loader import Loader

class ELFHeader(object):
    ET_NONE=1
    ET_REL=2
    ET_EXEC=3
    ET_DYN=4
    ET_LOPROC=0xff00
    ET_HIPROC=0xffff
    EM_NONE=0
    EM_M32=1
    EM_SPARC=2
    EM_386=3
    EM_68K=4
    EM_88k=5
    EM_860=7
    EM_MIPS=8
    EV_NONE=0
    EV_CURRENT=1

    EI_MAG0 = 0
    EI_MAG1 = 1
    EI_MAG2 = 2
    EI_MAG3 = 3
    EI_CLASS = 4
    EI_DATA = 5
    EI_VERSION = 6
    EI_PAD = 7
    EI_NIDENT = 16
    ELFMAGIC = '\x7fELF'
    ELFCLASSNONE = 0
    ELFCLASS32 = 1
    ELFCLASS64 = 2
    ELFDATANONE = 0
    ELFDATA2LSB = 1
    ELFDATA2MSB = 2

    def __init__(self):
        self.e_ident = list()
        self.e_type = ET_NONE
        self.e_machine = EM_NONE
        self.e_version = EV_CURRENT
        self.e_entry = 0x0
        self.e_phoff = 0x0
        self.e_shoff = 0x0
        self.e_flags = 0x0
        self.e_ehsize = 0x0
        self.e_phentsize = 0x0
        self.e_phnum = 0x0
        self.e_shentsize = 0x0
        self.e_shnum = 0x0
        self.e_shsrtndx = 0x0

def ELFSectionHeader(object):
    SHT_NULL = 0
    SHT_PROGBITS = 1
    SHT_SYMTAB = 2
    SHT_STRTAB = 3
    SHT_RELA = 4
    SHT_HASH = 5
    SHT_DYNAMIC = 6
    SHT_NOTE = 7
    SHT_NOBITS = 8
    SHT_REL = 9
    SHT_SHLIB = 10
    SHT_DYNSYM = 11
    SHT_LOPROC = 0x70000000
    SHT_HIPROC = 0x7fffffff
    SHT_LOUSER = 0x80000000
    SHT_HIUSER = 0xffffffff
    SHF_WRITE = 1
    SHF_ALLOC = 2
    SHF_EXECINSTR = 4
    SHF_MASKPROC = 0xf0000000


    def __init__(self):
        self.sh_name = ''
        self.sh_type = SHT_NULL
        self.sh_flags = 0
        self.sh_addr = 0
        self.sh_offset = 0
        self.sh_size = 0
        self.sh_link = 0
        self.sh_info = 0
        self.sh_addralign = 0x04
        self.sh_entsize = 0

def ELF32_ST_BIND(i):
    return i >> 4

def ELF32_ST_TYPE(i):
    return i & 0xf

def ELF32_ST_INFO(b,t):
    return ((b << 4) + (t & 0xf))

class ELFSymbol(object):
    STN_UNDEF = 0
    STB_LOCAL = 0
    STB_GLOBAL = 1
    STB_WEAK = 2
    STB_LOPROC = 13
    STB_HIPROC = 15

    def __init__(self):
        self.st_name = 0
        self.st_value = 0
        self.st_size = 0
        self.st_info = 0
        self.st_other = 0
        self.st_shndx = 0

STT_NOTYPE = 0
STT_OBJECT = 1
STT_FUNC = 2
STT_SECTION = 3
STT_FILE = 4
STT_LOPROC = 13
STT_HIPROC = 15

class ELFLoader(Loader):
    def __init__(self, filename=''):
        super(ELFLoader, self).__init__(self, filename)
        self.readHeader()

    def readHeader(self):
        header = ELFHeader()
        header.e_ident = unpack('4s',self.blob[:4])
        if header.e_ident != header.ELFMAGIC:
            raise ValueError("Not an ELF file.")

