from fastapi import FastAPI
import hashlib

app = FastAPI()
app.debug = True
salt = b'da812bc264dcd2634cc8b24e77d4157c3a76844dd7a5496902249'


@app.get('/')
async def make_hash(message: str=''):
    """
    Given a string produces an integer hash up to 18 digits long.
    The string is hashed using SHA-1 with salt.

    :param message: Arbitrary sting to be hashed
    :return: integer up to 18 digits long
    """
    return int.from_bytes(hashlib.sha1(salt + message.encode('utf8')).digest(), 'big', signed=False) % 10**18
