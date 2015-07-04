# Gem-to-Electrum export utility


### Usage:
A paths file is included in this repo for testing, the path/address pairs in that file correspond to the pubkeys in the follow command: (order matters: backup, cosigner, primary)

    ./generate_electrum_wallet_file.py -o ~/.electrum/wallets/gem_test_wallet xpub661MyMwAqRbcEqhjb6Hrj3QETJw59gLqRMvF4t8RHqQu5K3YNQ4jvYEucc66mP8UavH4upK4WCoyUM3t1F1nQRAQgB8nqNWVNcYJKRksXbe xpub661MyMwAqRbcGpiVi7tkzQsVQZJhZJgyhEZwaAb6CXmdw9U6gEJLvUPUv7Jq5e2pjNJFXfXyCqgkeTDC88Nu4Gp1BhMNWCugPM5LvPqdKvo xpub661MyMwAqRbcFBRHkmk4YyVZcf5qoMe5CRvEqTNzDNriz4T8j6ETuhydhuvrmEusqiQUsAp6yB4YppuB4YmnDzqtWC49iqBdM7Kc6c2PjX9 paths

This will put a `gem_test_wallet` file in your electrum wallets path (assuming it exists). You can verify electrum is loading the addresses correctly by running this command, from your electrum directory:

    ./electrum -o -w ~/.electrum/wallets/gem_test_wallet listaddresses

The addresses it outputs should match those in the paths file: (it doesn't right now)

    [{"path": "m/44/0/0/0/0", "string": "34gRcJbgzZsCnZP1Swt5DxL2m8UTMCHayv"},
     {"path": "m/44/0/1/0/0", "string": "3CWiyGDchREmsXYAKWEhYtoHt4DQeKfHPs"},
     {"path": "m/44/0/1/0/1", "string": "35PLtwgZ3qgFHmTzfJZm4oywSYMcbqiJsa"},
     {"path": "m/44/0/1/0/2", "string": "3JjR1GGE6BQnemoGCg9X7pmD8aqhYvmwMH"}]
