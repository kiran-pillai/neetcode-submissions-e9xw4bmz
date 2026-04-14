from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        gw_counter = 0
        for word in words:
            is_good = True
            freq_map = Counter(chars)
            for w in word:
                if w not in freq_map:
                    is_good = False
                    break
                freq_map[w]-=1
                if freq_map[w] == 0:
                    del freq_map[w]
                print(freq_map)
            if is_good:
                gw_counter += len(word)
        return gw_counter
                