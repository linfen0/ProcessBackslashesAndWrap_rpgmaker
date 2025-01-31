import re

# 定义需要匹配的模式
#补全丢失的特殊字符
patterns = [
    'nc<',
    'nr<',
    'px[', 
    'py[',
    'pic[',
    'oc[',
    'oo[',
    'fz[',
    'fn[',
    'fr'
    'af[',
    'ac[',
    'as[',
    'an[',
    'nc[',
    'ni[',
    'nw[',
    'na[',
    'ns[',
    'nt[',
    'ic[',
    'ii[',
    'iw[',
    'ia[',
    'is[',
    'it[',
    '{',
    '}',
    'v[',
    'n[',
    'p[',
    'c[',
    'i[',
    'w[',
    'n<',
    '$',
    '.',
    '|',
    '!',
    '>',
    '<',
    '^',
]
end_symbols=['{','}','$','.','|','!','<','>','^',']']
# 示例文本
text = """
v[x]     - Writes variable x's value.
n[x]     - Writes actor x's name.
p[x]     - Writes party member x's name.
g        - Writes gold currency name.
c[x]     - Changes the colour of the text to x.
i[x]     - Draws icon x at position of the text.
w[x]     - Waits x frames (60 frames = 1 second). Message window only.

NameWindow: Effect:
n<x>     - Creates a name box with x string. Left side. *Note
nc<x>    - Creates a name box with x string. Centered. *Note
nr<x>    - Creates a name box with x string. Right side. *Note

Position: Effect:
px[x]    - Sets x position of text to x.
py[x]    - Sets y position of text to y.

Picture: Effect:
pic[x]   - Draws picture x from the GraphicsPictures folder.

Outline: Effect:
oc[x]    - Sets outline colour to x.
oo[x]    - Sets outline opacity to x.

Font: Effect:
fr       - Resets all font changes.
fz[x]    - Changes font size to x.
fn[x]    - Changes font name to x.
fb       - Toggles font boldness.
fi       - Toggles font italic.
fo       - Toggles font outline.
fs       - Toggles font shadow.

Actor: Effect:
af[x]    - Shows face of actor x. *Note
ac[x]    - Writes out acto's class name. *Note
as[x]    - Writes out acto's subclass name. Req: Class System. *Note
an[x]    - Writes out acto's nickname. *Note

Names: Effect:
nc[x]    - Writes out class x's name.
ni[x]    - Writes out item x's name.
nw[x]    - Writes out weapon x's name.
na[x]    - Writes out armour x's name.
ns[x]    - Writes out skill x's name.
nt[x]    - Writes out state x's name.

Icon Names: Effect:
ic[x]    - Writes out class x's name including icon. *
ii[x]    - Writes out item x's name including icon.
iw[x]    - Writes out weapon x's name including icon.
ia[x]    - Writes out armour x's name including icon.
is[x]    - Writes out skill x's name including icon.
it[x]    - Writes out state x's name including icon.
"""

# 对文本中的模式进行匹配和替换

def add_backslashes(text:str) -> str:
    i=0
    result = []
    while i < len(text):
        for pattern in patterns:
            escape_pattern=re.escape(pattern)
            if re.match(escape_pattern, text[i:], re.IGNORECASE):
                result.append('\\')
                while i < len(text) and text[i] not in end_symbols:
                    result.append(text[i])
                    i+=1
                #if i < len(text):
                    #result.append(text[i])  # Add the end symbol of the special character to the result
        else:
            result.append(text[i])        
            i+=1
    return ''.join(result)
            
            
            

def is_special_escape(text, index):
    """
    判断从 index 位置开始的 \ 是否是特殊符号的转义符。
    """
    if index >= len(text):
            return False
    text_slice = text[index:]
    for pattern in patterns:
        pattern = re.escape('\\' + pattern)
        if re.match(pattern, text_slice, re.IGNORECASE):
            return True
    return False

# 处理文本中的反斜杠,并添加换行符
def process_backslashes_and_wrap(text, max_width=40):
    result = []
    current_width = 0
    i = 0
    while i < len(text):
        if text[i] == '\\' :
            if is_special_escape(text, i):
                #由于该算法在特殊字符末尾时会算一个宽度因此，宽度此时应该先减1
                current_width -= 1
                while i < len(text) and text[i] not in end_symbols:
                    result.append(text[i])
                    i += 1
                #if i < len(text):
                    #result.append(text[i])  # Add the end symbol of the special character to the result
            else:
                i+=1
        if current_width >= max_width:
            result.append('\n')
            current_width = 0  # Reset current width after wrapping
        if i < len(text):
            result.append(text[i])
            import wcwidth
            current_width += wcwidth.wcwidth(text[i])
        i += 1
    return ''.join(result)

