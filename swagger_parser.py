from prance import ResolvingParser

if __name__ == "__main__":
    parser = ResolvingParser("./swagger.yaml")
    print(parser.specification)  # contains fully resolved specs as a dict
