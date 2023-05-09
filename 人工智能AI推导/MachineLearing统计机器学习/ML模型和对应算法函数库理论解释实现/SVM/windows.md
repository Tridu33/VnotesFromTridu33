# windows










```
C:\svm_LIBSVM\libsvm\windows>dir
 Volume in drive C has no label.
 Volume Serial Number is 32C5-E3BF

 Directory of C:\svm_LIBSVM\libsvm\windows

04/27/2020  10:09 AM    <DIR>          .
04/27/2020  10:09 AM    <DIR>          ..
04/27/2020  10:09 AM         2,101,973 a3a.tet
04/27/2020  10:07 AM           227,902 a3a.train
05/18/2018  04:49 PM           259,072 libsvm.dll
05/18/2018  04:49 PM            14,336 libsvmread.mexw64
05/18/2018  04:49 PM            13,312 libsvmwrite.mexw64
05/18/2018  04:49 PM           212,992 svm-predict.exe
05/18/2018  04:49 PM           165,888 svm-scale.exe
05/18/2018  04:49 PM           226,816 svm-toy.exe
05/18/2018  04:49 PM           248,320 svm-train.exe
05/18/2018  04:49 PM            28,160 svmpredict.mexw64
05/18/2018  04:49 PM            68,608 svmtrain.mexw64
              11 File(s)      3,567,379 bytes
               2 Dir(s)   4,273,344,512 bytes free

C:\svm_LIBSVM\libsvm\windows>svm-train.exe a3a.train
*
optimization finished, #iter = 977
nu = 0.428951
obj = -1270.050992, rho = 0.620483
nSV = 1388, nBSV = 1344
Total nSV = 1388

C:\svm_LIBSVM\libsvm\windows>dir
 Volume in drive C has no label.
 Volume Serial Number is 32C5-E3BF

 Directory of C:\svm_LIBSVM\libsvm\windows

04/27/2020  10:12 AM    <DIR>          .
04/27/2020  10:12 AM    <DIR>          ..
04/27/2020  10:09 AM         2,101,973 a3a.test
04/27/2020  10:07 AM           227,902 a3a.train
04/27/2020  10:12 AM           101,141 a3a.train.model
05/18/2018  04:49 PM           259,072 libsvm.dll
05/18/2018  04:49 PM            14,336 libsvmread.mexw64
05/18/2018  04:49 PM            13,312 libsvmwrite.mexw64
05/18/2018  04:49 PM           212,992 svm-predict.exe
05/18/2018  04:49 PM           165,888 svm-scale.exe
05/18/2018  04:49 PM           226,816 svm-toy.exe
05/18/2018  04:49 PM           248,320 svm-train.exe
05/18/2018  04:49 PM            28,160 svmpredict.mexw64
05/18/2018  04:49 PM            68,608 svmtrain.mexw64
              12 File(s)      3,668,520 bytes
               2 Dir(s)   4,268,052,480 bytes free

C:\svm_LIBSVM\libsvm\windows>svm-predict.exe a3a.test a3a.train.model a3a.out
Accuracy = 83.8406% (24629/29376) (classification)

```