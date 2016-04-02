#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include <iomanip>

#define type double //change type precision here

using namespace std;

struct matrix {
    int rows;
    int columns;
    vector<vector<type>> M;
};

// returns a vector of 1,-1,1,-1, ...
matrix ones(int i, int option = 0) {
    matrix X;
    X.rows = 1;
    X.columns = i;
    vector<type> V;
    while (i--) {
        if (option == 0)V.push_back((i % 2 * 2) - 1);
        else if (option == 1) V.push_back(type(0));
        else V.push_back(type(option));
    }
    X.M.push_back(V);
    return X;
}

void printVector(vector<type> &V) {
    for (unsigned int i = 0; i < V.size(); i++)
        cout << V[i] << " ";
    cout << endl;
}

void printMatrix(matrix &M) {
    vector<vector<type>> V = M.M;
    for (unsigned int i = 0; i < V.size(); i++) {
        for (unsigned int j = 0; j < V[i].size(); j++)
            cout << setw(20) << V[i][j];
        cout << endl;
    }
}

void getMatrix(matrix &A) {
    ifstream input;
    input.open("input.in");
    if (!input.is_open()) cout << "wtf" << endl;
    vector<vector<type>> M;
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

matrix multiply(matrix A, matrix B) {
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
                sum += type(A.M[i][k] * B.M[k][j]);
            }
            row.push_back(sum);
        }
        C.M.push_back(row);
    }
    return C;
}

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

vector<type> scale(vector<type> V, type j) {
    for (unsigned int i = 0; i < V.size(); i++)
        V[i] *= j;
    return V;
}

matrix scaleMatrix(matrix &A, type scale) {
    for (int i = 0; i < A.rows; i++)
        for (int j = 0; j < A.columns; j++)
            A.M[i][j] *= scale;
    return A;
}

void swaprows(matrix &A, int i, int j) {
    if (i == j) return;
    vector<type> X;
    X = A.M[i];
    A.M[i] = A.M[j];
    A.M[j] = X;
}

double getNorm(vector<type> &A, vector<type> &B) {
    if (A.size() == B.size()) {
        double sum = 0;
        for (int i = 0; i < A.size(); i++) {
            sum += (A[i] - B[i]) * (A[i] - B[i]);
        }
        return sqrt(sum);
    }
    else {
        /*cout << "Printing vectors of different sizes..." << endl;
        printVector(A);
        printVector(B);*/
        return -1;
    }
}

matrix zeros(int rows, int columns) {
    matrix A;
    A.rows = rows;
    A.columns = columns;
    for (int i = 0; i < rows; i++) {
        vector<type> V;
        for (int j = 0; j < columns; j++)
            V.push_back(type(0));
        A.M.push_back(V);
    }
    return A;
}

matrix getL(matrix &A) {
    matrix L;
    L = zeros(A.rows, A.columns);
    L.columns = A.columns;
    L.rows = A.rows;
    for (int i = 0; i < A.rows; i++) {
        for (int j = 0; j < i; j++) {
            L.M[i][j] = A.M[i][j];
        }
    }
    return L;
}

matrix getD(matrix &A) {
    matrix L;
    L = zeros(A.rows, A.columns);
    L.columns = A.columns;
    L.rows = A.rows;
    for (int i = 0; i < A.rows; i++) {
        L.M[i][i] = A.M[i][i];
    }
    return L;
}

matrix getU(matrix &A) {
    matrix L;
    L = zeros(A.rows, A.columns);
    L.columns = A.columns;
    L.rows = A.rows;
    for (int i = 0; i < A.rows; i++) {
        for (int j = i + 1; j < A.columns; j++) {
            L.M[i][j] = A.M[i][j];
        }
    }
    return L;
}

matrix add(matrix A, matrix B, int option = 1) {
    if (A.columns != B.columns or A.rows != B.rows) cout << "Blad" << endl;
    matrix C = zeros(A.rows, A.columns);
    for (int i = 0; i < A.columns; i++)
        for (int j = 0; j < A.rows; j++)
            C.M[j][i] = A.M[j][i] + option * B.M[j][i];
    return C;
}

