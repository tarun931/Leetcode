class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        word_set = set(wordlist)
        word_case_map = {}
        word_vowel_map = {}
        for i in wordlist:
            if i.lower() not in word_case_map:
                word_case_map[i.lower()] = i
            new = (
                i.lower()
                .replace("a","#")
                .replace("e","#")
                .replace("i","#")
                .replace("o","#")
                .replace("u","#")
                )
            if new not in word_vowel_map:
                word_vowel_map[new] = i

        res = []
        for q in queries:
            if q in word_set:
                res.append(q)
            elif q.lower() in word_case_map:
                res.append(word_case_map[q.lower()])
            else:
                new = (
                q.lower()
                .replace("a","#")
                .replace("e","#")
                .replace("i","#")
                .replace("o","#")
                .replace("u","#")
                )
                if new in word_vowel_map:
                    res.append(word_vowel_map[new])
                else:
                    res.append("")
        return res