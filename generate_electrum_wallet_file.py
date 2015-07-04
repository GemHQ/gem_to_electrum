#! /usr/bin/env python
from pprint import pprint as pp
from coinop.multiwallet import MultiWallet
from pycoin.key import Key
from argparse import ArgumentParser
from json import load, dump


# Have to monkeypatch this because the fix hasn't been released and coinop is
# pinned to v0.52 of pycoin. Blargh.
class FixedPyKey(Key):
    def as_text(self):
        if self.secret_exponent():
            return self.wif()
        sec_hex = self.sec_as_hex()
        if sec_hex:
            return sec_hex
        return self.address()

    def public_copy(self):
        if self.secret_exponent() is None:
            return self
        return FixedPyKey(public_pair=self.public_pair(), prefer_uncompressed=self._prefer_uncompressed,
                          is_compressed=(self._hash160_compressed is not None), netcode=self._netcode)


parser = ArgumentParser(
    description="Generate an multisig electrum-format wallet file")

parser.add_argument('-o', '--output_file', help="location for the electrum wallet")
parser.add_argument('seeds', nargs='+', help="your multisig wallet's xpubs, xprivs, or hex-encoded entropic seeds IN ORDER")
parser.add_argument('path_file', help="a file containing a pickled list of paths to derive")

args = parser.parse_args()

public = {}
private = {}
private_seeds = {}
for i, s in enumerate(args.seeds):
    if s[:4] == 'xpub':
        public[i] = s
    elif s[:4] == 'xprv':
        private[i] = s
    else:
        private_seeds[i] = s

wallet = MultiWallet(public=public, private=private, private_seeds=private_seeds)

with open(args.path_file, 'r') as f:
    paths = load(f)

for path in paths:
    node = wallet.path(path['path'])
    path['private'] = node.private_keys
    path['public'] = node.public_keys
    path['output_format'] = []
    for n in sorted(path['public'].keys()):
        if n in path['private']:
            path['output_format'].append(
                FixedPyKey(
                    secret_exponent=path['private'][n].key.privkey.secret_multiplier
                ).sec_as_hex())
        else:
            path['output_format'].append(
                FixedPyKey(public_pair=(path['public'][n].key.pubkey.point.x(),
                                        path['public'][n].key.pubkey.point.y())
                ).sec_as_hex())

# m/a/c/i
output = {
    "accounts": {
        "0": {
            "receiving": [ p['output_format'] for p in paths ],
            "xpub": "xpub",
            "xpub2": "xpub",
            "xpub3": "xpub"
        }
    },
    "master_private_keys": {
    },
    "master_public_keys": {
        "x1/": "xpub",
        "x2/": "xpub",
        "x3/": "xpub"
    },
    "use_encryption": False,
    "wallet_type": "2of3"
}

with open(args.output_file, 'w') as f:
    dump(output, f)
