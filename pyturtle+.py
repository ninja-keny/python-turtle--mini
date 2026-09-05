import turtle

# Function value dictionaries
f_forward = {}
f_backward = {}
f_right = {}
f_left = {}
f_color = {}
f_pensize = {}
f_gox_dict = {}
f_goy_dict = {}

# Loop value dictionaries
l_forward = {}
l_backward = {}
l_right = {}
l_left = {}
l_color = {}
l_pensize = {}
l_gox_dict = {}
l_goy_dict = {}

loop_list = {}
loop = []
loop_index = 0

valid_commands = [
    "forward","backward","right","left",
    "penup","pendown","color","pensize","goto",
    "start_loop","end_loop","start_function","end_function"
]

# global counters
loop_n = loop_o = loop_q = loop_k = loop_l = loop_ps = loop_xs = loop_ys = 0
a = 1
n = 0
o = 0
q = 0
k = 0
l = 0
ps = 0
xs = 0
ys = 0

line_name = 1
print("welcome to pyturtle+ type run to run your code")

functions_name = []
functions = {}  
code = []
f_info = []

forward_distance = []
backward_distance = []
right_turns = []
left_turns = []
color_list = ["blue","green","black","orange","yellow","white","purple","red","pink"]
color_chosen = []
pensizes = []
gox = []
goy = []

looping = []
ls = 0

value = 0
list_add = []
add_off = True

run = True
loop_on = False
function_on = False
function_name = ""

