# In the book "Things to Make and Do in the Fourth Dimension: A Mathematician's Journey Through Narcissistic Numbers, Optimal Dating Algorithms, at Least Two Kinds of Infinity, and More"
# Matt Parker describes a bitmap function. He then explains
# how the binary can be translated to a number and gives a picture of
# a plot and the number... However this is not the actual number.
# Below I plot the number as it is.
from PIL import Image

# The number in the book as stated by some user called Ben Farrant as I am too poor to buy this book
nr = 4858485390999670448746903365089768368617710768834660012388173288524654178949978049944868710538516294877620353668483662935366626602594892897569165290588305741935268286384067811525624923136045761864695167648227909735247894905965266601185832734111836916088387799895732529972503459120508643887020302642994308338647923034771820182176605372325447019828390655784620186786800227025791813364831939280414817063175745207785502331527315365160190730899210873764484648366569393500481770411621586799225038123596991242202831343689507264087498985286559034507247

# To get to the bitmap (shortcut) we divide by 17, and obtain a black and white bitmap, alas the bitmap is
# bottom to top, left to right, so we'll have to correct for this
nr /= 17

# translate to binary string and remove 0b prefix
bmap = bin(nr)[2:]

# The image is going to range from 0 to 106 (107)
# and y from k to k + 17 (18)
# Note that it may start off by a number of zeros
if len(bmap) < 18 * 107:
    zeros = (18 * 107) - len(bmap)
    zeros = ("0" * zeros)
    bmap = zeros + bmap

assert len(bmap) == 18 * 107

# Image size is given by spec
img = Image.new("RGB", (107,18))

# to make our lives easy, let's use index i
i = 0

for x in range(107):
    for y in range(18):
        if bmap[i] == "0":
            # I like black as background colour
            colour = (0,0,0)
        else:
            # I like green as foreground colour
            colour = (50, 200, 50)
    
        img.putpixel((x, y), colour)
        i += 1

# scale to make it large enough to see
img = img.resize((107 * 150, 18 * 150))
img.save("outcome.png", "PNG")