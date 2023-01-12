#!/usr/bin/python3
if __name__ == "__main__":
    import importlib
    def print_module_names(file_path):
        hidden_4 = importlib.import_module("hidden_4")

        names = dir(hidden_4)

        for name in names:
            if not name.startswith("__"):
                print(name)
