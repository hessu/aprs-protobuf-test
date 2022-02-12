
import time
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
print(f"Len: {len(b)}")

# timestamp, uncompressed position, speed/course, comment, !DAO! for additional precision
uncompr = f"@191500h6016.25N/02421.91E$270/052 Hessu, https://aprs.fi/!wPv!".encode("ascii")
print(f"Plain: {uncompr}")
print(f"Len: {len(uncompr)}")

# a typical mic-e packet, with the same comment and !DAO!
mic_e = "`w(mpSU>/'\"4.}Hessu, https://aprs.fi/!wbC!".encode("ascii")
print(f"Mic-E: {mic_e}")
print(f"Len: {len(mic_e)}")

# Add a timestamp, because it's present in the other formats
mic_e_ts = "@191500h`w(mpSU>/'\"4.}Hessu, https://aprs.fi/!wbC!".encode("ascii")
print(f"Mic-E with timestamp: {mic_e_ts}")
print(f"Len: {len(mic_e_ts)}")
