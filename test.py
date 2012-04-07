#coding=utf-8

def test():
    print "test is running"

if __name__ == "__main__":  #自运行时调用该段程序
    print "test main is working"

if __name__ == "test":      #import时调用该段程序
    print "test is invoked"
