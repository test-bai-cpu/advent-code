from functools import cache


def part1():
    player1_score = 0
    player2_score = 0
    player1_stop = 1
    player2_stop = 6
    flag = True
    for i in range(1, 100000, 3):
        value = 3*i + 3
        if flag:
            stop = (value + player1_stop) % 10
            if stop == 0:
                stop = 10
            player1_stop = stop
            player1_score += stop
        else:
            stop = (value + player2_stop) % 10
            if stop == 0:
                stop = 10
            player2_stop = stop
            player2_score += stop
        if player1_score >= 1000:
            return player2_score * (i+2)
        if player2_score >= 1000:
            return player1_score * (i+2)
        flag = not flag


def get_dice_list():
    dice_list_tmp = []
    for i in range(1,4):
        for j in range(1, 4):
            for k in range(1, 4):
                dice_list_tmp.append([i,j,k])
    return dice_list_tmp


dice_list = get_dice_list()


@cache
def part2(player1_stop, player2_stop, player1_score, player2_score):
    player1_win_universe = 0
    player2_win_universe = 0
    for dice1 in dice_list:
        for dice2 in dice_list:
            stop = (sum(dice1) + player1_stop) % 10
            if stop == 0:
                stop = 10
            player1_stop_next = stop
            player1_score_next = player1_score + stop
            stop = (sum(dice2) + player2_stop) % 10
            if stop == 0:
                stop = 10
            player2_stop_next = stop
            player2_score_next = player2_score + stop
            if player1_score_next >= 21:
                player1_win_universe += 1
                break
            if player2_score_next >= 21:
                player2_win_universe += 1
                continue
            player1_universe_add, player2_universe_add = part2(player1_stop_next, player2_stop_next, player1_score_next, player2_score_next)
            player1_win_universe += player1_universe_add
            player2_win_universe += player2_universe_add

    return player1_win_universe, player2_win_universe


def main():
    print(part1())
    print(part2(1, 6, 0, 0))


if __name__ == "__main__":
    main()
