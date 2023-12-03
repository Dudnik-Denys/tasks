is_num = lambda x: True if 1 >= x.count('.') >= 0 and '-' not in x[1:] \
                           and ''.join(x.replace('-', '', 1).split('.')).isdigit() else False
