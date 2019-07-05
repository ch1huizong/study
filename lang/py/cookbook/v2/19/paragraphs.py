#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import itertools

# 输出段落,归组，可以更进一步抽象
def paragraphs(lines, is_separator=str.isspace, joiner=''.join):
    paragraph = []   # 使用一个list数据结构,临时列表
    for line in lines:
        if is_separator(line):
            if paragraph:
                yield joiner(paragraph)
                paragraph = []
        else:
            paragraph.append(line)
    if paragraph:
        yield joiner(paragraph)
        
def paragraphs1(lines, is_separator=str.isspace, joiner=''.join):
    for separator_group, lineiter in itertools.groupby(lines,key=is_separator):
        if not separator_group:
            yield joiner(lineiter)

# 把一些逻辑上连续的物理行(以\连接)输出
def logical_lines(physical_lines, joiner=''.join):
    logical_line = []
    for line in physical_lines:
        stripped = line.rstrip()
        if stripped.endswith('\\'):  #python程序内表示
            logical_line.append(stripped[:-1])
        else:
            logical_line.append(stripped)
            yield joiner(logical_line)
            logical_line = []
    if logical_line:   # 最后一行以\结尾
        yield joiner(logical_line)

# 文本够小，内存够大
def logical_lines1(physical_lines, joiner=''.join, seperator=''):
    return joiner(physical_lines).replace("\\\n",seperator).splitlines(True)

# 数据块流处理成行流, 数据块中数据以特定的分割符(eol)分割
def ilines(source_iterable, eol='\r\n', out_eol='\n'):
    tail = ''
    for block in source_iterable:
        pieces = (tail + block).split(eol)
        tail = pieces.pop()   # 若有，留待和下一个块组成新的数据块
        for line in pieces:
            yield line + out_eol
    if tail:
        yield tail


if __name__ == '__main__':
    text = "a first\nparagraph\n\nand a\nseconde one\n\n"
    for p in paragraphs(text.splitlines(True)):
        print repr(p)
    print "*"*60
    for p in paragraphs1(text.splitlines(True)):
        print repr(p)

    logical_text = 'some\\\n','lines\\\n','get\n','joined\\\n','up\n'
    print "Logical Joined:"
    for line in logical_text:
        print 'P:', repr(line)
    for line in logical_lines(logical_text,' '.join):
        print 'L:', repr(line)

