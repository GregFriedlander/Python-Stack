my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tuplesout(dic):
    newarr = []
    for key,value in my_dict.iteritems():
        newarr.append((key,value))
    print newarr

tuplesout(my_dict)
