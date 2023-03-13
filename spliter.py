def instructions():
    '''
       There are two parts in this code
       the first part is split pgn so that the pgn size is not too big
       the second part is to anaylsis the result of the games
       blunder and noob check is included
    '''

################################

#part 1 pgn split
#find the split point

def split_pgn(pgn_file):
    def output_file_list (a):
        game = input('how many games do you want per pgn (type enter for game = 100): ')
        while True:
            try: 
                game = int(game)
                if game > a:
                    game = game + 'apple'
                else:
                    break
            except:
                game = input('try again')
        return game
            
    # finding the last game
    
    last_game = 0
    open_file = open(pgn_file,'r')
    double_open = open(pgn_file,'r')
    
    lines = open_file.readlines()
    for i in range(len(lines)-1,0,-1):
        if lines[i][1:6] == 'Round':
            last_game = int(lines[i][8:-3])
            
            break
    
    print(f' there are total of {last_game} games')
    # determine number of files
    game = output_file_list(last_game) 
    #game = 100
    output_name= []
    copy_last_game = last_game // game
    for i in range(copy_last_game):
        output_name.append(f"game { i*game +1} - {(i+1)*game}.pgn")
        if i == copy_last_game - 1 and last_game > (i+1) * game:
            output_name.append(f'game {(i+1) * game + 1} - {last_game}.pgn')
    
    #variable for output file
    output_file = []
    for i in range(len(output_name)):
        output_file.append(f'{i}')
    
    
    game_section = []
    # create files
    for i in range(len(output_file)):
        output_file[i] = open(f'{output_name[i]}','w')
        game_section.append(str(int((i*game+1))))
        
    # find game location
    game_location = []
    for i in range(len(lines)):
        if lines[i][1:8] == 'Round "':
            if lines[i][8:-3] in game_section:
                game_location.append(i-3)
                print(lines[i][8:-3])
    game_location.append(len(lines))
    
    #writing the file
    for i in range(len(game_location) -1):
        for j in range(game_location[i],game_location[i+1]):
            output_file[i].write(lines[j])
        
#split_pgn()

##############################################################3

#part 2 decisive checker

#result datas
def result_data_anaysls(line):
    
    write_file = open('data.txt','w')
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

    print(f'There are {len(play_count)} total games')
    write_file.write(f'There are {len(play_count)} total games\n')
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
    write_file.write(f"white wins {len(white_win)} times\n")
    write_file.write(f"black wins {len(black_win)} times\n")
    write_file.write(f"there are {len(draw_game)} draws\n")
    
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
    
    ### NOT WORKING



    odd_game_addition(overall_result)

    pr1 = engine1 +' gained '+str(engine1_points)+' points \n'
    pr2 = engine2 +' gained '+str(engine2_points)+' points \n'
    write_file.write(pr1)
    write_file.write(pr2)
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
        even_game.append(odd_game[-1])

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
            write_file.write(f'{a}{b}\n')
            print('   :',end='')
            write_file.write(f'   :')
            temp = 0
            for i in onelist:
                if True: #if onelist[-2] != i and (onelist != double_win): # identify when game number is odd
                    if c[i-1] == '1-0' or c[i-1] == '0-1' :
                        if (i == temp and i % 2 != 1):
                            continue
                        else:
                            print('',i,end = ' ')
                            write_file.write(f'{i} ')
                            number += 1
                    temp = i
        else:
            print(a+b)
            write_file.write(f'{a}{b}\n')
            print("   : NONE",end = ' ')
            write_file.write("   : NONE ")
            
        print('.')
        write_file.write('.\n')
        return number / d

    def double_draw_list (a):
        num = 0
        print('list of games that draws for both engines')
        write_file.write('list of games that draws for both engines\n')
        write_file.write('   :')
        temp = 0
        for i in a:
            if temp == i: # temp + 1 == i does seems not working
                continue
            else:
                print(i,end = ' ')
                write_file.write(f"{i} ")
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
   
    write_file.write(f'{double_win_result_num} number of games resulted in win for both engines in white and black\n')
    write_file.write(f'{engine1} had {decisive_win_result1_num} decisive wins\n')
    write_file.write(f'{engine2} had {decisive_win_result2_num} decisive wins\n')
    write_file.write(f'{engine1} won from both white and black in the same opening {one_win_all_result1_num} times\n')
    write_file.write(f'{engine2} won from both white and black in the same opening {one_win_all_result2_num} times\n')
    write_file.write(f'there are {double_draw_result_num} rounds games results in draw for both sides\n')

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
    write_file = open('data.txt','a')
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
    write_file.write(f'the top {min_max_game_input} fastest wins game is :')
    for i in range(0,min_max_game_input,1):
        print(rank_decisive_plycount[i], end = ' ')
        write_file.write(f'{rank_decisive_plycount[i]} ')
    print()
    write_file.write('\n')
    print(f'the longest {min_max_game_input} wins game is',end = ' : ')
    write_file.write(f'the longest {min_max_game_input} wins game is : ')
    for i in range(-1,-(min_max_game_input+1),-1):
        print(rank_decisive_plycount[i],end = ' ')
        write_file.write(f'{rank_decisive_plycount[i]} ')
    
