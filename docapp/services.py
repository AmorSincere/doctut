from uuid import uuid4


def gen_code():
    kode = str(uuid4()).replace("-", "")
    return kode
