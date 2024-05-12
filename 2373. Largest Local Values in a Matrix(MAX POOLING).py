def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    ans = [[0]*(n-2) for _ in range(n-2)]
    for i in range(n-2):
        for j in range(n-2):
            tempM = 0
            for x in range(i,i+3):
                for y in range(j,j+3):
                    tempM = max(tempM,grid[x][y])
            ans[i][j] = tempM
    return ans
'''
Purpose of Max Pooling:
Dimensionality Reduction: Reduces the size of the input feature maps, leading to less computational overhead in subsequent layers.
Feature Dominance: Promotes the most prominent features by selecting the maximum value in the pooling window, which helps in making features invariant to small translations.
Prevent Overfitting: By providing an abstracted form of the representation, it helps to prevent overfitting in the neural network model.
'''
def max_pooling(input_feature_map, kernel_size=2, stride=2):
    # Extract the dimensions of the input feature map
    n_rows, n_cols = input_feature_map.shape

    # Calculate the size of the output feature map
    output_rows = (n_rows - kernel_size) // stride + 1
    output_cols = (n_cols - kernel_size) // stride + 1
    pooled_feature_map = np.zeros((output_rows, output_cols))

    # Perform max pooling
    for i in range(output_rows):
        for j in range(output_cols):
            row_start = i * stride
            row_end = row_start + kernel_size
            col_start = j * stride
            col_end = col_start + kernel_size

            # Find the maximum in each window
            pooled_feature_map[i, j] = np.max(input_feature_map[row_start:row_end, col_start:col_end])

    return pooled_feature_map

'''
actually here the problem is let the stride = 1 and kernel_size = 3
'''
