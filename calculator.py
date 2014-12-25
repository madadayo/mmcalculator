import tkinter

__author__ = {'name' : 'menma','Email' : '65519346@qq.com','Created' : '2014-12-24'}

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('最爱面码')
        self.main_window.geometry('670x600')
        self.main_window.iconbitmap('d:\\GitHub\\python\\menma.ico')

        self.num_btn_color = tkinter.StringVar()
        self.num_btn_color.set('blue')
        self.op_btn_color = tkinter.StringVar()
        self.op_btn_color.set('red')

        # 容器
        self.frame_input = tkinter.Frame(self.main_window)
        self.frame0 = tkinter.Frame(self.main_window)
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)

        # 初始化
        self.input_val = tkinter.StringVar()
        self.resetInput()
        self.entry = tkinter.Entry(self.frame_input,width=65,textvariable=self.input_val,justify=tkinter.RIGHT,takefocus=0,state='disabled',cursor='arrow').pack()
        self.calculate_result = tkinter.DoubleVar()
        self.calculate_action = tkinter.StringVar()
        self.input_toggle = tkinter.IntVar()
        self.resetToggle()
        
        # 按钮
        self.btn_reset = tkinter.Button(self.frame0,text='C',width=15,height=2,command=self.reset).pack(side='right')
        
        self.button1 = tkinter.Button(self.frame1,text='1',width=15,height=5,fg=self.num_btn_color.get(),command=lambda:self.typein('1')).pack(side='left')
        self.button2 = tkinter.Button(self.frame1,text='2',width=15,height=5,fg=self.num_btn_color.get(),command=lambda:self.typein('2')).pack(side='left')
        self.button3 = tkinter.Button(self.frame1,text='3',width=15,height=5,fg=self.num_btn_color.get(),command=lambda:self.typein('3')).pack(side='left')
        self.b_cheng = tkinter.Button(self.frame1,text='*',width=15,height=5,fg=self.op_btn_color.get(),command=self.multiplic).pack(side='left')
        
        self.button4 = tkinter.Button(self.frame2,text='4',width=15,height=5,fg=self.num_btn_color.get(),command=lambda:self.typein('4')).pack(side='left')
        self.button5 = tkinter.Button(self.frame2,text='5',width=15,height=5,fg=self.num_btn_color.get(),command=lambda:self.typein('5')).pack(side='left')
        self.button6 = tkinter.Button(self.frame2,text='6',width=15,height=5,fg=self.num_btn_color.get(),command=lambda:self.typein('6')).pack(side='left')
        self.b_chu = tkinter.Button(self.frame2,text='/',width=15,height=5,fg=self.op_btn_color.get(),command=self.divide).pack(side='left')
        
        self.button7 = tkinter.Button(self.frame3,text='7',width=15,height=5,fg=self.num_btn_color.get(),command=lambda:self.typein('7')).pack(side='left')
        self.button8 = tkinter.Button(self.frame3,text='8',width=15,height=5,fg=self.num_btn_color.get(),command=lambda:self.typein('8')).pack(side='left')
        self.button9 = tkinter.Button(self.frame3,text='9',width=15,height=5,fg=self.num_btn_color.get(),command=lambda:self.typein('9')).pack(side='left')
        self.b_jian = tkinter.Button(self.frame3,text='-',width=15,height=5,fg=self.op_btn_color.get(),command=self.minus).pack(side='left')
        
        self.button0 = tkinter.Button(self.frame4,text='0',width=15,height=5,fg=self.num_btn_color.get(),command=lambda:self.typein('0')).pack(side='left')
        self.b_dian = tkinter.Button(self.frame4,text='.',width=15,height=5,fg=self.num_btn_color.get(),command=lambda:self.typein('.')).pack(side='left')
        self.b_deng = tkinter.Button(self.frame4,text='=',width=15,height=5,fg=self.op_btn_color.get(),command=self.calculate).pack(side='left')
        self.b_jia = tkinter.Button(self.frame4,text='+',width=15,height=5,fg=self.op_btn_color.get(),command=self.add).pack(side='left')

        self.frame_input.pack(side='top')
        self.frame0.pack(side='top')
        self.frame1.pack(side='top')
        self.frame2.pack(side='top')
        self.frame3.pack(side='top')
        self.frame4.pack(side='top')
        
        self.main_window.mainloop()

    def typein(self,num):
        inputstr = self.input_val.get()
        toggle = self.input_toggle.get()

        if toggle == 1:
            self.input_toggle.set(0)
            if num == '.':
                inputstr = '0.'
            else:
                inputstr = num
        elif inputstr == '0':
            inputstr == num
        else:
            inputstr += num

        self.input_val.set(inputstr)

    def add(self):
        self.calculate()
        self.calculate_action.set('+')

    def minus(self):
        self.calculate()
        self.calculate_action.set('-')

    def multiplic(self):
        self.calculate()
        self.calculate_action.set('*')

    def divide(self):
        self.calculate()
        self.calculate_action.set('/')

    def calculate(self):
        intresult = self.calculate_result.get()
        intinput = float(self.input_val.get())
        action = self.calculate_action.get()

        if action == '+':
            result = intresult + intinput       
        elif action == '-':
            result = intresult - intinput
        elif action == '*':
            result = intresult * intinput
        elif action == '/':
            if intinput == float('0'):
                tkinter.messagebox.showinfo('警告','除数不能为0！')
                self.reset()
                return
            result = intresult / intinput
        else:
            result = intinput

        self.input_val.set(str(result).rstrip('0').rstrip('.'))
        self.calculate_result.set(result)
        self.resetAction()
        self.resetToggle()

    def resetInput(self):
        self.input_val.set('0')
    def resetResult(self):
        self.calculate_result.set(float(0))
    def resetAction(self):
        self.calculate_action.set('')
    def resetToggle(self):
        self.input_toggle.set(1)
    def reset(self):
        self.resetInput()
        self.resetResult()
        self.resetAction()
        self.resetToggle()
        
    # 测试点击按钮传参数
    def test(self,num):
        def wrapper(n=num):
            pass
            tkinter.messagebox.showinfo('Input','You input is:' + n)
        return wrapper

print(__name__)

mygui = MyGUI()
