# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:03:44 2020
Idea is to take a specification of connections and components
and produce the tree structure in a list visually (whatever that means)
and graphically with components

Idea for implementation:
  first generate non-cyclic tree with dfs, and store in a Tree
  or Graph data structure
  Then reproduce graph without duplicates, so if a component is connected
  to multiple fluid paths, display the component only once
  attached to all fluid paths



@author: me442
"""
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()




class Connection:
  def __init__(self,parent,child):
    self.parent = parent
    self.child = child
    self.parent.outlets.append(child)
    self.child.inlets.append(parent)
  def __repr__(self):
    return self.parent.name+'->'+self.child.name

class Component:
  def __init__(self, name, typE):
    self.name = name
    self.typE =typE
    self.inlets=[]
    self.outlets=[]
    self.x=0
    self.y=0
  def connectInlet(self,fluidpath):
    self.inlets.append(fluidpath)
  def connectOutlet(self,fluidpath):
    self.outlets.append(fluidpath)
  def __repr__(self):
    return self.name
    
class TerminalPath:
  def __init__(self,name):
    self.name=name
    self.direction=None
    self.connections=[]
    self.outlets=[]
    self.inlets=[]
    self.x=0
    self.y=0
  def __repr__(self):
    return self.name
       
class FluidPath:
  def __init__(self,name):
    self.name= name
    self.inlets=[]
    self.outlets=[]
    self.direction=None
    self.x=0
    self.y=0
  def addConnection(fluidpath):
    self.connections.append(fluidpath)
  def removeConnection(fluidpath):
    self.connections.remove(fluidpath)
  def assignDirection(self,direction):
    self.direction=direction
  def __repr__(self):
    return self.name
  
startPath0=TerminalPath('Supply0')
startPath1=TerminalPath('Supply1')
startPath2=TerminalPath('Supply2')
endPath=TerminalPath('Return') 

  
fluid_path0=FluidPath('fluid_path0')
fluid_path1=FluidPath('fluid_path1')
fluid_path2=FluidPath('fluid_path2')
fluid_path3=FluidPath('fluid_path3')
fluid_path4=FluidPath('fluid_path4')



c0 = Component('c0','junction')
c1 = Component('c1','junction')
c2 = Component('c2','junction')
c3 = Component('c3','junction')
c4 = Component('c4','junction')
c5 = Component('c5','junction')

family = []
family.append(Connection(startPath0,c1))
family.append(Connection(startPath0,c2))
family.append(Connection(startPath0,c3))
family.append(Connection(c1,fluid_path1))
family.append(Connection(fluid_path1,c4))
family.append(Connection(c2,fluid_path2))
family.append(Connection(fluid_path2,c4))
family.append(Connection(c3,fluid_path4))
family.append(Connection(c4,fluid_path3))
family.append(Connection(fluid_path3,c5))
family.append(Connection(fluid_path4,c5))
family.append(Connection(c5,endPath))
family.append(Connection(endPath,startPath0))

for i in range(len(family)):
  G.add_node(family[i].parent.name)
  G.add_node(family[i].child.name)
for i in range(len(family)):
  G.add_edge(family[i].parent.name,family[i].child.name)
  

nx.draw(G)
plt.show()



def dfs(root, depth ,items):
  tab = '  '
  print(tab*depth + root.name)
  if(items.get(root)):
    children =items.get(root)
  else: 
    return
  for child in children:
    dfs(child,depth+1,items)
    
class PrintTree:
  def __init__(self):
    self.items = dict()
    self.children = set()
    self.root = []
  def assignKVpairs(self,family):
    for rs in family:
      if(rs.parent not in self.items):
        self.items[rs.parent] = [rs.child]
      else:
        self.items.get(rs.parent).append(rs.child)
      self.children.add(rs.child)
  def findRoot(self,family):
    for k in family:
      if(k.parent not in self.children):
        self.root.append(k.parent)
    return self.root
  def printTree(self):
    for roots in root:
      dfs(roots,0,self.items)
#  
#def bfs(root,depth,items):
#  for k in family:
#    print(k.child)

      
""" perform breadth first search and print out
stuff like horizontal tree"""
      


  
    
  # perform DFS and keep track of depth
  
pt =PrintTree()
pt.assignKVpairs(family)
root = pt.findRoot(family)
pt.printTree()
ins=''
outs=''


        #print(component.parent,' inlets: ',component.parent.inlets)

for component in family:
  if(isinstance(component.parent,Component)):
    print(component.parent,' inlets: ',component.parent.inlets)
print(' ')

for component in family:
  if(isinstance(component.parent,Component)):
    print(component.parent,' outlets: ',component.parent.outlets)

print(' ')
print(' The connection equations are below')
for component in family:
  ins=''
  outs=''
  if(isinstance(component.parent,Component)):
    for i in range(len(component.parent.inlets)):
      if(i==len(component.parent.inlets)-1):
        ins = ins+component.parent.inlets[i].name
      else:
        ins = ins+component.parent.inlets[i].name+'+'
    print(ins,'=',end=" "),
    for i in range(len(component.parent.outlets)):
      if(i==len(component.parent.outlets)-1):
        outs = outs+component.parent.outlets[i].name
      else:
        outs = outs+component.parent.outlets[i].name+'+'
      print(outs,end=" ")
    print(" ")
        
""" Steps
create data structure for collection of relations
choose a hashmap where every parent is a key
and the value is the list of children
for example :
  lifeform -> [animal]
  animal -> [mammal, fish, bird]
  mammal->[cat]
  etc

1. loop through list to put each parent as a key and child as a value
2. Then also put children in a separate set, and find which
key is not in the set to learn which one is the root. 
3. perform DFS starting at root keep track of depth

"""
