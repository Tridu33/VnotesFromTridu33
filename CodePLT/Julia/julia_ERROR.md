























```
julia> import Pkg; Pkg.add("PyPlot")
 Resolving package versions...
 Installed LaTeXStrings ─ v1.0.3
 Installed PyPlot ─────── v2.8.1
 Installed PyCall ─────── v1.91.2
  Updating `C:\Users\shinelon\.julia\environments\v1.1\Project.toml`
  [d330b81b] + PyPlot v2.8.1
  Updating `C:\Users\shinelon\.julia\environments\v1.1\Manifest.toml`
  [b964fa9f] + LaTeXStrings v1.0.3
  [438e738f] + PyCall v1.91.2
  [d330b81b] + PyPlot v2.8.1
  Building PyCall → `C:\Users\shinelon\.julia\packages\PyCall\ttONZ\deps\build.log`
┌ Error: Error building `PyCall`, showing the last 100 of log:
│                           inelon\AppData\Roaming\cabal\bin;D:\Users\shinelon\AppData\Roaming\loc
│                           al\bin;C:\Users\shinelon\AppData\Local\Microsoft\WindowsApps;C:\Users\
│                           shinelon\AppData\Roaming\npm;D:\wget-1.19.4-win64;D:\Program
│                           Files\MiKTeX 2.9\miktex\bin\x64\;C:\Users\shinelon\AppData\Local\Micro
│                           soft\WindowsApps;E:\python_anaconda\manim2software\dvisvgm-2.6-win64;E
│                           :\python_anaconda\manim2software\ffmpeg-20180930-d702769-win64-static\
│                           ffmpeg-20180930-d702769-win64-static\bin;C:\Users\shinelon\AppData\Loc
│                           al\Pandoc\;D:\Server\Apache24\bin;E:\python_anaconda\manim2software\ff
│                           mpeg-20180930-d702769-win64-static\ffmpeg-20180930-d702769-win64-stati
│                           c\bin;C:\Program Files (x86)\Writage;C:\Program Files\Bandizip\;C:\Use
│                           rs\shinelon\AppData\Local\atom\bin;D:\Users\shinelon\AppData\Local\Jul
│                           ia-1.1.1\bin;
│              PSMODULEPATH=C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\Windows
│                           PowerShell\v1.0\Modules
│          PYTHONIOENCODING=UTF-8
│        REQUESTS_CA_BUNDLE=<not set>
│             SSL_CERT_FILE=<not set>
│     VBOX_MSI_INSTALL_PATH=C:\Program Files\Oracle\VirtualBox\
│
│      active environment : base
│     active env location : C:\Users\shinelon\.julia\conda\3
│        user config file : C:\Users\shinelon\.condarc
│  populated config files : C:\Users\shinelon\.condarc
│                           C:\Users\shinelon\.julia\conda\3\condarc-julia.yml
│           conda version : 4.5.4
│     conda-build version : not installed
│          python version : 3.6.5.final.0
│        base environment : C:\Users\shinelon\.julia\conda\3  (writable)
│            channel URLs : https://repo.anaconda.com/pkgs/main/win-64
│                           https://repo.anaconda.com/pkgs/main/noarch
│                           https://repo.anaconda.com/pkgs/free/win-64
│                           https://repo.anaconda.com/pkgs/free/noarch
│                           https://repo.anaconda.com/pkgs/r/win-64
│                           https://repo.anaconda.com/pkgs/r/noarch
│                           https://repo.anaconda.com/pkgs/pro/win-64
│                           https://repo.anaconda.com/pkgs/pro/noarch
│                           https://repo.anaconda.com/pkgs/msys2/win-64
│                           https://repo.anaconda.com/pkgs/msys2/noarch
│                           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/win-64
│                           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/noarch
│                           http://conda.anaconda.org/gurobi/win-64
│                           http://conda.anaconda.org/gurobi/noarch
│           package cache : C:\Users\shinelon\.julia\conda\3\pkgs
│                           C:\Users\shinelon\AppData\Local\conda\conda\pkgs
│        envs directories : C:\Users\shinelon\.julia\conda\3\envs
│                           C:\Users\shinelon\AppData\Local\conda\conda\envs
│                           C:\Users\shinelon\.conda\envs
│                platform : win-64
│              user-agent : conda/4.5.4 requests/2.18.4 CPython/3.6.5 Windows/10 Windows/10.0.17134
│           administrator : False
│              netrc file : None
│            offline mode : False
│
│
│ V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V
│
│ CondaHTTPError: HTTP 404 NOT FOUND for url <https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/noarch/repodata.json>
│ Elapsed: 00:00.020963
│
│ The remote server could not find the noarch directory for the
│ requested channel with url: https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
│
│ As of conda 4.3, a valid channel must contain a `noarch/repodata.json` and
│ associated `noarch/repodata.json.bz2` file, even if `noarch/repodata.json` is
│ empty. please request that the channel administrator create
│ `noarch/repodata.json` and associated `noarch/repodata.json.bz2` files.
│ $ mkdir noarch
│ $ echo '{}' > noarch/repodata.json
│ $ bzip2 -k noarch/repodata.json
│
│ You will need to adjust your conda configuration to proceed.
│ Use `conda config --show channels` to view your configuration's current state.
│ Further configuration help can be found at <https://conda.io/docs/config.html>.
│
│ A reportable application error has occurred. Conda has prepared the above report.
│ Upload successful.
│ ┌ Info: Using the Python distribution in the Conda package by default.
│ └ To use a different Python version, set ENV["PYTHON"]="pythoncommand" and re-run Pkg.build("PyCall").
│ [ Info: Downloading miniconda installer ...
│ [ Info: Installing miniconda ...
│ [ Info: Running `conda config --add channels defaults --file 'C:\Users\shinelon\.julia\conda\3\condarc-julia.yml' --force` in root environment
│ [ Info: Running `conda update -y conda` in root environment
│ ERROR: LoadError: failed process: Process(setenv(`'C:\Users\shinelon\.julia\conda\3\Scripts\conda.exe' update -y conda`,["USERDOMAIN_ROAMINGPROFILE=TRIDU33", "HOMEPATH=\\Users\\shinelon", "ChocolateyLastPathUpdate=周六 3月  2 17:41:18 2019", "ProgramData=C:\\ProgramData", "ProgramW6432=C:\\Program Files", "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC", "SESSIONNAME=Console", "GKS_USE_CAIRO_PNG=true", "APPDATA=C:\\Users\\shinelon\\AppData\\Roaming", "PUBLIC=C:\\Users\\Public", "USERDOMAIN=TRIDU33", "MW_MINGW64_LOC=C:\\TDM-GCC-64", "OS=Windows_NT", "PROCESSOR_REVISION=5e03", "TMP=C:\\Users\\shinelon\\AppData\\Local\\Temp", "GOOGLE_DEFAULT_CLIENT_ID=no", "NVTOOLSEXT_PATH=C:\\Program Files\\NVIDIA Corporation\\NvToolsExt\\", "ALLUSERSPROFILE=C:\\ProgramData", "Path=C:\\ProgramData\\DockerDesktop\\version-bin;C:\\Program Files\\Docker\\Docker\\Resources\\bin;C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.0\\bin;C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.0\\libnvvp;C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Program Files\\Haskell\\bin;D:\\Program Files\\Haskell Platform\\8.2.2\\lib\\extralibs\\bin;D:\\Program Files\\Haskell Platform\\8.2.2\\bin;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;D:\\Program Files\\Haskell Platform\\8.2.2\\mingw\\bin;C:\\Program Files (x86)\\Pandoc\\;D:\\Program Files\\nodejs\\;C:\\Program Files\\Git\\cmd;C:\\Program Files (x86)\\GtkSharp\\2.12\\bin;D:\\Program Files\\MATLAB\\R2017b\\runtime\\win64;D:\\Program Files\\MATLAB\\R2017b\\bin;C:\\Program Files\\Common Files\\Autodesk Shared\\;C:\\Program Files (x86)\\Autodesk\\Backburner\\;D:\\Program Files\\Java\\jdk1.8.0_181\\bin;D:\\Program Files\\Java\\jdk1.8.0_181\\jre\\bin;D:\\Program Files\\CMake\\bin;D:\\Program Files (x86)\\IBM\\SPSS\\Statistics\\24\\JRE\\bin;C:\\Program Files\\dotnet\\;C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;%CATALINA_HOME%\\bin;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.0\\bin;C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.0\\lib\\x64;D:\\Server\\Apache24\\bin;C:\\MinGW\\bin;D:\\Program Files\\nodejs\\node_global;C:\\ProgramData\\chocolatey\\bin;;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\TDM-GCC-32\\bin;C:\\TDM-GCC-64\\bin;D:\\Anaconda3;D:\\Anaconda3\\Library\\mingw-w64\\bin;D:\\Anaconda3\\Library\\usr\\bin;D:\\Anaconda3\\Library\\bin;D:\\Anaconda3\\Scripts;C:\\Users\\shinelon\\AppData\\Roaming\\cabal\\bin;D:\\Users\\shinelon\\AppData\\Roaming\\local\\bin;C:\\Users\\shinelon\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\shinelon\\AppData\\Roaming\\npm;D:\\wget-1.19.4-win64;D:\\Program Files\\MiKTeX 2.9\\miktex\\bin\\x64\\;C:\\Users\\shinelon\\AppData\\Local\\Microsoft\\WindowsApps;E:\\python_anaconda\\manim2software\\dvisvgm-2.6-win64;E:\\python_anaconda\\manim2software\\ffmpeg-20180930-d702769-win64-static\\ffmpeg-20180930-d702769-win64-static\\bin;C:\\Users\\shinelon\\AppData\\Local\\Pandoc\\;D:\\Server\\Apache24\\bin;E:\\python_anaconda\\manim2software\\ffmpeg-20180930-d702769-win64-static\\ffmpeg-20180930-d702769-win64-static\\bin;C:\\Program Files (x86)\\Writage;C:\\Program Files\\Bandizip\\;C:\\Users\\shinelon\\AppData\\Local\\atom\\bin;D:\\Users\\shinelon\\AppData\\Local\\Julia-1.1.1\\bin;", "COMPUTERNAME=TRIDU33", "JAVA_HOME=D:\\Program Files\\Java\\jdk1.8.0_181", "ADSK_3DSMAX_x64_2018=D:\\Program Files\\Autodesk\\3ds Max 2018\\", "USERNAME=shinelon", "CommonProgramFiles(x86)=C:\\Program Files (x86)\\Common Files", "CommonProgramFiles=C:\\Program Files\\Common Files", "CLASSPATH=.;D:\\Program Files\\Java\\jdk1.8.0_181\\lib\\dt.jar;D:\\Program Files\\Java\\jdk1.8.0_181\\lib\\tools.jar;", "CUDA_PATH=C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.0", "USERPROFILE=C:\\Users\\shinelon", "CONDARC=C:\\Users\\shinelon\\.julia\\conda\\3\\condarc-julia.yml", "GOOGLE_API_KEY=no", "PSModulePath=C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules", "STACK_ROOT=C:\\sr", "PROCESSOR_LEVEL=6", "CUDA_CACHE_MAXSIZE=268435456", "=C:=C:\\Users\\shinelon\\.julia\\packages\\PyCall\\ttONZ\\deps", "Anaconda3_Library_bin=D:\\Anaconda3\\Library\\bin", "SystemDrive=C:", "HOMEDRIVE=C:", "TEMP=C:\\Users\\shinelon\\AppData\\Local\\Temp", "PYTHONIOENCODING=UTF-8", "CUDA_PATH_V10_0=C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.0", "NODE_PATH=D:\\Program Files\\nodejs\\node_global", "LOCALAPPDATA=C:\\Users\\shinelon\\AppData\\Local", "GTK_BASEPATH=C:\\Program Files (x86)\\GtkSharp\\2.12\\", "MATLAB_Win64=D:\\Program Files\\MATLAB\\R2017b\\bin\\win64", "NVCUDASAMPLES10_0_ROOT=C:\\ProgramData\\NVIDIA Corporation\\CUDA Samples\\v10.0", "PROCESSOR_IDENTIFIER=Intel64 Family 6 Model 94 Stepping 3, GenuineIntel", "Anaconda3=D:\\Anaconda3\\python.exe", "DriverData=C:\\Windows\\System32\\Drivers\\DriverData", "NUMBER_OF_PROCESSORS=4", "VS150COMCOMNTOOLS=C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\Common7\\Tools\\", "PVIEW_KEYSHOT6_HOME=D:\\Program Files\\KeyShot6\\bin\\", "GOOGLE_DEFAULT_CLIENT_SECRET=no", "=::=::\\", "ComSpec=C:\\WINDOWS\\system32\\cmd.exe", "SystemRoot=C:\\WINDOWS", "OneDrive=C:\\Users\\shinelon\\OneDrive", "OneDriveConsumer=C:\\Users\\shinelon\\OneDrive", "VBOX_MSI_INSTALL_PATH=C:\\Program Files\\Oracle\\VirtualBox\\", "VRAY_SEND_FEEDBACK=1", "VS100COMNTOOLS=D:\\Program Files (x86)\\Microsoft Visual Studio 10.0\\Common7\\Tools\\", "ProgramFiles(x86)=C:\\Program Files (x86)", "Anaconda3_Scripts=D:\\Anaconda3\\Scripts", "GRDIR=C:\\Users\\shinelon\\.julia\\packages\\GR\\TMylY\\src\\..\\deps\\gr", "ChocolateyInstall=C:\\ProgramData\\chocolatey", "JUNORC_PATH=D:\\Users\\shinelon\\AppData\\Local\\JuliaPro-1.1.1.1\\.atom", "MYSQLCONNECTOR_ASSEMBLIESPATH=C:\\Program Files (x86)\\MySQL\\Connector NET 8.0\\Assemblies\\v4.5.2", "KEYSHOT6=C:\\Users\\Public\\Documents\\KeyShot 6", "GKS_FONTPATH=C:\\Users\\shinelon\\.julia\\packages\\GR\\TMylY\\src\\..\\deps\\gr", "LOGONSERVER=\\\\TRIDU33", "CONDA_PREFIX=C:\\Users\\shinelon\\.julia\\conda\\3", "windir=C:\\WINDOWS", "FPS_BROWSER_USER_PROFILE_STRING=Default", "JULIA_LOAD_PATH=@;C:\\Users\\shinelon\\AppData\\Local\\Temp\\jl_6327.tmp", "CommonProgramW6432=C:\\Program Files\\Common Files", "MATLAB=D:\\Program Files\\MATLAB\\R2017b\\bin", "ProgramFiles=C:\\Program Files", "FPS_BROWSER_APP_PROFILE_STRING=Internet Explorer", "NVCUDASAMPLES_ROOT=C:\\ProgramData\\NVIDIA Corporation\\CUDA Samples\\v10.0", "PROCESSOR_ARCHITECTURE=AMD64", "OPENBLAS_MAIN_FREE=1"]), ProcessExited(1)) [1]
│ Stacktrace:
│  [1] error(::String, ::Base.Process, ::String, ::Int64, ::String) at .\error.jl:42
│  [2] pipeline_error at .\process.jl:785 [inlined]
│  [3] #run#515(::Bool, ::Function, ::Cmd) at .\process.jl:726
│  [4] run at .\process.jl:724 [inlined]
│  [5] runconda(::Cmd, ::String) at C:\Users\shinelon\.julia\packages\Conda\CpuvI\src\Conda.jl:113
│  [6] runconda(::Cmd) at C:\Users\shinelon\.julia\packages\Conda\CpuvI\src\Conda.jl:111
│  [7] _install_conda(::String, ::Bool) at C:\Users\shinelon\.julia\packages\Conda\CpuvI\src\Conda.jl:172
│  [8] _install_conda(::String) at C:\Users\shinelon\.julia\packages\Conda\CpuvI\src\Conda.jl:152
│  [9] runconda(::Cmd, ::String) at C:\Users\shinelon\.julia\packages\Conda\CpuvI\src\Conda.jl:111
│  [10] add at C:\Users\shinelon\.julia\packages\Conda\CpuvI\src\Conda.jl:183 [inlined] (repeats 2 times)
│  [11] top-level scope at C:\Users\shinelon\.julia\packages\PyCall\ttONZ\deps\build.jl:84
│  [12] include at .\boot.jl:326 [inlined]
│  [13] include_relative(::Module, ::String) at .\loading.jl:1038
│  [14] include(::Module, ::String) at .\sysimg.jl:29
│  [15] include(::String) at .\client.jl:403
│  [16] top-level scope at none:0
│ in expression starting at C:\Users\shinelon\.julia\packages\PyCall\ttONZ\deps\build.jl:43
│
│ Full log at C:\Users\shinelon\.julia\packages\PyCall\ttONZ\deps\build.log
└ @ Pkg.Operations C:\cygwin\home\Administrator\buildbot\worker\package_win64\build\usr\share\julia\stdlib\v1.1\Pkg\src\Operations.jl:1075

```














