from tkinter import*
import random
import time


root = Tk()
root.geometry("1600x800+0+0")
root.title("Simple Restaurant Systems")

text_Input = StringVar()
operator=""

Tops = Frame(root, width =1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800,height= 700, relief= SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300,height= 700, relief=SUNKEN)
f2.pack(side=RIGHT)
#===========================Time==================
localtime=time.asctime(time.localtime(time.time()))
#=====================info=====================
lblInfo = Label(Tops, font = ('arial',50, 'bold'),text="Simple Restaurant System", fg="Black",bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font = ('arial',20, 'bold'),text=localtime, fg="Black",bd=10, anchor='w')
lblInfo.grid(row=1,column=0)

#==================Calculator=================
def btnClick(numbers) :
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup =str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Ref():
    x =random.randint(12908,509876)
    randomRef = str(x)
    rand.set(randomRef)


    blamb = float(lambchop.get())
    bcchop =float(chickenchop.get())
    bcgrill =float(chickengrill.get())
    bmeat =float(meatball.get())
    bspag =float(spaghetti.get())
    bsky =float(skyjuice.get())

    priceoflamb = blamb*17.00
    priceofcchop = bcchop*10.00
    priceofbcgrill = bcgrill*13.00
    priceofbmeat = bmeat*8.00
    priceofbspag = bspag*9.00
    priceofbsky = bsky*5.00

    Priceofmeal = "RM",str('%.2f' % (priceoflamb + priceofcchop + priceofbcgrill + priceofbmeat
                                     + priceofbspag + priceofbsky))
    Subtotal = (priceoflamb + priceofcchop + priceofbcgrill + priceofbmeat
                                     + priceofbspag + priceofbsky)
    payGST = ((priceoflamb + priceofcchop + priceofbcgrill + priceofbmeat
                                     + priceofbspag + priceofbsky)*0.06)
    payService = ((priceoflamb + priceofcchop + priceofbcgrill + priceofbmeat
                                     + priceofbspag + priceofbsky)/99)
    Service = "RM", str('%.2f' % payService)
    fulltotal = "RM", str('%.2f' % (payService + payGST + Subtotal))
    paygst ="RM", str ('%.2f' % payGST)

    service.set(Service)
    price.set(Priceofmeal)
    gst.set(paygst)
    subtotal.set(Priceofmeal)
    total.set(fulltotal)
                      

def qExit():
    root.destroy()

def Reset():
    rand.set(randomRef)
    lambchop.set("")
    chickenchop.set("")
    chickengrill.set("")
    meatball.set("")
    spaghetti.set("")
    skyjuice.set("")
    price.set("")
    #service.set("")
    #gst.set("")
    #subtotal.set("")
    #total.set("")
    
txtDisplay = Entry(f2,font=('arial',20,'bold'), textvariable= text_Input,bd=30, insertwidth=4,
                   bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="7", bg="powder blue", command =lambda: btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="8", bg="powder blue", command =lambda: btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="9", bg="powder blue", command =lambda: btnClick(9)).grid(row=2,column=2)
Additional=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="+", bg="powder blue", command =lambda: btnClick("+")).grid(row=2,column=3)
#---------------------------------------------------------------------------------------------

btn4=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="4", bg="powder blue", command =lambda: btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="5", bg="powder blue", command =lambda: btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="6", bg="powder blue", command =lambda: btnClick(6)).grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="-", bg="powder blue", command =lambda: btnClick("-")).grid(row=3,column=3)
#--------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="1", bg="powder blue", command =lambda: btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="2", bg="powder blue", command =lambda: btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="3", bg="powder blue", command =lambda: btnClick(3)).grid(row=4,column=2)
Multiply=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="*", bg="powder blue", command =lambda: btnClick("*")).grid(row=4,column=3)
#--------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="0", bg="powder blue", command =lambda: btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="C", bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="=", bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,bd=8, fg ="black", font =('arial',20,'bold'),
            text="/", bg="powder blue", command =lambda: btnClick("/")).grid(row=5,column=3)
#----------------------------------------------Restaurant Menu-----------------------------------------------
rand =StringVar()
lambchop = StringVar()
chickenchop = StringVar()
chickengrill = StringVar()
meatball = StringVar()
spaghetti = StringVar()
skyjuice =StringVar()
price= StringVar()
service = StringVar()
gst = StringVar()
subtotal = StringVar()
total = StringVar()

