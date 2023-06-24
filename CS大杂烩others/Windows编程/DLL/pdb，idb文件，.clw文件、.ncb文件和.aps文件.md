# pdb，idb文件，.clw文件、.ncb文件和.aps文件

LINK  uses a PDB to hold debugging information for the .EXE file or .DLL file. The program’s PDB is both an output file and an input file, because LINK updates the PDB when it rebuilds the program.  
  
The compiler saves state information from the first compile in the project’s .IDB file (the default name is project.IDB or VC60.IDB for files compiled without a project). The compiler uses this state information to speed subsequent compiles.   
  
If the compiler cannot find the project’s .PDB file or .IDB file (or either is read-only), it cannot incrementally compile


LINK       uses     a     PDB     to     hold     debugging     information     for     the     .EXE     file     or     .DLL     file.     The     program’s     PDB     is     both     an     output     file     and     an     input     file,     because     LINK     updates     the     PDB     when     it     rebuilds     the     program.     
      
    The     compiler     saves     state     information     from     the     first     compile     in     the     project’s     .IDB     file     (the     default     name     is     project.IDB     or     VC60.IDB     for     files     compiled     without     a     project).     The     compiler     uses     this     state     information     to     speed     subsequent     compiles.       
      
    If     the     compiler     cannot     find     the     project’s     .PDB     file     or     .IDB     file     (or     either     is     read-only),     it     cannot     incrementally     compile   

.clw文件记录了类的信息，如果classView中某个类不见了，重新生成该文件就可以了，方法：删除此文件，点击“建立类向导”，根据提示输入工程名称就可以了；  
.ncb文件记录了类的提示信息，如果类的成员函数和变量的提示不见了，重新生成该文件即可，方法同上；  
.aps文件记录了资源信息，要利用现成的资源，需要修改3个文件，.rc文件，Resource.h文件和.aps文件，.aps直接删除后，进入程序，VC会自动生成。

又有人说：？？？

.clw 支持ClassWizard

 .ncb 支持ClassView

.opt 保存工作空间的配置

 .aps 支持ResourceView




ilk,pch,pbd,obj,idb,pdb，这些都是文件的扩展名。  
ILK，是连接过程百中生成的一种中间文件，只供LINK工具使用。  
PCH，预编译头文件，由编译器在建立工程时自动生成，其中存放有工程中已经编译的部分代度码，在以后建立工程时不再重新编译这些代码。  
PBD，类似于DLL的文件。只是DLL是机器码，PBD 是伪代专码。  
obj，是3D模型文件格式。由Alias|Wavefront公司为[3D建模](和动画软件"Advanced Visualizer"开发的一种标准，适合用于模型之间的互导，也可以通过Maya读写。  
idb，一种 MSDev 中间层文件。  
PDB（程序数据库）文件保持着调试和项目状态信息，从属而可以对程序的调试配置进行增量链接。











