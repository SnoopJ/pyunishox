from pyunishox import compress, decompress

s = "おはようございます！"
payload = s.encode("utf-8")

print(f"Compressing payload: {s}...")
c = compress(payload)
print(f"Result: {c}")

print("Decompressing...")
d = decompress(c)
print(f"Result: {d.decode('utf-8')}")
