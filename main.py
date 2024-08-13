
from dotenv import load_dotenv
import os
load_dotenv()  # loads the configs from .env

print("hello world")
print("Foo: {}".format(os.getenv('FOO')))
