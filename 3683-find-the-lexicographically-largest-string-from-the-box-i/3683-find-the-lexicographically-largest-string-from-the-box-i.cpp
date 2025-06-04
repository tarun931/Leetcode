string lastSubstring(string s) {
        int i = 0, j = 1, n = s.size();
        while (j < n) {
            int k = 0;
            while (j + k < n && s[i + k] == s[j + k]) {
                k++;
            }
            if (j + k < n && s[i + k] < s[j + k]) {
                int t = i;
                i = j;
                j = max(j + 1, j + k );
            } else {
                j = j + k + 1;
            }
        }
        return s.substr(i, n - i);
    }
class Solution {
public:
    string answerString(string word, int numFriends) {
       if (numFriends == 1) {
            return word;
        }
        string last = lastSubstring(word);
        int n = word.size(), m = last.size();
        return last.substr(0, min(m, n - numFriends + 1));
    }
};