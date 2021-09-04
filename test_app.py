import app

def test_hello():
    a = app.hello()

def test_echo():
    record = {i:0 for i in range(1,13)}
    a = app.echo(2)
    assert a[2] == "February"
    b = app.echo(13)
    assert b["error"] == "invalid input"