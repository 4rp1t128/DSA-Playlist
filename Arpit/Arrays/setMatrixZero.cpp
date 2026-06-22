#include <bits/stdc++.h>
using namespace std;

void setMatZero(vector<vector<int>> &arr, int row, int col)
{
    int col0 = 1;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            if (arr[i][j] == 0)
            {
                arr[i][0] = 0; // mark the ith row
                if (j != 0)
                {
                    arr[0][j] = 0; // mark the jth column
                }
                else
                {
                    col0 = 0;
                }
            }
        }
    }
    for (int i = 1; i < row; i++)
    {
        for (int j = 1; j < col; j++)
        {
            if (arr[i][j] != 0)
            {
                if (arr[0][j] == 0 || arr[i][0] == 0)
                {
                    arr[i][j] = 0;
                }
            }
        }
    }
    if (arr[0][0] == 0)
    {
        for (int j = 0; j < col; j++)
        {
            arr[0][j] = 0;
        }
    }
    if (col0 == 0)
    {
        for (int i = 0; i < row; i++)
        {
            arr[i][0] = 0;
        }
    }
}

void displayMatrix(vector<vector<int>> &arr, int row, int col)
{
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}
int main()
{
    int row, col;
    cout << "Enter the row and column of a matrix: ";
    cin >> row >> col;
    vector<vector<int>> mat(row, vector<int>(col, 0));
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cin >> mat[i][j];
        }
    }
    displayMatrix(mat, row, col);
    setMatZero(mat, row, col);

    return 0;
}