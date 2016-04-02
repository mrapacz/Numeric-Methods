//Maciej Rapacz
#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include <time.h>

#define type double //change type precision here

using namespace std;

struct matrix {
    int rows;
    int columns;
    vector<vector<type> > M;
};

// returns a vector of 1,-1,1,-1, ...
matrix ones(int i) {
    matrix X;
    X.rows = 1;
    X.columns = i;
    vector<type> V;
    while (i--)
        V.push_back((i % 2 * 2) - 1);
    X.M.push_back(V);
    return X;
}

//prints given vector
void printVector(vector<type> V) {
    for (unsigned int i = 0; i < V.size(); i++)
        cout << V[i] << " ";
    cout << endl;
}

//prints given matrix
void printMatrix(matrix M) {
    vector<vector<type> > V = M.M;
    for (unsigned int i = 0; i < V.size(); i++) {
        for (unsigned int j = 0; j < V[i].size(); j++)
            cout << V[i][j] << "\t\t";
        cout << endl;
    }
}

//reads matrix from input.in file
void getMatrix(matrix &A) {
    ifstream input;
    input.open("input.in");
    vector<vector<type> > M;
    input >> A.rows;
    input >> A.columns;
    for (int j = 0; j < A.rows; j++) {
        vector<type> row;
        for (int i = 0; i < A.columns; i++) {

            type a;
            input >> a;
            row.push_back(a);
        }
        M.push_back(row);
    }
    A.M = M;
    input.close();
}

//multiplies two matrices
matrix multiply(matrix &A, matrix &B) {
    matrix C;
    if (A.columns != B.rows) {
        cout << "Did not manage to multiply matrixes, because of wrong dimensions: " << A.rows << "x" << A.columns <<
        " * " << B.rows << "x" << B.columns << endl;
        return C;
    }

    C.rows = A.rows;
    C.columns = B.columns;
    for (int i = 0; i < C.rows; i++) {
        vector<type> row;
        for (int j = 0; j < C.columns; j++) {
            double sum = 0;
            for (int k = 0; k < A.columns; k++) {
                sum += A.M[i][k] * B.M[k][j];
            }
            row.push_back(sum);
        }
        C.M.push_back(row);
    }
    return C;
}

//returns tranposition of given matrix
matrix transpose(matrix A) {
    matrix B;
    B.rows = A.columns;
    B.columns = A.rows;
    for (int i = 0; i < A.columns; i++) {
        vector<type> V;
        for (int j = 0; j < A.rows; j++)
            V.push_back(A.M[j][i]);
        B.M.push_back(V);
    }
    return B;
}

//multiplies each element of given vector by given j constant
vector<type> scale(vector<type> V, type j) {
    for (unsigned int i = 0; i < V.size(); i++)
        V[i] *= j;
    return V;
}

//swaps two rows in a given matrix
void swaprows(matrix &A, int i, int j) {
    if (i == j) return;
    vector<type> X;
    X = A.M[i];
    A.M[i] = A.M[j];
    A.M[j] = X;
}

//scales and substracts one row from another in order to generate a zero at the beginning
void modify(vector<type> &A, vector<type> &B, type scale, unsigned int j) {

    B[j] = 0;
    for (unsigned int i = j + 1; i < B.size(); i++) {
        //cout << "B[i] " << B[i] << " scale: " << scale << " A[i] " << A[i] << endl;
        B[i] = type(B[i] * scale) - type(A[i]);
    }
}

//gauss elimination method
matrix gauss(matrix &A) {
    int j = 0;
    int i = 0;
    while (i < min(A.rows, A.columns) && j < A.columns) {
        // i == row number
        bool allZeroes = true;
        int k = i;
        while (k < A.rows && allZeroes) {
            if (A.M[k][j] != 0) allZeroes = false;
            else k++;
        }
        if (allZeroes) {
            j++;
            continue;
        }
        swaprows(A, i, k); // A[i][j] != 0 now
        for (int k = i + 1; k < A.rows; k++) {
            if (A.M[k][j] == 0) continue;
            type scale;
            scale = type(A.M[i][j]) / type(A.M[k][j]);
            //cout << scale << endl;
            modify(A.M[i], A.M[k], scale, j);
        }
        i++;
    }
    return A;
}

//puts matrix A and Y together as a new matrix
matrix AY(matrix A, matrix Y) {
    for (unsigned int i = 0; i < A.M.size(); i++)
        A.M[i].push_back(Y.M[i][0]);
    return A;
}

//retrieves x values from the matrix after Gauss elimination method
vector<type> getResult(matrix &A, matrix &G) {
    vector<type> newX(A.columns, 0);
    for (int i = A.columns - 1; i >= 0; i--) {
        type sum = G.M[i][A.columns];
        for (int j = i + 1; j < A.columns; j++) {

            sum -= type(G.M[i][j] * newX[j]);

        }
        if (G.M[i][i] == 0) cout << "blad" << endl;
        else {
            newX[i] = type(sum / G.M[i][i]);
        }
    }
    return newX;
}

//computes a norm of difference between two vectors
double getNorm(vector<type> &A, vector<type> &B) {
    if (A.size() == B.size()) {
        double sum = 0;
        for (int i = 0; i < A.size(); i++) {
            sum += (A[i] - B[i]) * (A[i] - B[i]);
        }
        return sqrt(sum);
    }
    else return -1;
}

