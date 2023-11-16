def minion_game(string):
    Stuart_count = 0
    Kevin_count = 0
    str_l = len(string)
    for i in range(0, str_l):
        if string[i] in ('A', 'E', 'I', 'O', 'U'):
            Kevin_count += str_l-i
        else:
            Stuart_count += str_l-i

    if Stuart_count > Kevin_count:
        print(f"Stuart {Stuart_count}")
    elif Stuart_count < Kevin_count:
        print(f"Kevin {Kevin_count}")
    else:
        print("Draw")
    return


if __name__ == '__main__':
    s = input()
    minion_game(s)


#problem Link: https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true