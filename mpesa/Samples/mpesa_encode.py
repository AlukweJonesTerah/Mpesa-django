import keys
import base64


def generate_password(formatted_time):
    # creating passwords
    """ mpesa passwords are created by combining business_shortCode, passkey and timestamp"""
    # combining characters to create the password into base64
    data_to_encode = keys.business_shortCode + keys.lipa_na_mpesa_passkey + formatted_time
    # converting the data_to_encode to base64 encryption
    # (.encode function first coverts the data_to_encode to bytes UTF8 format)
    # this is to avoid TypeError: a bytes-like object is required, not 'str'
    encoded_string = base64.b64encode(data_to_encode.encode())
    print(encoded_string)
    # decoding the result from binary to string in utf8 formt
    decoded_password = encoded_string.decode('utf-8')
    print(decoded_password)

    return decoded_password
