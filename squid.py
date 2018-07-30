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
    print('              ...Let your tentacles penetrate those GIANT csv files...')
    print('                    Written by Dr Stefan Scriba, Copyleft 2017')
    print('')
    print('                             Version control with Git...')
    print('')
    print('  NOTE: Type <ENTER> for help.')
    print('')
    print('')

def help(subject):
    if subject=='':
        print('')
        print('  NOTE: Type any command name without parameters to see its help article.')
        print('')
        print('  COMMANDS:')
        print('  =========')
        print('  list       (l)   - List content of present working directory.')
        print('  cd         (cd)  - Change the present working directory.')
        print('  open       (o)   - Point to a new csv file.')
        print('  columns    (c)   - View the first row of the file, currently pointed to.')
        print('  view       (v)   - View the content of a file.')
        print('  delimiter  (d)   - Change the csv file delimiter.')
        print('  exit/quit  (x,q) - Quit the program.')
        print('')
    if subject=='o':
        print('  Open:')
        print('  =====')
        print('')
        print('  Description:')
        print('  The open command points to the file that Squid should work on.')
        print('  A path should be defined with unix-like front-slashes.')
        print('  If no path is defined, the file is assumed to be in the pwd.')
        print('')
        print('  Syntax 1: open path/csv_filename')
        print('  Syntax 2: o path/csv_filename')
        print('')
    if subject=='c':
        print('  Columns:')
        print('  ========')
        print('')
        print('  Description:')
        print('  Lists all columns.')
        print('')
        print('  Syntax: columns')
        print('')
    if subject=='v':
        print('  View:')
        print('  =====')
        print('')
        print('  Description:')
        print('  View displays the requested columns of the rows specified.')
        print('  To select the columns, place them in the square brackets, with : for ranges.')
        print('  By default, view lists the first 10 rows of the csv file loaded.')
        print('  If start_row is specified, 10 rows from that point onwards will be listed.')
        print('  By specifying end_row, less or more than 10 rows can be listed.')
        print('')
        print('  Syntax: [1:10,11] start_row end_row')
        print('')
    if subject=='d':
        print('  Delimiter:')
        print('  ==========')
        print('')
        print('  Description:')
        print('  By default, the delimiter in a csv file is assumed to be a comma.')
        print('  By specifying character, the delimiter can be changed to one or more other symbols.')
        print('')
        print('  Syntax: delimiter [character]')
        print('')

##################################################################################################

###############
# MODEL LAYER:
###############

def cursor(pwd):
    query_line=input("SQUID: " + pwd + "> ")
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
        print('')
        file_list= [ f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(),f)) ]
        for i in file_list:
            print('      ' + i)
        print('')
    if query_len>1:
        print('  SYNTAX ERROR - : No parameters expected.')
        print('')
    return

def cd(query_line, query_array, query, query_len):
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
                number=int(input('Pick the directory number: '))
                if number>0 and number<x:
                    path=directories[number]
            except:
                print('Wrong selection')
                print('')
                pass
    else:
        path=query_line.split('cd ')[1]

    try:
        os.chdir(path)
    except:
        print('  No such directory')
        print('')
        pass

    pwd=os.getcwd()
    return pwd

def open_file(query_line, query_array, query, query_len, csv_filename):
    if query_len==1:
        help('o')
        if csv_filename=='':
            print('  No file currently loaded.')
        else:
            print('  Current loaded file:')
            print('  ' + csv_filename)
        print('')

        files={}
        file_list= [ f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(),f)) ]
        if len(file_list)>0:
            x=1;
            for i in file_list:
                files[x]=i
                print(str(x)+':',str(i))
                x+=1
            print('')
            try:
                number=int(input('Pick the file number: '))
                if number>0 and number<x:
                    csv_filename=files[number]
                    print('  Loaded: ' + csv_filename)
            except:
                print('Wrong selection')
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
        print('  SYNTAX ERROR - No new file loaded. Incorrect number of parameters.')
        print('')
    return csv_filename

def columns(query_line, query_array, query, query_len):
    if query_len==1:
        help('c')
        if csv_filename=='':
            print('  ERROR - No file currently loaded.')
            print('')
        else:
            if not os.path.exists(csv_filename):
                print('  ERROR - File disappeared...?')
                print('')
            else:
                print('  Current loaded file:')
                print('  ' + csv_filename)
                print('')
                csv_file=open(csv_filename, 'r')
                file_line=csv_file.readline()
                csv_file.close()
                line_array=file_line.split(delimiter_char)
                line_no=1
                for i in line_array:
                    print(str(line_no)+':',str(i))
                    line_no+=1
                print('')
    else:
        print('  SYNTAX ERROR - No parameters expected.')
        print('')
    return

def view(query_line, query_array, query, query_len):
    start_line=0
    end_line=10
    if query_len==1:
        help('v')
    if csv_filename=='':
        print('  No file currently loaded.')
        print('')
    else:
        if not os.path.exists(csv_filename):
            print('  ERROR -  File disappeared...?')
            print('')
        else:
            print('  Current loaded file:')
            print('  ') + csv_filename
            print('')

            if len(query_array)>1:
                start_line=int(query_array[1])
            if len(query_array)>2:
                end_line=int(query_array[2])
            if len(query_array)<4:
                csv_file=open(csv_filename, 'r')
                file_line=csv_file.readline()
                line_no=1
                while file_line and line_no<=end_line:
                    if line_no>=start_line:
                        print(str(line_no) + ':', file_line)
                    file_line=csv_file.readline()
                    line_no+=1
                csv_file.close()
    return

def delimiter(query_line, query_array, query, query_len, delimiter_char):
    if query_len==1:
        help('d')
    if query_len==2:
        delimiter_char=query_array[1]
        print('  The delimiter character has been changed to:')
        print('  ' + delimiter_char)
        print('')
    if query_len>2:
        print('  SYNTAX ERROR - too many arguments')
        print('')
    return delimiter_char

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
    query_line, query_array, query, query_len=cursor(pwd)
    if query=='':
        help('')
    elif query=='ls' or query=='l':
        list_directory()
    elif query=='cd':
        pwd=cd(query_line, query_array, query, query_len)
    elif query=='open' or query=='o':
        csv_filename=open_file(query_line, query_array, query, query_len, csv_filename)
    elif query=='columns' or query=='c':
        columns(query_line, query_array, query, query_len)
    elif query=='view' or query=='v':
        view(query_line, query_array, query, query_len)
    elif query=='delimiter' or query=='d':
        delimiter_char=delimiter(query_line, query_array, query, query_len, delimiter_char)
    elif query=='quit' or query=='q' or query=='x':
        print('  Thank you for this session!')
        print('  Good bye...')
    else:
        print('Unknown command...')
#quit()
