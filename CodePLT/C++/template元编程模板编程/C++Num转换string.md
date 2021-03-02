# C++Num转换string



https://stackoverflow.com/questions/201593/is-there-a-simple-way-to-convert-c-enum-to-string



http://th-thielemann.de/tools/cpp-enum-to-string.html

```python

# This script is used to generate strings from C++ enums

import re
import sys
import os

fileName = sys.argv[1]
enumName = os.path.basename(os.path.splitext(fileName)[0])

with open(fileName, 'r') as f:
    content = f.read().replace('\n', '')

searchResult = re.search('enum(.*)\{(.*?)\};', content)
tokens = searchResult.group(2)
tokens = tokens.split(',')
tokens = map(str.strip, tokens)
tokens = map(lambda token: re.search('([a-zA-Z0-9_]*)', token).group(1), tokens)

textOut = ''
textOut += '\n#include "' + enumName + '.hpp"\n\n'
textOut += 'namespace myns\n'
textOut += '{\n'
textOut += '    std::string ToString(ErrorCode errorCode)\n'
textOut += '    {\n'
textOut += '        switch (errorCode)\n'
textOut += '        {\n'

for token in tokens:
    textOut += '        case ' + enumName + '::' + token + ':\n'
    textOut += '            return "' + token + '";\n'

textOut += '        default:\n'
textOut += '            return "Last";\n'
textOut += '        }\n'
textOut += '    }\n'
textOut += '\n'
textOut += '    ' + enumName + ' FromString(const std::string &errorCode)\n'
textOut += '    {\n'
textOut += '        if ("' + tokens[0] + '" == errorCode)\n'
textOut += '        {\n'
textOut += '            return ' + enumName + '::' + tokens[0] + ';\n'
textOut += '        }\n'

for token in tokens[1:]:
    textOut += '        else if("' + token + '" == errorCode)\n'
    textOut += '        {\n'
    textOut += '            return ' + enumName + '::' + token + ';\n'
    textOut += '        }\n'

textOut += '\n'
textOut += '        return ' + enumName + '::Last;\n'
textOut += '    }\n'
textOut += '}\n'

fileOut = open(enumName + '.cpp', 'w')
fileOut.write(textOut)
```




```hpp
#pragma once

#include <string>
#include <cstdint>

namespace myns
{
    enum class ErrorCode : uint32_t
    {
        OK = 0,
        OutOfSpace,
        ConnectionFailure,
        InvalidJson,
        DatabaseFailure,
        HttpError,
        FileSystemError,
        FailedToEncrypt,
        FailedToDecrypt,
        EndOfFile,
        FailedToOpenFileForRead,
        FailedToOpenFileForWrite,
        FailedToLaunchProcess,

        Last
    };

    std::string ToString(ErrorCode errorCode);
    ErrorCode FromString(const std::string &errorCode);
}
```

```
python generate_enum_strings.py ErrorCode.hpp
```

结果是ErrorCode.cpp：




```cpp

```



























