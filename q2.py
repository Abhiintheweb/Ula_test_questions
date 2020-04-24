
class PrintDiagonals(object):
    def __init__(self):
        self.test()
    

    def find_diagonals(self, matrix,row,col,n):
        temp = []
        temp_max_row=col
        temp_min_col = row
        while row <= temp_max_row and col >= temp_min_col:
            temp.append(matrix[row][col])
            col -= 1
            row += 1
        return temp

    def diagonals(self,matrix):
        dia_elements = []
        n = len(matrix)
        row,col = 0, 0
        while row < n and col < n:
            val = self.find_diagonals(matrix,row,col,n)
            col += 1
            if col == n:
                col -= 1
                row += 1
            dia_elements.append(val)
        return dia_elements
    def test(self):
        matrix = [[1,2,3],[1,3,2],[3,5,7]]
        res = [[1], [2, 1], [3, 3, 3], [2, 5], [7]]
        result = self.diagonals(matrix)
        if res == result:
            print("Passed testcase 1")
        # print(result)

if __name__ == "__main__":
    PrintDiagonals()
    