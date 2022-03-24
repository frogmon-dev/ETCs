from SharedMemory import SharedMemory
import contextlib

def test_connection():
    print("Create Server instance without Client:", end=" ")
    try:
        # with contextlib.redirect_stdout(None):
        s = SharedMemory("test1", log="./test_server.log", client=False)
        print('values = %s' % s.getValue())
        s.close()
        assert True
        print("SUCCESSED")
    except:
        print("FAILED")
        assert False

print("-"*10)
test_connection()        

'''
# Creating server instance access to the shared named 'shared_space'
S = SharedMemory("test1", log="./test_server.log", client=False)

firstValue = S.getValue()

while True:
    if S.getAvailability():
        if firstValue != S.getValue():
            firstValue = S.getValue()
            print("new values = %s" % firstValue)
'''