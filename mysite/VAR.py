
def LANG(request):
    try:
        username=request.session['user_name']
        userid=request.session['user_id']
        is_login=request.session['is_login']
    except Exception as e:
        username=None
        userid=None
        is_login=False
    lang={
        'SITE':'笑话大全',
        'username':username,
        'userid':userid,
        'is_login':is_login,
    }
    return lang