import json
import os


class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data[1] < self.data[1]:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data[1] > self.data[1]:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            elif data[0] != self.data[0]:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data
# findLeast method return the node with least element
    def findLeast(self):
        if self.data:
            if self.left is None:
                return self.data
            else:
                return self.left.findLeast()
        else:
            return []

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
            print( self.data),
        if self.right:
            self.right.PrintTree()



def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current
# removeLeast method remove the least element

def deleteNode(root, key):
 # Base Case
    if root is None:
        return root

    # If the key to be deleted is smaller than the root's
    # key then it lies in  left subtree
    if key < root.data[1]:
        root.left = deleteNode(root.left, key)

    # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif(key > root.data[1]):
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None :
            temp = root.right
            root = None
            return temp

        elif root.right is None :
            temp = root.left
            root = None
            return temp

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.data = temp.data

        # Delete the inorder successor
        root.right = deleteNode(root.right , temp.data[1])


    return root

def getStd(file1,line, num):
    file1.readline() #	"personality"
    #Openness
    file1.readline() #  "name": "Openness"
    line = file1.readline()  #"percentile": 0.5706102052484376
    start = line.find(":")+2
    temp= line[start:]
    Openness= float(temp)
    #Conscientiousness
    file1.readline() #  "name": "Conscientiousness"
    line = file1.readline()  #"percentile": 0.5706102052484376
    start = line.find(":")+2
    temp= line[start:]
    Conscientiousness = float(temp)
    #Extraversion
    file1.readline() #  "name": "Extraversion"
    line = file1.readline()  #"percentile": 0.5706102052484376
    start = line.find(":")+2
    temp= line[start:]
    Extraversion = float(temp)
    #Agreeableness
    file1.readline() #  "name": "Agreeableness"
    line = file1.readline()  #"percentile": 0.5706102052484376
    start = line.find(":")+2
    temp= line[start:]
    Agreeableness = float(temp)
    #Emotional
    file1.readline() #  "name": "Emotional"
    line = file1.readline()  #"percentile": 0.5706102052484376
    start = line.find(":")+2
    temp= line[start:]
    Emotional = float(temp)
    #calculate std
    std = (Openness - num[0])**2+(Conscientiousness-num[1])**2+(Extraversion-num[2])**2+(Agreeableness-num[3])**2+(Emotional-num[4])**2
    return std


#num = list(map(float, input("Enter a multiple value: ").split()))
#print("List of floats: ", num)
def get_recommend(num, total_need):
    #num = list(map(float, input("Enter a multiple value: ").split()))
    #print("List of floats: ", num)
    path1 = "movies/package1/fillered.txt"
    path2 = "movies/package2/fillered.txt"
    path3 = "movies/package3/fillered.txt"
    path4 = "movies/package4/fillered.txt"
    path5 = "movies/package5/fillered.txt"
    first = 0
    # Using readlines()
    file1 = open(path1)
    line = file1.readline()
    root = 1
    total = 0
    while(line != ''):
        id_index = line.find("netflixid")
        if(id_index>0):
            total= total+1
            ID_str = line[13:]
            ID = int(ID_str)
            #print("ID is "+ID_str)
            std =getStd(file1, line, num)
            #print("std is: "+str(std))
            if first == 0:
                root = Node([ID, std, 1])
                first = 1
            else:
                root.insert([ID, std, 1])
        line = file1.readline()
    file1.close()

    file2 = open(path2)
    line = file2.readline()
    while(line != ''):
        id_index = line.find("netflixid")
        if(id_index>0):
            total= total+1
            ID_str = line[13:]
            ID = int(ID_str)
            #print("ID is "+ID_str)
            std =getStd(file2, line, num)
            #print("std is: "+str(std))
            root.insert([ID, std, 2])
        line = file2.readline()
    file2.close()

    file3 = open(path3)
    line = file3.readline()
    while(line != ''):
        id_index = line.find("netflixid")
        if(id_index>0):
            total= total+1
            ID_str = line[13:]
            ID = int(ID_str)
            #print("ID is "+ID_str)
            std =getStd(file3, line, num)
            #print("std is: "+str(std))
            root.insert([ID, std, 3])
        line = file3.readline()
    file3.close()

    file4 = open(path4)
    line = file4.readline()
    while(line != ''):
        id_index = line.find("netflixid")
        if(id_index>0):
            total= total+1
            ID_str = line[13:]
            ID = int(ID_str)
            #print("ID is "+ID_str)
            std =getStd(file4, line, num)
            #print("std is: "+str(std))
            root.insert([ID, std, 4])
        line = file4.readline()
    file4.close()

    file5 = open(path5)
    line = file5.readline()
    while(line != ''):
        id_index = line.find("netflixid")
        if(id_index>0):
            total= total+1
            ID_str = line[13:]
            ID = int(ID_str)
            #print("ID is "+ID_str)
            std =getStd(file5, line, num)
            #print("std is: "+str(std))
            root.insert([ID, std, 5])
        line = file5.readline()
    file5.close()

    #root.PrintTree()
    #print("\n\n\n")
    recommend = []
    while total_need >0:
        least = root.findLeast()
        root = deleteNode(root, least[1])
        #root.PrintTree()
        #print("total nodes is "+str(total))
        print("least is :"+str(least[0])+"    "+str(least[1])+"     "+str(least[2]))
        moviePath = "movies/package"+str(least[2])+"/plot.txt"
        plot = open(moviePath)
        line = plot.readline()
        while line:
            #print("Line {}: {}".format(cnt, line.strip()))
            if(line.find(str(least[0]))>0):
                recommend.append([least[0],line])
                break
            line = plot.readline()
        total_need = total_need -1
    return recommend
