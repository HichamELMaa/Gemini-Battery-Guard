import os
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]

# 1. Load secrets immediately
load_dotenv()

#2. get the key
mykey = os.getenv("GEMINI_API_KEY")

print(mykey[:4])