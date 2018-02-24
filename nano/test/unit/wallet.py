import context
import unittest
import nano.utils
import nano.protocol.wallet
import nano.protocol.conversions

EXAMPLE_XRB_ACCOUNT_1 = "xrb_3e3j5tkog48pnny9dmfzj1r16pg8t1e76dz5tmac6iq689wyjfpi00000000"
EXAMPLE_WALLET_1 = "000D1BAEC8EC208142C99059B393051BAC8380F9B5A2E6B2489A277D81789F3F"
EXAMPLE_PUBLIC_KEY_1 = "3068BB1CA04525BB0E416C485FE6A67FD52540227D267CC8B6E8DA958A7FA039"

class TestWallet(unittest.TestCase):

	def test_wallet_create(self):
		expected = {"action": "wallet_create"}
		actual = nano.protocol.wallet.wallet_create()
		self.assertEqual(expected, actual)


def main():
	print "Running unit tests for: Wallet"
	suite = unittest.TestLoader().loadTestsFromTestCase(TestWallet)
	unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
	main()