class Solution:
    def calPoints(self, operations: List[str]) -> int:
        final_score = 0
        score_list = []

        for i in range(len(operations)):

            if operations[i] == "+":
                score_list.append(score_list[-1] + score_list[-2])
            
            elif operations[i] == "C":
                score_list.pop()

            elif operations[i] == "D":
                score_list.append(2  * score_list[-1])

            else:
                score_list.append(int(operations[i]))



        for num in score_list:
            final_score += num

            
        return final_score
        