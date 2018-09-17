import unittest
from main import convert_to_roman_numerals


class TestRomanNumerals(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_this_thing_on(self):
        self.assertTrue(True)

    def test_returns_I_for_1(self):
        self.assertEqual(convert_to_roman_numerals(1), 'I')

    def test_returns_II_for_2(self):
        self.assertEqual(convert_to_roman_numerals(2), 'II')

    def test_returns_III_for_3(self):
        self.assertEqual(convert_to_roman_numerals(3), 'III')

    """ denominations """

    def test_returns_V_for_5(self):
        self.assertEqual(convert_to_roman_numerals(5), 'V')

    def test_returns_X_for_10(self):
        self.assertEqual(convert_to_roman_numerals(10), 'X')

    def test_returns_L_for_50(self):
        self.assertEqual(convert_to_roman_numerals(50), 'L')

    def test_returns_C_for_100(self):
        self.assertEqual(convert_to_roman_numerals(100), 'C')

    def test_returns_D_for_500(self):
        self.assertEqual(convert_to_roman_numerals(500), 'D')

    def test_returns_M_for_1000(self):
        self.assertEqual(convert_to_roman_numerals(1000), 'M')

    """ above """

    def test_returns_VI_for_6(self):
        self.assertEqual(convert_to_roman_numerals(6), 'VI')

    def test_returns_VII_for_7(self):
        self.assertEqual(convert_to_roman_numerals(7), 'VII')

    def test_returns_XI_for_11(self):
        self.assertEqual(convert_to_roman_numerals(11), 'XI')

    def test_returns_XII_for_12(self):
        self.assertEqual(convert_to_roman_numerals(12), 'XII')

    def test_returns_XV_for_15(self):
        self.assertEqual(convert_to_roman_numerals(15), 'XV')

    def test_returns_XXI_for_21(self):
        self.assertEqual(convert_to_roman_numerals(21), 'XXI')

    def test_returns_XXII_for_22(self):
        self.assertEqual(convert_to_roman_numerals(22), 'XXII')

    def test_returns_LI_for_51(self):
        self.assertEqual(convert_to_roman_numerals(51), 'LI')

    def test_returns_LII_for_52(self):
        self.assertEqual(convert_to_roman_numerals(52), 'LII')

    def test_returns_LXI_for_61(self):
        self.assertEqual(convert_to_roman_numerals(61), 'LXI')

    def test_returns_LXII_for_62(self):
        self.assertEqual(convert_to_roman_numerals(62), 'LXII')

    """ below """

    def test_returns_IV_for_4(self):
        self.assertEqual(convert_to_roman_numerals(4), 'IV')

    def test_returns_IX_for_9(self):
        self.assertEqual(convert_to_roman_numerals(9), 'IX')

    def test_returns_XIV_for_14(self):
        self.assertEqual(convert_to_roman_numerals(14), 'XIV')

    def test_returns_XIX_for_19(self):
        self.assertEqual(convert_to_roman_numerals(19), 'XIX')

    def test_returns_XL_for_40(self):
        self.assertEqual(convert_to_roman_numerals(40), 'XL')

    def test_returns_XLIV_for_44(self):
        self.assertEqual(convert_to_roman_numerals(44), 'XLIV')

    def test_returns_XLV_for_45(self):
        self.assertEqual(convert_to_roman_numerals(45), 'XLV')

    def test_returns_XLIX_for_49(self):
        self.assertEqual(convert_to_roman_numerals(49), 'XLIX')

    def test_returns_XC_for_90(self):
        self.assertEqual(convert_to_roman_numerals(90), 'XC')

    def test_returns_XCIV_for_94(self):
        self.assertEqual(convert_to_roman_numerals(94), 'XCIV')

    def test_returns_XC_for_95(self):
        self.assertEqual(convert_to_roman_numerals(95), 'XCV')

    def test_returns_XCIX_for_99(self):
        self.assertEqual(convert_to_roman_numerals(99), 'XCIX')

    def test_returns_CXL_for_140(self):
        self.assertEqual(convert_to_roman_numerals(140), 'CXL')

    def test_returns_CXC_for_190(self):
        self.assertEqual(convert_to_roman_numerals(190), 'CXC')

    def test_returns_CD_for_400(self):
        self.assertEqual(convert_to_roman_numerals(400), 'CD')

    def test_returns_CDXLIX_for_449(self):
        self.assertEqual(convert_to_roman_numerals(449), 'CDXLIX')

    def test_returns_XM_for_900(self):
        self.assertEqual(convert_to_roman_numerals(900), 'CM')

    def test_returns_CMXCIX_for_999(self):
        self.assertEqual(convert_to_roman_numerals(999), 'CMXCIX')

    def test_returns_MCD_for_1400(self):
        self.assertEqual(convert_to_roman_numerals(1400), 'MCD')

    def test_returns_MCDXCIX_for_1499(self):
        self.assertEqual(convert_to_roman_numerals(1499), 'MCDXCIX')

    def test_returns_MCM_for_1900(self):
        self.assertEqual(convert_to_roman_numerals(1900), 'MCM')
