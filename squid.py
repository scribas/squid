import os.path

##################################################################################################

###############
# VIEW LAYER:
###############

def welcome():
    print('')
    print('')
    print('')
    print('                              ====================')
    print('                              = Welcome to Squid =')
    print('                              ====================')
    print('              ...Let your tentacles penetrate those GIANT text files...')
    print('                    Written by Dr Stefan Scriba, Copyleft 2019')
    print('')
    print('                             Version control with Git...')
    print('')
    print('  NOTE: Type <ENTER> for help.')
    print('')
    print('')

def help(subject):
    if subject=='':
        print('')
        print('  COMMANDS:')
        print('  =========')
        print('    list       (l,ls)  - List content of present working directory.')
        print('    cd         (cd)    - Change the present working directory.')
        print('    open       (o)     - Point to a new text file.')
        print('    columns    (c)     - View the column headings within the file.')
        print('    rows       (r)     - Count the number of rows within the file.')
        print('    view       (v)     - View the a portion of the content of a file.')
        print('    delimiter  (d)     - Change the csv file delimiter.')
        print('    exit/quit  (x,q)   - Quit the program.')
        print('')
    if subject=='o':
        print('  Open:')
        print('  =====')
        print('')
        print('  Description:')
        print('    The open command points to the file that Squid should work on.')
        print('    A path should be defined with unix-like front-slashes.')
        print('    If no path is defined, the file is assumed to be in the present working directory.')
        print('')
        print('    Syntax: open path/csv_filename')
        print('')
    if subject=='c':
        print('  Columns:')
        print('  ========')
        print('')
        print('  Description:')
        print('    Lists all columns.')
        print('')
    if subject=='v':
        print('  View:')
        print('  =====')
        print('')
        print('  Description:')
        print('    View displays the requested columns of the rows specified.')
        print('    By default, view lists the first 10 rows of the csv file loaded.')
        print('    If start_row is specified, 10 rows from that point onwards will be listed.')
        print('    By specifying end_row, less or more than 10 rows can be listed.')
        print('    If start_col is specified, 10 cols from that point onwards will be listed.')
        print('    By specifying end_col, less or more than 10 cols can be listed.')
        print('')
        print('    Syntax: v start_row end_row start_col end_col')
        print('')
    if subject=='d':
        print('  Delimiter:')
        print('  ==========')
        print('')
        print('  Description:')
        print('    By default, the delimiter in a csv file is assumed to be a comma.')
        print('    By specifying character, the delimiter can be changed to one or more other symbols.')
        print('')

def loaded_file(csv_filename):
    if csv_filename=='':
        print('  Currently not pointing to any text file. Use `open` to point to a text file.')
    else:
        print('  Currently pointing to file:')
        print('  ' + csv_filename)
    print('')


##################################################################################################

###############
# MODEL LAYER:
###############

def cursor(pwd,csv_filename):
    if csv_filename=='':
        query_line=input("SQUID: " + pwd + "> ")
    else:
        query_line=input("SQUID: " + pwd + "\\<" + csv_filename + "> ")
    query_array=query_line.split(' ')
    query=str(query_array[0]).lower()
    query_len=0
    query_len=len(query_array)
    print('')
    return query_line, query_array, query, query_len

def list_directory():
    if query_len==1:
        print('')
        file_list= [ f for f in os.listdir(os.getcwd()) if not os.path.isfile(os.path.join(os.getcwd(),f)) ]
        for i in file_list:
            print('   D: ' + i)
        file_list= [ f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(),f)) ]
        for i in file_list:
            print('   F: ' + i)
        print('')
    if query_len>1:
        print('  SYNTAX ERROR - : No parameters expected.')
        print('')
    return

def cd(query_line,csv_filename):
    path=os.getcwd()
    if len(query_line.split('cd '))==1:
        directories={}
        file_list= [ f for f in os.listdir(os.getcwd()) if not os.path.isfile(os.path.join(os.getcwd(),f)) ]
        if len(file_list)>0:
            x=1;
            for i in file_list:
                directories[x]=i
                print(str(x)+':',str(i))
                x+=1
            print('')
            try:
                number=int(input('  Pick the directory number: '))
                if number>0 and number<x:
                    path=directories[number]
                print('')
            except:
                print('  Wrong selection')
                print('')
                pass
    else:
        path=query_line.split('cd ')[1]

    try:
        os.chdir(path)
        csv_filename=''
    except:
        print('  No such directory')
        print('')
        pass

    pwd=os.getcwd()
    return pwd, csv_filename

