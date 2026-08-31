orig = open(r"Q:\Dos_G\StarControl2\uqm-work\extracted\base\base\comm\commander\commander.txt", "rb").read()
new = open(r"Q:\Dos_G\StarControl2\uqm-work\zh-TW-addon\content\base\comm\commander\commander.txt", "rb").read()

def first_hdr(data):
    for line in data.split(b"\n"):
        if line.startswith(b"#("):
            return line
    return b""

oh = first_hdr(orig)
nh = first_hdr(new)
print("Orig header:", oh[:60])
print("  hex     :", oh[:60].hex(" "))
print()
print("New  header:", nh[:60])
print("  hex     :", nh[:60].hex(" "))
print()
tab_marker = b")\t"
sp_marker = b") "
print(f"Orig has TAB after )?: {tab_marker in oh}")
print(f"Orig has SP  after )?: {sp_marker in oh}")
print(f"New  has TAB after )?: {tab_marker in nh}")
print(f"New  has SP  after )?: {sp_marker in nh}")
