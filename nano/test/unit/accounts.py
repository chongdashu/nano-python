import context
import unittest
import nano.utils
import nano.protocol.accounts
import nano.protocol.conversions

EXAMPLE_XRB_ACCOUNT_1 = "xrb_3e3j5tkog48pnny9dmfzj1r16pg8t1e76dz5tmac6iq689wyjfpi00000000"
EXAMPLE_WALLET_1 = "000D1BAEC8EC208142C99059B393051BAC8380F9B5A2E6B2489A277D81789F3F"
EXAMPLE_PUBLIC_KEY_1 = "3068BB1CA04525BB0E416C485FE6A67FD52540227D267CC8B6E8DA958A7FA039"

class TestAccounts(unittest.TestCase):

	def test_account_balance(self):
		expected = {"action": "account_balance", "account": EXAMPLE_XRB_ACCOUNT_1}
		actual = nano.protocol.accounts.account_balance(EXAMPLE_XRB_ACCOUNT_1)
		self.assertEqual(expected, actual)

	def test_account_block_count(self):
		expected = {"action": "account_block_count", "account": EXAMPLE_XRB_ACCOUNT_1}
		actual = nano.protocol.accounts.account_block_count(EXAMPLE_XRB_ACCOUNT_1)
		self.assertEqual(expected, actual)

	def test_account_info(self):
		expected = {"action": "account_info", "account": EXAMPLE_XRB_ACCOUNT_1, "representative": "false", "weight": "false", "pending": "false"}
		actual = nano.protocol.accounts.account_info(EXAMPLE_XRB_ACCOUNT_1)
		self.assertEqual(expected, actual)

	def test_account_info_and_set_representative(self):
		expected = {"action": "account_info", "account": EXAMPLE_XRB_ACCOUNT_1, "representative": "true", "weight": "false", "pending": "false"}
		actual = nano.protocol.accounts.account_info(EXAMPLE_XRB_ACCOUNT_1, representative=True)
		self.assertEqual(expected, actual)

	def test_account_info_and_set_weight(self):
		expected = {"action": "account_info", "account": EXAMPLE_XRB_ACCOUNT_1, "representative": "false", "weight": "true", "pending": "false"}
		actual = nano.protocol.accounts.account_info(EXAMPLE_XRB_ACCOUNT_1, weight=True)
		self.assertEqual(expected, actual)

	def test_account_info_and_set_pending(self):
		expected = {"action": "account_info", "account": EXAMPLE_XRB_ACCOUNT_1, "representative": "false", "weight": "false", "pending": "true"}
		actual = nano.protocol.accounts.account_info(EXAMPLE_XRB_ACCOUNT_1, pending=True)
		self.assertEqual(expected, actual)

	def test_account_info_and_set_all_except_representative(self):
		expected = {"action": "account_info", "account": EXAMPLE_XRB_ACCOUNT_1, "representative": "false", "weight": "true", "pending": "true"}
		actual = nano.protocol.accounts.account_info(EXAMPLE_XRB_ACCOUNT_1, pending=True, weight=True)
		self.assertEqual(expected, actual)

	def test_account_info_and_set_all_except_weight(self):
		expected = {"action": "account_info", "account": EXAMPLE_XRB_ACCOUNT_1, "representative": "true", "weight": "false", "pending": "true"}
		actual = nano.protocol.accounts.account_info(EXAMPLE_XRB_ACCOUNT_1, representative=True, pending=True)
		self.assertEqual(expected, actual)

	def test_account_info_and_set_all_except_pending(self):
		expected = {"action": "account_info", "account": EXAMPLE_XRB_ACCOUNT_1, "representative": "true", "weight": "true", "pending": "false"}
		actual = nano.protocol.accounts.account_info(EXAMPLE_XRB_ACCOUNT_1, representative=True, weight=True)
		self.assertEqual(expected, actual)

	def test_account_create(self):
		expected = {"action": "account_create", "wallet": EXAMPLE_WALLET_1}
		actual = nano.protocol.accounts.account_create(EXAMPLE_WALLET_1)
		self.assertEqual(expected, actual)

	def test_account_create_disable_work_generation(self):
		expected = {"action": "account_create", "wallet": EXAMPLE_WALLET_1, "work": "false"}
		actual = nano.protocol.accounts.account_create(EXAMPLE_WALLET_1, work=False)
		self.assertEqual(expected, actual)

	def test_account_get(self):
		expected = {"action": "account_get", "key": EXAMPLE_PUBLIC_KEY_1}
		actual = nano.protocol.accounts.account_get(EXAMPLE_PUBLIC_KEY_1)
		self.assertEqual(expected, actual)

	def test_account_history_count_zero(self):
		expected = {"action": "account_history", "account": EXAMPLE_XRB_ACCOUNT_1, "count": 0}
		actual = nano.protocol.accounts.account_history(account=EXAMPLE_XRB_ACCOUNT_1, count=0)
		self.assertEqual(expected, actual)

	def test_account_history_count_one(self):
		expected = {"action": "account_history", "account": EXAMPLE_XRB_ACCOUNT_1, "count": 0}
		actual = nano.protocol.accounts.account_history(account=EXAMPLE_XRB_ACCOUNT_1, count=0)
		self.assertEqual(expected, actual)

	def test_account_history_count_big(self):
		expected = {"action": "account_history", "account": EXAMPLE_XRB_ACCOUNT_1, "count": 99999}
		actual = nano.protocol.accounts.account_history(account=EXAMPLE_XRB_ACCOUNT_1, count=99999)
		self.assertEqual(expected, actual)

	def test_account_history_count_small(self):
		expected = {"action": "account_history", "account": EXAMPLE_XRB_ACCOUNT_1, "count": 5}
		actual = nano.protocol.accounts.account_history(account=EXAMPLE_XRB_ACCOUNT_1, count=5)
		self.assertEqual(expected, actual)


def main():
	print "Running unit tests for: accounts"
	# unittest.main()
	suite = unittest.TestLoader().loadTestsFromTestCase(TestAccounts)
	unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
	main()