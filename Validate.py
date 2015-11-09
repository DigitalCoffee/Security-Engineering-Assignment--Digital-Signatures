from sys import exit
import re
from datetime import date, datetime
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

key = ""
expDate = ""

# Open license file
try:
    license = open('license').read()
except:
    print "License file not found"
    exit(0)

# Check expiration date, exit if expired or does not exist
dateMatch = re.search(r'(?<=EXP_DATE:\n)\d{4}-\d{2}-\d{2}', license)
if dateMatch:
    expDate = dateMatch.group()
    if datetime.strptime(expDate, '%Y-%m-%d').date() < date.today():
        print "Invalid license: expired"
        exit(0)
else:
    exit(0)

# Find the public key, exit if it does not exist
keyMatch = re.search(r'(?<=KEY:\n)-----BEGIN PUBLIC KEY-----.+-----END PUBLIC KEY-----', license, flags=re.DOTALL)
if keyMatch:
    key = RSA.importKey(keyMatch.group())
else:
    exit(0)

sigMatch = re.search(r'(?<=SIGNATURE:\n).+', license, flags=re.DOTALL)
if sigMatch:
    signature = sigMatch.group()
else:
    exit(0)
# Generate hash of the license
hashLcn = SHA.new(expDate)

# Create verification object using the public key
verifier = PKCS1_v1_5.new(key)

# Verify
if verifier.verify(hashLcn, signature):
    print "License accepted"
    print "Hello World!"
    exit(0)
else:
    print "Invalid license: integrity check failed"
    exit(1)