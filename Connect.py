import OpenSSL.crypto as crypto

expected_name = "20331A0564ADMIN.AWS"

with open('domainCA.crt', 'rb') as cert_file:
    cert_data = cert_file.read()

cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_data)

subject_name = cert.get_subject().commonName

if subject_name == expected_name:
    print("connection secure")
else:
    print("ERROR: certificate does not match expected name")
