import slowclap as sc
import requests

def getActivated(headers):
	resp = requests.get("http://projects.danjscott.co.uk/intheroom/isActivated", headers=headers)
	if resp.status_code == 200:
		return True;
	else:
		return False;


deactivateUrl = "http://projects.danjscott.co.uk/intheroom/Deactivate"

activateUrl = "http://projects.danjscott.co.uk/intheroom/Activate"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYWRtaW4iLCJwYXNzIjoiYWRtaW4iLCJpYXQiOjE1NTQzMzE3NDYsImV4cCI6MS4wMDAwMDAwMDAwMDE1NTQ1ZSsyMX0.qzxBdYfCGxcvQkhaCBsKiC7DVVG0wOZMe68axjw0x5M"
headers = {'x-access-token': token}

activated = getActivated(headers)




if __name__ == '__main__':
	if (activated):
		print("Started - Currently set to Activated")
	else:
		print("Started - Currently set to Deactivated")

	while (True):
		print("Awaiting Clap...")
		feed = sc.MicrophoneFeed()
		detector = sc.AmplitudeDetector(feed, threshold=15000000)
		for clap in detector:
			print("Clap Detected")
			if (activated):
				resp = requests.put(deactivateUrl, headers=headers)
				if resp.status_code == 200:
					print("PyBot Deactivated")
					activated = False;
				else:
					print("PyBot Deactivated FAILED")


			else:
				resp = requests.put(activateUrl, headers=headers)
				if resp.status_code == 200:
					print("PyBot Activated")
					activated = True;
				else:
					print("PyBot Activated FAILED")

			break;

