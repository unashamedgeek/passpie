import gnupg


def generate_key_input(path, passphrase):
    return gnupg.GPG(homedir=path).gen_key_input(
        name_real="Pysswords",
        name_email="pysswords@pysswords",
        name_comment="Auto-generated by Pysswords",
        key_length=4096,
        expire_date=0,
        passphrase=passphrase)


def getgpg(path):
    return gnupg.GPG(homedir=path)


def generate_keys(path, key_input):
    key = gnupg.GPG(homedir=path).gen_key(key_input)
    return key


def create_keyring(path, passphrase):
    key_input = generate_key_input(path, passphrase)
    generate_keys(path, key_input)
    return path


def is_encrypted(data):
    if data.startswith("-----BEGIN PGP MESSAGE-----"):
        return True
    else:
        return False
