def infinite():
        i = 1
        while True:
                try:	
                        print(str(i))
                except KeyboardInterrupt:
                        infinite()
                i += 1
infinite()
