def checking(secret_number, attempt):
    if(secret_number == attempt):
        return 'ok'
    if(secret_number > attempt):
        return 'small'
    if(secret_number < attempt):
        return 'big'