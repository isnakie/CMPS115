def index():
    if request.vars.sym:
        session.sym = request.vars.sym
        redirect(URL('index'))
    graphURL = "https://blash.pythonanywhere.com/blash/static/prices/"+str(session.sym)+".html"
    TitleString = str(session.sym)
    if session.sym is None:
        TitleString = "AAPL"
    
    return locals();
