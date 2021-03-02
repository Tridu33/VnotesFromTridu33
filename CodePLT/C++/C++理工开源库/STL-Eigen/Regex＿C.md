# 1. Regex＿C




```

	ifstream in(dir);  //读入文件
	regex pat_regex("[[:digit:]]+");  //匹配原则，这里代表一个或多个数字
	//获取矩阵rowT,colT
	while (getline(in, line)) {  //按行读取
		rowT++;
		colT = 0;//每行列数设置初始0,变量作用域
		for (sregex_iterator it(line.begin(), line.end(), pat_regex), end_it; it != end_it; ++it) {  //表达式匹配，匹配一行中所有满足条件的字符
			colT++;//colT++
		}
	};
```

源程序

```
%矩阵A的极大代数法k次幂
function AK=MP_AKpower(A,k)
  [m,n]=size(A);
if(m==n)
  E=-inf*ones(m,m);
  for i=1:m 
    E(i,i)=0;
  endfor
  AK=E;
  for j=1:k
  AK=MP_MaTimesMb(AK,A);
  endfor
elseif
  disp('Horizontal dimension of A should equal to vertical dimension');
endif
endfunction
```





answer:

```
//4 矩阵A的极大代数法k次幂MP_AKpower();
	MatrixXd  MP_AKpower(MatrixXd A, int k) {
		printf("\n矩阵A的极大代数法k次幂MP_AKpower\n ");
		int m = A.rows();
		MatrixXd AK= MatrixXd::Ones(m, m);
		if (A.rows() == A.cols()) {
			MatrixXd E = INT_MIN * MatrixXd::Ones(m, m);
			for (int i = 0; i < m; i++) {
				E(i, i) = 0;
			}
			cout <<E<< endl;
			MatrixXd AK = E;
			for (int j = 0; j < k ; j++) {
			cout << "the" << j << "turns:\n" << AK << "\n" << A << endl;
			AK = MP_MaTimesMb(AK, A);
			
			}
		}
		else
			printf("Horizontal dimension of A should equal to vertical dimension");
		return AK;
	}//
```
















