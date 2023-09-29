""""Main module"""
from src.classes.atom import Atom

def main():
    """Enter point"""
    atom = Atom(26, 1.83)
    print(atom.get_eletronic_configuration())

if __name__ == "__main__":
    main()
