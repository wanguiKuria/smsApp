
from flask import Flask, request, jsonify
from Crypto.Cipher import AES
import os

app = Flask(__name__)

# Encryption functions here

@app.route('/encrypt', methods=['POST'])
def encrypt_message():
    data = request.json.get('data').encode()
    key = generate_key()
    nonce, ciphertext, tag = encrypt(data, key)
    return jsonify({
        'key': key.hex(),
        'nonce': nonce.hex(),
        'ciphertext': ciphertext.hex(),
        'tag': tag.hex()
    })

@app.route('/decrypt', methods=['POST'])
def decrypt_message():
    key = bytes.fromhex(request.json.get('key'))
    nonce = bytes.fromhex(request.json.get('nonce'))
    ciphertext = bytes.fromhex(request.json.get('ciphertext'))
    tag = bytes.fromhex(request.json.get('tag'))
    data = decrypt(nonce, ciphertext, tag, key)
    return jsonify({'data': data.decode()})

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
