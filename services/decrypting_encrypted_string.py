import base64


def decrypting_encrypted_string(encrypted_string:str):
    decoded_bytes = base64.b64decode(encrypted_string)
    decoded_string = decoded_bytes.decode('utf-8')
    list_decoded = list(decoded_string.split(','))
    return list_decoded