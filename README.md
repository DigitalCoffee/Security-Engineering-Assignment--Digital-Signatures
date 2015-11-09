# Security Engineering Assignment: Digital Signatures
Assignment 1 for UVic's Security Engineering course (SENG360)
This assignment was intended to teach students how license files are created and verified through digital signatures.

##Setup
These scripts run on Python 2.7.
You will need a public and private RSA key pair saved in the same directory as the scripts named pubkey.der and privkey.der, respectively.
Go here to quickly get a keypair: http://travistidwell.com/jsencrypt/demo/

First run GenerateLicense.py. This will create the license file.
The license file contains the current date (timestamp), the public key needed to verify the license, and the digital signature itself.
Run Validate.py to verify that the license is valid.

You can test that the validation fails when the license file has been edited/corrupted. Pass in any of the following arguments to GenerateLicense.py:

* **-c**: Adds random bits to the digital signature. This simulates corruption.

* **-t**: Changes the date in the timestamp. Simulates tampering with the license's message.
