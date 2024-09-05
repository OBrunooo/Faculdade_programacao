def checking(joker, attempt):
    if(joker == attempt):
        return 'ok'
    if(joker > attempt):
        return 'small'
    if(joker < attempt):
        return 'big'