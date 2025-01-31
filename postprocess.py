import pandas as pd
import os
import re

# 定义输入文件夹和输出文件夹路径
def process_text(text):
    if pd.isna(text):
        return ''
    # 移除所有换行符、制表符和回车符
    processed_text = re.sub(r'[\t\n\r]', '', text)
    #补全特殊字符
    import patterns as pt
    processed_text = pt.add_backslashes(processed_text)
    #清除多余的反斜杠
    processed_text = re.sub(r'\\\\', r'\\', processed_text)
    # 处理反斜杠,并换行
    processed_text = pt.process_backslashes_and_wrap(processed_text)
    
    return ''.join(processed_text)

# 示例用法
original_text = """\\n\\p这是一段包含中文和English的混合文本，这里有一个\n换行符和一个\t制表符。
接下来是超长的测试行：这是一行需要测试自动换行功能的文本，包含中文字符和English单词，直到达到42个半角字符宽度自动换行。"""
test2='\\。\\。\\木头人你好我是N[2]Mort\\\\\\isFn[Vampire Caligraphy],木N[3]兹\\C[3\n]米Itis mygo,'
input_folder = "D:\\MY_APPLICATION\\RpG_GAME\\Rpg game\\ai_trans_monline\\ai_transv3\\exported\\YAML\\res00000"  # 输入文件夹路径
output_folder = "D:\\MY_APPLICATION\\RpG_GAME\\Rpg game\\ai_trans_monline\\ai_transv3\\exported\\YAML\\output"  # 输出文件夹路径
print(f'raw_text:\n{test2}')
processed_result = process_text(test2)
processed_result = process_text(processed_result)
print(f'processed_result:\n{processed_result}')
# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith('.xlsx'):
        # 构建完整的输入文件路径
        input_file_path = os.path.join(input_folder, filename)
        # 读取Excel文件
        df = pd.read_excel(input_file_path)
        
        # 假设第二列的列名是 'Initial'，如果不是，请替换为实际的列名
        # 删除第二列中的多余反斜杠
        
        #df['Initial'] = df['Initial'].str.replace(r'\\+', '', regex=True)
        
        # 每21个中文字符插入一个换行符
        df['Initial'] = df['Machine translation']
        df['Machine translation'] = df['Initial'].apply(process_text)
        
        # 构建完整的输出文件路径
        output_file_path = os.path.join(output_folder, filename)
        
        # 保存修改后的Excel文件到输出文件夹
        df.to_excel(output_file_path, index=False)

        print(f"Processed and saved: {output_file_path}")