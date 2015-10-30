import base64

bits = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

def encode(txt):
    return base64.b64encode(txt, bits)
