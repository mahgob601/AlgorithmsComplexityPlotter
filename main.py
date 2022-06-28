from tkinter import *
import tkinter.font as font
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

appBg = "#42f5a7"

# Background color of the buttons of my app
btnBg = "#f5b942"

# Foreground color (button text color) of the buttons of my app
btnFg = "white"

dropDownBg = "#42c8f5"


class App(Tk):
    unsortedArray = []
    noElements = 1010
    elementsNo = []

    counterM = 0
    counterH = 0
    timeCounter = 0
    counterQS = 0
    counterBubS = 0
    counterSS = 0
    counterCS = 0
    counterRS = 0

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Setup Frame
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (FirstPage, StartPage, GraphAlgorithms, CompareGraphs):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()





    def testFile(self, fileOpt, fileName):
        App.unsortedArray = []
        if fileOpt == "Generate Test file":
            App.noElements = 1010
            App.unsortedArray = list(np.random.randint(1, App.noElements+1, size=App.noElements))
            with open(f'{fileName}.txt', 'w+') as F:
                for i in range(App.noElements):
                    val = str(App.unsortedArray[i])
                    F.write(f'{val}\n')
            print(App.unsortedArray, f" Written {len(App.unsortedArray)}")
            print(f"After Writing Number of elements: {App.noElements}")

        elif fileOpt == "Upload a test file":
            with open(f'{fileName}.txt', 'r+') as myF:
                nums = myF.readlines()
                nums = ((''.join(nums)).strip()).split('\n')
                for j in nums:
                    App.unsortedArray.append(int(j))

                App.noElements = len(App.unsortedArray)


            print(App.unsortedArray, f" read {len(App.unsortedArray)}")
            print(f"After Reading Number of elements: {App.noElements}")
        App.elementsNo = [i for i in range(10,App.noElements+1, 50)]

        self.show_frame(StartPage)

    def doThat(self, sortType, compCheck):
        worstCaseLabel = "null"
        timeArr = []
        if sortType == "Insertion Sort":
            worstCaseLabel = "Worst Case Complexity: o (n ^ 2)"
            for i in range(10, App.noElements + 1, 50):
                myArr = App.unsortedArray[:i + 1:]
                App.timeCounter = 0
                self.insertionSort(myArr)
                timeArr.append(App.timeCounter)
            worstCaseArr = list(map(lambda x: x ** 2, App.elementsNo))



        elif sortType == "Merge Sort":
            worstCaseLabel = "Worst Case Complexity: o (n Log(n))"
            for i in range(10, App.noElements + 1, 50):
                App.counterM = 0
                myArr = App.unsortedArray[:i + 1:]
                self.mergeSort(myArr,0,len(myArr)-1)
                timeArr.append(App.counterM)
            worstCaseArr = list(map(lambda x: x * np.log2(x), App.elementsNo))
            #print("Actual time", timeArr)
            #print("Worst time", worstCaseArr)
            #self.plotGraph(App.elementsNo, timeArr, worstCaseArr, "Worst Case Complexity: o (n Log(n))", "Merge Sort")


        elif sortType == "Heap Sort":
            worstCaseLabel = "Worst Case Complexity: o (n Log(n))"
            for i in range(10, App.noElements + 1, 50):
                myArr = App.unsortedArray[:i + 1:]
                App.counterH = 0
                mytime = self.heapSort(myArr)
                timeArr.append(App.counterH)
            worstCaseArr = list(map(lambda x: x * np.log2(x), App.elementsNo))

        elif sortType == "Quick Sort":
            worstCaseLabel = "Worst Case Complexity: o (n ^ 2)"
            for i in range(10, App.noElements + 1, 50):
                myArr = App.unsortedArray[:i + 1:]
                App.counterQS = 0
                self.quickSort(myArr, 0, len(myArr) - 1)
                timeArr.append(App.counterQS)
            worstCaseArr = list(map(lambda x: x * x, App.elementsNo))

        elif sortType == "Bubble Sort":
            worstCaseLabel = "Worst Case Complexity: o (n ^ 2)"
            for i in range(10, App.noElements + 1, 50):
                myArr = App.unsortedArray[:i + 1:]
                App.counterBubS = 0
                self.bubbleSort(myArr)
                timeArr.append(App.counterBubS)
            worstCaseArr = list(map(lambda x: x * x, App.elementsNo))

        elif sortType == "Selection Sort":
            worstCaseLabel = "Worst Case Complexity: o (n ^ 2)"
            for i in range(10, App.noElements + 1, 50):
                myArr = App.unsortedArray[:i + 1:]
                App.counterSS = 0
                self.selectionSort(myArr, len(myArr))
                timeArr.append(App.counterSS)
            worstCaseArr = list(map(lambda x: x * x, App.elementsNo))


        elif sortType == "Counting Sort":
            worstCaseLabel = "Worst Case Complexity: o (n + k)"
            worstCaseArr = list()
            for i in range(10, App.noElements + 1, 50):
                myArr = App.unsortedArray[:i + 1:]
                k = max(myArr) - min(myArr)
                App.counterCS  = 0
                self.countingSort(myArr)
                timeArr.append(App.counterCS)
                worstCaseArr.append(len(myArr) + k)



        elif sortType == "Radix Sort":
            worstCaseLabel = "Worst Case Complexity: o ((n + b) * d)"
            worstCaseArr = list()
            b = 10
            for i in range(10, App.noElements + 1, 50):
                myArr = App.unsortedArray[:i + 1:]
                k = max(myArr) - min(myArr)
                d = np.log(k) / np.log(b)
                App.counterRS = 0
                self.radixSort(myArr)
                timeArr.append(App.counterRS)
                worstCaseArr.append((len(myArr) + 10) * d)


        if(compCheck == 0):
            return timeArr, worstCaseArr, worstCaseLabel

        return timeArr

    #############################################################################################################
    def insertionSort(self, myArr):
        App.timeCounter = 1
        for i in range(1, len(myArr)):
            App.timeCounter = App.timeCounter + 4
            key = myArr[i]
            j = i - 1
            while j >= 0 and key < myArr[j]:
                myArr[j + 1] = myArr[j]
                j -= 1
                App.timeCounter = App.timeCounter + 3
            myArr[j + 1] = key
            App.timeCounter = App.timeCounter + 1
        #return App.timeCounter

    #################################################################################################################

    def merge(self, a, p, q, r):
        App.counterM = App.counterM + 4
        n1 = q - p + 1
        n2 = r - q
        L = [0] * n1
        R = [0] * n2

        App.counterM = App.counterM + 1
        for i in range(0, n1):
            L[i] = a[p + i]
            App.counterM = App.counterM + 2

        App.counterM = App.counterM + 1
        for j in range(0, n2):
            R[j] = a[q + j + 1]
            App.counterM = App.counterM + 2

        App.counterM = App.counterM + 3
        i = 0
        j = 0
        k = p

        App.counterM = App.counterM + 1
        while i < n1 and j < n2:
            App.counterM = App.counterM + 1
            App.counterM = App.counterM + 1
            if L[i] <= R[j]:
                a[k] = L[i]
                i = i + 1
                App.counterM = App.counterM + 3
            else:
                a[k] = R[j]
                j = j + 1
                App.counterM = App.counterM + 2
            k = k + 1
            App.counterM = App.counterM + 1

        App.counterM = App.counterM + 1
        while i < n1:
            a[k] = L[i]
            i = i + 1
            k = k + 1
            App.counterM = App.counterM + 4

        App.counterM = App.counterM + 1
        while j < n2:
            a[k] = R[j]
            j = j + 1
            k = k + 1
            App.counterM = App.counterM + 4

    def mergeSort(self, a, p, r):
        App.counterM = App.counterM + 1
        if p < r:
            App.counterM = App.counterM + 1
            q = (p + r) // 2

            App.counterM = App.counterM + 1
            self.mergeSort(a, p, q)

            App.counterM = App.counterM + 1
            self.mergeSort(a, q + 1, r)

            App.counterM = App.counterM + 1
            self.merge(a, p, q, r)
            App.counterM = App.counterM + 1

    ##################################################################################################
    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2
        App.counterH = App.counterH + 3

        # See if left child of root exists and is
        # greater than root
        App.counterH = App.counterH + 1
        if l < n and arr[i] < arr[l]:
            largest = l
            App.counterH = App.counterH + 1

        # See if right child of root exists and is
        # greater than root
        App.counterH = App.counterH + 1
        if r < n and arr[largest] < arr[r]:
            largest = r
            App.counterH = App.counterH + 1

        # Change root, if needed
        App.counterH = App.counterH + 1
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            App.counterH = App.counterH + 2

            App.counterH = App.counterH + 1

            # Heapify the root.
            self.heapify(arr, n, largest)

    # The main function to sort an array of given size
    def heapSort(self, arr):
        n = len(arr)
        App.counterH = App.counterH + 1
        # Build a maxheap.
        # Since last parent will be at ((n//2)-1) we can start at that location.
        App.counterH = App.counterH + 1
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
            App.counterH = App.counterH + 2

        # One by one extract elements
        App.counterH = App.counterH + 1
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.heapify(arr, i, 0)
            App.counterH = App.counterH + 3
    ##################################################################################################################

    def partition(self, arr, low, high):
        App.counterQS = App.counterQS + 2
        i = (low - 1)
        pivot = arr[high]

        App.counterQS = App.counterQS + 1
        for j in range(low, high):
            App.counterQS = App.counterQS + 2
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                App.counterQS = App.counterQS + 2

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        App.counterQS = App.counterQS + 2
        App.counterQS = App.counterQS + 1
        return (i + 1)


    def quickSort(self, arr, low, high):
        App.counterQS = App.counterQS + 1
        if len(arr) == 1:
            App.counterQS = App.counterQS + 1
            return arr

        App.counterQS = App.counterQS + 1
        if low < high:
            App.counterQS = App.counterQS + 1
            pi = self.partition(arr, low, high)

            App.counterQS = App.counterQS + 2
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    ##################################################################################################################
    def bubbleSort(self, arr):
        App.counterBubS = App.counterBubS + 1
        n = len(arr)
        App.counterBubS = App.counterBubS + 1
        for i in range(n - 1):
            App.counterBubS = App.counterBubS + 1
            App.counterBubS = App.counterBubS + 1
            for j in range(0, n - i - 1):
                App.counterBubS = App.counterBubS + 1
                App.counterBubS = App.counterBubS + 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    App.counterBubS = App.counterBubS + 2


    ##################################################################################################################
    def selectionSort(self, arr, size):
        App.counterSS = App.counterSS + 1
        for step in range(size):
            App.counterSS = App.counterSS + 1
            min_idx = step
            App.counterSS = App.counterSS + 1
            App.counterSS = App.counterSS + 1
            for i in range(step + 1, size):
                App.counterSS = App.counterSS + 2
                if arr[i] < arr[min_idx]:
                    min_idx = i
                    App.counterSS = App.counterSS + 1

            (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])
            App.counterSS = App.counterSS + 1

    ##################################################################################################################
    def countingSort(self, array):

        App.counterCS = App.counterCS + 1
        size = len(array)

        App.counterCS = App.counterCS + 1
        output = [0] * size

        App.counterCS = App.counterCS + 1
        count = [0] * (max(array) + 1)

        App.counterCS = App.counterCS + 1
        for i in range(0, size):
            count[array[i]] += 1
            App.counterCS = App.counterCS + 2

        App.counterCS = App.counterCS + 1
        for i in range(1, (max(array) + 1)):
            count[i] += count[i - 1]
            App.counterCS = App.counterCS + 2

        i = size - 1
        App.counterCS = App.counterCS + 1

        App.counterCS = App.counterCS + 1
        while i >= 0:
            output[count[array[i]] - 1] = array[i]
            count[array[i]] -= 1
            i -= 1
            App.counterCS = App.counterCS + 4

        App.counterCS = App.counterCS + 1
        for i in range(0, size):
            array[i] = output[i]
            App.counterCS = App.counterCS + 2

    ##################################################################################################################
    def radixcountingSort(self, arr, exp1):
        App.counterRS = App.counterRS + 1
        n = len(arr)

        App.counterRS = App.counterRS + 2
        output = [0] * (n)

        count = [0] * (max(arr) + 1)

        App.counterRS = App.counterRS + 1
        for i in range(0, n):
            index = arr[i] // exp1
            count[index % 10] += 1
            App.counterRS = App.counterRS + 3

        App.counterRS = App.counterRS + 1
        for i in range(1, (max(arr) + 1)):
            count[i] += count[i - 1]
            App.counterRS = App.counterRS + 2

        App.counterRS = App.counterRS + 1
        i = n - 1
        App.counterRS = App.counterRS + 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
            App.counterRS = App.counterRS + 5

        App.counterRS = App.counterRS + 1
        i = 0
        App.counterRS = App.counterRS + 1
        for i in range(0, len(arr)):
            arr[i] = output[i]
            App.counterRS = App.counterRS + 2

    def radixSort(self,arr):

        App.counterRS = App.counterRS + 1
        max1 = max(arr)

        App.counterRS = App.counterRS + 1
        exp = 1

        App.counterRS = App.counterRS + 1
        while max1 / exp > 1:
            self.radixcountingSort(arr, exp)
            exp *= 10
            App.counterRS = App.counterRS + 3

    ##################################################################################################################

    def plotGraph(self, x, y1, y2, label1 ,label2, windowLabel):
        myroot = Tk()

        fig = Figure(figsize=(8, 5), dpi=85)

        # adding the subplot
        plot1 = fig.add_subplot(111, xlabel="No. elements", ylabel="Running time")

        # plotting the graph
        plot1.plot(x, y1)
        plot1.plot(x, y2, 'r--')
        plot1.legend([label1, label2])

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
                                   master=myroot)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        myroot.title(windowLabel)

        myroot.resizable(False, False)
        myroot.mainloop()

    ##################################################################################################################

    def compGraphs(self, sortType1,sortType2, compCheck):
        if compCheck == 0 and sortType2 == "none":
            y1,y2,worstCaseLabel = self.doThat(sortType1, compCheck)
            self.plotGraph(App.elementsNo, y1, y2, f"Actual time: {sortType1}", f"Worst time complexity: {worstCaseLabel}", sortType1 )
        elif compCheck == 1 and sortType2 != "none":
            y1 = self.doThat(sortType1, compCheck)
            y2 = self.doThat(sortType2, compCheck)
            self.plotGraph(App.elementsNo, y1, y2, sortType1, sortType2 ,f"{sortType1} vs {sortType2}")

class FirstPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=appBg)
        options = ["Generate Test file", "Upload a test file"]
        label = Label(self, text="Algorithms Graph Calculator", font=('Helvetica 16 bold'), bg=appBg)
        label.place(relx=0.4, rely=0.04)

        clicked = StringVar()
        clicked.set("Generate Test file")
        drop = OptionMenu(self, clicked, *options)
        drop.place(relx=0.45, rely=0.35)

        myFont = font.Font(size=15)
        myFont1 = font.Font(size=12)

        label = Label(self, text="Test file option: ", font=("Arial", 13, "bold"), bg=appBg).place(relx=0.35,
                                                                                                        rely=0.35)

        label2 = Label(self, text="Enter name of file: ", font=("Arial", 13, "bold"), bg=appBg).place(relx=0.35,
                                                                                                   rely=0.50)


        thisFilename = StringVar()
        fileNameField2 = Entry(self, textvariable=thisFilename, font=('calibre', 10, 'normal')).place(relx=0.46, rely=0.5)

        label3 = Label(self, text="Note: test file is a text file and should/would be in same directory of the app", font=("Arial", 11, "bold"), bg=appBg).place(relx=0.35,
                                                                                                   rely=0.6)


        choiceBtn = Button(self, text="Proceed", bg='#0052cc', fg='#ffffff',
                           command=lambda: controller.testFile(clicked.get(), thisFilename.get()))
        choiceBtn['font'] = myFont
        choiceBtn.place(relx=0.48, rely=0.7)




