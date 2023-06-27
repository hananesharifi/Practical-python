import time
def queue_bakery():
    single_queue = list()
    multi_queue = list()
    
    while True:
        x = input('please enter (Exit(E) / service (S) / code) and how many do you want :')
        x = x.strip()
        z = input('how many you want')
        z = z.strip()
        z1 = eval(z)
        if x.lower() == 'exit' or x.lower() == 'e':
            print(single_queue)
            print(multi_queue)
            break
        elif x.lower() == 'service' or x.lower() == 's':
                if len(single_queue) > 0:
                    y1 = single_queue.pop()
                    print(y1  , 'is serving.....')
                    time.sleep(5)
                else:
                    print('queue is ewmpty')
                    continue
                if len(multi_queue) > 0:
                    z1 -= 1
                    if eval(z) == 1:
                        y2 = multi_queue.pop()
                        print(y1  , 'is serving.....')
                        time.sleep(5)
                else:
                    print('queue is ewmpty')
                    continue
        if x in single_queue or x in multi_queue:
             print(x + 'inserted')
        else:
            if z1 == 1:
                single_queue.insert(0 , x)
            elif z1 > 1:
                multi_queue.insert(0 , x)
            else:
                continue
    return single_queue , multi_queue
queue_bakery()