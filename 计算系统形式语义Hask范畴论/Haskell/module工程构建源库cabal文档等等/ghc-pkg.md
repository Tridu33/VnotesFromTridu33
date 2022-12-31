
# ghc

```
> ghc --help
Usage:

    ghc.exe [command-line-options-and-input-files]

To compile and link a complete Haskell program, run the compiler like
so:

    ghc.exe Main

where the module Main is in a file named Main.hs (or Main.lhs) in the
current directory.  The other modules in the program will be located
and compiled automatically, and the linked program will be placed in
the file `Main' (or `Main.exe' on Windows).

Alternatively, ghc.exe can be used to compile files individually.  Each
input file is guided through (some of the) possible phases of a
compilation:

    - unlit:    extract code from a "literate program"
    - hscpp:    run code through the C pre-processor (if -cpp flag given)
    - hsc:      run the Haskell compiler proper
    - gcc:      run the C compiler (if compiling via C)
    - as:       run the assembler
    - ld:       run the linker

For each input file, the phase to START with is determined by the
file's suffix:

    - .lhs      literate Haskell                 unlit
    - .hs       plain Haskell                    ghc
    - .hc       C from the Haskell compiler      gcc
    - .c        C not from the Haskell compiler  gcc
    - .s        assembly language                as
    - other     passed directly to the linker    ld

The phase at which to STOP processing is determined by a command-line
option:

    -E          stop after generating preprocessed, de-litted Haskell
                     (used in conjunction with -cpp)
    -C          stop after generating C (.hc output)
    -S          stop after generating assembler (.s output)
    -c          stop after generating object files (.o output)

Other commonly-used options are:

    -v[n]           Control verbosity (n is 0--5, normal verbosity level is 1,
                      -v alone is equivalent to -v3)

    -O              An `optimising' package of compiler flags, for faster code

    -prof           Compile for cost-centre profiling
                     (add -fprof-auto for automagic cost-centres on all
                      top-level functions)

    -H14m           Increase compiler's heap size (might make compilation
                    faster, especially on large source files).

    -M              Output Makefile rules recording the
                    dependencies of a list of Haskell files.

Given the above, here are some TYPICAL invocations of ghc.exe:

    # compile a Haskell module to a .o file, optimising:
    % ghc.exe -c -O Foo.hs
    # link three .o files into an executable called "test":
    % ghc.exe -o test Foo.o Bar.o Baz.o
    # compile a Haskell module to C (a .hc file), using a bigger heap:
    % ghc.exe -C -H16m Foo.hs
    # compile Haskell-produced C (.hc) to assembly language:
    % ghc.exe -S Foo.hc

The User's Guide has more information about GHC's *many* options.  An
online copy can be found here:

   http://www.haskell.org/ghc/docs/latest/html/users_guide/

If you *really* want to see every option, then you can pass
'--show-options' to the compiler.
```






# 1. ghc-pkg

C:\Program Files\Haskell Platform\8.6.3\lib


C:\Users\admin\AppData\Roaming\ghc\x86_64-mingw32-8.6.3




C:\Users\admin\AppData\Roaming\cabal\x86_64-windows-ghc-8.6.3\


