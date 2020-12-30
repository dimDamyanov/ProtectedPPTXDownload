from binascii import a2b_base64

data = ['']

for ind, uri in enumerate(data):
    uri = uri[uri.find(',')+1:]
    print(uri)
    binary = a2b_base64(uri)
    with open(f'img{ind+1}.png', 'wb') as outfile:
        outfile.write(binary)