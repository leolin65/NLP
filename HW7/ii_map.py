#!/usr/bin/env python
# -*- coding: utf-8 -*-


def inverted_index_map(lines):
    for k, line in enumerate(lines, 1):
        buffer_str=" "
        downspace="_"
        word_list=line.split()
        i=" "
        j=word_list[len(line.split())-1]
        if len(line.split())==2:
            for word in line.split():
                yield word_list[0], i, buffer_str, buffer_str, buffer_str, buffer_str, word_list[0], buffer_str, buffer_str, buffer_str, buffer_str, j
        elif len(line.split())==3:
            yield word_list[0], word_list[1], i, buffer_str, buffer_str, buffer_str, word_list[0], word_list[1], buffer_str, buffer_str, buffer_str, j
            yield  downspace, word_list[1], i, buffer_str, buffer_str, buffer_str, word_list[0], word_list[1], buffer_str, buffer_str, buffer_str, j
            yield word_list[0],  downspace, i, buffer_str, buffer_str, buffer_str, word_list[0], word_list[1], buffer_str, buffer_str, buffer_str, j
        elif len(line.split())==4:
            yield word_list[0], word_list[1], word_list[2], i, buffer_str, buffer_str, word_list[0], word_list[1], word_list[2], buffer_str, buffer_str, j
            yield word_list[0], word_list[1],  downspace, i, buffer_str, buffer_str, word_list[0], word_list[1], word_list[2], buffer_str, buffer_str, j
            yield word_list[0],  downspace, word_list[2], i, buffer_str, buffer_str, word_list[0], word_list[1], word_list[2], buffer_str, buffer_str, j
            yield  downspace, word_list[1], word_list[2], i, buffer_str, buffer_str, word_list[0], word_list[1], word_list[2], buffer_str, buffer_str, j
            yield  downspace,  downspace, word_list[2], i, buffer_str, buffer_str, word_list[0], word_list[1], word_list[2], buffer_str, buffer_str, j
            yield  downspace, word_list[1],  downspace, i, buffer_str, buffer_str, word_list[0], word_list[1], word_list[2], buffer_str, buffer_str, j
            yield word_list[0],  downspace,  downspace, i, buffer_str, buffer_str, word_list[0], word_list[1], word_list[2], buffer_str, buffer_str, j
        elif len(line.split())==5:
            yield word_list[0], word_list[1], word_list[2], word_list[3], i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield word_list[0], word_list[1], word_list[2],  downspace, i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield word_list[0], word_list[1],  downspace, word_list[3], i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield word_list[0],  downspace, word_list[2], word_list[3], i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield  downspace, word_list[1], word_list[2], word_list[3], i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield  downspace,  downspace, word_list[2], word_list[3], i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield  downspace, word_list[1],  downspace, word_list[3], i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield  downspace, word_list[1], word_list[2],  downspace, i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield word_list[0],  downspace,  downspace, word_list[3], i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield word_list[0],  downspace, word_list[2],  downspace, i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield word_list[0], word_list[1],  downspace,  downspace, i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield  downspace,  downspace,  downspace, word_list[3], i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield  downspace,  downspace, word_list[2],  downspace, i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield  downspace, word_list[1],  downspace,  downspace, i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
            yield word_list[0],  downspace,  downspace,  downspace, i, buffer_str, word_list[0], word_list[1], word_list[2], word_list[3], buffer_str, j
        elif len(line.split())==6:
            yield word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0], word_list[1], word_list[2], word_list[3],  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0], word_list[1], word_list[2],  downspace, word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0], word_list[1], word_list[2],  downspace,  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0], word_list[1],  downspace, word_list[3], word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0], word_list[1],  downspace, word_list[3],  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0], word_list[1],  downspace,  downspace, word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0], word_list[1],  downspace,  downspace,  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0],  downspace, word_list[2], word_list[3], word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0],  downspace, word_list[2], word_list[3],  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0],  downspace, word_list[2],  downspace, word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0],  downspace, word_list[2],  downspace,  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0],  downspace,  downspace, word_list[3], word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0],  downspace,  downspace, word_list[3],  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0],  downspace,  downspace,  downspace, word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield word_list[0],  downspace,  downspace,  downspace,  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace, word_list[1], word_list[2], word_list[3], word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace, word_list[1], word_list[2], word_list[3],  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace, word_list[1], word_list[2],  downspace, word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace, word_list[1], word_list[2],  downspace,  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace, word_list[1],  downspace, word_list[3], word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace, word_list[1],  downspace, word_list[3],  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace, word_list[1],  downspace,  downspace, word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace, word_list[1],  downspace,  downspace,  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace,  downspace, word_list[2], word_list[3], word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace,  downspace, word_list[2], word_list[3],  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace,  downspace, word_list[2],  downspace, word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace,  downspace, word_list[2],  downspace,  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace,  downspace,  downspace, word_list[3], word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace,  downspace,  downspace, word_list[3],  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            yield  downspace,  downspace,  downspace,  downspace, word_list[4], i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j
            #yield  downspace,  downspace,  downspace,  downspace,  downspace, i, word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], j

            


if __name__ == '__main__':
    import fileinput
    for a1, a2 , a3 , a4 , a5 , a6 , a7 , a8 , a9 , a10 , a11 , a12 in inverted_index_map(fileinput.input()):
        print(a1, a2, a3, a4, a5, a6 , a7 , a8 , a9 , a10 , a11, a12)
