import pandas
# Just disables the warning, doesn't enable AVX/FMA
import os
from datetime import datetime

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from multi_armed_bandit.algorithm.algorithm import EpsilonGreedy
from multi_armed_bandit.arms.arm import NormalArm

from tkinter import *


if __name__ == '__main__':

    root = Tk()
    root.title("Однорукий бандит на Python")
    def create_bandits():
        arms = [NormalArm(1, input_sigma1.get(), input_mu1.get()),
                NormalArm(2, input_sigma2.get(), input_mu2.get()),
                NormalArm(3, input_sigma3.get(), input_mu3.get()),
                NormalArm(4, input_sigma4.get(), input_mu4.get()),
                ]
        epsilon = input_epsilon.get()
        algorithm = EpsilonGreedy(arms, epsilon)
        results = algorithm.run_simulation(1000)
        df = pandas.DataFrame(results)
        date = datetime.now()

        df.to_csv("results (e={}) {}.csv".format(epsilon, date), index=False)
        print('Well done! \n Result in file "results (e={}) {}.csv"'.format(epsilon, date))

        result_label = Label(text='Готово, рещультат в файле "results (e={}) {}.csv"'.format(epsilon, date), font="Arial 22")
        result_label.place(anchor="c")
        result_label.pack()

        print([input_sigma1.get(), input_mu1.get()])
        print([input_sigma2.get(), input_mu2.get()])
        print([input_sigma3.get(), input_mu3.get()])
        print([input_sigma4.get(), input_mu4.get()])



    input_mu1, input_sigma1 = DoubleVar(), DoubleVar()
    input_mu2, input_sigma2 = DoubleVar(), DoubleVar()
    input_mu3, input_sigma3 = DoubleVar(), DoubleVar()
    input_mu4, input_sigma4 = DoubleVar(), DoubleVar()


    mu_label1 = Label(text='mu Бандита №1', font="Arial 12")
    arm_mu1 = Entry(textvariable=input_mu1)

    sigma_label1 = Label(text='sigma Бандита №1', font="Arial 12")
    arm_sigma1 = Entry(textvariable=input_sigma1)


    mu_label1.place(anchor="e")
    mu_label1.pack()

    arm_mu1.place(anchor="w")
    arm_mu1.pack()

    sigma_label1.place(anchor="e")
    sigma_label1.pack()

    arm_sigma1.place(anchor="w")
    arm_sigma1.pack()

    mu_label2 = Label(text='mu Бандита №2', font="Arial 12")
    arm_mu2 = Entry(textvariable=input_mu2)

    sigma_label2 = Label(text='sigma Бандита №2', font="Arial 12")
    arm_sigma2 = Entry(textvariable=input_sigma2)

    mu_label2.place(anchor="e")
    mu_label2.pack()

    arm_mu2.place(anchor="w")
    arm_mu2.pack()

    sigma_label2.place(anchor="e")
    sigma_label2.pack()

    arm_sigma2.place(anchor="w")
    arm_sigma2.pack()

    mu_label3 = Label(text='mu Бандита №3', font="Arial 12")
    arm_mu3 = Entry(textvariable=input_mu3)

    sigma_label3 = Label(text='sigma Бандита №3', font="Arial 12")
    arm_sigma3 = Entry(textvariable=input_sigma3)

    mu_label3.place(anchor="e")
    mu_label3.pack()

    arm_mu3.place(anchor="w")
    arm_mu3.pack()

    sigma_label3.place(anchor="e")
    sigma_label3.pack()

    arm_sigma3.place(anchor="w")
    arm_sigma3.pack()

    mu_label4 = Label(text='mu Бандита №4', font="Arial 12")
    arm_mu4 = Entry(textvariable=input_mu4)

    sigma_label4 = Label(text='sigma Бандита №4', font="Arial 12")
    arm_sigma4 = Entry(textvariable=input_sigma4)

    mu_label4.place(anchor="e")
    mu_label4.pack()

    arm_mu4.place(anchor="w")
    arm_mu4.pack()

    sigma_label4.place(anchor="e")
    sigma_label4.pack()

    arm_sigma4.place(anchor="w")
    arm_sigma4.pack()


    input_arm_button = Button(text='Создать бандитов', command=create_bandits)

    input_arm_button.place(anchor="c")
    input_arm_button.pack()




    # root.geometry("300x250")

    input_epsilon = DoubleVar()
    epsilon_label = Label(text='эпсилон = ', font="Arial 12")
    input_arms_entry = Entry(textvariable=input_epsilon)
    epsilon_label.place(anchor="c")
    epsilon_label.pack()
    input_arms_entry.place(anchor="c")
    input_arms_entry.pack()

    # input_arms_button = Button(text="Количество бандитов", command=create_arms)
    # input_arms_button.place(anchor="c")
    # input_arms_button.pack()


    root.mainloop()


