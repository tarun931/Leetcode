class Solution {
public:
    string pushDominoes(string dominoes) {
        string ans = "";
        vector<int> disL(dominoes.length(),-1);
        vector<int> disR(dominoes.length(),-1);
        int l= -1;
        for(int i=0;i<dominoes.length();i++)
        {
            if(dominoes[i]=='R'){
                 disL[i]= 0 ;
                 l = i;
            } 
            else if(dominoes[i]=='L')
            {
                disL[i] = -1;
                l = -1;
            } 
            else
            {
                if(l== -1)
                    disL[i] = -1;
                else
                   disL[i] = abs(l-i);    
            }
        }
        int r = -1;
        for(int i = dominoes.length()-1 ; i >= 0 ; i--)
        {
             if(dominoes[i]=='L'){
                 disR[i]= 0 ;
                 r = i;
            } 
            else if(dominoes[i]=='R')
            {
                disR[i] = -1;
                r = -1;
            } 
            else
            {
                if(r== -1)
                    disR[i] = -1;
                else
                   disR[i] = abs(r-i);    
            }
        }
        for(int i=0;i<dominoes.length();i++)
        {
            string ch = "";
            if(disL[i]== -1 && disR[i]== -1)
                ch = ".";
            else if (disL[i]== 0)
               ch = "R";
            else if(disR[i]==0)
               ch = "L";
            else if(disL[i] == -1)
               ch = "L";
            else if(disR[i]== -1)
                ch  = "R";
            else if(disL[i] == disR[i])
                ch = ".";
            else if(disL[i] < disR[i])
                ch = "R";
            else 
                ch = "L";
            ans += ch ;            
                                
        }
        
        return ans;
    }
};