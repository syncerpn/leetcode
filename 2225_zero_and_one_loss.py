#1. make sure to count only loss, using dict, obviously
def solve(matches: list) -> list:
    stat = {}
    for w, l in matches:
        if w not in stat:
            stat[w] = 0
        if l not in stat:
            stat[l] = 0
        stat[l] -= 1
    
    zero_loss = []
    one_loss = []
    for i in sorted(stat.keys()):
        if stat[i] == 0:
            zero_loss.append(i)
        elif stat[i] == -1:
            one_loss.append(i)

    return [zero_loss, one_loss]