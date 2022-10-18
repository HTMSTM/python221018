#temp3.py

def userURIBuilder(server, port, **user):
    str="http://" + server + ":" + port + "/?"
    # 딕셔너리는 기정의된 메소드 : items(), keys(), values()
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

print( userURIBuilder("test.com", "8080") )

print( userURIBuilder("test.com", "8080", id="kim", passwd="1234") )

print( userURIBuilder("test.com", "8080", id="kim", passwd="1234", name = "mike") )

