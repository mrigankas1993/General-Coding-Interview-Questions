# Suffix Array Data Structure
class suffix_Array:
    def __init__(self, s1):
        self.suf_arr = []
        for i in range(len(s1)):
            self.suf_arr.append(s1[-i + 1:])
        self.suf_arr.sort()
    def lcp_array(self):
        self.lcp = [0]
        for i in range(len(self.suf_arr) - 1):
            c = self.suf_arr[i]
            f = self.suf_arr[i + 1]
            len1 = len(c)
            len2 = len(f)
            count = 0
            for j in range(min(len1, len2)):
                if c[j] == f[j]:
                    count += 1
                else:
                    break
            self.lcp.append(count)
        return self.lcp
A = suffix_Array("ABABBAB")
print(A.lcp_array())

                
                           
                           
                           
            
            
            
            
        
        

            
            
            
