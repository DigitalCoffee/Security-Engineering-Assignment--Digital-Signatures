from sys import exit, argv
import getopt
from datetime import date, timedelta
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Random import random

usage = "GenerateLicense.py {-c|-t}"
corruption = ""
addDays = 30

try:
	opts, args = getopt.getopt(argv[1:],"ct")
except getopt.GetoptError:
	print usage
	exit(1)
for opt, arg in opts:
	if opt in ("-c"):
		corruption = str(random.getrandbits(19))
	elif opt in ("-t"):
		addDays = random.randint(-100, -1)


# ---- Begin message generation ----


# Make the license expire in 30 days
expDate     = date.today() + timedelta(days=addDays)

# Include public key to decrypt signature
publicKey   = open('pubkey.der').read()

# Message body
licenseStr  = "EXP_DATE:\n" + str(expDate) + "\nKEY:\n" + publicKey + "\n"

# Write the expiry date + "vendor's" public key
license     = open("license", 'w+')
license.write(licenseStr)


# ---- Begin digital signature generation ----


# Import private key
key         = RSA.importKey(open('privkey.der').read())

# Hash the message
hash        = SHA.new(str(expDate) + corruption)

# Create signer and sign the hash
signer      = PKCS1_v1_5.new(key)
signature   = signer.sign(hash)

# Write the digital signature
license.write("SIGNATURE:\n" + signature)