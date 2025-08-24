# requirements.py
"""
This file lists the required Python packages for Interactive Learning System.
Run this file to print the requirements for use in requirements.txt.
"""

REQUIREMENTS = [
    "torch",
    "transformers",
    "sentence-transformers",
    "numpy",
    "networkx",
    "scikit-learn",
    "nltk",
    "psutil",
    "PyYAML",
    "aiohttp",
    "beautifulsoup4",
    "gymnasium",
    "matplotlib"
]

def print_requirements():
    for req in REQUIREMENTS:
        print(req)

if __name__ == "__main__":
    print_requirements()
