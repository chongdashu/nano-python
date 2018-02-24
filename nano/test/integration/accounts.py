import context
import nano.utils
import nano.protocol.accounts
import nano.protocol.conversions


result = ""

def test_seanomlor_account_balance():
	
	print "Test: Query for Sean Omlor's public address account balance."
	account = "xrb_163thh9pcxgox4fej3otqdre17q8k7sntzajitun76cfite9jc1toza8hano"
	action = nano.protocol.accounts.account_balance(account)
	result = nano.utils.request(action)

	print ""
	print "Test: Convert the account balance to Mxrb."

	data = nano.utils.from_json(result)
	balance = data["balance"]
	pending = data["pending"]

	action = nano.protocol.conversions.mrai_from_raw(balance)
	result = nano.utils.request(action)

	action = nano.protocol.conversions.mrai_from_raw(pending)
	result = nano.utils.request(action)
	

def main():
	print "Running tests for: accounts"

	test_seanomlor_account_balance()

if __name__ == "__main__":
	main()