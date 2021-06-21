Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3<br>
4 5 6<br>
9 8 9  <br>
The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is |15 - 17| = 2.

Function description

Complete the diagonalDifference function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers<br>
Return

int: the absolute diagonal difference<br>
Input Format

The first line contains a single integer, n, the number of rows and columns in the square matrix arr.<br>
Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

Constraints<br>
-100 <= arr[i][j] <= 100

Output Format<br>
Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input<br>
3<br>
11 2 4<br>
4 5 6<br>
10 8 -12

Sample Output<br>
15

Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19<br>
Difference: |4 - 19| = 15

Note: |x| is the absolute value of x