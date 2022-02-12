
A quick comparison between Protocol Buffers, Mic-E and uncompressed APRS
--------------------------------------------------------------------------

This is a small demo to compare packet lengths for a hypothetical
Protocol Buffers packet format with Mic-E and uncompressed APRS formats. The
compressed format is similar to Mic-E in length, but less obscure and more
precise for coordinates.

This is a demo to compare only the lengths of encoded packets, not an
argument that this would make any practical sense at this moment for APRS.
In some other setting, such as LoRa, this might be good.

The example packets contain coordinates, speed and course, no altitude, a
relatively short comment string (takes almost exactly the same amount of
space in all formats).

The Protocol Buffers encoding has more precision and range in all numeric
fields - latitude and longitude are 32-bit floating point.  Many Mic-E
packets out there transmit the !DAO! extension to improve precision
(Byonics TT3 at least do it), Kenwood doesn't. I included !DAO! in this
example to get more precision - a minimal packet without it would be 5 bytes
shorter.

To run this, on ubuntu/debian:

    sudo apt install python-protobuf protobuf-compiler
    protoc -I=. --python_out=. aprs.proto
    python3 test.py

The output you'd get:

    $ python3 test.py
    Protobuf: b'\n\x0f\rj\xa6pB\x15T\xae\xc1A\x18y \x8e\x02\x12\x02/>\x18\xef\xab\xa0\x90\x06R\x17Hessu, https://aprs.fi/'
    Len: 52
    Plain: b'@191500h6016.25N/02421.91E$270/052 Hessu, https://aprs.fi/!wPv!'
    Len: 63
    Mic-E: b'`w(mpSU>/\'"4.}Hessu, https://aprs.fi/!wbC!'
    Len: 42
    Mic-E with timestamp: b'@191500h`w(mpSU>/\'"4.}Hessu, https://aprs.fi/!wbC!'
    Len: 50


Hessu, OH7LZB/AF5QT

