def open_file():
    '''None->file object
    Function will prompt the user for a file-name, and try to open that file If the file exists, it will return the file
    object; otherwise it will re-prompt until it can successfully open the file
    '''
    while True:
        try:
            file=open(input("Enter the name of the file: ").strip())
            return file

        except FileNotFoundError:
            print("There is no file with that name. Try again.")


def remove_punc(word):#own function
    '''(str)->(str or empty string)
    Precondition: Parameter must be a string
    Description: Function takes a string as input and gets rid of any character that isn't a letter
    '''
    if len(word)>=2:
        if word.isalpha()==False:
            for letter in word:
                if letter.isalpha()==False:
                    word=word.replace(letter,'')
    else:
        word=word.replace(word,'')

    return word

def remove_punc2(word):#own function
    '''(str)->(str or empty string)
    Precondition: Parameter must be a string
    Description: Function takes a string as input and gets rid of any character that isn't a letter, space or a number
    '''
    if word.isalpha()==False:
        for letter in word:
            if letter.isalpha()==False and letter!=' ' and letter not in ['0','1','2','3','4','5','6','7','8','9']:
                word=word.replace(letter,'')

    return word

def make_dict(lsw):#own function
    '''(list)->(dictionnary)
    Precondition: Parameter must be a list
    Description: Function takes a list as parameter and returns a dictionnary with the keys being the elements in the list and the values being the line in the file
    '''
    d={}
    
    for i in range(len(lsw)):
        for word in lsw[i]:
            if word in d:
                    d[word].update({i+1})
            else:
                d[word]={i+1}
    return d


def read_file(fp):
    '''(file object)->dict
    Function reads the contents of the file line by line, processes them and stores them in a dictionary
    '''
    x=fp.read().lower().splitlines()
    newlst=[]
    clean_lst=[]

    
    for element in x:
        newlst.append(element.split(' '))

    for i in range(len(newlst)):
        clean_lst.append([])
        for word in newlst[i]:
            if remove_punc(word)!='':
                clean_lst[i].append(remove_punc(word))
            
    dictionnary=make_dict(clean_lst)

    return dictionnary

def is_valid(D, query):#own function
    '''(dictionnary,str)->(str or Bool)
    Precondition: Parameters must be a string and a dictionnary
    Description: Function checks if dictionnary contains the word(s) 
    '''
    query=query.split()

    if query==[]:
        return ''

    else:
        for i in range(len(query)):
            if D.get(query[i])==None:
                return query[i]

        return True

    
def find_coexistance(D, query):
    '''(dict,str)->list
    Function returns the lines that the words coexist in
    '''
    sets=[]
    query=query.split()

    
    for i in range(len(query)):
        sets.append(D[query[i]])

    if len(sets)==1:
        return sorted(list(sets[0]))

    elif len(sets)>1:
        x=sets[0].intersection(sets[1])
        for j in range(len(sets)-1):
            x=x.intersection(sets[j])
    else:
        return ''
    
    return sorted(list(x))

    
        
##############################
# main
##############################
file=open_file()
d=read_file(file)
flag=True

while flag:
    query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    query=remove_punc2(query)
    
    if query=='q':
        flag=False

    elif is_valid(d,query)!=True:
        print("Word '"+str(is_valid(d,query))+"' not in the file")

    elif find_coexistance(d, query)==[]:
        print("The one or more words you entered does not coexist in a same line of the file")
        
    else:
        print("The one or more words you entered coexisted in the following lines of the file")
        y=find_coexistance(d,query)
        for item in range(len(y)):
            print(y[item],end=' ')
        print('\n')
