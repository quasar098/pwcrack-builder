from PIL import Image
import binascii


with open("./example/beemovie.txt") as f:
    TO_ENCODE = f.read()


def h2i(_):
    return binascii.unhexlify(_).decode('ascii')


hexed_text = binascii.hexlify(TO_ENCODE.encode("ascii")).decode("ascii")
while int(len(hexed_text)/2) % 3 != 0:
    hexed_text += "03"
while pow(int(len(hexed_text)/2) // 3, 0.5) != int(pow(int(len(hexed_text)/2) // 3, 0.5)):
    hexed_text += "030303"

pixels = []
for group_index in range(int(len(hexed_text)/6)):
    color = hexed_text[:6]
    rh, gh, bh = color[:2], color[2:4], color[4:]
    pixels.append(tuple([ord(h2i(_2)) for _2 in (rh, gh, bh)]))
    hexed_text = hexed_text[6:]
# not the best way to do this but whatever
factors = []
for _ in range(1, len(pixels)+1):
    factors.append(_) if len(pixels) % _ == 0 else None
middle_lower = factors[int(len(factors)/2)-1] if len(factors) % 2 == 0 else factors[int(len(factors)/2)]
middle_upper = factors[int(len(factors)/2)]

newimage = Image.new(mode="RGB", size=(middle_upper, middle_lower))
for index, pixel in enumerate(pixels):
    x = index % middle_upper
    y = index // middle_upper
    newimage.putpixel((x, y), pixel)
newimage.show()
