i = 1
def test():
        global i
        while i < 999999999:
                try:	
                        print(str(i))
                except KeyboardInterrupt:
                        test()
                i += 1