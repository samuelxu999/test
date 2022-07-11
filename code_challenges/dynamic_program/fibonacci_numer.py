
import sys
import time
## generate th of fibonacci number
def fib_dp(num):
   i=0
   fib_list=[]
   while(i<num):
      if(i<2):
         fib_list.append(1)
      else:
         fib_list.append(fib_list[-1]+fib_list[-2])
      i+=1

   return fib_list

if __name__ == "__main__":
   if(len(sys.argv)<2 or not sys.argv[1].isnumeric() ):
      print("input number of th Fibonacci sequence.")
   else:
      num_th=int(sys.argv[1])
      start_time=time.time()  
      ret=fib_dp(num_th)
      exec_time=time.time()-start_time

      print("{}th Fibonacci sequence is: {}, running time: {} ms".format(num_th, 
                                 ret[-1], format(exec_time*1000, '.3f')))


