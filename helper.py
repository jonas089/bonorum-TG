def format_net(net):
    s = str(net)
    _s = s.split('.')
    res = _s[0] + '.' + _s[1][:2]
    return res
