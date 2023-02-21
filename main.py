# Coded By Matthew Myles & Nicholas DiLuzio

import matplotlib.pyplot as plt
import DataFrameCode as df


def showOverActLim(x):
    plot=''
    if x==1:
        plot= df.clusterActOver()
    elif x==2:
        plot = df.clusterActOver_M()
    elif x==3:
        plot = df.clusterActOver_F()
    plot.plot()

def showOverCogDec(x):
    plot = ''
    if x == 1:
        plot = df.clusterCogOver()
    elif x == 2:
        plot= df.clusterCogOver_M()
    elif x == 3:
        plot = df.clusterCogOver_F()
    plot.plot()

def showOverMent(x):
    plot=''
    if x==1:
        plot= df.clusterMentOver()
    elif x==2:
        plot = df.clusterMentOver_M()
    elif x==3:
        plot = df.clusterMentOver_F()
    plot.plot()

def showOverSleep(x):
    plot = ''
    if x == 1:
        plot = df.clusterSleepOver()
    elif x == 2:
        plot= df.clusterSleepOver_M()
    elif x == 3:
        plot = df.clusterSleepOver_F()
    plot.plot()


def show5064ActLim(x):
    plot=''
    if x==1:
        plot= df.clusterAct5064()
    elif x==2:
        plot = df.clusterAct5064_M()
    elif x==3:
        plot = df.clusterAct5064_F()
    plot.plot()

def show5064CogDec(x):
    plot = ''
    if x == 1:
        plot = df.clusterCog5064()
    elif x == 2:
        plot= df.clusterCog5064_M()
    elif x == 3:
        plot = df.clusterCog5064_F()
    plot.plot()

def show5064Ment(x):
    plot=''
    if x==1:
        plot= df.clusterMent5064()
    elif x==2:
        plot = df.clusterMent5064_M()
    elif x==3:
        plot = df.clusterMent5064_F()
    plot.plot()

def show5064Sleep(x):
    plot = ''
    if x == 1:
        plot = df.clusterSleep5064()
    elif x == 2:
        plot= df.clusterSleep5064_M()
    elif x == 3:
        plot = df.clusterSleep5064_F()
    plot.plot()


def show65ActLim(x):
    plot=''
    if x==1:
        plot= df.clusterAct65()
    elif x==2:
        plot = df.clusterAct65_M()
    elif x==3:
        plot = df.clusterAct65_F()
    plot.plot()

def show65CogDec(x):
    plot = ''
    if x == 1:
        plot = df.clusterCog65()
    elif x == 2:
        plot= df.clusterCog65_M()
    elif x == 3:
        plot = df.clusterCog65_F()
    plot.plot()

def show65Ment(x):
    plot=''
    if x==1:
        plot= df.clusterMent65()
    elif x==2:
        plot = df.clusterMent65_M()
    elif x==3:
        plot = df.clusterMent65_F()
    plot.plot()

def show65Sleep(x):
    plot = ''
    if x == 1:
        plot = df.clusterSleep65()
    elif x == 2:
        plot= df.clusterSleep65_M()
    elif x == 3:
        plot = df.clusterSleep65_F()
    plot.plot()


