import string
import collections


def caesar(rotate_string, number_to_rotate_by):
	
	upper = collections.deque(string.ascii_uppercase)
	lower = collections.deque(string.ascii_lowercase)

	upper.rotate(number_to_rotate_by)
	lower.rotate(number_to_rotate_by)

	upper = ''.join(list(upper))
	lower = ''.join(list(lower))

	return rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))

print("Welcome to Kode Byter!")

print("Press Ctrl+C at any time to exit")

print("Press Ctrl+Shift+C to copy")

print("Press Ctrl+Shift+V to paste")

print("Will exit in 5")

print("Enter message:")
message = raw_input()

print("Enter rotation:")
rotation = raw_input()

print str(rotation)
print caesar(message, int(rotation))

print("Will exit in 4")

print("Enter message:")
message = raw_input()

print("Enter rotation:")
rotation = raw_input()

print str(rotation)
print caesar(message, int(rotation))

print("Will exit in 3")

print("Enter message:")
message = raw_input()

print("Enter rotation:")
rotation = raw_input()

print str(rotation)
print caesar(message, int(rotation))

print("Will exit in 2")

print("Enter message:")
message = raw_input()

print("Enter rotation:")
rotation = raw_input()

print str(rotation)
print caesar(message, int(rotation))

print("Will exit in 1")

print("Enter message:")
message = raw_input()

print("Enter rotation:")
rotation = raw_input()

print str(rotation)
print caesar(message, int(rotation))

print("Will exit in 0")

print("Press enter to exit...")
exit = raw_input()