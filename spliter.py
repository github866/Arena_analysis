def instructions():
    '''
        options are the doing the same thing but output in different amount of files
        the purpose to create two options is to avoid some bugs that may lose some lines in pythons


    '''

################################

#part 1 pgn split
#find the split point

def option_one():
    open_file = open("C:\\Users\\ZZHzh\\Desktop\\arena_3.5.1\\Arena.pgn",'r')
    double_open = open("C:\\Users\\ZZHzh\\Desktop\\arena_3.5.1\\Arena.pgn",'r')
    output = open("output1.pgn",'w')
    output2 = open("output2.pgn",'w')
    output3 = open("output3.pgn",'w')
    output4 = open("output4.pgn",'w')
    output5 = open("output5.pgn",'w')
    
    game1 = 1
    game101 = 0
    game201 = 0
    game301 = 0
    game401 = 0
    
    
    for i in range(0,1000000):
        lines = open_file.readline()
        
        if lines == '[Round "101"]\n':
            game101 = i - 3
        if lines == '[Round "201"]\n':
            game201 = i - 3
        if lines == '[Round "301"]\n':
            game301 = i - 3
        if lines == '[Round "401"]\n':
            game401 = i - 3

    # write the file separately
    for i in range(0,1000000):

        newlines = double_open.readline()
    
        if i >= game401: #depend on different values
            output5.write(newlines)

        if i >= game301 and i <game401: #depend on different values
            output4.write(newlines)
        
        if i >= game201 and i <game301: #depend on different values
            output3.write(newlines)
        
        if i >= game101 and i <game201: #depend on different values
            output2.write(newlines)
        
        if i >= game1 and i <game101: #depend on different values
            output.write(newlines)
        
    open_file.close()
    double_open.close()


def option_2():
    
    open_file = open("C:\\Users\\ZZHzh\\Desktop\\arena_3.5.1\\Arena.pgn",'r')
    double_open = open("C:\\Users\\ZZHzh\\Desktop\\arena_3.5.1\\Arena.pgn",'r')
    output = open("output1.pgn",'w')
    output2 = open("output2.pgn",'w')
    output3 = open("output3.pgn",'w')
    output4 = open("output4.pgn",'w')
    output5 = open("output5.pgn",'w')
    output6 = open("output6.pgn",'w')
    output7 = open("output7.pgn",'w')
    output8 = open("output8.pgn",'w')
    output9 = open("output9.pgn",'w')
    output10 = open("output10.pgn",'w')


    ################################

    #part 1 pgn split
    #find the split point
    game1 = 1
    game51 = 0
    game101 = 0
    game151 = 0
    game201 = 0
    game251 = 0
    game351 = 0
    game401 = 0
    game451 = 0




    for i in range(0,1000000):
        lines = open_file.readline()
        
        if lines == '[Round "51"]\n':
            game51 = i - 3
        if lines == '[Round "101"]\n':
            game101 = i - 3
        if lines == '[Round "151"]\n':
            game151 = i - 3
        if lines == '[Round "201"]\n':
            game201 = i - 3
        if lines == '[Round "251"]\n':
            game251 = i - 3
        if lines == '[Round "301"]\n':
            game301 = i - 3
        if lines == '[Round "351"]\n':
            game351 = i - 3
        if lines == '[Round "401"]\n':
            game401 = i - 3    
        if lines == '[Round "451"]\n':
            game451 = i - 3    
            
    # write the file separately
    for i in range(0,1000000):

        newlines = double_open.readline()
        
        if i >= game451: #depend on different values
            output10.write(newlines)
            
        if i >= game401 and i <game451: #depend on different values
            output9.write(newlines)
        
        if i >= game351 and i <game401: #depend on different values
            output8.write(newlines)
           
        if i >= game301 and i <game351: #depend on different values
            output7.write(newlines)
           
        if i >= game251 and i <game301: #depend on different values
            output6.write(newlines)
           


        if i >= game201 and i <game251: #depend on different values
            output5.write(newlines)
           
        if i >= game151 and i <game201: #depend on different values
            output4.write(newlines)
        
        
        if i >= game101 and i <game151: #depend on different values
            output3.write(newlines)
            
        if i >= game51 and i <game101: #depend on different values
            output2.write(newlines)
            
        if i >= game1 and i <game51: #depend on different values
            output.write(newlines)
            
    open_file.close()
    double_open.close()

