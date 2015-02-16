# Cythera CLUT in python array format provided by Chris Pickel,
# sfiera@sfzmail.com
html = [
    'ffffff', '0000a8', '00a800', '00a8a8', 
    'a80000', 'a800a8', 'a85400', 'a8a8a8', 
    '545454', '5454fc', '54fc54', '54fcfc', 
    'fc5454', 'fc54fc', 'fcfc54', 'fcfcfc',
    'fcfcfc', 'ececec', 'd8d8d8', 'c8c8c8', 
    'b8b8b8', 'a8a8a8', '989898', '848484', 
    '747474', '646464', '545454', '444444', 
    '343434', '202020', '101010', '080808',
    'fcf400', 'f8c800', 'f4a400', 'ec8000', 
    'e86000', 'e44000', 'e02000', 'dc0000', 
    'c80000', 'b40000', 'a00000', '8c0000', 
    '7c0000', '680000', '540000', '400000',
    'fcfcfc', 'fcf4c0', 'fcec84', 'fce448', 
    'fcdc38', 'fcd024', 'fcc814', 'fcb800', 
    'e89000', 'd07000', 'bc5400', 'a83c00', 
    '942800', '7c1800', '680800', '540000',
    'e8905c', 'dc7848', 'd0603c', 'c04c2c', 
    'b4381c', 'a82414', '9c1008', '900000', 
    '800000', '6c0000', '5c0000', '480000', 
    '380000', '240000', '100000', '000000',
    'f8fcd8', 'f4fcb8', 'e8fc9c', 'e0fc7c', 
    'd0fc5c', 'c4fc40', 'b4fc20', 'a0fc00', 
    '90e400', '80cc00', '74b400', '609c00', 
    '508400', '447000', '345800', '284000',
    'd8fcd8', 'bcfcb8', '9cfc9c', '80fc7c', 
    '60fc5c', '40fc40', '20fc20', '00fc00', 
    '00e400', '04cc00', '04b400', '049c00', 
    '088400', '047000', '045800', '044000',
    'd8ecfc', 'b8dcfc', '9cd0fc', '7cbcfc', 
    '5cacfc', '4094fc', '2084fc', '0070fc', 
    '0068e4', '005ccc', '0058b4', '00509c', 
    '004484', '003c70', '003058', '002440',
    'fcc87c', 'f0b870', 'e8a868', 'dc9c60', 
    'd09058', 'c88450', 'bc784c', 'b46c44', 
    'a0643c', '906034', '80542c', '6c4c24', 
    '5c401c', '483818', '382c10', '28200c',
    'fcd8fc', 'fcb8fc', 'fc9cfc', 'fc7cfc', 
    'fc5cfc', 'fc40fc', 'fc20fc', 'fc00fc', 
    'e000e4', 'c800cc', 'b400b4', '9c009c', 
    '840084', '6c0070', '580058', '400040',
    'fce8dc', 'fce0d0', 'fcd8c4', 'fcd4bc', 
    'fcccb0', 'fcc4a4', 'fcbc9c', 'fcb890', 
    'e8a47c', 'd0946c', 'bc8458', 'a8744c', 
    '94643c', '805830', '684824', '543c1c',
    'fce8dc', 'f4c8b4', 'e8b090', 'e09470', 
    'd47850', 'cc6034', 'c44818', 'bc3400', 
    'a82800', '981c00', '881400', '781000', 
    '680800', '580400', '480000', '380000',
    'fcf46c', 'f0f060', 'dce454', 'ccdc48', 
    'b8d040', 'a8c434', '94b82c', '84b024', 
    '749820', '64841c', '506c14', '405810', 
    '30400c', '202c08', '101404', '000000',
    'fcfcfc', 'e8e8f0', 'd4d4e8', 'c0c4dc', 
    'b4b4d0', 'a0a0c8', '9494bc', '8484b4', 
    '74749c', '646484', '505470', '404058', 
    '303044', '20202c', '101018', '000000',
    'fc0000', 'fc1c00', 'fc4000', 'fc6000', 
    'fc7c00', 'fc9800', 'fcbc00', 'fcdc00', 
    '0010fc', '1028fc', '1c44fc', '2c5cfc', 
    '3874fc', '4484fc', '5498fc', '60a8fc',
    'd02094', 'dc34c0', 'ec48e8', 'ec60fc', 
    '704820', '84542c', '9c6038', 'b46c44', 
    '24a800', '1cbc00', '10d000', '00e400', 
    '000000', '000000', 'fcf4c0', '000000',
]
rgb = [[int(c[:2],16), int(c[2:4],16), int(c[4:],16)
    ] for c in html]
rgb24 = [(r<<16)|(g<<8)|b for r,g,b in rgb]

idx_rgb24 = {rgb24value: idx for idx,rgb24value in enumerate(rgb24)}

def colormatch_rgb24(color):
    return idx_rgb24.get(color, closest_color(rgb,
        (color&0xFF0000)>>16,
        (color&0x00FF00)>>8,
        (color&0x0000FF)))

def closest_color(pal, r,g,b,starts=0x10,ends=0xE0):
    best = 0
    best_distance = 2048
    idx = starts
    for rc,gc,bc in pal[starts:ends]:
        distance = abs(r-rc)+abs(b-bc)+abs(g-gc)
        if distance < best_distance:
            best = idx; best_distance = distance
        idx += 1
    return best
            
        

pil = []
for c in rgb: pil.extend(c)

