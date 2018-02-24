import json

"""
Based on the official Nano protocol:
https://github.com/nanocurrency/raiblocks/wiki/RPC-protocol#account-balance

Date: 22-Feb 2018 02:59 GMT+8
"""

def account_balance(account):
	"""
	Returns how many RAW is owned and how many have not yet been received by account.
	"""
	data = {"action": "account_balance", "account" : account}
	return data

def account_block_count(account):
	"""
	Get number of blocks for a specific account.
	"""
	data = {"action": "account_block_count", "account" : account}
	return data

def account_info(account, representative=False, weight=False, pending=False):
	"""
	Returns frontier, open block, change representative block, balance, 
	last modified timestamp from local database & block count for account.
	Additionally returns representative, voting weight, pending balance for account.
	"""
	data = {"action": "account_info", "account" : account}
	
	if representative is not None:
		data["representative"] = str(representative).lower()
	if weight is not None:
		data["weight"] = str(weight).lower()
	if pending is not None:
		data["pending"] = str(pending).lower()

	return data

def account_create(wallet, work=True):
	"""
	Creates a new account, insert next deterministic key in wallet.
	Additionally disables work generation after creating account.
	"""
	data = {"action": "account_create", "wallet" : wallet}
	if not work:
		data["work"] = str(work).lower()
	return data

def account_get(key):
	"""
	Get account number for the public key.
	"""
	data = {"action": "account_get", "key" : key}
	return data

def account_history(account, count):
	"""
	Reports send/receive information for a account.
	"""
	data = {"action": "account_history", "account" : account, "count" : count}
	return data

def account_move(wallet, source, accounts):
	"""
	Moves accounts from source to wallet.
	"""
	data = {"action": "account_move", "wallet" : wallet, "source" : source, "accounts" : accounts}
	return data

def account_key(account):
	"""
	Moves accounts from source to wallet.
	"""
	data = {"action": "account_key", "account" : account}
	return data

def account_remove(account, wallet):
	"""
	Remove account from wallet
	"""
	data = {"action": "account_remove", "wallet" : wallet, "account" : account}
	return 

def account_representative(account):
	"""
	Returns the representative for account.
	"""
	data = {"action": "account_remove", "wallet" : wallet, "account" : account}
	return data

def account_representative_set(account, wallet, representative, work=None):
	"""
	Sets the representative for account in wallet.
	"""
	data = {"action": "account_representative_set", "wallet" : wallet, "account" : account, "representative" : representative}
	if work is not None:
		data["work"] = work
	return data

def account_weight(account):
	"""
	Returns the voting weight for account.
	"""
	data = {"action": "account_weight", "account" : account}
	return data

def accounts_balances(accounts):
	"""
	Returns how many RAW is owned and how many have not yet been received by accounts list.
	"""
	data = {"action": "accounts_balances", "accounts" : accounts}
	return data

def accounts_create(wallet, count, work=True):
	"""
	Returns how many RAW is owned and how many have not yet been received by accounts list.
	(Optional) work Disables work generation after creating account.
	"""
	data = {"action": "accounts_create", "wallet" : wallet, "count" : count, "work" : work}
	return data

def accounts_frontiers(accounts):
	"""
	Returns a list of pairs of account and block hash representing the head block for accounts list.
	"""
	data = {"action": "accounts_frontiers", "accounts" : accounts}
	return data

def accounts_pending(accounts, count=1, threshold=None, source=False):
	"""
	Returns a list of block hashes which have not yet been received by these accounts
	"""
	data = {"action": "accounts_pending", "accounts" : accounts, "count": 1, "source" : source}
	if threshold is not None:
		data["threshold"] = threshold
	return data


