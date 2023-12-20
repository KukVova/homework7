def check(func):
    def inside():
        try:
            func()
        except ValueError:
            print('Enter number')
        except IndexError:
            print('Enter number')
        except ZeroDivisionError:
            print('You can"t divide by 0!')
        except TypeError:
            print('Enter number')

    inside()
@check
def calculate():
    a = int(input('Enter number:'))
    a2 = int(input('Enter second number: '))
    o = int(input('what you want to do? \n-  \n+ \n/ \n*'))
    if o == 1:
        print('Result:', a - a2)
    if o == 2:
        print('Result:', a + a2)
    if o == 3:
        print('Result:', a / a2)
    if o == 4:
        print('Result:', a * a2)
    return eval