def showplots(in1, in2, in3):
    #If else ladder for overall
    if in1 == 1 and in2 == 1 and in3 == 1:
        showOverActLim(1)
    elif in1 == 1 and in2 == 1 and in3 == 2:
        showOverActLim(2)
    elif in1 == 1 and in2 == 1 and in3 == 3:
        showOverActLim(3)
    elif in1 == 1 and in2 == 2 and in3 == 1:
        showOverCogDec(1)
    elif in1 == 1 and in2 == 2 and in3 == 2:
        showOverCogDec(2)
    elif in1 == 1 and in2 == 2 and in3 == 3:
        showOverCogDec(3)
    elif in1 == 1 and in2 == 3 and in3 == 1:
        showOverMent(1)
    elif in1 == 1 and in2 == 3 and in3 == 2:
        showOverMent(2)
    elif in1 == 1 and in2 == 3 and in3 == 3:
        showOverMent(3)
    elif in1 == 1 and in2 == 4 and in3 == 1:
        showOverSleep(1)
    elif in1 == 1 and in2 == 4 and in3 == 2:
        showOverSleep(2)
    elif in1 == 1 and in2 == 4 and in3 == 3:
        showOverSleep(3)

    #Elif ladder for 5064
    elif in1 == 2 and in2 == 1 and in3 == 1:
        show5064ActLim(1)
    elif in1 == 2 and in2 == 1 and in3 == 2:
        show5064ActLim(2)
    elif in1 == 2 and in2 == 1 and in3 == 3:
        show5064ActLim(3)
    elif in1 == 2 and in2 == 2 and in3 == 1:
        show5064CogDec(1)
    elif in1 == 2 and in2 == 2 and in3 == 2:
        show5064CogDec(2)
    elif in1 == 2 and in2 == 2 and in3 == 3:
        show5064CogDec(3)
    elif in1 == 2 and in2 == 3 and in3 == 1:
        show5064Ment(1)
    elif in1 == 2 and in2 == 3 and in3 == 2:
        show5064Ment(2)
    elif in1 == 2 and in2 == 3 and in3 == 3:
        show5064Ment(3)
    elif in1 == 2 and in2 == 4 and in3 == 1:
        show5064Sleep(1)
    elif in1 == 2 and in2 == 4 and in3 == 2:
        show5064Sleep(2)
    elif in1 == 2 and in2 == 4 and in3 == 3:
        show5064Sleep(3)

    # Elif ladder for 65+
    elif in1 == 3 and in2 == 1 and in3 == 1:
        show65ActLim(1)
    elif in1 == 3 and in2 == 1 and in3 == 2:
        show65ActLim(2)
    elif in1 == 3 and in2 == 1 and in3 == 3:
        show65ActLim(3)
    elif in1 == 3 and in2 == 2 and in3 == 1:
        show65CogDec(1)
    elif in1 == 3 and in2 == 2 and in3 == 2:
        show65CogDec(2)
    elif in1 == 3 and in2 == 2 and in3 == 3:
        show65CogDec(3)
    elif in1 == 3 and in2 == 3 and in3 == 1:
        show65Ment(1)
    elif in1 == 3 and in2 == 3 and in3 == 2:
        show65Ment(2)
    elif in1 == 3 and in2 == 3 and in3 == 3:
        show65Ment(3)
    elif in1 == 3 and in2 == 4 and in3 == 1:
        show65Sleep(1)
    elif in1 == 3 and in2 == 4 and in3 == 2:
        show65Sleep(2)
    else:
        show65Sleep(3)



def run():
    stop=False
    while not stop:
        plt.close('all')
        print("What age group would you like to see? \n 1. Overall  2. 50-64  3. 65+ (Enter -1 To Stop)")
        option1 = int(input())
        if option1 == -1:
            stop= True
        elif option1 != 1 and option1 != 2 and option1 != 3:
            while option1 != 1 and option1 != 2 and option1 != 3 and option1 != -1:
                print("Incorrect input! What age group would you like to see? \n 1. Overall  2. 50-64  3. 65+ (Enter Number, -1 to stop)")
                option1 = int(input())
            if option1 == -1:
                stop = True
        else:
            print("What kind of question would you like to see? \n 1. Activity Limitations  2. Cognitive Decline  3. Mental Distress  4. Sufficient Sleep  (Enter Number, -1 to stop)")
            option2 = int(input())
            if option2 == -1:
                stop = True
            elif option2 != 1 and option2 != 2 and option2 != 3 and option2 != 4:
                while option2 != 1 and option2 != 2 and option2 != 3 and option2 != 4 and option2 != -1:
                    print("Incorrect input! What kind of question would you like to see? \n 1. Activity Limitations  2. Cognitive Decline  3. Mental Distress  4. Sufficient Sleep  (Enter Number, -1 to stop)")
                    option2 = int(input())
                    if option2 == -1:
                        stop = True
            else:
                print("What specific gender would you like to see? \n 1. None  2. Male  3. Female  (Enter Number Option, -1 to stop)")
                option3 = int(input())
                if option3 == -1:
                    stop = True
                elif option3 != 1 and option3 != 2 and option3 != 3:
                    while option3 != 1 and option3 != 2 and option3 != 3 and option3 != -1:
                        print("Incorrect input! What specific gender would you like to see? \n 1. None  2. Male  3. Female  (Enter Number Option, -1 to stop)")
                        option3 = int(input())
                        if option3 == -1:
                            stop = True
                else:
                    showplots(option1, option2, option3)
                    plt.show()

print("Welcome to the program! Feel free to look over all the clusters")
run()