# INPUT LOOP
while run:
    line = input("line "+str(line_name)+":")
    line_name += 1

    if line == "run":
        run = False

    elif line == "forward":
        try:
            forward_num = int(input("how much steps do you want the turtle to move"))
            if loop_on:
                loop.append("forward")
                l_forward[str(loop_index)].append(forward_num)
            elif function_on:
                f_info.append("forward")
                f_forward[function_name].append(forward_num)
            else:
                forward_distance.append(forward_num)
                code.append("forward")
        except:
            print("syntax error make sure you typed a number")

    elif line == "backward":
        try:
            backward_num = int(input("how much steps do you want the turtle to move backward"))
            if loop_on:
                loop.append("backward")
                l_backward[str(loop_index)].append(backward_num)
            elif function_on:
                f_info.append("backward")
                f_backward[function_name].append(backward_num)
            else:
                backward_distance.append(backward_num)
                code.append("backward")
        except:
            print("syntax error make sure you typed a number")

    elif line == "right":
        try:
            right_num = int(input("how much degrees do you want the turtle to turn right"))
            if loop_on:
                loop.append("right")
                l_right[str(loop_index)].append(right_num)
            elif function_on:
                f_info.append("right")
                f_right[function_name].append(right_num)
            else:
                right_turns.append(right_num)
                code.append("right")
        except:
            print("syntax error make sure you typed a number")

    elif line == "left":
        try:
            left_num = int(input("how much steps do you want the turtle to turn left"))
            if loop_on:
                loop.append("left")
                l_left[str(loop_index)].append(left_num)
            elif function_on:
                f_info.append("left")
                f_left[function_name].append(left_num)
            else:
                left_turns.append(left_num)
                code.append("left")
        except:
            print("syntax error make sure you typed a number")

    elif line == "penup":
        if loop_on:
            loop.append("penup")
        elif function_on:
            f_info.append("penup")
        else:
            code.append("penup")

    elif line == "pendown":
        if loop_on:
            loop.append("pendown")
        elif function_on:
            f_info.append("pendown")
        else:
            code.append("pendown")

    elif line == "color":
        turtle_color = input("what color do you want the turtle to be")
        if turtle_color in color_list:
            if loop_on:
                loop.append("color")
                l_color[str(loop_index)].append(turtle_color)
            elif function_on:
                f_info.append("color")
                f_color[function_name].append(turtle_color)
            else:
                color_chosen.append(turtle_color)
                code.append("color")
        else:
            print("syntax error: make sure you type a color")

    elif line == "pensize":
        try:
            size = int(input("what pen size do you want"))
            if loop_on:
                loop.append("pensize")
                l_pensize[str(loop_index)].append(size)
            elif function_on:
                f_info.append("pensize")
                f_pensize[function_name].append(size)
            else:
                pensizes.append(size)
                code.append("pensize")
        except:
            print("syntax error make sure you typed a number")

    elif line == "goto":
        try:
            x_axis = int(input("where do you want the turtle x axis to be"))
            y_axis = int(input("where do you want the turtle y axis to be"))
            if loop_on:
                loop.append("goto")
                l_gox_dict[str(loop_index)].append(x_axis)
                l_goy_dict[str(loop_index)].append(y_axis)
            elif function_on:
                f_info.append("goto")
                f_gox_dict[function_name].append(x_axis)
                f_goy_dict[function_name].append(y_axis)
            else:
                gox.append(x_axis)
                goy.append(y_axis)
                code.append("goto")
        except:
            print("syntax error make sure you typed a number")

    elif line == "start_loop":
        loops = int(input("how much loops do you want"))
        looping.append(loops)
        code.append("start_loop")
        loop_on = True
        loop_index += 1
        loop = []

        l_forward[str(loop_index)] = []
        l_backward[str(loop_index)] = []
        l_right[str(loop_index)] = []
        l_left[str(loop_index)] = []
        l_color[str(loop_index)] = []
        l_pensize[str(loop_index)] = []
        l_gox_dict[str(loop_index)] = []
        l_goy_dict[str(loop_index)] = []

    elif line == "end_loop":
        if loop_on:
            loop_list[str(loop_index)] = loop
            code.append("end_loop")
            loop_on = False
        else:
            print("make sure you have a start loop command at the top")

    elif line == "start_function":
        function_name = input("what do you want your function to be called")
        functions_name.append(function_name)
        function_on = True
        f_info = []

        functions[function_name] = []
        f_forward[function_name] = []
        f_backward[function_name] = []
        f_right[function_name] = []
        f_left[function_name] = []
        f_color[function_name] = []
        f_pensize[function_name] = []
        f_gox_dict[function_name] = []
        f_goy_dict[function_name] = []

        code.append(function_name)

    elif line == "end_function":
        if function_on:
            functions[function_name] = f_info 
            function_on = False
        else:
            print("make sure you have a start function command at the top")

    elif line == "addition":
      add_inputs = input("type the numbers you want to add and to seperate them use spaces ")
      list_add = add_inputs.split()
      for i in range(0,len(list_add)):
        list_add[i] = int(list_add[i])
        value = list_add[i] + value
      print("the value is: " + str(value))

    elif line == "subtraction":
      subtract_inputs = input("type the numbers you want to subtract and to seperate them use spaces ")
      list_subtract = subtract_inputs.split()
      value = int(list_subtract[0])
      for i in range(1 , len(list_subtract)):
        list_subtract[i] = int(list_subtract[i])
        value = value - list_subtract[i]
      print("the value is: " + str(value))

    elif line == "multiplication":
        multiply_inputs = input("type the numbers you want to multiply a0nd to seperate them use spaces ")
        list_multiply = multiply_inputs.split()
        value = int(list_multiply[0])
        for i in range(1 , len(list_multiply)):
            list_multiply[i] = int(list_multiply[i])
            value = value * list_multiply[i]
        print("the value is: " + str(value))

    elif line == "division":
        divide_inputs = input("type the numbers you want to divide and to seperate them use spaces ")
        list_divide = divide_inputs.split()
        value = int(list_divide[0])
        for i in range(1 , len(list_divide)):
            list_divide[i] = int(list_divide[i])
            value = value / list_divide[i]
        print("the value is: " + str(value))

    else:
        print("\033[31myour code will not run since it is not a proper command\033[0m")

