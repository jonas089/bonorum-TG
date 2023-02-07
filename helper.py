def format_net(net, i):
    s = str(net)
    _s = s.split('.')
    res = _s[0] + '.' + _s[1][:i]
    return res
