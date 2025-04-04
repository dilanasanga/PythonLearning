class ReverseClass(object):
    def reverse(self,x):
#        str = x[::-1]
#        print(str)
        char_list = []
        number_list = []
        for chars in x:
            char_list.append(chars)
        i = 0
        negative = False
        while i < len(char_list):
            if char_list[i].isnumeric():
                number_list.append(char_list[i])
                if i > 0:
                    if char_list[i-1] =="-":
                        negative = True
                if i <= len(char_list):
                    if char_list[i] == " " or char_list[i].isnumeric()==False:
                        number_over = True
                        break
            else:
                print(number_list)
            i +=1
        print(number_list)

        result = ''.join(number_list)
        print(type(number_list))
        print(type(result))
        int_number = int(result)
        if negative == True:
            int_number = int_number*-1
        print(int_number)

        
new_ReverseClass = ReverseClass()
new_ReverseClass.reverse(" -A-004309 -c9 ")
#new_ReverseClass.reverse("42")
