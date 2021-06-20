def ps(array,multiplier=1):
      total=0
      
      for ele in array:
            if type(ele) is list:
               total += ps(ele,multiplier+1)
            else:
               total += ele
      return total* multiplier