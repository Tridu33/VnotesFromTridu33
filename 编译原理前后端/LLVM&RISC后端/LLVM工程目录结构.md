


LLVM IR入门指南(1)——LLVM架构简介





LLVM IR入门指南(1)——LLVM架构简介 - 勥巭炛的文章 - 知乎
https://zhuanlan.zhihu.com/p/161626997



LLVM编译器架构 - 吴建明wujianming的文章 - 知乎
https://zhuanlan.zhihu.com/p/339512886


LLVM编译基础结构介绍(结尾有干货哦!） - 青色的海牛的文章 - 知乎
https://zhuanlan.zhihu.com/p/47732527







# 1. LLVM工程目录结构


















```
	bin
		LLVM\bin\api-ms-win-core-console-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-console-l1-2-0.dll   
		LLVM\bin\api-ms-win-core-datetime-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-debug-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-errorhandling-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-file-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-file-l1-2-0.dll   
		LLVM\bin\api-ms-win-core-file-l2-1-0.dll   
		LLVM\bin\api-ms-win-core-handle-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-heap-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-interlocked-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-libraryloader-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-localization-l1-2-0.dll   
		LLVM\bin\api-ms-win-core-memory-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-namedpipe-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-processenvironment-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-processthreads-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-processthreads-l1-1-1.dll   
		LLVM\bin\api-ms-win-core-profile-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-rtlsupport-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-string-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-synch-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-synch-l1-2-0.dll   
		LLVM\bin\api-ms-win-core-sysinfo-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-timezone-l1-1-0.dll   
		LLVM\bin\api-ms-win-core-util-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-conio-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-convert-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-environment-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-filesystem-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-heap-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-locale-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-math-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-multibyte-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-private-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-process-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-runtime-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-stdio-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-string-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-time-l1-1-0.dll   
		LLVM\bin\api-ms-win-crt-utility-l1-1-0.dll   
		LLVM\bin\clang.exe   
		LLVM\bin\clang++.exe   
		LLVM\bin\clang-apply-replacements.exe   
		LLVM\bin\clang-change-namespace.exe   
		LLVM\bin\clang-check.exe   
		LLVM\bin\clang-cl.exe   
		LLVM\bin\clang-cpp.exe   
		LLVM\bin\clangd.exe   
		LLVM\bin\clang-doc.exe   
		LLVM\bin\clang-extdef-mapping.exe   
		LLVM\bin\clang-format.exe   
		LLVM\bin\clang-import-test.exe   
		LLVM\bin\clang-include-fixer.exe   
		LLVM\bin\clang-move.exe   
		LLVM\bin\clang-offload-bundler.exe   
		LLVM\bin\clang-offload-wrapper.exe   
		LLVM\bin\clang-query.exe   
		LLVM\bin\clang-refactor.exe   
		LLVM\bin\clang-rename.exe   
		LLVM\bin\clang-reorder-fields.exe   
		LLVM\bin\clang-scan-deps.exe   
		LLVM\bin\clang-tidy.exe   
		LLVM\bin\concrt140.dll   
		LLVM\bin\find-all-symbols.exe   
		LLVM\bin\git-clang-format   
		LLVM\bin\hmaptool   
		LLVM\bin\ld.lld.exe   
		LLVM\bin\ld64.lld.exe   
		LLVM\bin\libclang.dll   
		LLVM\bin\libiomp5md.dll   
		LLVM\bin\liblldb.dll   
		LLVM\bin\libomp.dll   
		LLVM\bin\lld.exe   
		LLVM\bin\lldb.exe   
		LLVM\bin\lldb-argdumper.exe   
		LLVM\bin\lldb-instr.exe   
		LLVM\bin\lldb-server.exe   
		LLVM\bin\lldb-vscode.exe   
		LLVM\bin\lld-link.exe   
		LLVM\bin\llvm-ar.exe   
		LLVM\bin\LLVM-C.dll   
		LLVM\bin\llvm-cov.exe   
		LLVM\bin\llvm-cxxfilt.exe   
		LLVM\bin\llvm-lib.exe   
		LLVM\bin\llvm-nm.exe   
		LLVM\bin\llvm-objcopy.exe   
		LLVM\bin\llvm-objdump.exe   
		LLVM\bin\llvm-profdata.exe   
		LLVM\bin\llvm-ranlib.exe   
		LLVM\bin\llvm-rc.exe   
		LLVM\bin\llvm-size.exe   
		LLVM\bin\llvm-strings.exe   
		LLVM\bin\llvm-strip.exe   
		LLVM\bin\llvm-symbolizer.exe   
		LLVM\bin\LTO.dll   
		LLVM\bin\modularize.exe   
		LLVM\bin\msvcp140.dll   
		LLVM\bin\pp-trace.exe   
		LLVM\bin\Remarks.dll   
		LLVM\bin\scan-build   
		LLVM\bin\scan-build.bat   
		LLVM\bin\scan-view   
		LLVM\bin\ucrtbase.dll   
		LLVM\bin\vcruntime140.dll   
		LLVM\bin\vcruntime140_1.dll   
		LLVM\bin\wasm-ld.exe   
	include
		LLVM\include\clang-c   
		LLVM\include\llvm-c   
		LLVM\include\clang-c\BuildSystem.h   
		LLVM\include\clang-c\CXCompilationDatabase.h   
		LLVM\include\clang-c\CXErrorCode.h   
		LLVM\include\clang-c\CXString.h   
		LLVM\include\clang-c\Documentation.h   
		LLVM\include\clang-c\ExternC.h   
		LLVM\include\clang-c\FatalErrorHandler.h   
		LLVM\include\clang-c\Index.h   
		LLVM\include\clang-c\Platform.h   
		LLVM\include\llvm-c\lto.h   
		LLVM\include\llvm-c\Remarks.h   
	lib
		LLVM\lib\clang   
		LLVM\lib\site-packages   
		LLVM\lib\libclang.lib   
		LLVM\lib\libiomp5md.lib   
		LLVM\lib\liblldb.lib   
		LLVM\lib\libomp.lib   
		LLVM\lib\LLVM-C.lib   
		LLVM\lib\LTO.lib   
		LLVM\lib\Remarks.lib   
		LLVM\lib\clang\10.0.0   
		LLVM\lib\clang\10.0.0\include   
		LLVM\lib\clang\10.0.0\lib   
		LLVM\lib\clang\10.0.0\share   
		LLVM\lib\clang\10.0.0\include\cuda_wrappers   
		LLVM\lib\clang\10.0.0\include\fuzzer   
		LLVM\lib\clang\10.0.0\include\openmp_wrappers   
		LLVM\lib\clang\10.0.0\include\ppc_wrappers   
		LLVM\lib\clang\10.0.0\include\profile   
		LLVM\lib\clang\10.0.0\include\sanitizer   
		LLVM\lib\clang\10.0.0\include\xray   
		LLVM\lib\clang\10.0.0\include\__clang_cuda_builtin_vars.h   
		LLVM\lib\clang\10.0.0\include\__clang_cuda_cmath.h   
		LLVM\lib\clang\10.0.0\include\__clang_cuda_complex_builtins.h   
		LLVM\lib\clang\10.0.0\include\__clang_cuda_device_functions.h   
		LLVM\lib\clang\10.0.0\include\__clang_cuda_intrinsics.h   
		LLVM\lib\clang\10.0.0\include\__clang_cuda_libdevice_declares.h   
		LLVM\lib\clang\10.0.0\include\__clang_cuda_math_forward_declares.h   
		LLVM\lib\clang\10.0.0\include\__clang_cuda_runtime_wrapper.h   
		LLVM\lib\clang\10.0.0\include\__stddef_max_align_t.h   
		LLVM\lib\clang\10.0.0\include\__wmmintrin_aes.h   
		LLVM\lib\clang\10.0.0\include\__wmmintrin_pclmul.h   
		LLVM\lib\clang\10.0.0\include\adxintrin.h   
		LLVM\lib\clang\10.0.0\include\altivec.h   
		LLVM\lib\clang\10.0.0\include\ammintrin.h   
		LLVM\lib\clang\10.0.0\include\arm_acle.h   
		LLVM\lib\clang\10.0.0\include\arm_cmse.h   
		LLVM\lib\clang\10.0.0\include\arm_fp16.h   
		LLVM\lib\clang\10.0.0\include\arm_mve.h   
		LLVM\lib\clang\10.0.0\include\arm_neon.h   
		LLVM\lib\clang\10.0.0\include\arm64intr.h   
		LLVM\lib\clang\10.0.0\include\armintr.h   
		LLVM\lib\clang\10.0.0\include\avx2intrin.h   
		LLVM\lib\clang\10.0.0\include\avx512bf16intrin.h   
		LLVM\lib\clang\10.0.0\include\avx512bitalgintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512bwintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512cdintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512dqintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512erintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512fintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512ifmaintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512ifmavlintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512pfintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vbmi2intrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vbmiintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vbmivlintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vlbf16intrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vlbitalgintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vlbwintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vlcdintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vldqintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vlintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vlvbmi2intrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vlvnniintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vlvp2intersectintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vnniintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vp2intersectintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vpopcntdqintrin.h   
		LLVM\lib\clang\10.0.0\include\avx512vpopcntdqvlintrin.h   
		LLVM\lib\clang\10.0.0\include\avxintrin.h   
		LLVM\lib\clang\10.0.0\include\bmi2intrin.h   
		LLVM\lib\clang\10.0.0\include\bmiintrin.h   
		LLVM\lib\clang\10.0.0\include\cetintrin.h   
		LLVM\lib\clang\10.0.0\include\cldemoteintrin.h   
		LLVM\lib\clang\10.0.0\include\clflushoptintrin.h   
		LLVM\lib\clang\10.0.0\include\clwbintrin.h   
		LLVM\lib\clang\10.0.0\include\clzerointrin.h   
		LLVM\lib\clang\10.0.0\include\cpuid.h   
		LLVM\lib\clang\10.0.0\include\emmintrin.h   
		LLVM\lib\clang\10.0.0\include\enqcmdintrin.h   
		LLVM\lib\clang\10.0.0\include\f16cintrin.h   
		LLVM\lib\clang\10.0.0\include\float.h   
		LLVM\lib\clang\10.0.0\include\fma4intrin.h   
		LLVM\lib\clang\10.0.0\include\fmaintrin.h   
		LLVM\lib\clang\10.0.0\include\fxsrintrin.h   
		LLVM\lib\clang\10.0.0\include\gfniintrin.h   
		LLVM\lib\clang\10.0.0\include\htmintrin.h   
		LLVM\lib\clang\10.0.0\include\htmxlintrin.h   
		LLVM\lib\clang\10.0.0\include\ia32intrin.h   
		LLVM\lib\clang\10.0.0\include\immintrin.h   
		LLVM\lib\clang\10.0.0\include\intrin.h   
		LLVM\lib\clang\10.0.0\include\inttypes.h   
		LLVM\lib\clang\10.0.0\include\invpcidintrin.h   
		LLVM\lib\clang\10.0.0\include\iso646.h   
		LLVM\lib\clang\10.0.0\include\limits.h   
		LLVM\lib\clang\10.0.0\include\lwpintrin.h   
		LLVM\lib\clang\10.0.0\include\lzcntintrin.h   
		LLVM\lib\clang\10.0.0\include\mm_malloc.h   
		LLVM\lib\clang\10.0.0\include\mm3dnow.h   
		LLVM\lib\clang\10.0.0\include\mmintrin.h   
		LLVM\lib\clang\10.0.0\include\module.modulemap   
		LLVM\lib\clang\10.0.0\include\movdirintrin.h   
		LLVM\lib\clang\10.0.0\include\msa.h   
		LLVM\lib\clang\10.0.0\include\mwaitxintrin.h   
		LLVM\lib\clang\10.0.0\include\nmmintrin.h   
		LLVM\lib\clang\10.0.0\include\omp.h   
		LLVM\lib\clang\10.0.0\include\opencl-c.h   
		LLVM\lib\clang\10.0.0\include\opencl-c-base.h   
		LLVM\lib\clang\10.0.0\include\pconfigintrin.h   
		LLVM\lib\clang\10.0.0\include\pkuintrin.h   
		LLVM\lib\clang\10.0.0\include\pmmintrin.h   
		LLVM\lib\clang\10.0.0\include\popcntintrin.h   
		LLVM\lib\clang\10.0.0\include\prfchwintrin.h   
		LLVM\lib\clang\10.0.0\include\ptwriteintrin.h   
		LLVM\lib\clang\10.0.0\include\rdseedintrin.h   
		LLVM\lib\clang\10.0.0\include\rtmintrin.h   
		LLVM\lib\clang\10.0.0\include\s390intrin.h   
		LLVM\lib\clang\10.0.0\include\sgxintrin.h   
		LLVM\lib\clang\10.0.0\include\shaintrin.h   
		LLVM\lib\clang\10.0.0\include\smmintrin.h   
		LLVM\lib\clang\10.0.0\include\stdalign.h   
		LLVM\lib\clang\10.0.0\include\stdarg.h   
		LLVM\lib\clang\10.0.0\include\stdatomic.h   
		LLVM\lib\clang\10.0.0\include\stdbool.h   
		LLVM\lib\clang\10.0.0\include\stddef.h   
		LLVM\lib\clang\10.0.0\include\stdint.h   
		LLVM\lib\clang\10.0.0\include\stdnoreturn.h   
		LLVM\lib\clang\10.0.0\include\tbmintrin.h   
		LLVM\lib\clang\10.0.0\include\tgmath.h   
		LLVM\lib\clang\10.0.0\include\tmmintrin.h   
		LLVM\lib\clang\10.0.0\include\unwind.h   
		LLVM\lib\clang\10.0.0\include\vadefs.h   
		LLVM\lib\clang\10.0.0\include\vaesintrin.h   
		LLVM\lib\clang\10.0.0\include\varargs.h   
		LLVM\lib\clang\10.0.0\include\vecintrin.h   
		LLVM\lib\clang\10.0.0\include\vpclmulqdqintrin.h   
		LLVM\lib\clang\10.0.0\include\waitpkgintrin.h   
		LLVM\lib\clang\10.0.0\include\wbnoinvdintrin.h   
		LLVM\lib\clang\10.0.0\include\wmmintrin.h   
		LLVM\lib\clang\10.0.0\include\x86intrin.h   
		LLVM\lib\clang\10.0.0\include\xmmintrin.h   
		LLVM\lib\clang\10.0.0\include\xopintrin.h   
		LLVM\lib\clang\10.0.0\include\xsavecintrin.h   
		LLVM\lib\clang\10.0.0\include\xsaveintrin.h   
		LLVM\lib\clang\10.0.0\include\xsaveoptintrin.h   
		LLVM\lib\clang\10.0.0\include\xsavesintrin.h   
		LLVM\lib\clang\10.0.0\include\xtestintrin.h   
		LLVM\lib\clang\10.0.0\include\cuda_wrappers\algorithm   
		LLVM\lib\clang\10.0.0\include\cuda_wrappers\complex   
		LLVM\lib\clang\10.0.0\include\cuda_wrappers\new   
		LLVM\lib\clang\10.0.0\include\fuzzer\FuzzedDataProvider.h   
		LLVM\lib\clang\10.0.0\include\openmp_wrappers\__clang_openmp_math.h   
		LLVM\lib\clang\10.0.0\include\openmp_wrappers\__clang_openmp_math_declares.h   
		LLVM\lib\clang\10.0.0\include\openmp_wrappers\cmath   
		LLVM\lib\clang\10.0.0\include\openmp_wrappers\math.h   
		LLVM\lib\clang\10.0.0\include\ppc_wrappers\emmintrin.h   
		LLVM\lib\clang\10.0.0\include\ppc_wrappers\mm_malloc.h   
		LLVM\lib\clang\10.0.0\include\ppc_wrappers\mmintrin.h   
		LLVM\lib\clang\10.0.0\include\ppc_wrappers\pmmintrin.h   
		LLVM\lib\clang\10.0.0\include\ppc_wrappers\smmintrin.h   
		LLVM\lib\clang\10.0.0\include\ppc_wrappers\tmmintrin.h   
		LLVM\lib\clang\10.0.0\include\ppc_wrappers\xmmintrin.h   
		LLVM\lib\clang\10.0.0\include\profile\InstrProfData.inc   
		LLVM\lib\clang\10.0.0\include\sanitizer\allocator_interface.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\asan_interface.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\common_interface_defs.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\coverage_interface.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\dfsan_interface.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\hwasan_interface.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\linux_syscall_hooks.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\lsan_interface.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\msan_interface.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\netbsd_syscall_hooks.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\scudo_interface.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\tsan_interface.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\tsan_interface_atomic.h   
		LLVM\lib\clang\10.0.0\include\sanitizer\ubsan_interface.h   
		LLVM\lib\clang\10.0.0\include\xray\xray_interface.h   
		LLVM\lib\clang\10.0.0\include\xray\xray_log_interface.h   
		LLVM\lib\clang\10.0.0\include\xray\xray_records.h   
		LLVM\lib\clang\10.0.0\lib\windows   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.asan_cxx-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.asan_dll_thunk-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.asan_dynamic_runtime_thunk-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.asan_dynamic-x86_64.dll   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.asan_dynamic-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.asan-preinit-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.asan-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.builtins-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.fuzzer_no_main-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.fuzzer-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.profile-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.stats_client-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.stats-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.ubsan_standalone_cxx-x86_64.lib   
		LLVM\lib\clang\10.0.0\lib\windows\clang_rt.ubsan_standalone-x86_64.lib   
		LLVM\lib\clang\10.0.0\share\asan_blacklist.txt   
		LLVM\lib\clang\10.0.0\share\cfi_blacklist.txt   
		LLVM\lib\site-packages\lldb   
		LLVM\lib\site-packages\six.py   
		LLVM\lib\site-packages\lldb\formatters   
		LLVM\lib\site-packages\lldb\utils   
		LLVM\lib\site-packages\lldb\__init__.py   
		LLVM\lib\site-packages\lldb\_lldb.pyd   
		LLVM\lib\site-packages\lldb\embedded_interpreter.py   
		LLVM\lib\site-packages\lldb\lldb-argdumper.exe   
		LLVM\lib\site-packages\lldb\formatters\cpp   
		LLVM\lib\site-packages\lldb\formatters\__init__.py   
		LLVM\lib\site-packages\lldb\formatters\attrib_fromdict.py   
		LLVM\lib\site-packages\lldb\formatters\cache.py   
		LLVM\lib\site-packages\lldb\formatters\Logger.py   
		LLVM\lib\site-packages\lldb\formatters\metrics.py   
		LLVM\lib\site-packages\lldb\formatters\synth.py   
		LLVM\lib\site-packages\lldb\formatters\cpp\__init__.py   
		LLVM\lib\site-packages\lldb\formatters\cpp\gnu_libstdcpp.py   
		LLVM\lib\site-packages\lldb\formatters\cpp\libcxx.py   
		LLVM\lib\site-packages\lldb\utils\__init__.py   
		LLVM\lib\site-packages\lldb\utils\in_call_stack.py   
		LLVM\lib\site-packages\lldb\utils\symbolication.py   
	libexec
		LLVM\libexec\c++-analyzer   
		LLVM\libexec\c++-analyzer.bat   
		LLVM\libexec\ccc-analyzer   
		LLVM\libexec\ccc-analyzer.bat   
	share
		LLVM\share\clang   
		LLVM\share\man   
		LLVM\share\opt-viewer   
		LLVM\share\scan-build   
		LLVM\share\scan-view   
		LLVM\share\clang\clang-doc-default-stylesheet.css   
		LLVM\share\clang\clang-format.el   
		LLVM\share\clang\clang-format.py   
		LLVM\share\clang\clang-format-bbedit.applescript   
		LLVM\share\clang\clang-format-diff.py   
		LLVM\share\clang\clang-format-sublime.py   
		LLVM\share\clang\clang-include-fixer.el   
		LLVM\share\clang\clang-include-fixer.py   
		LLVM\share\clang\clang-rename.el   
		LLVM\share\clang\clang-rename.py   
		LLVM\share\clang\clang-tidy-diff.py   
		LLVM\share\clang\index.js   
		LLVM\share\clang\run-clang-tidy.py   
		LLVM\share\clang\run-find-all-symbols.py   
		LLVM\share\man\man1   
		LLVM\share\man\man1\scan-build.1   
		LLVM\share\opt-viewer\opt-diff.py   
		LLVM\share\opt-viewer\optpmap.py   
		LLVM\share\opt-viewer\optrecord.py   
		LLVM\share\opt-viewer\opt-stats.py   
		LLVM\share\opt-viewer\opt-viewer.py   
		LLVM\share\opt-viewer\style.css   
		LLVM\share\scan-build\scanview.css   
		LLVM\share\scan-build\sorttable.js   
		LLVM\share\scan-view\bugcatcher.ico   
		LLVM\share\scan-view\FileRadar.scpt   
		LLVM\share\scan-view\GetRadarVersion.scpt   
		LLVM\share\scan-view\Reporter.py   
		LLVM\share\scan-view\ScanView.py   
		LLVM\share\scan-view\startfile.py   
	Uninstall.exe

```