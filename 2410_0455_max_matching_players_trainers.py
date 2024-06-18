# simply do greedy matching
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        pi = 0
        ti = 0
        c = 0
        while ti < len(trainers) and pi < len(players):
            if trainers[ti] >= players[pi]:
                c += 1
                pi += 1
            ti += 1
        
        return c