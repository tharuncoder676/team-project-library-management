"""Library Management System - application entry point.

Each team member develops one module on their own branch. A module is
activated by registering its name in the MODULES list below.
"""

MODULES = [
    "core",
    "auth",
]


def load_modules():
    """Load every registered module in order."""
    for name in MODULES:
        print(f"  loading module: {name}")


if __name__ == "__main__":
    print("Library Management System v0.1")
    load_modules()
    print(f"{len(MODULES)} module(s) active")
