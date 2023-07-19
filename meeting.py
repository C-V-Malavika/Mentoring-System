#SOFTWARE DEVELOPMENT PROJECT - MALAVIKA C V, MADHUKRISHAA N K

import ctypes

class Empty(Exception):
    pass


class Stack:

    '''Implementing a stack using dynamic array approach'''

    def __init__(self,capacity):

        '''The aim of this function is to initialise the 
        value of data members.'''

        self._capacity=capacity
        self._top=0
        self._item=self.makearray(self._capacity)
    #end of the function __init__

    
    def makearray(self,cap):

        '''The aim of this function is to create an array 
        of specified capacity.'''

        return (cap*ctypes.py_object)()
    #end of the function makearray


    def resize(self,cap):

        '''The aim of this function is to increase the size of the array 
        by the specified capacity.'''

        B=self.makearray(cap)
        for i in range(self._top):
            B[i]=self._item[i]
        
        self._item=B
        self._capacity=cap
    #end of function resize
    

    def isempty(self):

        '''The aim of this function is to check whether the 
        stack is empty or not.'''

        return self._top==0
    #end of the function isempty


    def push(self,element):

        '''The aim of this function is add an element to the 
        stack.'''

        if self._top==self._capacity:
            self.resize(2*self._capacity)
        self._item[self._top]=element
        self._top+=1
    #end of the function push


    def pop(self):

        '''The aim of this function is remove an element from
        the stack.'''

        if self.isempty():
            raise Empty("Stack is Empty!!!")
        else:
            popped_item=self._item[self._top-1]
            self._item[self._top-1]=None
            self._top-=1
        return popped_item
    #end of the function pop
    

    def __len__(self):

        '''The aim of this function is return the length of 
        the stack.'''

        return self._top
    #end of the function __len__


    def __getitem__(self,index):

        '''The aim of this function is return the element
        the stack given the index of the element.'''

        return self._item[index]
    #end of the function __len__


    def peek(self):

        '''The aim of this function is return the top element
        of the stack.'''

        return self._item[self._top-1]
    #end of the function __len__
    

    def __str__(self):

        '''The aim of this function is return the
        the stack for printing purpose.'''
        
        try:
            List=[]
            for i in range(self._top):
                List+=[self[i]]
            return str(List)
        except ValueError:
            return []
    #end of the function __str__

def prev_Meeting_details(filename):

    import csv
    try:
        with open(filename,"r") as f:
            reader = csv.reader(f, delimiter=',')
            DATA=[]
            for row in reader:
                DATA.append(row)
            f.close()
        return DATA
    except FileNotFoundError:
        pass


def LoadMeeting_dtls(filename,DATA):

    '''this function is used to load the
      details into the respective csv file'''

    import csv

    with open(filename,"w",newline="") as f:
        writer=csv.writer(f)
        for row in DATA:
            writer.writerow(row)


def Adding_to_stack(DATA,Stack):

    '''this function is used to collect the entire csv file
    data and store it in a single respective stack'''

    try:
        for data in DATA:
            Stack.push(data)
    except TypeError:
        pass


def Displaying_from_stack(Stack):

    '''this function is used to print the data
    from the stack in the reverse order so that
    the latest meeting details will be at the top'''
    list_data=[]
    for item in range(len(Stack)):
        ele=Stack.pop()
        list_data.append(ele)
    return list_data