class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=appBg)

        label = Label(self, text="Algorithms Graph Calculator", font=('Helvetica 20 bold'), bg=appBg)
        label.place(relx=0.36, rely=0.1)

        page_one = Button(self, text="Graph algorithms", command=lambda: controller.show_frame(GraphAlgorithms),
                          width=20
                          , height=5, foreground=btnFg, bg=btnBg, font=('Helvetica 16 bold'))

        page_one.place(relx=0.3, rely=0.5, anchor=CENTER)

        page_two = Button(self, text="Comparison graphs", command=lambda: controller.show_frame(CompareGraphs),
                          width=20,
                          height=5, font=('Helvetica 16 bold'), bg=btnBg, foreground=btnFg)
        page_two.place(relx=0.7, rely=0.5, anchor=CENTER)

        myFont1 = font.Font(size=12)

        start_page1 = Button(self, text="Start Page", bg='#d442f5', fg='#ffffff',
                             command=lambda: controller.show_frame(FirstPage))
        start_page1['font'] = myFont1
        start_page1.pack(side=LEFT)

class GraphAlgorithms(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=appBg)
        options = ["Insertion Sort", "Merge Sort", "Heap Sort", "Quick Sort" , "Bubble Sort","Selection Sort" , "Counting Sort", "Radix Sort"]
        label = Label(self, text="Graphing Algorithms", font=('Helvetica 16 bold'), bg=appBg)
        label.place(relx=0.4, rely=0.04)

        clicked = StringVar()
        clicked.set("Insertion Sort")
        drop = OptionMenu(self, clicked, *options)
        drop.place(relx=0.5, rely=0.35)

        myFont = font.Font(size=15)
        myFont1 = font.Font(size=12)

        label = Label(self, text="Choose your algorithm: ", font=("Arial", 13, "bold") ,bg=appBg).place(relx = 0.35, rely = 0.355)
        choiceBtn = Button(self, text="Graph", bg='#0052cc', fg='#ffffff' ,command=lambda: controller.compGraphs(clicked.get(), "none", 0))
        choiceBtn['font'] = myFont
        choiceBtn.place( relx=0.48, rely=0.7)
        start_page1 = Button(self, text="Previous", bg='#d442f5', fg='#ffffff', command=lambda: controller.show_frame(StartPage))
        start_page1['font'] = myFont1
        start_page1.pack(side=LEFT)
        page_two = Button(self, text="Compare Graphs",bg='#d442f5', fg='#ffffff', command=lambda: controller.show_frame(CompareGraphs))
        page_two['font'] = myFont1
        page_two.pack(side=RIGHT)


