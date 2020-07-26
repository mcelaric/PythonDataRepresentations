"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.

CodeSkulptor URL - https://py3.codeskulptor.org/#user305_BTtdAlDDdp_14.py

"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between 
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    
    rtn_val = 0
    #print("len(line1) is" , len(line1), "len(line2) is" , len(line2))
    if line1 == line2:
        rtn_val = IDENTICAL
#     elif (line1 in line2):
#         rtn_val = len(line1)
#     elif (line2 in line1):
#         rtn_val = len(line2)    
    else:
        for idx in range(len(line1)):
            if line1[idx] != line2[idx]:
                #print("line1[idx] = ", line1[idx],  "line2[idx] = ", line2[idx])
                rtn_val = idx 
                break

    return rtn_val


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    rtn_val = ""
    if idx != -1:
        if len(line1) <= idx or len(line2) <= idx: 
            rtn_val = ""
        elif line1[-1:] == "\n" or line2[-1:] == "\n" or line1[-1:] == "\r" or line2[-1:] == "\r": 
            rtn_val = ""
        else:
            sld = singleline_diff(line1, line2)
            if idx == sld:
                rtn_val = "".join((line1 , "\n" , ("=" * (idx)) , "^\n" , line2 , "\n"))
    return rtn_val

"""    
#expected 3 but received 0
print(singleline_diff('abc', 'abcd'))

# expected 'abc\n=^\nabd\n' but received ''
print(singleline_diff_format('abc', 'abd', 1))
 
#expected '\n^\na\n' but received (Exception: IndexError) "string index out of range" at line 62, in singleline_diff_format
print(singleline_diff_format('abc', 'abd', 2) )

#expected 'abc\n==^\nabd\n' but received 'abc\n==^\nabd'
print(singleline_diff_format('', 'a', 0) )

#expected '' but received 'abcdefg\n=====^\nabc\n'
print(singleline_diff_format('abcdefg', 'abc', 5)) 

#expected 'bc\n^\nabc\n' but received ''
print(singleline_diff_format('bc', 'abc', 0)) 
"""

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    line_num = 0
    return_tuple = (IDENTICAL, IDENTICAL)
    
    diff_found = False
    short_list = lines1
    long_list = lines2  
    
    if len(lines1) > len(lines2):
        short_list = lines2
        long_list = lines1 
            
    for ndx in range(len(short_list)):
        line_diff = singleline_diff(long_list[ndx], short_list[ndx])
        if line_diff != -1:
            print(singleline_diff_format(long_list[ndx], short_list[ndx], line_diff))
            diff_found = True
            return_tuple = (line_num, line_diff)
            break
        else:
            line_num += 1   
    
    
    
    return return_tuple


# expected (0, 3) but received (1, 4)
#print(multiline_diff(['taco', 'fishing'], ['tackle', 'fish'])) 

# expected (2, 0) but received (-1, -1)
print(multiline_diff(['line1', 'line2'], ['line1', 'line2', 'line3']))

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list_of_lines = []
    datafile1 = open(filename, "rt")

    for line in datafile1.readlines():
        if line.rfind("\n") != -1  or line.rfind("\r") != -1:
            list_of_lines.append(line[:-1])
        else:
            list_of_lines.append(line)
    
    datafile1.close()
    
    return list_of_lines

#print('get_file_lines("the_idiot.txt")')
#print(get_file_lines("the_idiot.txt"))

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    return ""