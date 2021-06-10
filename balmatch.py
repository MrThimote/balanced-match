import re

## Get a balanced match in a string
## For an example balanced_match("{", "}", "a{b{c{}}}d}") returns
## (1, 8, 'b{c{}}') with the start of the { the start of the end } and the string
## Also works with regex for example balanced_match("({)|(\[)", "}", "a{b[c{}}}d}")
## returns (1, 8, 'b[c{}}')
def balanced_match(a, b, str):
    ## Compile the two regular expressions
    re_a = re.compile(a)
    re_b = re.compile(b)

    ## Get all occurences of the expressions and add coefficients
    ## 1 is for an openning sequence and -1 for the closing
    re_l = list(map(lambda x:(1,x), re_a.finditer(str)))
    re_l.extend(list(map(lambda x:(-1,x) , re_b.finditer(str))))
                
    ## Sort the occurences by the start of the regular expressions
    re_l.sort(key=lambda x: x[1].start())

    ## Get the first occurence of the openning sequence by checking the first with a one coefficient
    index = 0
    for index in range(len(re_l)):
        if re_l[index][0] == 1:
            break
    ## If there is no openning sequence, stop the programm
    if index == len(re_l):
        return (-1, -1, "")

    ## Get the starting index and the start sequence
    sindex = re_l[index][1].span()[1]
    sre = re_l[index][1]
    ## Create the end index and count of sequence
    eindex = -1
    count = 0
    ## While there is a sequence (openning or closing)
    while index < len(re_l):
        ## Add the data to the count (At first iteration will always be 1)
        count += re_l[index][0]
        ## If there is a balanced match, at some point it will close
        if count == 0:
            ## We set the end index to the actual sequence (must be closing because count must always be
            ## zero if closing (coefficients are only 1 or -1))
            eindex = re_l[index][1].start()
            ## Match found, we break
            break
        ## We increase the index
        index += 1
    ## If no match was found and the endindex is -1 we return no match
    if eindex == -1:
        return (-1, -1, "")
    ## Otherwise, we return the start of the start, the start of the end and the string that is between
    ## both data
    return (sre.start(), re_l[index][1].start(), str[sindex:eindex])