class CompareGraphs(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=appBg)

        myFont = font.Font(size=15)
        myFont1 = font.Font(size=12)
        label = Label(self, text="Comparing Algorithms", font=('Helvetica 16 bold'), bg=appBg)
        label.place(relx = 0.4, rely = 0.04)

        options = ["Insertion Sort", "Merge Sort", "Heap Sort", "Quick Sort" , "Bubble Sort","Selection Sort" , "Counting Sort", "Radix Sort"]


        clicked = StringVar()
        clicked.set("Insertion Sort")
        drop = OptionMenu(self, clicked, *options)
        drop.place(relx=0.45, rely=0.25)
        label1 = Label(self, text="Choose your first algorithm: ", font=("Arial", 13, "bold") ,bg=appBg).place(relx = 0.28, rely = 0.25)

        clicked2 = StringVar()
        clicked2.set("Merge Sort")
        drop2 = OptionMenu(self, clicked2, *options)
        drop2.place(relx=0.45, rely=0.5)
        label2 = Label(self, text="Choose your second algorithm: ", font=("Arial", 13, "bold"), bg=appBg).place(relx=0.26, rely=0.5)
        choiceBtn = Button(self, text="Compare Graphs", bg='#0052cc', fg='#ffffff' ,command=lambda: controller.compGraphs(clicked.get(), clicked2.get(), 1))
        choiceBtn['font'] = myFont
        choiceBtn.place(relx=0.42, rely=0.8)

        start_page = Button(self, text="Start Page",  bg='#d442f5', fg='#ffffff', command=lambda: controller.show_frame(FirstPage))
        start_page['font'] = myFont1
        start_page.pack(side=LEFT)
        page_one = Button(self, text="Graph Algorithm",  bg='#d442f5', fg='#ffffff' ,command=lambda: controller.show_frame(GraphAlgorithms))
        page_one['font'] = myFont1
        page_one.pack(side=RIGHT)


if __name__ == "__main__":
    app = App(className="Algorithms Graph Calculator")
    # app.geometry("600x500")
    app.state('zoomed')
    app.resizable(False, False)
    app.mainloop()
