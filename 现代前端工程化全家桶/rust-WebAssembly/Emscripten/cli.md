# cli










```
\emsdk>emsdk install latest
 emsdk: No command given. Please call one of the following:

   emsdk list [--old] [--uses]  - Lists all available SDKs and tools and their
                                  current installation status. With the --old
                                  parameter, also historical versions are
                                  shown. If --uses is passed, displays the
                                  composition of different SDK packages and
                                  dependencies.

   emsdk update                 - Updates emsdk to the newest version, and also
                                  runs 'update-tags' (below). If you have
                                  bootstrapped emsdk via cloning directly from
                                  GitHub, call "git pull" instead to update emsdk.

   emsdk update-tags            - Fetches the most up to date list of available
                                  Emscripten tagged and other releases from the
                                  servers.

   emsdk install [options] <tool 1> <tool 2> <tool 3> ...
                                - Downloads and installs given tools or SDKs.
                                  Options can contain:

                         -j<num>: Specifies the number of cores to use when
                                  building the tool. Default: use one less
                                  than the # of detected cores.

                  --build=<type>: Controls what kind of build of LLVM to
                                  perform. Pass either 'Debug', 'Release',
                                  'MinSizeRel' or 'RelWithDebInfo'. Default:
                                  'RelWithDebInfo'.

              --generator=<type>: Specifies the CMake Generator to be used
                                  during the build. Possible values are the
                                  same as what your CMake supports and whether
                                  the generator is valid depends on the tools
                                  you have installed. Defaults to 'Unix Makefiles'
                                  on *nix systems. If generator name is multiple
                                  words, enclose with single or double quotes.

                       --shallow: When installing tools from one of the git
                                  development branches, this parameter can be
                                  passed to perform a shallow git clone instead
                                  of a full one.  This reduces the amount of
                                  network transfer that is needed. This option
                                  should only be used when you are interested in
                                  downloading one of the development branches,
                                  but are not looking to develop Emscripten
                                  yourself.  Default: disabled, i.e. do a full
                                  clone.

                   --build-tests: If enabled, LLVM is built with internal tests
                                  included. Pass this to enable running test
                                  other.test_llvm_lit in the Emscripten test
                                  suite. Default: disabled.
             --enable-assertions: If specified, LLVM is built with assert()
                                  checks enabled. Useful for development
                                  purposes. Default: Enabled
            --disable-assertions: Forces assertions off during the build.

      --vs2013/--vs2015/--vs2017: If building from source, overrides to build
                                  using the specified compiler. When installing
                                  precompiled packages, this has no effect.
                                  Note: The same compiler specifier must be
                                  passed to the emsdk activate command to
                                  activate the desired version.

                                  Notes on building from source:

                                  To pass custom CMake directives when configuring
                                  LLVM build, specify the environment variable
                                  LLVM_CMAKE_ARGS="param1=value1,param2=value2"
                                  in the environment where the build is invoked.
                                  See README.md for details.

   emsdk uninstall <tool/sdk>   - Removes the given tool or SDK from disk.

   emsdk activate [--global] [--embedded] [--build=type] [--vs2013/--vs2015/--vs2017] <tool/sdk>

                                - Activates the given tool or SDK in the
                                  environment of the current shell. If the
                                  --global option is passed, the registration
                                  is done globally to all users in the system
                                  environment. If the --embedded option is
                                  passed, all Emcripten configuration files as
                                  well as the temp, cache and ports directories
                                  are located inside the Emscripten SDK
                                  directory rather than the user home
                                  directory. If a custom compiler version was
                                  used to override the compiler to use, pass
                                  the same --vs2013/--vs2015/--vs2017 parameter
                                  here to choose which version to activate.

   emcmdprompt.bat              - Spawns a new command prompt window with the
                                  Emscripten environment active.

       Both commands 'install' and 'activate' accept an optional parameter
       '--build=type', which can be used to override what kind of installation
       or activation to perform. Possible values for type are Debug, Release,
       MinSizeRel or RelWithDebInfo. Note: When overriding a custom build type,
       be sure to match the same --build= option to both 'install' and
       'activate' commands and the invocation of 'emsdk_env', or otherwise
       these commands will default to operating on the default build type
       which in and RelWithDebInfo.
```