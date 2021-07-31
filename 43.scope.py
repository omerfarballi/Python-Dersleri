#global scope
x = 'globol x'
def func():
    #local scope
    global x
    x = 'local x'
    # print(x)
    def func2():
        
        x = 'local local x'
        # print(x)
    # print(x)
    func2()
func()
print(x)

# print(x)
#############################################