def note_deletion(pgn_file):
    temp_file = open(pgn_file,'r')
    lines = temp_file.readlines()
    
    newlines = []
    write_flag = True
    
    for i in range(len(lines)):
        
        if lines[i][0:3] == '[Ro' or lines[i] == "":
            
            #new_file.write(lines[i])
            if lines[i] != '\n':
                newlines.append(lines[i])
        
        elif lines[i][0] == '[':
            continue
    
        else:
        
                
            for j in lines[i]:
                if j == '(' or j == '/':
                    write_flag = False
                elif j == ')' or j == '}':
                    write_flag = True
    
                
                if write_flag == True and j != ")":
                    newlines[-1] += j
                    #new_file.write(j)
           
    return newlines    

def next_line_delete (array):
    
    # make an empty string list with some length
    new_list = []
    for i in range(len(array)):
        new_list.append('')
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '\n':
                new_list[i] += ' '
            else:
                new_list[i] += array[i][j]
    
    return new_list

def eval_adjust (array):
    for i in range(len(array)):
        if '-M' in array[i]:
            array[i] = -900
        elif '+M' in array[i]:
            array[i] = 900
        
        try:    
            array[i] = float(array[i])
        except:
            try:    
                array[i] = float(array[i][0:-1])
            except:
                array[i] = array[i-1]
            
    return array

def eval_compare_blunder (white_array,black_array,overall_result):
    if overall_result == '1-0':
        for i in range(len(white_array)-1):
            if white_array[i] > -0.4 and white_array[i+1] > white_array[i] + 0.9 and white_array[i] < 2.5:
                return True
                break
    elif overall_result == '0-1':
        for i in range(len(black_array)-1):
            if black_array[i] > -0.4 and black_array[i+1] > black_array[i] + 0.9 and black_array[i] < 2.5:
                return True
                break
    else:
        return False
    
def eval_compare_noob (array,array2,overall_result):
    
    if overall_result == '1/2-1/2':
        for i in range(len(array)):
            if array[i] > 2:
                return True
                break
        for i in range(len(array2)):
            if array2[i] > 2:
                return True
                break
    else:
        return False 

