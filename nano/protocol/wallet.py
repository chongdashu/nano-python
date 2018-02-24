import json

"""
Based on the official Nano protocol:
https://github.com/nanocurrency/raiblocks/wiki/RPC-protocol#account-balance

Date: 22-Feb 2018 02:59 GMT+8
"""

def wallet_create():
	"""
	Creates a new random wallet id.
	"""
	data = {"action": "wallet_create"}
	return data

def wallet_destroy(wallet):
	"""
	Destroys wallet and all contained accounts.
	"""
	data = {"action": "wallet_destroy", "wallet": wallet}
	return data

def wallet_export(wallet):
	"""
	Destroys wallet and all contained accounts.
	"""
	data = {"action": "wallet_export", "wallet": wallet}
	return data

def wallet_frontiers(wallet):
	"""
	Returns a list of pairs of account and block hash representing the head block starting for accounts from wallet
	"""
	data = {"action": "wallet_frontiers", "wallet": wallet}
	return 

def wallet_pending(wallet, count, threshold=None, source=None):
	"""
	Returns a list of block hashes which have not yet been received by accounts in this wallet.
	(Optional) Returns a list of pending block hashes with amount more or equal to threshold
	(Optional) Returns a list of pending block hashes with amount and source accounts
	"""
	data = {"action": "wallet_pending", "wallet": wallet, "count": count}

	if threshold is not None:
		data["threshold"] = str(threshold)

	if source is not None:
		data["source"] = str(source).lower()
		
	return data


def wallet_republish(wallet, count):
	"""
	Rebroadcast blocks starting at hash to the network.
	"""
	data = {"action": "wallet_republish", "wallet": wallet, "count": count}
	return data

def wallet_work_get(wallet):
	"""
	Retrieves work for account in wallet.
	"""
	data = {"action": "wallet_republish", "wallet": wallet}
	return data

def wallet_password_change(wallet, password):
	"""
	Changes the password for wallet to password.
	"""
	data = {"action": "password_change", "wallet": wallet, "password": password}
	return data

def wallet_password_enter(wallet, password):
	"""
	Enters the password in to wallet.
	"""
	data = {"action": "password_enter", "wallet": wallet, "password": password}
	return 


def wallet_password_valid(wallet):
	"""
	Checks whether the password entered for wallet is valid.
	"""
	data = {"action": "password_valid", "wallet": wallet}
	return data

def wallet_locked(wallet):
	"""
	Checks whether wallet is locked.
	"""
	data = {"action": "wallet_locked", "wallet": wallet}
	return data