//returns the matrix presented in the first task
matrix taskOne(int n) {
    matrix A;
    A.columns = A.rows = n;
    for (int i = 1; i <= n; i++) {
        vector<type> V;
        for (int j = 1; j <= n; j++) {
            type x;
            if (i == 1) x = type(1);
            else x = type(1) / type(i + j - 1);
            V.push_back(x);
        }
        A.M.push_back(V);
    }
    return A;
}

//returns the matrix presented in the second task
matrix taskTwo(int n) {
    matrix A;
    A.columns = A.rows = n;
    for (int i = 1; i <= n; i++) {
        vector<type> V;
        for (int j = 1; j <= n; j++) {
            type x;
            if (i <= j) x = type(2 * i) / type(j);
            else x = type(2 * j) / type(i);
            V.push_back(x);
        }
        A.M.push_back(V);
    }
    return A;
}


//returns the tridiagonal matrix presented in the third t
matrix taskThree(int n, int k, int m) {
    matrix A;
    A.columns = A.rows = n;
    for (int i = 1; i <= n; i++) {
        vector<type> V;
        for (int j = 1; j <= n; j++) {
            type x;
            if (i == j) x = type(k);
            else if (j == i + 1) x = type(1 / type(i + m));
            else if (j == i - 1) x = type(k / type(i + m + 1));
            else x = 0;
            V.push_back(x);
        }
        A.M.push_back(V);
    }
    return A;
}

//thomas algorithm for a given nxn matrix G = AY
//returns vector of sought x values
vector<type> thomas(matrix &A, matrix &G) {
    vector<type> newX(A.columns, 0);
    if (A.columns > 1) {
        G.M[0][A.columns] /= G.M[0][0];
        G.M[0][1] /= G.M[0][0];
    }
    for (int i = 1; i < A.columns; i++) {
        type ci = G.M[i][i + 1];
        type bi = G.M[i][i];
        type ai = G.M[i][i - 1];
        type di = G.M[i][A.columns];
        type prevc = G.M[i - 1][i];
        type prevd = G.M[i - 1][A.columns];
        if (i < A.columns - 1) G.M[i][i + 1] = type(ci) / type(bi - ai * prevc);
        G.M[i][A.columns] = type(di - ai * prevd) / type(bi - ai * prevc);
    }
    newX[A.columns - 1] = G.M[A.columns - 1][A.columns];
    for (int i = A.columns - 2; i >= 0; i--) {
        type ci = G.M[i][i + 1];
        type di = G.M[i][A.columns];

        newX[i] = di - ci * newX[i + 1];
    }
    return newX;
}

//returns the difference between the time given as an argument and current time
double getTime(clock_t &tStart) {
    return (double) (clock() - tStart) / CLOCKS_PER_SEC;
}


//thomas algorithm for nx3 matrix
vector<type> thomas2(matrix A, matrix &Y) {
    vector<type> newX(A.rows, 0);
    if (A.rows > 1) {
        Y.M[0][0] /= A.M[0][0];
        A.M[0][1] /= A.M[0][0];
    }
    for (int i = 1; i < A.rows; i++) {
        type ci = A.M[i][2];
        type bi = A.M[i][1];
        type ai = A.M[i][0];
        type di = Y.M[i][0];
        type prevc = A.M[i - 1][2];
        type prevd = Y.M[i - 1][0];

        if (i < A.rows - 1) A.M[i][2] = type(ci) / type(bi - ai * prevc);
        Y.M[i][0] = type(di - ai * prevd) / type(bi - ai * prevc);
    }
    newX[A.rows - 1] = Y.M[A.rows - 1][0];
    for (int i = A.rows - 2; i >= 0; i--) {
        type ci = A.M[i][2];
        type di = Y.M[i][0];

        newX[i] = di - ci * newX[i + 1];
    }
    return newX;
}
//converts an nxn tridiagonal matrix to nx3
matrix tridiagonalToNormal(matrix A) {
    matrix B;
    B.rows = A.rows;
    B.columns = 3;
    for (int i = 0; i < A.rows; i++) {
        int j = i - 1;
        vector<type> V;
        if (i == 0) j++;
        if (i == A.rows - 1) j--;
        for (int k = 0; k < 3; k++) V.push_back(A.M[i][j++]);
        B.M.push_back(V);
    }
    return B;
}

//converting and solving matrix with thomas algorithm
vector<type> solveThomasSaveMem(int n, int k, int m) {
    matrix A = taskThree(n, k, m);
    matrix X = ones(n);
    X = transpose(X);
    matrix Y = multiply(A, X);
    vector<type> V = thomas2(tridiagonalToNormal(A), Y);
    X = transpose(X);
    return V;
}


void solveForX(int n, int task, int method) {
    matrix A;
    if (task == 1) A = taskOne(n);
    if (task == 2) A = taskTwo(n);
    if (task == 3) A = taskThree(n, 5, 4);
    //printMatrix(A);
    matrix X = ones(A.columns);
    X = transpose(X);
    matrix Y = multiply(A, X);
    matrix G = AY(A, Y);
    vector<type> result;


    clock_t tStart;

    if (method == 0) {
        tStart = clock();
        gauss(G);
        result = getResult(A, G);

    }
    else if (method == 1) {
        tStart = clock();
        result = thomas(A, G);

        //result = thomas2(A, Y);
    }
    //uncomment to print time of algorithm
    //cout << n << ":" << getTime(tStart) << endl;

    X = transpose(X);
    cout << n << ": " << getNorm(result, X.M[0]) << endl;

}



int main() {

    for (int i = 1; i <= 10; i++) {
        solveForX(i, 3, 1);
        //n - matrix size
        //task - matrix of type 1, 2 or 3
        //method - 0=Gauss, 1=Thomas
    }
    return 0;
}
