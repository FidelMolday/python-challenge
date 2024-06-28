
    #Sequences are a generic term for an ordered set which means that the order in which we input the items will be the same when we access them.

 Input: [1,2,3,4,5]



    #List is a sequence
    #List stores multiples element in a single variable

list=[1,'UG-SEP','dev',1.2,(7,'Python')]

    #List can contain heterogenous element.
    #List is mutable.


#Syntax

List= [ expression(element) for element in old List if condition ]


#List are created using square brackets( [] ) in the square brackets we write elements separating by commas( , )

list=['Welcome','Dev','Community']

#How to create empty list?

# if the square brackets are empty it will considered as empty list
l1=[]
# list() function used to creates list objects
l2=list()

How to take input from user

# Using List comprehension
l1=[eval(i) for i in input("Enter data separating by commas").split(',')]

# So in the above line what happen is that first we will enter in
# list comprehension and take input from user after that it will 
# be split each element using commas as the criteria the split() 
# function split() string on a given criteria and I pass , as the 
# criteria so no the each element separated by , are treated as 
# list element and now the for run and we evaluate the element and 
# assign it.

# using for loop
# create a empty list
l2=list()
# take the size of list
for i in range(0,int(input("Enter the size"))):
# append is a function to add data at the last of the list we will 
# learn about it 
     l2.append(eval(input()))


Syntax

# Let first create a str
s='text'
# let replace 'tex' by 'res' gives 'rest' does not changes in s 
# return str object which i have again stored in s so it become 
# rest
s=s.replace('tex','res')
# find the index of s which is 2
s.find('s')
# count the occurrence of 'st' which is 1
s.count('st')
# split string on the basis of '' empty space means each char will 
# become element of the list l=['r','e','s','t']
l=s.split('')
# join l on the separating by ',' s="r,e,s,t"
s=','.join(l)
# check whether s starts with 'r,e,s' or not True
s.startswith('r,e,s')
# check whether s ends with 's,t' or not True
s.endswith('s,t')
# remove extra white space of '  My  ' using strip s='My'
s='  My  '.strip() 
# lowercase the string
s.lowercase()
# uppercase the string
s.uppercase()


    tuple is immutable
    tuple can store heterogenous element
    tuple elements are separated by ','

t=(1,'Comment','Share',1.5)


#How to create empty tuple

# by using tuple() function which create tuple object
t=tuple()
# by leaving the parenthesis empty
t=()

# using List comprehension we convert the list into tuple using 
# tuple() function let check how
t=tuple([eval(i) for i in input("Enter data separated by commas ").split(',')])


 #create a tuple
t=(1,2,3,4,'blogging',1)
# get the index of 3 in t which is 2
t.index(3)
# count the occurrence of 1 in t which is 2
t.count(1)

# create a sequence
l=[2,5,1,4,3]
# find the len of l which is 5
len(l)
# find the max element which is 5
max(l)
# find the min element which is 1
min(l)
# find the sum which is 15
sum(l)
# sort l but no changes in l return list which is [1,2,3,4,5]
sorted(l)





