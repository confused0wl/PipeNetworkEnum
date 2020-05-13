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
  def connectInlet(self,fluidpath):
    self.inlets.append(fluidpath)
  def connectOutlet(self,fluidpath):
    self.outlets.append(fluidpath)
    
class TerminalPath:
  def __init__(self,name):
    self.name=name
    self.direction=None
    self.connections=[]
    self.outlets=[]
    self.inlets=[]
    
    
class FluidPath:
  def __init__(self,name):
    self.name= name
    self.inlets=[]
    self.outlets=[]
    self.direction=None
    self.typE = 'FluidPath'
  def addConnection(fluidpath):
    self.connections.append(fluidpath)
  def removeConnection(fluidpath):
    self.connections.remove(fluidpath)
  def assignDirection(self,direction):
    self.direction=direction
  def __repr__(self):
    return self.name
  
startPath=TerminalPath('Supply')
startPath.direction = 'east'
endPath=TerminalPath('Return') 
endPath.direction = 'west' 
  
fluid_path0=FluidPath('fluid_path0')
fluid_path0.assignDirection('east')
fluid_path0_0=FluidPath('fluid_path0_0')
fluid_path0_1=FluidPath('fluid_path0_1')
fluid_path0_1_0=FluidPath('fluid_path0_1_0')
fluid_path0_1_1=FluidPath('fluid_path0_1_1')
fluid_path1=FluidPath('fluid_path1')
fluid_path0.assignDirection('west')
fluid_path2=FluidPath('fluid_path2')
fluid_path0.assignDirection('north')
fluid_path3=FluidPath('fluid_path3')
fluid_path0.assignDirection('south')

c0 = Component('c0','junction')
c1 = Component('c1','junction')
c2 = Component('c2','junction')
c3 = Component('c3','junction')
c4 = Component('c4','junction')
c5 = Component('c5','junction')

family = []
family.append(Connection(startPath,c0))
family.append(Connection(c0,fluid_path0))
family.append(Connection(fluid_path0,c1))
family.append(Connection(c1,fluid_path0_0))
family.append(Connection(c1,fluid_path0_1))
family.append(Connection(fluid_path0_1,c2))
family.append(Connection(c2,fluid_path0_1_0))
family.append(Connection(c2,fluid_path0_1_1))

family.append(Connection(c0,fluid_path1))
family.append(Connection(c0,fluid_path2))
family.append(Connection(c0,fluid_path3))

family.append(Connection(fluid_path0_1_0,c3))
family.append(Connection(c3,endPath))
family.append(Connection(fluid_path0_1_1,c3))


family.append(Connection(fluid_path1,c3))
family.append(Connection(fluid_path2,c3))
family.append(Connection(fluid_path3,c3))





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
    self.root = None
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
        self.root = k.parent
    return self.root
  def printTree(self):
    dfs(self.root,0,self.items)
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
