# html_polite_to_plain.py

import re
import sys

def convert_text(text: str) -> str:
    # 공손체 종결어미를 단정체로 매핑
    patterns = {
        r'합니다': '한다',
        r'했습니다': '했다',
        r'되었습니다': '되었다',
        r'됐습니다': '됐다',
        r'였습니다': '이었다',
        r'입니다': '이다',
        r'되었습니다': '되었다',
        r'없습니다': '없다',
        r'있습니다': '있다',
        r'됩니다': '된다',
        r'습니까': '는가',
    }
    for pat, repl in patterns.items():
        text = re.sub(pat, repl, text)
        
    return text

def convert_file(input_path: str, output_path: str):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    converted = convert_text(content)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(converted)
    print(f"Converted file saved to {output_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python html_polite_to_plain.py <input.html> <output.html>")
        sys.exit(1)
    convert_file(sys.argv[1], sys.argv[2])