def decode(data):
    ret = []
    for i in range(0, len(data)/2):
        ret.append(0b00000000);

        for p in range(0, 2):
            print(bin(data[i*2+p]));

            for j in range(0, 4):
                part = (data[i*2+p] >> (6-(j*2))) & 0b11
                if part == 0b10:
                    ret[i] = ret[i] | (1 << (j+(1-p)*4))
    return ret;
