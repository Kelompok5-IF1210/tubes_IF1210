# read csv
def read_csv(path_csv:str) -> tuple:
    file = open(path_csv,'r')
    # count line
    count=0

    for line in file:
        # header
        if count==0:
            count+=1

            # determine len arr needed to store the string
            count_delimiter=0
            for char in line:
                if char==";":
                    count_delimiter+=1
            # initialization of mtx
            mtx=[["" for i in range (count_delimiter+1)] for i in range (10)]
            mtx_idx=count-1

        # not header
        else:
            str_temp=""
            arr_temp=["" for i in range (count_delimiter+1)]
            # indexing for arr_temp
            arr_idx=0
            mtx_idx=count-1

            for char in range (len(line)):
                if line[char]==";" or line[char]=="\n":
                    arr_temp[arr_idx]=str_temp
                    arr_idx+=1
                    str_temp=""
                else:
                    str_temp+=line[char]

            mtx[mtx_idx]=arr_temp
            '''debugging station'''
            print(mtx)
            print("INDEX OF MATRIX", mtx_idx)

            count+=1
        
    # antisipasi csv hanya berisi header
    # antisipasi csv diakhiri newline
    '''debugging station'''
    print( mtx[mtx_idx-1]==["" for i in range (count_delimiter+1)])
    print("IS BEFORE", mtx_idx-2,  mtx[mtx_idx-2]==["" for i in range (count_delimiter+1)])
    if mtx_idx!=0 and mtx[mtx_idx-1]==["" for i in range (count_delimiter+1)]:
        mtx_idx-=1
    
    mtx[mtx_idx]=["MARK" for i in range(count_delimiter+1)]
    print(mtx)
    
    return (mtx, mtx_idx+1)

read_csv("default/user.csv")