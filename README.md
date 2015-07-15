# Gem-to-Electrum export utility


### Usage:
A paths file is included in this repo for testing, the path/address pairs in that file correspond to the pubkeys in the follow command: (order matters: backup, cosigner, primary)

    ./generate_electrum_wallet_file.py -o ~/.electrum/wallets/gem_test_wallet xprv9s21ZrQH143K4AKEig6sgeivfyvxHJAJwiiGEaM3SFJ8f8kHhAHytXf2Bjc4RTnFA485wD9J8oFpL4vQzEdRWzSBfzt9pjmXggbgDcpKJXG xpub661MyMwAqRbcGpiVi7tkzQsVQZJhZJgyhEZwaAb6CXmdw9U6gEJLvUPUv7Jq5e2pjNJFXfXyCqgkeTDC88Nu4Gp1BhMNWCugPM5LvPqdKvo xprv9s21ZrQH143K4KmtH6LSKyDEkwsRqeAUF5ELX7zoC2kGLA579un52gqRiwyANoks24dH9YuzAGGbPhzipF4dZcchcMcuSwSLLncJqFYRq7s paths


NOTE: the below assumes you're working off of the Gem electrum fork which adds support for imported p2sh addresses: [GemHQ/electrum (rev: jbok-multisig)](https://github.com/GemHQ/electrum/tree/jbok_multisig)
This will put a `gem_test_wallet` file in your electrum wallets path (assuming it exists). You can verify electrum is loading the addresses correctly by running this command, from your electrum directory:

    ./electrum -o -w ~/.electrum/wallets/gem_test_wallet listaddresses

The addresses it outputs should match those in the paths file:

    [{"path": "m/44/0/0/0/0", "string": "3JL83qWAa4DfYVcwYB6DuoQYP2JvPUDDMq"}]

You can create a transaction and get the raw hex with this command (which assumes no one has taken these coins):

    ./electrum -o -v payto 1PLDBvZkxVxb9kdZJxfE7L2kPw5AWPtSbN 0.0001

To view/verify the tx in a readable format add the -d flag:

    ./electrum -o -v -d payto 1PLDBvZkxVxb9kdZJxfE7L2kPw5AWPtSbN 0.0001

You can confirm signatures are correct with `tx -a [HEX_FROM_ABOVE]`

If your electrum is synced (possibly syncing is broken for the new Imported_Wallet?), you can broadcast with `--broadcast`. This is untested, because my electrum was just hanging during the syncing process and I got impatient -- but it's not a deal-breaker even if it's broken, since you can just sendrawtransaction from any bitcoind interface or etc.

    ./electrum --broadcast payto 1PLDBvZkxVxb9kdZJxfE7L2kPw5AWPtSbN 0.0001
