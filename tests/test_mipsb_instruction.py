from mipsb.instruction import BigEndianMipsInstruction
import unittest

class TestRInstructionOperands(unittest.TestCase):
    def setUp(self):
        self.bin = '\x00\xc7\x28\x20' # add $a1, $a2, $a3
        self.instruction = BigEndianMipsInstruction(self.bin)
    def test_getRd(self):
        self.assertEqual(self.instruction.rd,5)
    def test_getRt(self):
        self.assertEqual(self.instruction.rt,7)
    def test_getRs(self):
        self.assertEqual(self.instruction.rt,6)

class TestRInstructionShift(unittest.TestCase):
    def setUp(self):
        self.skipTest('Test implementation incomplete')
        self.bin = '' # sll $a1, $a2, 4
        self.instruction = BigEndianMipsInstruction(self.bin)
    def test_getShiftAmount(self):
        self.assertEqual(self.instruction.shift,4)


if '__main__' == __name__:
    unittest.main()