lblReference = Label (f1,font=('arial', 16,'bold'), text="Reference", bd=16, anchor ='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
txtReference.grid(row=0,column=1)

lbllambchop = Label (f1,font=('arial', 16,'bold'), text="Lamb Chop", bd=16, anchor ='w')
lbllambchop.grid(row=1,column=0)
txtlambchop=Entry(f1,font=('arial', 16, 'bold'), textvariable=lambchop, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
txtlambchop.grid(row=1,column=1)

lblchickenchop = Label (f1,font=('arial', 16,'bold'), text="Chicken Chop", bd=16, anchor ='w')
lblchickenchop.grid(row=2,column=0)
txtchickenchop=Entry(f1,font=('arial', 16, 'bold'), textvariable=chickenchop, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
txtchickenchop.grid(row=2,column=1)

lblchickengrill = Label (f1,font=('arial', 16,'bold'), text="Chicken Grill", bd=16, anchor ='w')
lblchickengrill.grid(row=3,column=0)
txtchickengrill=Entry(f1,font=('arial', 16, 'bold'), textvariable=chickengrill, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
txtchickengrill.grid(row=3,column=1)

lblmeatball = Label (f1,font=('arial', 16,'bold'), text="Meatball", bd=16, anchor ='w')
lblmeatball.grid(row=4,column=0)
txtmeatball=Entry(f1,font=('arial', 16, 'bold'), textvariable=meatball, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
txtmeatball.grid(row=4,column=1)

lblspaghetti = Label (f1,font=('arial', 16,'bold'), text="Spaghetti", bd=16, anchor ='w')
lblspaghetti.grid(row=5,column=0)
txtspaghetti=Entry(f1,font=('arial', 16, 'bold'), textvariable=spaghetti, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
txtspaghetti.grid(row=5,column=1)

#--------------------------------------Restaurant Menu-------------------------

lblskyjuice = Label (f1,font=('arial', 16,'bold'), text="Sky Juice", bd=16, anchor ='w')
lblskyjuice.grid(row=0,column=2)
txtskyjuice=Entry(f1,font=('arial', 16, 'bold'), textvariable=skyjuice, bd=10, insertwidth=4,
                    bg="#ffffff", justify = 'right')
txtskyjuice.grid(row=0,column=3)

lblprice = Label (f1,font=('arial', 16,'bold'), text="Price", bd=16, anchor ='w')
lblprice.grid(row=1,column=2)
txtprice=Entry(f1,font=('arial', 16, 'bold'), textvariable=price, bd=10, insertwidth=4,
                    bg="#ffffff", justify = 'right')
txtprice.grid(row=1,column=3)

lblservice = Label (f1,font=('arial', 16,'bold'), text="Service", bd=16, anchor ='w')
lblservice.grid(row=2,column=2)
txtservice=Entry(f1,font=('arial', 16, 'bold'), textvariable=service, bd=10, insertwidth=4,
                    bg="#ffffff", justify = 'right')
txtservice.grid(row=2,column=3)

lblgst = Label (f1,font=('arial', 16,'bold'), text="GST", bd=16, anchor ='w')
lblgst.grid(row=3,column=2)
txtgst=Entry(f1,font=('arial', 16, 'bold'), textvariable=gst, bd=10, insertwidth=4,
                    bg="#ffffff", justify = 'right')
txtgst.grid(row=3,column=3)

lblsubtotal = Label (f1,font=('arial', 16,'bold'), text="Sub Total", bd=16, anchor ='w')
lblsubtotal.grid(row=4,column=2)
txtsubtotal=Entry(f1,font=('arial', 16, 'bold'), textvariable=subtotal, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
txtsubtotal.grid(row=4,column=3)

lbltotal = Label (f1,font=('arial', 16,'bold'), text="Total Price", bd=16, anchor ='w')
lbltotal.grid(row=5,column=2)
#txttotal=Entry(f1,font=('arial', 16, 'bold'), textvariable=total, bd=10, insertwidth=4,
                    #bg="powder blue", justify = 'right')
txttotal.grid(row=5,column=3)

#---------------------------------Buttons--------------------------------------------

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)
root.mainloop()
