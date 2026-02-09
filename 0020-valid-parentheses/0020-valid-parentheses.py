class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(0,len(s)):
            if s[i] in ('(', '{' , '['):
                st.append(s[i])
            else:
                if s[i] == ')':
                    if (not st) or (st and (( st[-1]) != '(')):
                        return False
                    elif st and st[-1]=='(':
                        st.pop()
                elif s[i] == '}':
                    if (not st) or ((st) and ((st[-1]) != '{')):
                        return False
                    elif st and st[-1]=='{':
                        st.pop()
                elif s[i] == ']':
                    if (not st) or ((st) and (( st[-1]) != '[' )):
                        return False
                    elif st and st[-1]=='[':
                        st.pop()        
        if st :
            return False
        return True                            

        