def split_pgn():
    choose_option = int(input('do you want option 1 or 2(type "1" or "2"): '))
    if choose_option == 1:
        option_one()
    elif choose_option == 2:
        option_2()
        
#split_pgn()

##############################################################3

#part 2 decisive checker

#result datas
def result_data_anaysls(line):
    white_win = []
    black_win = []
    draw = []
    overall_result = []
    copy_overall_result = []

    # even round and odd round
    odd_game = []
    even_game = []

    #play_count data
    play_count = []
    copy_plycount = []
    total_play_count = 0
    
    
    # points
    engine1_points = 0
    engine2_points = 0
    


    # engine name
    engine1 = ''
    engine2 = ''

    for i in range(20):
        if line[i][0:7] == "[White ":        
            engine1 = line[i][8:-3]
            engine2 = line[i+1][8:-3]
            
            break
  
    # result based on games
    for i in range(len(line)):
        
        # find the number of round
        if line[i][1:6] == 'Round':
            line[i] = int(line[i][8:-3])
            
            # finding result
            if line[i+3][0:8] == "[Result ": #unnecessary code
                if line[i+3][9:-3] == "1-0":
                    white_win.append(line[i])
                if line[i+3][9:-3] == "1/2-1/2":
                    draw.append(line[i])
                if line[i+3][9:-3] == "0-1":
                    black_win.append(line[i])
                overall_result.append(line[i+3][9:-3])
            
        
        elif line[i][1:9] == "PlyCount":    
            play_count.append((line[i][11:-3]))
            copy_plycount.append((line[i][11:-3]))
            total_play_count += int(line[i][11:-3])

    print('There are',len(play_count),'total games')

    # transfer from str to int
    for i in range(len(play_count)):
        play_count[i] = int(play_count[i])
        copy_plycount[i] = int(play_count[i])

    # find games that white wins and black wins
    white_win = []
    num_white_win = 0
    black_win = []
    num_black_win = 0
    draw_game = []
    num_draw_game = 0
    for i in range(len(overall_result)):
        if overall_result[i] =='1-0':
            white_win.append(i)
            num_white_win += 1
        elif overall_result[i] == '0-1':
            black_win.append(i)
            num_black_win += 1
        elif overall_result[i] == '1/2-1/2':
            draw_game.append(i)
            num_draw_game += 1

     
    print(f"white wins {len(white_win)} times")    
    print(f"black wins {len(black_win)} times")    
    print(f"there are {len(draw_game)} draws")
    #print(f"list of white win games {white_win}")
    #print(f"list of black win games {black_win}")
    #print(f"list of draw games {draw_games}")
    print(total_play_count / len(play_count)/2,'moves per game')

    def odd_game_addition (a):
        if len(a) % 2 == 1:
            a.append('')


    #print(black_win,'black win')
    #print(white_win,'white win')
    #print(draw,'draw')
    #print(len(overall_result),'is total games')

    # split games, counting points
    for i in range(len(overall_result)):
        if i % 2 == 0:
            odd_game.append(overall_result[i])
        else:
            even_game.append(overall_result[i])

    for i in range(len(odd_game)):
        if odd_game[i] == '1-0':
            engine1_points += 1
        elif odd_game[i] == '1/2-1/2':
            engine1_points += 0.5
            engine2_points += 0.5
        elif odd_game[i] == '0-1':
            engine2_points += 1

    for i in range(len(even_game)):
        if even_game[i] == '1-0':
            engine2_points += 1
        elif even_game[i] == '1/2-1/2':
            engine1_points += 0.5
            engine2_points += 0.5
        elif even_game[i] == '0-1':
            engine1_points += 1

    #pr = point_result
    a = open('r.txt','w')
    ### NOT WORKING



    odd_game_addition(overall_result)

    pr1 = engine1 +' gained '+str(engine1_points)+' points \n'
    pr2 = engine2 +' gained '+str(engine2_points)+' points \n'
    a.write(pr1)
    a.write(pr2)
    print(engine1,' gained ',engine1_points,' points ')
    print(engine2,' gained ',engine2_points,' points ')

    # decisive parameter
    double_draw = []
    decisive_win = []
    decisive_win1 = []
    decisive_win2 = []
    double_win = []
    one_win_all = []
    one_win_all1 = []
    one_win_all2 = []

    # if the total games is odd, add an 1/2-1/2 in even game list
    if len(odd_game) > len(even_game):
        even_game.append('1/2-1/2')

    #determine decisives
    for i in range(len(odd_game)):
        if even_game[i] == '':
            continue
        if odd_game[i] == '1/2-1/2' and even_game[i] == '1/2-1/2':
            double_draw.append(i)
        elif (odd_game[i] == '1/2-1/2' and even_game[i] == '1-0') or (odd_game[i] == '0-1' and even_game[i] == '1/2-1/2'):
            decisive_win.append(i)
            decisive_win2.append(i)
        elif (odd_game[i] == '1-0' and even_game[i] == '1-0') or (odd_game[i] == '0-1' and even_game[i] == '0-1'):
            double_win.append(i)
        elif (odd_game[i] == '1-0' and even_game[i] == '1/2-1/2') or (odd_game[i] == '1/2-1/2' and even_game[i] == '0-1'):
            decisive_win.append(i)
            decisive_win1.append(i)
        elif (odd_game[i] == '1-0' and even_game[i] == '0-1') or (odd_game[i] == '0-1' and even_game[i] == '1-0'):
            one_win_all.append(i)
            if odd_game[i] == '1-0' and even_game[i] == '0-1':
                one_win_all1.append(i)
            elif odd_game[i] == '0-1' and even_game[i] == '1-0':
                one_win_all2.append(i)


    # functions that transfer rounds to games
    def round_to_games(a):
        for i in range(len(a)):
            a[i] += 1
            a.append(a[i]*2 - 1)
            a[i] = a[i]*2
            
        a.sort()
        return a

    def print_result(a,onelist,b,c,d):
        number = 0
        if onelist != []:
            print(a+b)
            print('   :',end='')
            temp = 0
            for i in onelist:
                if True: #if onelist[-2] != i and (onelist != double_win): # identify when game number is odd
                    if c[i-1] == '1-0' or c[i-1] == '0-1' :
                        if (i == temp and i % 2 != 1):
                            continue
                        else:
                            print('',i,end = ' ')
                            number += 1
                    temp = i
        else:
            print(a+b)
            print("   : NONE",end = ' ')
            
        print('.')
        return number / d

    def double_draw_list (a):
        num = 0
        print('list of games that draws for both engines')
        temp = 0
        for i in a:
            if temp == i: # temp + 1 == i does seems not working
                continue
            else:
                print(i,end = ' ')
                num += 1
            temp = i
        return num/2
        
            
    double_draw = round_to_games(double_draw)
    decisive_win = round_to_games(decisive_win)
    decisive_win1 = round_to_games(decisive_win1)
    decisive_win2 = round_to_games(decisive_win2)
    double_win = round_to_games(double_win)
    one_win_all = round_to_games(one_win_all)
    one_win_all1 = round_to_games(one_win_all1)
    one_win_all2 = round_to_games(one_win_all2)



    double_win_result_num = int(print_result('here are list of games results in win for both engines when reversed ',double_win,'',overall_result,2))
    decisive_win_result1_num = int(print_result('here are the games that decisive wins for ',decisive_win1,engine1,overall_result,1))
    decisive_win_result2_num = int(print_result('here are the games that decisive wins for ',decisive_win2,engine2,overall_result,1))
    one_win_all_result1_num = int(print_result('here are the games that wins for both white and black for ',one_win_all1,engine1,overall_result,2))
    one_win_all_result2_num = int(print_result('here are the games that wins for both white and black for ',one_win_all2,engine2,overall_result,2))
    double_draw_result_num = int(double_draw_list(double_draw))


    print()
    #total = double_draw_result_num + one_win_all_result2_num + one_win_all_result1_num + decisive_win_result2_num + decisive_win_result1_num + double_win_result_num
    #print(total)
    print(f'{double_win_result_num} number of games resulted in win for both engines in white and black')
    print(f'{engine1} had {decisive_win_result1_num} decisive wins')
    print(f'{engine2} had {decisive_win_result2_num} decisive wins')
    print(f'{engine1} won from both white and black in the some opening {one_win_all_result1_num} times')
    print(f'{engine2} won from both white and black in the same opening {one_win_all_result2_num} times')
    print(f'there are {double_draw_result_num} rounds games results in draw for both sides')


    #print(double_draw)
    #print(decisive_win)
    #print(decisive_win1)
    #print(decisive_win2)
    #print(double_win)
    #print(one_win_all）
    #print(one_win_all1)



    '''
    # testing section, not useful
    total = double_draw + decisive_win + double_win + one_win_all
    total.sort()
    print(len(total))
    for i in range(len(total)):
        if total[i] == i+1:
            print('true',i,end=',')
        else:
            print('false',i,end = '')

    '''
    #double test
    '''
    total = double_draw + decisive_win1 + decisive_win2 + double_win + one_win_all1 + one_win_all2
    total.sort()
    print(len(total))
    for i in range(len(total)):
        if total[i] == i+1:
            print('true',i,end=',')
        else:
            print('false',i,end = '')
            
    '''
    total_win = white_win + black_win


    # play count NOT using sort method
    return [copy_plycount,play_count,overall_result,total_win]


