# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m,n = len(matrix),len(matrix[0])
        row = 0
        col = n-1
        while row<m and 0<=col:
            if matrix[row][col]<target:
                row += 1
            elif matrix[row][col]>target:
                col -= 1
            else:
                return True
        return False
''' CPP version solution
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int r = 0;
        int c = matrix[0].size()-1;
        int m =matrix.size();
        while (r<m && c>=0){
            if (matrix[r][c]<target){
                r+=1;
            }else if(matrix[r][c]>target){
                c-=1;
            }else{
                return true;
            }
        }
        return false;
    }
};
'''