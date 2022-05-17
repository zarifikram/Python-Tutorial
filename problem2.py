input_user = input("Give me an expression and I will calculate the answer :    ")

# "100-14"

sign_place = -1
sign_place = input_user.find("+") if input_user.find("+") > sign_place else sign_place
sign_place = input_user.find("-") if input_user.find("-") > sign_place else sign_place
sign_place = input_user.find("/") if input_user.find("/") > sign_place else sign_place
sign_place = input_user.find("*") if input_user.find("*") > sign_place else sign_place

if sign_place == -1:
    print('INVALID EXPRESSION!')
else:
    a = float(input_user[:sign_place])
    b = float(input_user[sign_place + 1 : ])
    operator = input_user[sign_place]
    r = {
        "+" : a + b,
        "-" : a - b,
        "*" : a * b,
        "/" : a / b
    }
    print(r[operator])