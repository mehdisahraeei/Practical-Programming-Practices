import hashlib

input_ = "Hey"


md5_hash = hashlib.md5()
md5_hash.update(input_.encode())
md5_hex = md5_hash.hexdigest()



print(md5_hex)