```
C:\Users\admin>ghc-pkg
ghc-pkg: missing command
For usage information see 'ghc-pkg --help'.

C:\Users\admin>ghc-pkg --help
Usage:
  ghc-pkg init {path}
    Create and initialise a package database at the location {path}.
    Packages can be registered in the new database using the register
    command with --package-db={path}.  To use the new database with GHC,
    use GHC's -package-db flag.

  ghc-pkg register {filename | -}
    Register the package using the specified installed package
    description. The syntax for the latter is given in the ghc-pkg
    documentation.  The input file should be encoded in UTF-8.

  ghc-pkg update {filename | -}
    Register the package, overwriting any other package with the
    same name. The input file should be encoded in UTF-8.

  ghc-pkg unregister [pkg-id]
    Unregister the specified packages in the order given.

  ghc-pkg expose {pkg-id}
    Expose the specified package.

  ghc-pkg hide {pkg-id}
    Hide the specified package.

  ghc-pkg trust {pkg-id}
    Trust the specified package.

  ghc-pkg distrust {pkg-id}
    Distrust the specified package.

  ghc-pkg list [pkg]
    List registered packages in the global database, and also the
    user database if --user is given. If a package name is given
    all the registered versions will be listed in ascending order.
    Accepts the --simple-output flag.

  ghc-pkg dot
    Generate a graph of the package dependencies in a form suitable
    for input for the graphviz tools.  For example, to generate a PDF
    of the dependency graph: ghc-pkg dot | tred | dot -Tpdf >pkgs.pdf

  ghc-pkg find-module {module}
    List registered packages exposing module {module} in the global
    database, and also the user database if --user is given.
    All the registered versions will be listed in ascending order.
    Accepts the --simple-output flag.

  ghc-pkg latest {pkg-id}
    Prints the highest registered version of a package.

  ghc-pkg check
    Check the consistency of package dependencies and list broken packages.
    Accepts the --simple-output flag.

  ghc-pkg describe {pkg}
    Give the registered description for the specified package. The
    description is returned in precisely the syntax required by ghc-pkg
    register.

  ghc-pkg field {pkg} {field}
    Extract the specified field of the package description for the
    specified package. Accepts comma-separated multiple fields.

  ghc-pkg dump
    Dump the registered description for every package.  This is like
    "ghc-pkg describe '*'", except that it is intended to be used
    by tools that parse the results, rather than humans.  The output is
    always encoded in UTF-8, regardless of the current locale.

  ghc-pkg recache
    Regenerate the package database cache.  This command should only be
    necessary if you added a package to the database by dropping a file
    into the database directory manually.  By default, the global DB
    is recached; to recache a different DB use --user or --package-db
    as appropriate.

 Substring matching is supported for {module} in find-module and
 for {pkg} in list, describe, and field, where a '*' indicates
 open substring ends (prefix*, *suffix, *infix*).  Use --ipid to
 match against the installed package ID instead.

  When asked to modify a database (register, unregister, update,
  hide, expose, and also check), ghc-pkg modifies the global database by
  default.  Specifying --user causes it to act on the user database,
  or --package-db can be used to act on another database
  entirely. When multiple of these options are given, the rightmost
  one is used as the database to act upon.

  Commands that query the package database (list, tree, latest, describe,
  field) operate on the list of databases specified by the flags
  --user, --global, and --package-db.  If none of these flags are
  given, the default is --global --user.

 The following optional flags are also accepted:

                 --user                   use the current user's package database
                 --global                 use the global package database
  -f FILE/DIR    --package-db=FILE/DIR    use the specified package database
                 --package-conf=FILE/DIR  use the specified package database (DEPRECATED)
                 --global-package-db=DIR  location of the global package database
                 --no-user-package-db     never read the user package database
                 --user-package-db=DIR    location of the user package database (use instead of default)
                 --no-user-package-conf   never read the user package database (DEPRECATED)
                 --force                  ignore missing dependencies, directories, and libraries
                 --force-files            ignore missing directories and libraries only
                 --enable-multi-instance  allow registering multiple instances of the same package version
                 --expand-env-vars        expand environment variables (${name}-style) in input package descriptions
                 --expand-pkgroot         expand ${pkgroot}-relative paths to absolute in output package descriptions
                 --no-expand-pkgroot      preserve ${pkgroot}-relative paths in output package descriptions
  -?             --help                   display this help and exit
  -V             --version                output version information and exit
                 --simple-output          print output in easy-to-parse format for some commands
                 --names-only             only print package names, not versions; can only be used with list --simple-output
                 --ignore-case            ignore case for substring matching
                 --ipid, --unit-id        interpret package arguments as unit IDs (e.g. installed package IDs)
  -v[Verbosity]  --verbose[=Verbosity]    verbosity level (0-2, default 1)

C:\Users\admin>ghc-pkg -V
GHC package manager version 8.6.3

C:\Users\admin>ghc-pkg -list
ghc-pkg: unrecognized option `-l'
unrecognized option `-i'
unrecognized option `-s'
unrecognized option `-t'
For usage information see 'ghc-pkg --help'.

C:\Users\admin>ghc-pkg list
C:\Program Files\Haskell Platform\8.6.3\lib\package.conf.d
    Cabal-2.4.0.1
    Win32-2.6.1.0
    array-0.5.3.0
    base-4.12.0.0
    binary-0.8.6.0
    bytestring-0.10.8.2
    containers-0.6.0.1
    deepseq-1.4.4.0
    directory-1.3.3.0
    filepath-1.4.2.1
    (ghc-8.6.3)
    ghc-boot-8.6.3
    ghc-boot-th-8.6.3
    ghc-compact-0.1.0.0
    ghc-heap-8.6.3
    ghc-prim-0.5.3
    ghci-8.6.3
    haskeline-0.7.4.3
    hpc-0.6.0.3
    hscolour-1.24.4
    integer-gmp-1.0.2.0
    libiserv-8.6.3
    mtl-2.2.2
    parsec-3.1.13.0
    pretty-1.1.3.6
    process-1.6.3.0
    rts-1.0
    stm-2.5.0.0
    template-haskell-2.14.0.0
    text-1.2.3.1
    time-1.8.0.2
    transformers-0.5.5.0
    xhtml-3000.2.2.1

C:\Users\admin\AppData\Roaming\ghc\x86_64-mingw32-8.6.3\package.conf.d
    Boolean-0.2.4
    Euterpea-2.0.7
    GLURaw-2.0.0.4
    GLUT-2.7.0.15
    HCodecs-0.5.1
    HSoM-1.0.0
    JuicyPixels-3.3.3.1
    MemoTrie-0.6.9
    NumInstances-1.4
    ObjectName-1.1.0.1
    OpenGL-3.0.3.0
    OpenGLRaw-3.3.3.0
    PortMidi-0.2.0.0
    QuickCheck-2.13.2
    SHA-1.6.4.4
    StateVar-1.2
    Stream-0.4.7.2
    UISF-0.4.0.0
    adjunctions-4.4
    ansi-terminal-0.9.1
    arrows-0.4.4.2
    async-2.2.2
    base-orphans-0.8.1
    base16-bytestring-0.1.1.6
    base64-bytestring-1.0.0.2
    bifunctors-5.5.4
    blaze-builder-0.4.1.0
    bytestring-builder-0.10.8.2.0
    cabal-doctest-1.0.6
    call-stack-0.2.0
    case-insensitive-1.2.1.0
    cereal-0.5.8.1
    circle-packing-0.1.0.6
    colour-2.3.5
    comonad-5.0.5
    contravariant-1.5.2
    cryptohash-sha256-0.11.101.0
    data-default-class-0.1.2.0
    data-default-instances-containers-0.0.1
    data-default-instances-dlist-0.0.1
    diagrams-solve-0.1.1
    digest-0.0.1.2
    distributive-0.6
    dlist-0.8.0.7
    ed25519-0.0.5.0
    edit-distance-0.2.2.1
    entropy-0.4.1.4
    exceptions-0.10.2
    fast-math-1.0.2
    fingertree-0.1.4.2
    fixed-0.3
    free-5.1.1
    groups-0.4.1.0
    half-0.3
    hashable-1.2.7.0
    hashable-1.3.0.0
    heap-1.0.4
    integer-logarithms-1.0.3
    invariant-0.5.3
    kan-extensions-5.2
    lazysmallcheck-0.6
    lens-4.17.1
    loop-0.3.0
    markov-chain-0.0.3.4
    matrices-0.5.0
    microlens-0.4.11.2
    mintty-0.1.2
    mtl-compat-0.2.2
    network-uri-2.6.1.0
    newtype-generics-0.5.3
    old-locale-1.0.0.7
    parallel-3.2.2.0
    primitive-0.7.0.0
    profunctors-5.4
    pure-fft-0.2.0
    random-1.1
    reflection-2.1.4
    semigroupoids-5.3.2
    semigroups-0.19
    splitmix-0.0.3
    tagged-0.8.6
    tar-0.5.1.1
    th-abstraction-0.3.1.0
    transformers-base-0.4.5.2
    transformers-compat-0.6.5
    unordered-containers-0.2.10.0
    vector-0.12.0.3
    void-0.7.3
    windns-0.1.0.1
    zlib-0.6.2


```



