def blunder_check (array,overall_result):
    
    write_file = open('data.txt','a')
    blunder_exist = []
    noob_exist = []
    for i in range(len(array)):
        move_sequence = 0
        white_eval = []
        black_eval = []
        location = 0
        for j in range(len(array[i])):
            if array[i][j] == '}':
                location = j
                break
        
        # game that white play first
        if array[i][location+4] != ' ':
            move_sequence += 1
            
        # eval location
        for j in range(len(array[i])):
            
            # black play first
            if move_sequence % 2 == 0:
                if array[i][j] == '{':
                    move_sequence += 1
                    black_eval.append(array[i][(j+2):(j+7)])
                
            # white play first
            elif move_sequence % 2 == 1:
                if array[i][j] == '{':
                    move_sequence += 1
                    white_eval.append(array[i][(j+2):(j+7)])
                
        #eval transfer from string to float
        white_eval = eval_adjust(white_eval)
        black_eval = eval_adjust(black_eval)
             
        # boolean value
        blunder_val = eval_compare_blunder(white_eval,black_eval ,overall_result[i])
        noob_val = eval_compare_noob(white_eval,black_eval, overall_result[i])
        
        if blunder_val == True:
            blunder_exist.append(i)
        if noob_val == True:
            noob_exist.append(i)

    print('list of game that blunder for one engine:   ',end = '')
    write_file.write('list of game that blunder for one engine:   ')
    for i in range(len(blunder_exist)):
        blunder_exist[i] += 1
        print(f' {blunder_exist[i]}',end = '')
        write_file.write(f' {blunder_exist[i]}')
    print()
    write_file.write('\n')    
    
    print('list of game that noobed for one engine:    ',end = '')
    write_file.write('list of game that noobed for one engine:    ')
    for i in range(len(noob_exist)):
        noob_exist[i] += 1
        print(f' {noob_exist[i]}',end = '')
        write_file.write(f' {noob_exist[i]}')
    
def tb_nodes_check(file):
    read_file = open(file,'r')
    lines = read_file.readlines()
    
    largest_tb = 0
    largest_nodes = 0
    largest_time = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            try:
                if(lines[i][j:j+5] == "nodes"):
                    space = j + 6
                    while(lines[i][space] != ' '):
                        space += 1
                        
                    nodes = int((lines[i][j+6:space]))
                    if nodes > largest_nodes:
                        largest_nodes = nodes
                        
                if(lines[i][j:j+6] == "tbhits"):
                    space = j + 7
                    while(lines[i][space] != ' '):
                        space += 1
                    
                    tbhits = int((lines[i][j+7:space]))
                    if tbhits > largest_tb:
                        largest_tb = tbhits
                        
                if(lines[i][j:j+4] == "time"):
                    space = j + 5
                    while(lines[i][space] != ' '):
                        space += 1
                    
                    time = int((lines[i][j+5:space]))
                    if time > largest_time:
                        largest_time = time
                    
            except:
                continue
            
        if i % 100000 == 0:
            print(i / (len(lines)))
            
            
    print(f'{largest_nodes} is the largest nodes')
    print(f'{largest_tb} is the largest tb')
    print(f'{largest_time} is the largest time used')

    read_file.close()
    
    write_file = open('data.txt','a')
    write_file.write(f'\n{largest_nodes} is the largest nodes\n')
    write_file.write(f'{largest_tb} is the largest tb\n')
    write_file.write(f'{largest_time} is the largest time used\n')
    
def main():
    help(instructions)
    pgn_file = input("please enter your file location: (default is Arena.pgn,press enter)")
    if pgn_file == '':
        pgn_file = 'Arena.pgn'
    pgn_file = "C:\\Users\\ZZHzh\\Desktop\\arena_3.5.1\\Arena.pgn"
    split_pgn(pgn_file)
    decisive_file = open(pgn_file,'r')
    line = decisive_file.readlines()
    result_data = result_data_anaysls(line)
    find_plycount_min(result_data[0],result_data[1],result_data[2],result_data[3])
    print()
    blunder_check(next_line_delete(note_deletion(pgn_file)),result_data[2])
    print(len(result_data[2]))
    
    #log_file = input("put your debugger file: ")
    log_file = "C:\\Users\\ZZHzh\\Desktop\\arena_3.5.1\\arena.debug"
    tb_nodes_check(log_file)
if __name__=="__main__":
    main()
