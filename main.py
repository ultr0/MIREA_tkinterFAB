import pandas
# Just disables the warning, doesn't enable AVX/FMA
import os
from datetime import datetime


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from multi_armed_bandit.algorithm.algorithm import EpsilonGreedy
from multi_armed_bandit.arms.arm import NormalArm

from tkinter import *

if __name__ == '__main__':
    arms = [NormalArm(0, 0.3, 1), NormalArm(1, 0.5, 1), NormalArm(2, 1, 1)]
    epsilon = 0.1
    algorithm = EpsilonGreedy(arms, epsilon)
    results = algorithm.run_simulation(1000)
    df = pandas.DataFrame(results)
    date = datetime.now()

    from tkinter import *
    from tkinter import messagebox


    def create_arms():
        arms_number = input_number_arms.get()
        for arm in range(0, arms_number):
            print(arm)
            input_mu = DoubleVar()
            input_sigma = DoubleVar()
            mu_label = Label(text='mu Бандита №{}'.format(arm+1), font="Arial 12")
            arm_mu = Entry(textvariable=input_mu)
            sigma_label = Label(text='sigma Бандита №{}'.format(arm+1), font="Arial 12")
            arm_sigma = Entry(textvariable=input_sigma)
            mu_label.place(anchor="e")
            mu_label.pack()
            arm_mu.place(anchor="w")
            arm_mu.pack()
            sigma_label.place(anchor="e")
            sigma_label.pack()
            arm_sigma.place(anchor="w")
            arm_sigma.pack()

            # if bu


    root = Tk()
    root.title("Однорукий бандит на Python")
    # root.geometry("300x250")

    input_number_arms = IntVar()

    input_arms_entry = Entry(textvariable=input_number_arms)
    input_arms_entry.place(anchor="c")
    input_arms_entry.pack()

    input_arms_button = Button(text="Количество бандитов", command=create_arms)
    input_arms_button.place(anchor="c")
    input_arms_button.pack()

    root.mainloop()

    df.to_csv("results (e={}) {}.csv".format(epsilon, date), index=False)
    print('Well done! \n Result in file "results (e={}) {}.csv"'.format(epsilon, date))
