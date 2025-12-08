#!/usr/bin/python3
import marshal
import types

def main():
    # Load the compiled .pyc file
    with open("/tmp/hidden_4.pyc", "rb") as f:
        f.read(16)  # Skip header
        code = marshal.load(f)

    # Convert code to executable module
    module = types.ModuleType("hidden_4")
    exec(code, module.__dict__)

    # Print names in the module excluding __
    for name in sorted([n for n in dir(module) if not n.startswith("__")]):
        print(name)

if __name__ == "__main__":
    main()
