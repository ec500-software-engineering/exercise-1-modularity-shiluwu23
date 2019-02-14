import Input_Module_lkn
import AiModule
import Alert_module
import UserInterface_module
#from queue import Queue
import threading
import time
import random


def generate():
    # INPUT
    bloodoxy = Input_Module_lkn.read_data('./bloodoxy.txt')
    bloodpressure = Input_Module_lkn.read_data('./bloodpressure.txt')
    pulse = Input_Module_lkn.read_data('./pulse.txt')
    #AI
    AI = AiModule.AiModule()
    AI.input_check(bloodoxy,bloodpressure,pulse)
    a, b, c = AI.predict()

    # Alert
    alarm = Alert_module.Alert()
    for i in range(len(bloodoxy)):
        boi = bloodoxy[i], 0
        bpi = bloodpressure[i], 1
        puli = pulse[i], 2
        boa = alarm.get_bo_data(boi)
        bpa = alarm.get_bp_data(bpi)
        pula = alarm.get_pul_data(puli)
        #UserInterface
    User = UserInterface_module.userInterface()
    UserInterface_module.ai_output(a, b, c)




while True:
	for i in range(5):
		t = threading.Thread(target = generate)
		t.start()
		time.sleep(random.randint(2,4))

