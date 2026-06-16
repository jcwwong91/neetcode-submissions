class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = list()

        for op in operations:
            if op == "+":
                record.append(record[-1] + record[-2])
            elif op == "C":
                record.pop()
            elif op == "D":
                record.append(record[-1] * 2)
            else:
                score = int(op)
                record.append(score)

        return sum(record)