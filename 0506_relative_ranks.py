#1. sorting then check the order
def solve(score: list) -> list:
    index = list(range(len(score)))
    score_index = sorted(index, key=lambda x: -score[x])
    ranks = ["" for _ in score]
    for i, s in enumerate(score_index):
        if i == 0:
            ranks[s] = "Gold Medal"
        elif i == 1:
            ranks[s] = "Silver Medal"
        elif i == 2:
            ranks[s] = "Bronze Medal"
        else:
            ranks[s] = str(i+1)
    return ranks