#Program to Convert String in to Byte Stream and Vice Versa
#Strings : Sequence of unicode characters
#Bytes : Sequence of Raw 8 Bit Values

#Encoding the String to Bytes
String = "Ramesh - Software Engineer (Google)"
Byte_Stream = String.encode(encoding="utf-32")
print(Byte_Stream)

#Decoding the Bytes to String
String_Stream = Byte_Stream.decode(encoding="utf-32")
print(String_Stream)
print(String == String_Stream)