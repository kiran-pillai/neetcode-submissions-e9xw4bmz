class Solution:
    """
    /neetcode/practice/.../
    """
    def simplifyPath(self, path: str) -> str:
        stack = []
        inter = []
        i=0
        def time_to_append(index, char):
            if index==len(path)-1 or char=='/':
                return True
        for i, char in enumerate(path):
            if char!='/':
                inter.append(char)
            if time_to_append(i, char) and inter:
                stack.append("".join(inter))
                inter=[]
        print("stack",stack)
        output = []
        for path in stack:
            if path == '..' and output:
                output.pop()
            elif path == '.':
                continue   
            else:
                output.append(path)
        print("output", output)
        final_output = []
        for path in output:
            if "." in path and (len(path)==1 or len(path)==2):
                continue
            else:
                final_output.append(path) 
        return "/" + "/".join(final_output)


        
            
            


            

        