# EXECUTION
i = 0
while i < len(code):

    if code[i] == "forward":
        turtle.forward(forward_distance[n])
        n += 1

    elif code[i] == "backward":
        turtle.backward(backward_distance[o])
        o += 1

    elif code[i] == "right":
        turtle.right(right_turns[q])
        q += 1

    elif code[i] == "left":
        turtle.left(left_turns[k])
        k += 1

    elif code[i] == "color":
        turtle.color(color_chosen[l])
        l += 1

    elif code[i] == "penup":
        turtle.penup()

    elif code[i] == "pendown":
        turtle.pendown()

    elif code[i] == "pensize":
        turtle.pensize(pensizes[ps])
        ps += 1

    elif code[i] == "goto":
        turtle.goto(gox[xs], goy[ys])
        xs += 1
        ys += 1

    elif code[i] == "start_loop":
        loop_n = loop_o = loop_q = loop_k = loop_l = loop_ps = loop_xs = loop_ys = 0

    elif code[i] == "end_loop":

        for _ in range(looping[ls]):
            for j in range(len(loop_list[str(a)])):


                if loop_list[str(a)][j] == "forward":
                  try:
                    turtle.forward(l_forward[str(a)][loop_n])
                    loop_n += 1
                  except:
                    turtle.forward(l_forward[str(a)][loop_n-1])

                elif loop_list[str(a)][j] == "backward":
                  try:
                    turtle.backward(l_backward[str(a)][loop_o])
                    loop_o += 1
                  except:
                    turtle.backward(l_backward[str(a)][loop_o-1])

                elif loop_list[str(a)][j] == "right":
                   try:
                    turtle.right(l_right[str(a)][loop_q])
                    loop_q += 1
                   except:
                     turtle.right(l_right[str(a)][loop_q-1])

                elif loop_list[str(a)][j] == "left":
                   try:
                    turtle.left(l_left[str(a)][loop_k])
                    loop_k += 1
                   except:
                     turtle.left(l_left[str(a)][loop_k-1])

                elif loop_list[str(a)][j] == "color":
                    turtle.color(l_color[str(a)][loop_l-1])
                    loop_l += 1

                elif loop_list[str(a)][j] == "penup":
                    turtle.penup()

                elif loop_list[str(a)][j] == "pendown":
                    turtle.pendown()

                elif loop_list[str(a)][j] == "pensize":
                   try:
                    turtle.pensize(l_pensize[str(a)][loop_ps])
                    loop_ps += 1
                   except:
                     turtle.pensize(l_pensize[str(a)][loop_ps-1])

                elif loop_list[str(a)][j] == "goto":
                  try:
                    turtle.goto(
                        l_gox_dict[str(a)][loop_xs],
                        l_goy_dict[str(a)][loop_ys]
                    )
                    loop_xs += 1
                    loop_ys += 1
                  except:
                    turtle.goto(
                        l_gox_dict[str(a)][loop_xs-1],
                        l_goy_dict[str(a)][loop_ys-1]
                    )

        a += 1
        ls += 1

    elif code[i] in functions:

        fname = code[i]

        fn = fo = fq = fk = fl = fps = fxs = fys = 0

        for d in range(len(functions[fname])):

            if functions[fname][d] == "forward":
                turtle.forward(f_forward[fname][fn])
                fn += 1

            elif functions[fname][d] == "backward":
                turtle.backward(f_backward[fname][fo])
                fo += 1

            elif functions[fname][d] == "right":
                turtle.right(f_right[fname][fq])
                fq += 1

            elif functions[fname][d] == "left":
                turtle.left(f_left[fname][fk])
                fk += 1

            elif functions[fname][d] == "color":
                turtle.color(f_color[fname][fl])
                fl += 1

            elif functions[fname][d] == "penup":
                turtle.penup()

            elif functions[fname][d] == "pendown":
                turtle.pendown()

            elif functions[fname][d] == "pensize":
                turtle.pensize(f_pensize[fname][fps])
                fps += 1

            elif functions[fname][d] == "goto":
                turtle.goto(f_gox_dict[fname][fxs], f_goy_dict[fname][fys])
                fxs += 1
                fys += 1

    i += 1

turtle.done()
