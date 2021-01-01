DATA_FILE = './data/day25.txt'


def cryptographic_handshake(subject, loop_size):
    input = 1
    for _ in range(loop_size):
        input = transform(input, subject)
    return input


def transform(input, subject):
    return (input * subject) % 20201227


def get_cryptographic_pairs(public_keys):
    pairs = []
    loop_size = 1
    product = 1
    while len(pairs) != len(public_keys):
        product = transform(product, 7)
        try:
            index = public_keys.index(product)
            pairs.append((public_keys[index], loop_size))
        except ValueError:
            pass
        loop_size += 1
    return pairs


def get_encryption_key(pairs):
    first_public_key, first_loop_size = pairs[0]
    second_public_key, second_loop_size = pairs[1]

    encryption_key = cryptographic_handshake(first_public_key, second_loop_size)
    if encryption_key != cryptographic_handshake(second_public_key, first_loop_size):
        raise Exception('Encryption keys do not match')

    return encryption_key


with open(DATA_FILE) as file:
    lines = file.readlines()

    public_keys = [int(line.rstrip()) for line in lines]
    cryptographic_pairs = get_cryptographic_pairs(public_keys)
    encryption_key = get_encryption_key(cryptographic_pairs)
    print(f'encryption_key: {encryption_key}')
