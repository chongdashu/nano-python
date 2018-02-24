import random, json, requests

def is_xrb_address(address):
	return address.startswith("xrb_")

def bool_to_string(bool):
	return str(bool).lower()

def request(data):
	try:
		r = requests.post("http://localhost:7076", data = json.dumps(data)) 
		print(r.status_code, r.reason)
		print (r.text)
		return r.text
	
	except requests.exceptions.HTTPError as errh:
		print ("HTTPError")
		print (errh)
		return "HTTP Error"
	except requests.exceptions.ConnectionError as errc:
		print ("ConnectionError")
		print (errc)
		return "Connection Error"
	except requests.exceptions.Timeout as errt:
		print ("Timeout")
		print (errt)
		return "Timeout Error"
	except requests.exceptions.RequestException as err:
		print ("Generic Server Error")
		print (err)
		return "Server Error"

def from_json(data):
	return json.loads(data)

if __name__ == "__main__":
	pass