# DryWetMIDI







https://melanchall.github.io/drywetmidi/



DryWetMIDI 是用于处理 MIDI 数据和 MIDI 设备的 .NET 库。它允许：

读取、写入和创建标准 MIDI 文件 (SMF)。也可以读取SMF 包装到 RIFF 块的RMID文件。在读取或写入 MIDI 文件时，您可以轻松捕获特定错误，因为 MIDI 文件中的所有可能错误都显示为单独的异常类。
向 MIDI 设备发送MIDI 事件/从 MIDI 设备接收它们，播放MIDI 数据并记录它。此 API 支持 Windows 和 macOS。
微调读写过程。例如，它允许读取损坏的文件并修复它们，或构建 MIDI 文件验证器。
实现可以写入和读取 MIDI 文件的自定义元事件和自定义块。
使用低级对象（如事件）或高级对象（如 note）管理 MIDI 文件的内容（阅读库文档的高级数据管理部分）。
构建音乐作品（参见图书馆文档的Pattern页面）并使用音乐理论 API（参见Music Theory - Overview文章）。
执行复杂的任务，如量化、音符拆分或将 MIDI 文件转换为 CSV 表示（请参阅库文档的工具页面）。














