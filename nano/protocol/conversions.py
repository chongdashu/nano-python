import json

def rai_from_raw(amount):
	"""
	Divide a raw amount down by the rai ratio.
	"""
	data = {"action": "rai_from_raw", "amount" : amount}
	return data

def rai_to_raw(amount):
	"""
	Multiply an rai amount by the rai ratio.
	"""
	data = {"action": "rai_to_raw", "amount" : amount}
	return data


def mrai_from_raw(amount):
	"""
	Divide a raw amount down by the Mrai ratio.
	"""
	data = {"action": "mrai_from_raw", "amount" : amount}
	return data

def mrai_to_raw(amount):
	"""
	Multiply an Mrai amount by the Mrai ratio.
	"""
	data = {"action": "mrai_to_raw", "amount" : amount}
	return data