
import sys
import time

def grid_traverse(row,col, memo={}):
   key= str(row)+','+str(col)

   ## direct return value given a duplicated tree
   if(key in memo):
      return memo[key]

   ## retrun 1 step until the destination (1,1)
   if(row==1 and col==1):
      return 1

   ## return 0 for steps out of gird.
   if(row==0 or col==0):
      return 0

   ## sum memory of children binary tree for a new node (m,n)
   memo[key]=grid_traverse(row-1,col, memo) + grid_traverse(row,col-1, memo)

   return memo[key]

if __name__ == "__main__":
   if(len(sys.argv)<3 or not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric() ):
      print("input dimension of a gird (m, n).")
   else:
      m=int(sys.argv[1])
      n=int(sys.argv[2])
      start_time=time.time()  
      ret=grid_traverse(m,n)
      exec_time=time.time()-start_time

      print("Traverse grid ({},{}) has solutions: {}, running time: {} ms".format(m,n, 
                                 ret, format(exec_time*1000, '.3f')))


