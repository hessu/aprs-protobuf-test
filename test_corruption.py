
import time
import random
import aprs_pb2

# Create a protobuf message, assign values to the fields
m = aprs_pb2.APRSMessage()
m.position.latitude = 60.162512
m.position.longitude = 24.210122
m.position.speed = 121
m.position.course = 270
m.timestamp = int(time.time())
m.comment = "Hessu, https://aprs.fi/"
m.symbol = "/>"

# Look, this is the whole packet encoder you need to write!
b = m.SerializeToString()

print(f"Protobuf: {b}")
print(f"Len: {len(b)}\n")

# Corrupt a random byte in the message
b = bytearray(b)
b[random.randint(0, len(b)-1)] = random.randint(0, 255)

# Remove a random byte in the message
#i = random.randint(0, len(b)-1)
#b = b[0:i] + b[i+1:]

# Truncate from random point
#i = random.randint(0, len(b)-1)
#b = b[0:i]

# Try to decode, handle errors:
decoded = aprs_pb2.APRSMessage()
try:
    decoded.ParseFromString(b)
    print("Decoded: %r" % decoded)
except Exception as ex:
    print("Failed to decode: %s" % ex)

