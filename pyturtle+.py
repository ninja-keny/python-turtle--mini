import turtle

# varibles values
varible_value = {}

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
            forward_num = input("how much steps do you want the turtle to move ")
            try:
             forward_num = int(forward_num)
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
               try:
                  forward_num = float(forward_num)
               except:
                if forward_num in varible_value:
                  forward_num = varible_value[forward_num]
                  if loop_on:
                   loop.append("forward")
                   l_forward[str(loop_index)].append(forward_num)
                  elif function_on:
                   f_info.append("forward")
                   f_forward[function_name].append(forward_num)
                  else:
                   forward_distance.append(forward_num)
                   code.append("forward")
                else:                
                 print("syntax error make sure you typed a number or varible")

    elif line == "backward":
     backward_num = input("how much steps do you want the turtle to move ")
     try:
        backward_num = int(backward_num)
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
        try:
            backward_num = float(backward_num)
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
            if backward_num in varible_value:
                backward_num = varible_value[backward_num]
                if loop_on:
                    loop.append("backward")
                    l_backward[str(loop_index)].append(backward_num)
                elif function_on:
                    f_info.append("backward")
                    f_backward[function_name].append(backward_num)
                else:
                    backward_distance.append(backward_num)
                    code.append("backward")
            else:
                print("syntax error make sure you typed a number or varible")

    elif line == "right":
     right_num = input("how much degrees do you want the turtle to turn right ")
     try:
        right_num = int(right_num)
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
         try:
            right_num = float(right_num)
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
            if right_num in varible_value:
                right_num = varible_value[right_num]
                if loop_on:
                    loop.append("right")
                    l_right[str(loop_index)].append(right_num)
                elif function_on:
                    f_info.append("right")
                    f_right[function_name].append(right_num)
                else:
                    right_turns.append(right_num)
                    code.append("right")
            else:
                print("syntax error make sure you typed a number or varible")
    
    elif line == "left":
     left_num = input("how much degrees do you want the turtle to turn left ")
     try:
        left_num = int(left_num)
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
        try:
            left_num = float(left_num)
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
            if left_num in varible_value:
                left_num = varible_value[left_num]
                if loop_on:
                    loop.append("left")
                    l_left[str(loop_index)].append(left_num)
                elif function_on:
                    f_info.append("left")
                    f_left[function_name].append(left_num)
                else:
                    left_turns.append(left_num)
                    code.append("left")
            else:
                print("syntax error make sure you typed a number or varible")


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

    elif line in functions_name:
     code.append(line)

    elif line == "addition":
      add_inputs = input("type the numbers you want to add and to seperate them use spaces ")
      list_add = add_inputs.split()
      value = 0
      for x in range (len(list_add)):
       try:
          list_add[x] = int(list_add[x])
       except:
        try:
          list_add[x] = float(list_add[x])
        except: 
           if list_add[x] in varible_value:
              list_add[x] = varible_value[list_add[x]]
           else:
              pass
              
      for i in range (len(list_add)):
       try:
         value = list_add[i] + value
         if i == len(list_add)-1:
          print("the value is " + str(value))
       except:
        print(str(list_add[i]) + " is not a number or varible or decimal or the varibal is a string")
      

    elif line == "subtraction":
      subtract_inputs = input("type the numbers you want to subtract and to seperate them use spaces ")
      list_subtract = subtract_inputs.split()
      for x in range(0, len(list_subtract)):
             try:
              list_subtract[x] = int(list_subtract[x])
             except:
              try:
               list_subtract[x] = float(list_subtract[x])
              except:
               if list_subtract[x] in varible_value:
                list_subtract[x] = varible_value[list_subtract[x]]
               else:
                print(str(list_subtract[0]) + " is not a varible or a number or a decimall or varibal is a string")
      value = list_subtract[0]
      for a in range(1 , len(list_subtract)):
       try:
        value = value - list_subtract[a]
        if a == len(list_subtract)-1:
         print("the value is: " + str(value))
       except:
         print(str(list_subtract[a]) + " is not a varible or a number or a decimall or varibal is a string")

    elif line == "multiplication":
     multiply_inputs = input("type the numbers you want to multiply and to seperate them use spaces ")
     list_multiply = multiply_inputs.split()

     # convert each item safely
     for x in range(len(list_multiply)):
        try:
            list_multiply[x] = int(list_multiply[x])
        except:
            try:
                list_multiply[x] = float(list_multiply[x])
            except:
                if list_multiply[x] in varible_value:
                    list_multiply[x] = varible_value[list_multiply[x]]
                else:
                    print(str(list_multiply[x]) + " is not a varible or a number or a decimall or varibal is a string")
                    break

     # start with the first value
     value = list_multiply[0]

     # multiply through the rest
     for i in range(1, len(list_multiply)):
        try:
            value = value * list_multiply[i]
            if i == len(list_multiply) - 1:
                print("the value is: " + str(value))
        except:
            print(str(list_multiply[i]) + " is not a varible or a number or a decimall or varibal is a string")


    elif line == "division":
     divide_inputs = input("type the numbers you want to divide and to seperate them use spaces ")
     list_divide = divide_inputs.split()

    # convert each item safely
     for x in range(len(list_divide)):
        try:
            list_divide[x] = int(list_divide[x])
        except:
            try:
                list_divide[x] = float(list_divide[x])
            except:
                if list_divide[x] in varible_value:
                    list_divide[x] = varible_value[list_divide[x]]
                else:
                    print(str(list_divide[x]) + " is not a varible or a number or a decimall or varibal is a string")
                    break

    # start with the first value
     value = list_divide[0]

    # divide through the rest
     for i in range(1, len(list_divide)):
        try:
            value = value / list_divide[i]
            if i == len(list_divide) - 1:
                print("the value is: " + str(value))
        except:
            print(str(list_divide[i]) + " is not a varible or a number or a decimall or varibal is a string")


    elif line == "varible":
     varible_name = input("what do you want your varible name to be ")
     varible_input = input("type the value of your varible ")
     try:
      varible_input = int(varible_input)
     except:
      try:
       varible_input = float(varible_input)
      except:
        varible_input = str(varible_input)
     varible_value[varible_name] = varible_input
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
