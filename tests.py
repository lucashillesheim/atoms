""""Main module"""
from src.classes.atom import Atom

def main():
    """Enter point"""
    atom = Atom(75)
    expected = str("{\"K\": {\"S\": 2}, \"L\": {\"S\": 2, \"P\": 6}, \"M\": {\"S\": 2, \"P\": 6, \"D\": 10}, \"N\": {\"S\": 2, \"P\": 6, \"D\": 10, \"F\": 14}, \"O\": {\"S\": 2, \"P\": 6, \"D\": 5}, \"P\": {\"S\": 2}}")
    actual = str(atom.get_eletronic_configuration())
    print(expected == actual)

if __name__ == "__main__":
    main()