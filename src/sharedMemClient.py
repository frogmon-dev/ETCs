from SharedMemory.SharedMemory import SharedMemory
import contextlib
import time

def test_str():
    print("Create Client instance containing a \"string\":", end=" ")
    try:
        # with contextlib.redirect_stdout(None):
        c = SharedMemory("test1", "azerty", log='./test_client.log', client=True)
        assert type(c.getValue()) is str
        assert type(c[0]) is str
        #time.sleep(10)
        #exit()

        print('values = %s' % c.getValue())
        c.close()
        print("SUCCESSED")
    except:
        print("FAILED")
        assert False

print("-"*10)
test_str()


