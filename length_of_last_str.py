def len_of_last_str(s): 
    return len(s.strip().split(' ')[-1]) 
    # s=' '+s
    # print(s)
    # count = 0 
    # flag_counter_started = 0 
    # for i in range(len(s)-1, 0, -1): 
    #     if s[i] == ' ': 
    #         if flag_counter_started == 0: 
    #             count = 0 
    #             continue 
    #         else: 
    #             return count 
    #     else: 
    #         count+=1 
    #         flag_counter_started = 1 
    # return count 
