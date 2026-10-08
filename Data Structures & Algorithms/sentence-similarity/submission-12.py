class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False
        
        pairs = {(sim1, sim2) for sim1, sim2 in similarPairs}
        for i in range(len(sentence1)):
            if (
                sentence1[i] != sentence2[i] and
                (sentence1[i], sentence2[i]) not in pairs and
                (sentence2[i], sentence1[i]) not in pairs
            ):
                return False

        return True

        