def find_plycount_min(copy_plycount,play_count,overall_result,total_win):
    
    def decisive_game_with_plycount(a):
        while True:
            try:
                b = int(input('please enter the number games for minimum and maximum playcount:'))
                if b > 0 and b <= a:
                    return b
                    break
                else:
                    b = int(b)
                    b = b + 3
            except:
                print('try again: ',end = '')
                
    def find_missing_game(a,b):
        for i in range(len(b)):
            if not( i in a):
                
                a.append(i)     
        return a



    decisive_last_five_play_count = []
    copy_plycount.sort()

    
    ### use sorted plycount to find the shortest playcount
    for i in range(len(copy_plycount)-1):
        start = copy_plycount[i]
        if copy_plycount[i+1] == copy_plycount[i]:
            continue

        else:
        
            # find the spot where
            for j in range(len(play_count)):
                if start == play_count[j]:
                    decisive_last_five_play_count.append(j)

    find_missing_game(decisive_last_five_play_count,play_count)
    
    
    rank_decisive_plycount = []
    #determine decisive using overall result
    #minimum

    for i in decisive_last_five_play_count:
        if overall_result[i] == '1-0' or overall_result[i] == '0-1':
            rank_decisive_plycount.append(i)

            
    for i in range(len(rank_decisive_plycount)):
        rank_decisive_plycount[i] += 1

    min_max_game_input = decisive_game_with_plycount(len(total_win))
    # printing the final top 5 minimum plycount and top 5 maximum plycount
    print(f'the top {min_max_game_input} fastest wins game is',end = ' : ')
    for i in range(0,min_max_game_input,1):
        print(rank_decisive_plycount[i], end = ' ')
    print()

    print(f'the longest {min_max_game_input} wins game is',end = ' : ')
    for i in range(-1,-(min_max_game_input+1),-1):
        print(rank_decisive_plycount[i],end = ' ')
    
def main():
    help(instructions)
    #split_pgn()
    decisive_file = open("C:\\Users\\ZZHzh\\Desktop\\arena_3.5.1\\Arena.pgn",'r')
    line = decisive_file.readlines()
    result_data = result_data_anaysls(line)
    find_plycount_min(result_data[0],result_data[1],result_data[2],result_data[3])
    
if __name__=="__main__":
    main()
