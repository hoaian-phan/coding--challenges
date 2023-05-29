class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        seen = set()
        loss_counts = {}
        for win, loss in matches:
            seen.add(win)
            seen.add(loss)
            loss_counts[loss] = loss_counts.get(loss, 0) + 1
            
        zero_loss = []
        one_loss = []
        for player in seen:
            if player not in loss_counts:
                zero_loss.append(player)
            elif loss_counts[player] == 1:
                one_loss.append(player)
            
        return [sorted(zero_loss), sorted(one_loss)]