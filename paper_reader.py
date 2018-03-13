import codecs
import coding


def decode_paper_words(file_src_path="paper_sources.txt"):
    l = ''
    encoding = coding.file_encoding(file_src_path)
    print(encoding)
    with codecs.open(file_src_path, 'r', encoding) as f:
        for line in f:
            if line.strip() == '':
                l += '\n' + '  '
            else:
                l += line.rstrip() + ' '
    l.encode('gbk')
    with open('paper_decoded.txt', 'w') as f:
        f.write(l)
    print('格式化完成')

if __name__ == '__main__':
    decode_paper_words()
