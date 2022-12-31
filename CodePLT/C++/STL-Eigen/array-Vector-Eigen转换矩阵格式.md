# 1. Eigen转换矩阵格式

https://www.cnblogs.com/VVingerfly/p/8037490.html



Eigen::Matrix与array数据转换



```
#include <iostream>
#include <vector>
#include <Eigen/Dense>

using namespace std;
using namespace Eigen;

void array2eigenMat();
void eigenMat2array();

void array2eigenVec();
void eigenVec2array();

void vector2eigenMat();
void eigenMat2vector();

void vector2eigenVec();
void eigenVec2vector();


int main()
{
    cout << "hello world" << endl;
    array2eigenMat();
    eigenMat2array();

    array2eigenVec();
    eigenVec2array();

    vector2eigenMat();
    eigenMat2vector();

    vector2eigenVec();
    eigenVec2vector();
    return 0;
}

void array2eigenMat()
{
    cout << "-------------------------- array2eigenMat  --------------------------" << endl;

    int array[9];
    for (int i = 0; i < 9; ++i) array[i] = i;
    cout << "array = [ "; for (int i = 0; i < 9; ++i) cout << array[i] << " "; cout << "]" << endl;

    cout << "colMajor matrix = \n" << Map<Matrix3i>(array) << endl;                     // map a contiguous array as a column-major matrix
    cout << "rowMajor matrix = \n" << Map<Matrix<int, 3, 3, RowMajor>>(array) << endl;  // map a contiguous array as a row-major matrix


    cout << "stride matrix = \n" << Map<MatrixXi, 0, OuterStride<>>(array, 3, 3, OuterStride<>(2)) << endl;
    //mapping an array while specifying an outer stride. Here, since we're mapping as a column-major matrix, 
    // 'outer stride' means the pointer increment between two consecutive columns


    Map<MatrixXi> eigMat1(array, 3, 3);
    MatrixXi      eigMat2 = Map<MatrixXi>(array, 3, 3);
    array[0] = 9;

    cout << "eigMat1 matrix = \n"; cout << eigMat1 << endl;
    cout << "eigMat2 matrix = \n"; cout << eigMat2 << endl;
    cout << "---------------------------------------------------------------------" << endl;

}
void eigenMat2array()
{
    cout << "-------------------------- eigenMat2array  --------------------------" << endl;
    Matrix3d eigMat;
    eigMat <<
        1, 2, 3,
        4, 5, 6,
        7, 8, 9;
    cout << "init eigMat = \n";    cout << eigMat << endl;

    double* eigMatptr = eigMat.data();
    cout << "array = [ "; for (int i = 0; i < 9; ++i) cout << eigMatptr[i] << " "; cout << "]" << endl;

    eigMat(0, 0) = 9;
    cout << "array = [ "; for (int i = 0; i < 9; ++i) cout << eigMatptr[i] << " "; cout << "]" << endl;


    double* eigMatptrnew = new double[eigMat.size()];
    Map<MatrixXd>(eigMatptrnew, eigMat.rows(), eigMat.cols()) = eigMat;

    eigMat(2, 2) = 0;
    cout << "init matrix = \n"; cout << eigMat << endl;
    cout << "array = [ "; for (int i = 0; i < 9; ++i) cout << eigMatptr[i] << " "; cout << "]" << endl;
    cout << "---------------------------------------------------------------------" << endl;
}

void array2eigenVec()
{
    cout << "-------------------------- array2eigenVec  --------------------------" << endl;

    int array[9];
    for (int i = 0; i < 9; ++i) array[i] = i;
    cout << "data array = [ "; for (int i = 0; i < 9; ++i) cout << array[i] << " "; cout << "]" << endl;

    Map<VectorXi> eigVec(array, 5);
    cout << "eigen  vector transpose = " << eigVec.transpose() << endl;
    cout << "stride vector transpose = " << Map<VectorXi, 0, InnerStride<2> >(array, 4).transpose() << endl;
    // map an array as a vector, specifying an inner stride, that is, the pointer increment between two consecutive coefficients

    array[0] = 9;
    cout << "eigen  vector transpose = " << eigVec.transpose() << endl;
    cout << "stride vector transpose = " << Map<VectorXi, 0, InnerStride<2> >(array, 4).transpose() << endl;

    cout << "---------------------------------------------------------------------" << endl;
}
void eigenVec2array()
{
    cout << "-------------------------- eigenVec2array  --------------------------" << endl;
    VectorXf eigvec(5);
    eigvec << 0, 1, 2, 3, 4;
    cout << "eigen  vector transpose = " << eigvec.transpose() << endl;

    float* array = new float;
    array = eigvec.data();
    cout << "data array = [ "; for (int i = 0; i < eigvec.size(); ++i) cout << array[i] << " "; cout << "]" << endl;

    eigvec(0) = 9;
    cout << "data array = [ "; for (int i = 0; i < eigvec.size(); ++i) cout << array[i] << " "; cout << "]" << endl;

    array[0] = 5;
    cout << "eigen  vector transpose = " << eigvec.transpose() << endl;

    cout << "---------------------------------------------------------------------" << endl;
}

void vector2eigenMat()
{
    cout << "-------------------------- vector2eigenMat --------------------------" << endl;
    vector<int> stdvec{ 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    Map<Matrix<int, 3, 3, RowMajor>> eigMat1(stdvec.data());
    MatrixXi                         eigMat2 = Map<Matrix<int, 3, 3, RowMajor>>(stdvec.data());

    cout << "eigMat1 matrix = \n"; cout << eigMat1 << endl;
    cout << "eigMat2 matrix = \n"; cout << eigMat2 << endl;

    stdvec[0] = 9;
    cout << "eigMat1 matrix = \n"; cout << eigMat1 << endl;
    cout << "eigMat2 matrix = \n"; cout << eigMat2 << endl;

    cout << "---------------------------------------------------------------------" << endl;
}
void eigenMat2vector()
{
    cout << "-------------------------- eigenMat2vector --------------------------" << endl;
    Matrix3d eigMatCol;
    eigMatCol <<
        1, 2, 3,
        4, 5, 6,
        7, 8, 9;
    cout << "eigen matrix col = \n";    cout << eigMatCol << endl;
    vector<double> stdvec1(eigMatCol.data(), eigMatCol.data() + eigMatCol.size());
    cout << "std   vector1 = ["; for (int i = 0; i < stdvec1.size(); ++i) cout << stdvec1[i] << " "; cout << "]" << endl;

    Matrix<double, 3, 3, RowMajor> eigMatRow = eigMatCol;
    cout << "eigen matrix row = \n";    cout << eigMatCol << endl;
    vector<double> stdvec2(eigMatRow.data(), eigMatRow.data() + eigMatRow.size());
    cout << "std   vector2 = ["; for (int i = 0; i < stdvec2.size(); ++i) cout << stdvec2[i] << " "; cout << "]" << endl;

    cout << "---------------------------------------------------------------------" << endl;
}

void vector2eigenVec()
{
    cout << "-------------------------- vector2eigenVec --------------------------" << endl;
    vector<int> stdvec{ 1, 2, 3, 4, 5 };
    cout << "std   vector = ["; for (int i = 0; i < stdvec.size(); ++i) cout << stdvec[i] << " "; cout << "]" << endl;

    Map<VectorXi> eigVec1(stdvec.data(), stdvec.size());
    VectorXi eigVec2 = Map<VectorXi>(stdvec.data(), stdvec.size());
    cout << "eigen  vector1 transpose = " << eigVec1.transpose() << endl;
    cout << "eigen  vector2 transpose = " << eigVec2.transpose() << endl;
    cout << "stride vector  transpose = " << Map<VectorXi, 0, InnerStride<2> >(stdvec.data(), 2).transpose() << endl;


    stdvec[0] = 9;
    cout << "eigen  vector1 transpose = " << eigVec1.transpose() << endl;
    cout << "eigen  vector2 transpose = " << eigVec2.transpose() << endl;

    cout << "stride vector  transpose = " << Map<VectorXi, 0, InnerStride<2> >(stdvec.data(), 2).transpose() << endl;

    cout << "---------------------------------------------------------------------" << endl;
}
void eigenVec2vector()
{
    cout << "-------------------------- eigenVec2vector --------------------------" << endl;
    VectorXf eigvec(5);
    eigvec << 0, 1, 2, 3, 4;
    cout << "eigen  vector transpose = " << eigvec.transpose() << endl;

    vector<float> stdvec(eigvec.data(), eigvec.data() + eigvec.size());
    cout << "std   vector = ["; for (int i = 0; i < stdvec.size(); ++i) cout << stdvec[i] << " "; cout << "]" << endl;

    eigvec(0) = 5;
    cout << "std   vector = ["; for (int i = 0; i < stdvec.size(); ++i) cout << stdvec[i] << " "; cout << "]" << endl;
    cout << "---------------------------------------------------------------------" << endl;
}

```







