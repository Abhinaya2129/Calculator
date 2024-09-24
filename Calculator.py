print("_______________________________________________________")
print("------------------C A L C U L A T O R------------------")
print("_______________________________________________________")
print("Enter your Operation : ")
number_1 = int(input("number_1 = "))
operator = input("Operator : ")
number_2 = int(input("number_2 = "))
Addition = lambda number_1,number2:number_1 + number_2
Substraction = lambda number_1,number2:number_1 - number_2
Multiplication = lambda number_1,number2:number_1 * number_2
Division = lambda number_1,number2:number_1 % number_2
Modulo_Division = lambda number_1,number2:number_1 / number_2
Floor_Division = lambda number_1,number2:number_1 // number_2
match (operator):
    case "+":
        print(number_1,"+",number_2, "=",Addition(number_1,number_2))
    case "-":
        print(number_1,"-",number_2, "=",Substraction(number_1,number_2))
    case "*":
        print(number_1,"*",number_2, "=",Multiplication(number_1,number_2))
    case "%":
        print(number_1,"%",number_2, "=",Division(number_1,number_2))
    case "/":
        print(number_1,"/",number_2, "=",Modulo_Division(number_1,number_2))
    case "//":
        print(number_1,"//",number_2, "=",Floor_Division(number_1,number_2))

