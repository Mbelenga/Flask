class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight


def main():
    packages = [
        Package(number=1, sender="Mali", recipient="Baraka", weight="10"),
        Package(number=2, sender="James", recipient="Mwangi", weight="5")
    ]
    for package in packages:
        print(f"Package {package.number}: {package.sender} to {package.recipient}, {package.weight}kg")

main()