def open_file(query_array, query_len, csv_filename):
    if query_len==1:
        help('o')
        if csv_filename=='':
            print('  Currently not pointing to any text file.')
        else:
            print('  Currently pointing to file:')
            print('  ' + csv_filename)
        print('')

        files={}
        file_list= [ f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(),f)) ]
        if len(file_list)>0:
            x=1;
            for i in file_list:
                files[x]=i
                print('    ' + str(x)+':',str(i))
                x+=1
            print('')
            try:
                number=int(input('  Pick the file number: '))
                if number>0 and number<x:
                    csv_filename=files[number]
                    print('  Pointing to: ' + csv_filename)
                    print('')
            except:
                print('  Wrong selection')
                print('')
                pass

    if query_len==2:
        if os.path.exists(query_array[1]):
            csv_filename=query_array[1]
            print('  Loaded: ' + csv_filename)
        else:
            print('  ERROR - File does not exist.')
        print('')
    if query_len>2:
        print('  SYNTAX ERROR - Not pointing to any file. Incorrect number of parameters.')
        print('')
    return csv_filename

def columns(query_len):
    if query_len==1:
        help('c')
        if csv_filename=='':
            print('  ERROR - Currently not pointing to any file.')
            print('')
        else:
            if not os.path.exists(csv_filename):
                print('  ERROR - Cannot find file...?')
                print('')
            else:
                csv_file=open(csv_filename, 'r')
                file_line=csv_file.readline()
                line_array=file_line.split(delimiter_char)
                col_no=0
                out_line = ''
                for i in line_array:
                    out_line += '    [' + str(col_no)+']: ' + str(i)
                    col_no+=1
                    if col_no%5==0:
                        print(out_line)
                        out_line=''
                print(out_line)
                print('')
                csv_file.close()
    else:
        print('  SYNTAX ERROR - No parameters expected.')
        print('')
    return

def view(query_array, query_len, csv_filename,delimiter_char):
    start_line=0
    end_line=9
    start_col=0
    end_col=9
    if query_len==1:
        help('v')
    if csv_filename!='':
        if not os.path.exists(csv_filename):
            print('  ERROR -  Cannot find file...?')
            print('')
        else:
            print('  Fetching rows... (This can take some time)')
            print('')

            if len(query_array)>1:
                start_line=int(query_array[1])
                end_line=start_line+9
            if len(query_array)>2:
                end_line=int(query_array[2])
            if len(query_array)>3:
                start_col=int(query_array[3])
                end_col=start_col+9
            if len(query_array)>4:
                end_col=int(query_array[4])
            if len(query_array)<6:
                csv_file=open(csv_filename, 'r')
                file_line=csv_file.readline()
                rows=0
                while file_line and rows<=end_line:
                    if rows>0 and rows%100000==0:
                        print('      >>> ' + str(rows))
                    if rows==0 or rows>=start_line:
                        fields = file_line.strip('\n').split(delimiter_char)
                        col_num=0
                        out_line = ''
                        for i in fields:
                            if col_num>=start_col:
                                out_line += '[' + str(col_num) + ']' + i + ' '
                            col_num+=1
                            if col_num>end_col:
                                break;
                        print('    ' + str(rows) + ':', out_line)
                    if rows==0:
                        print('      =================================================================================')

                    file_line=csv_file.readline()
                    rows+=1
                csv_file.close()
            print('')
        return

def delimiter(delimiter_char):
    if query_len==1:
        help('d')

        new_delimiter_char=input('  Type new delimiter character: ')
        if new_delimiter_char!='':
            delimiter_char = new_delimiter_char
        print('  The delimiter character has been changed to:')
        print('  ' + delimiter_char)
        print('')
    if query_len>1:
        print('  SYNTAX ERROR - too many arguments')
        print('')
    return delimiter_char

def rows(csv_filename):
    if not os.path.exists(csv_filename):
        print('  ERROR - Cannot find file...?')
        print('')
    else:
        csv_file=open(csv_filename, 'r')
        rows=1;
        file_line=csv_file.readline()
        print('  Counting rows... (This can take some time)')
        while file_line:
            file_line=csv_file.readline()
            if rows%100000==0:
                print('      >>> ' + str(rows))
            rows+=1
        print('')
        print('  Total rows: ' + str(rows))
        print('')
        csv_file.close()


##################################################################################################

###############
# CONTROL LAYER:
###############


query=''
csv_filename=''
delimiter_char=','
pwd= os.getcwd()


welcome()

while query!='quit' and query!='q' and query!='x':
    query_line, query_array, query, query_len=cursor(pwd,csv_filename)
    if query=='':
        help('')
        loaded_file(csv_filename)
    elif query=='ls' or query=='l':
        list_directory()
        loaded_file(csv_filename)
    elif query=='cd':
        pwd,csv_filename=cd(query_line,csv_filename)
        loaded_file(csv_filename)
    elif query=='open' or query=='o':
        csv_filename=open_file(query_array, query_len, csv_filename)
    elif query=='columns' or query=='c':
        columns(query_len)
    elif query=='view' or query=='v':
        loaded_file(csv_filename)
        view(query_array, query_len, csv_filename,delimiter_char)
    elif query=='delimiter' or query=='d':
        delimiter_char=delimiter(delimiter_char)
    elif query=='rows' or query=='r':
        rows(csv_filename)
    elif query=='quit' or query=='q' or query=='x':
        print('  Thank you for this session!')
        print('  Good bye...')
        print('')
        print('')
    else:
        print('Unknown command...')
