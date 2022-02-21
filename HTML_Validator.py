#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation
    by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a
    # list of html tags without any extra text;
    # then process these html tags using the balanced parentheses
    # algorithm from the class/book
    # the main difference between your code and the code from class
    # will be that you will have to keep track of not just the 3
    # types of parentheses,
    # but arbitrary text located between the html tags
    valid_html = _extract_tags(html)

    stack = []

    for tag in valid_html:
        if tag[1] != "/":
            stack.append(tag)
        else:
            if len(stack) != 0 and stack[-1] == "<" + tag[2:]:
                stack.pop()
            else:
                return False
    if len(valid_html) == 0 and ('<' in html or '>' in html):
        return False
    return len(stack) == 0


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not
    meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained
    in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    flag = False
    tag_list = []
    for char in html:
        if char == "<":
            tag_list.append("")
            flag = True
        elif char == ">":
            tag_list[-1] += ">"
            flag = False
        elif char == " " and flag:
            flag = False
        if flag:
            tag_list[-1] += char
    if len(tag_list) != 0 and tag_list[-1][-1] != ">":
        tag_list.pop()
    return tag_list
