import sys
sys.path.append(r"C:/Users/hp/Desktop/campusCredentialsNotes/pythonday4")
from oops import microWave
usha = microWave("usha","3","333")
print(usha.brandName)
print(usha.turnedOn())
usha.run(30)
bosch = microWave("bosch","2","324")
print(usha+bosch)
print(usha)
print(repr(usha))