import pprint

with open("input2", "r") as f:
    hex = f.read().strip()

# hex = "9C0141080250320F1802104A08"  # this returns 1 as expected (1 + 3 == 2 * 2)
b = bin(int(hex, 16))[2:].zfill(len(hex) * 4)  # binary string, fill with 0s

version_count = 0


# p is the position in the binary
def read_packet(p):
    packet = {}
    packet["v"] = int(b[p: p + 3], 2)
    p += 3
    global version_count
    version_count += packet["v"]

    packet["t"] = int(b[p: p + 3], 2)
    p += 3

    # if literal value
    if packet["t"] == 4:
        packet["bval"] = []
        while int(b[p]):
            packet["bval"].append(b[p + 1: p + 5])
            p += 5
        # once more for final value:
        packet["bval"].append(b[p + 1: p + 5])
        p += 5

        # join binary values into one number
        packet["val"] = int(''.join(packet["bval"]), 2)

    # not a literal value
    else:
        packet['i'] = b[p]
        p += 1

        packet['subs'] = []
        # if length id is 15 or 11
        if packet['i'] == "1":
            packet['p_count'] = int(b[p:p + 11], 2)
            p += 11
            for _ in range(packet['p_count']):
                sub_pack, p = read_packet(p)
                packet['subs'].append(sub_pack)
        else:
            packet['length'] = int(b[p:p + 15], 2)
            p += 15
            packet_end = p + packet['length']

            # while not reached end, crawl sub packages
            while p < packet_end:
                sub_pack, p = read_packet(p)
                packet['subs'].append(sub_pack)

        sub_vals = [pack["val"] for pack in packet["subs"]]

        if packet["t"] == 0:
            packet["val"] = sum(sub_vals)
        elif packet["t"] == 1:
            prod_value = 1
            for val in sub_vals:
                prod_value *= val
            packet["val"] = prod_value
        elif packet["t"] == 2:
                packet["val"] = min(sub_vals)
        elif packet["t"] == 3:
                packet["val"] = max(sub_vals)
        elif packet["t"] == 5:
                packet["val"] = (0, 1)[sub_vals[0] > sub_vals[1]]
        elif packet["t"] == 6:
                packet["val"] = (0, 1)[sub_vals[0] < sub_vals[1]]
        elif packet["t"] == 7:
                packet["val"] = (0, 1)[sub_vals[0] == sub_vals[1]]

    return packet, p


packet, _ = read_packet(0)

def main():
    data_input = save_input()
    ans = part1(data_input)
    print(ans)


if __name__ == "__main__":
    main()