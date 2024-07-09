import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"

def markdown_to_blocks(markdown):
    return list(map(lambda a: a.strip(), re.split("\n{2,}", markdown)))

def block_to_block_type(block):
    lines = block.split("\n")
    if all(bool(re.match(r"^[#]{1,6} ", line) for line in lines)):
        return block_type_heading
    if all(bool(re.match(r"^```.*```$", line) for line in lines)):
        return block_type_code
    if all(bool(re.match(r"^>", line) for line in lines)):
        return block_type_quote
    if all(bool(re.match(r"^[*-]{1} ", line) for line in lines)):
        return block_type_ulist
    if lines[0][0:2] == '1. ':
        flag_ordered_list = True
        previous_num = 1
        for line in lines[1:]:
            if bool(re.match(r"^[*-]{1} ", line)) and int(line[0:line.index(". ")]) - 1 == previous_num:
                pass
            else:
                flag_ordered_list = False
                break
        if flag_ordered_list:
            return block_type_olist
    return block_type_paragraph

