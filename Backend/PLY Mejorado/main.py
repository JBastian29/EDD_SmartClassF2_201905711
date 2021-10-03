
from analyzers.Syntactic import parser
from analyzers.Syntactic import user_list, task_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open('Estudiantes.txt',"r", encoding="utf-8")
    mensaje = f.read()
    # print(mensaje)
    f.close()
    # parser.parse('¿ Elements ? ¿Element type = "task"?  ¿item Carnet = "201901425" $? ¿$Element? ¿ $Elements ?')
    parser.parse(mensaje)

    user_list.getList()
    print("------------------------")
    task_list.getList()

