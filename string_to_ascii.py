"""Converts string to a list of ASCII values
"""
def sv_main(string=[[]]):
    in_sockets = [
        ['s', 'String', string]]

    ascii_values = []

    if len(string[0]) > 0:
        joined = ''.join([ ''.join(word) for word in string[0] ])
        ascii_values = [ ord(c) for c in joined ]

    out_sockets = [['s', 'ASCII', [ascii_values]]]

    return in_sockets, out_sockets
