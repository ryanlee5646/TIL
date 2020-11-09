def login(_id):
    members = ['gyujin', 'egoing']

    for member in members:
        if member == _id:
            return True
    return False
