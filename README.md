# 自动修复机翻文本插件

这个插件旨在解决机翻过程中出现的常见问题，特别是在游戏本地化和翻译过程中。它能够自动删除机翻后多余的反斜杠符号、修复翻译软件自动换行带来的特殊符号破坏，并确保文本格式符合实际显示需求。
- **例如下面的情况**
![bc73066a8eac1030ceffb4c7ebf1ee5d](https://github.com/user-attachments/assets/e9011d8a-3e81-4b3a-92bb-c90504ddfd68)
‘}’是rpgmaker中用于控制文本大小的特殊符号，因为机翻过程中丢失了其前面的反斜杠 所以在文本中被显示了
## 功能特性

- **删除多余反斜杠**：在使用机器翻译时，可能会出现多余的反斜杠（`\`）。本插件能自动识别并删除这些无效符号，确保文本的清洁与正常显示。
  
- **解决 Translator++ 自动换行带来的符号破坏**：当使用 Translator++ 时，由于自动换行，某些符号可能会被错误处理，本插件能够修复这些符号的破坏，恢复正确的格式。

- **补全缺少的反斜杠**：如果机翻后文本中的特殊符号缺少必要的反斜杠，本插件会自动补全，确保符号格式正确。

- **自动换行处理**：插件可以根据游戏中实际会显示的文本内容跳过RPGMAKER中的特殊符号，进行换行处理，避免显示问题。
## 实际使用范例
![image](https://github.com/user-attachments/assets/c852da90-db08-47e5-b241-64ff32ac5cde)
- **设置每40个全角字符时进行换行，可以看到\N[1]这样的特殊符号 未被计入换行**
## 使用方式
1. 在patterns内定义你的项目的特殊符号（只需要完整符号的一部分即可 如 \N[1],定义成N[,），在end_symbols定义特殊符号的结束符，例如\N[1]，是']'
