is_non_negative_num = lambda x: True if 1 >= x.count('.') >= 0 and ''.join(x.split('.')).isdigit() and \
                                        int(''.join(x.split('.')).isdigit()) >= 0 else False

# is_non_negative_num = lambda q: q.replace('.', '', 1).isdigit()
