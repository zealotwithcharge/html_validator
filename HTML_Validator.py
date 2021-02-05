#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    stack = []
    try:
        tags = _extract_tags(html)
    except ValueError:
        return False

    for tag in tags:

        # if the tag is an opening tag,
        # then push it on to the stack
        if tag[1] != '/':
            stack.append(tag)

        # if it's a closing tag,
        # then check if the top of the stack matches
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if top[1:-1] != tag[2:-1]:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    tags = []
    current_tag = None
    inside_tag = False
    seen_space = False

    for i in range(len(html)):
        if html[i] == '<':
            current_tag = ''
            inside_tag = True

        if inside_tag and html[i] == ' ':
            seen_space = True

        if inside_tag and (not seen_space or html[i] == '>'):
            current_tag += html[i]

        if html[i] == '>':
            inside_tag = False
            seen_space = False
            tags.append(current_tag)

    if inside_tag:
        raise ValueError('found < without matching >')

    return tags