void reciprocalD(matrix &D) {
    for (int i = 0; i < D.rows; i++)
        D.M[i][i] = 1 / D.M[i][i];
}


matrix taskThree(type k, type m, int n) {
    matrix A = zeros(n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) A.M[i][i] = k;
            else if (j > i) {
                int sign = (j % 2 == 0) ? -1 : 1;
                A.M[i][j] = sign * m / (j + 1);
            }
            else if (j == i - 1) {
                A.M[i][j] = m / (i + 1);
            }
            else A.M[i][j] = type(0);
        }
    }
    return A;
}

type stopCriteriaTwo(matrix &A, matrix &newX, matrix Y) {
    matrix temp = multiply(A, newX);
    temp = transpose(temp);
    Y = transpose(Y);
    return getNorm(temp.M[0], Y.M[0]);
}

void solveJacob(int n, double ro, int stop, int option) {
    matrix A;
    type k = 5, m = 0.5;
    A = taskThree(k, m, n);
    //printMatrix(A);

    matrix X = ones(A.columns);
    X = transpose(X);
    //printMatrix(X);
    matrix Y = multiply(A, X);
    //printMatrix(Y);
    matrix result, probX, D, N, U, L, M, newX;

    probX = ones(A.rows, option);
    probX = transpose(probX);

    D = getD(A);
    reciprocalD(D);

    N = D;
    D = scaleMatrix(D, -1);
    U = getU(A);
    L = getL(A);

    M = multiply(D, add(U, L));
    newX = add(multiply(M, probX), multiply(N, Y));
    matrix newXt = transpose(newX);

    X = transpose(X);
    //DZIALAJACE PIERWSZE KRYTERIUM STOPU
    int i = 1;
    if (stop == 1) {
        type norma = getNorm(X.M[0], newXt.M[0]);
        while (norma > ro) {
            newX = add(multiply(M, newX), multiply(N, Y));
            newXt = transpose(newX);
            i++;
            norma = getNorm(X.M[0], newXt.M[0]);
        }
    }
        //DRUGIE DZIAŁAJĄCE KRYTERIUM STOPU
    else {
        type norma = stopCriteriaTwo(A, newX, Y);
        while (norma > ro) {
            newX = add(multiply(M, newX), multiply(N, Y));
            newXt = transpose(newX);
            i++;
            norma = stopCriteriaTwo(A, newX, Y);
        }
    }

    cout << n << ":" << i << endl;
}

void SOR(int n, double ro, int option, double omega) {
    matrix A;
    type k = 5, m = 0.5;
    A = taskThree(k, m, n);
    //printMatrix(A);

    matrix X = ones(A.columns);
    X = transpose(X);
    matrix Y = multiply(A, X);

    matrix newX = ones(A.rows, option);
    X = transpose(X);
    matrix nextX;

    int it = 1;
    type norma = getNorm(X.M[0], newX.M[0]);
    while (norma > ro) {
        nextX = newX;
        for (int i = 0; i < n; i++) {
            type sum = 0, sum2 = 0;
            for (int j = 0; j < i; j++)
                sum += A.M[i][j] * nextX.M[0][j];
            for (int j = i + 1; j < n; j++)
                sum2 += A.M[i][j] * newX.M[0][j];
            nextX.M[0][i] = ((1 - omega) * newX.M[0][i]) + (omega / A.M[i][i]) * (Y.M[0][i] - sum - sum2);
        }
        it++;
        newX = nextX;
        norma = getNorm(X.M[0], newX.M[0]);
    }

    cout << n << ":" << it << endl;
}

int main() {
    double ro = 0.00001;
    int option = 1; //wektor X: option=0 => [-1,1,-1,1..], option=1 => [0,0,0,0,0], inne => [option, option, option...]
    int stop = 1; // {1,2} => kryterium stopu
    for (int i = 1; i <= 20; i++) {
        solveJacob(i, ro, stop, option);
    }
    return 0;
}
