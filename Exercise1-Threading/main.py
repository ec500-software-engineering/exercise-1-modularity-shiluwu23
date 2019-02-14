# Copyright by @Shilu Wu

import Input_Module_lkn
import storage
import AiModule
import Alert_Module_Xinsha
import UserInterface_module
import threading

def generate(a,b,c):
	bloodoxy = Input_Module_lkn.read_data(a)
	bloodpressure = Input_Module_lkn.read_data(b)
	pulse = Input_Module_lkn.read_data(c)
	database = []

	for i in range(len(bloodoxy)):
		database.append(storage.storage(bloodoxy[i],bloodpressure[i],pulse[i]))

	AI = AiModule.AiModule()
	AI.input_check(bloodoxy,bloodpressure,pulse)
	a,b,c=AI.predict()

	UserInterface_module.ai_output(a,b,c)

	alarm = Alert_Module_Xinsha.Alert()

	for i in range(len(bloodoxy)):
		alarm.get_bo_data(bloodoxy[i])
		alarm.get_bp_data(bloodpressure[i])
		alarm.get_pul_data(pulse[i])

	UserInterface_module.alert_out(alarm.Alert_Output())

if __name__ == '__main__':

	a = './bloodoxy1.txt'
	b = './bloodpressure1.txt'
	c = './pulse1.txt'
	t1 = threading.Thread(target=generate(a,b,c))
	t1.start()

	a = './bloodoxy2.txt'
	b = './bloodpressure2.txt'
	c = './pulse2.txt'
	t2 = threading.Thread(target=generate(a,b,c))
	t2.start()

	a = './bloodoxy3.txt'
	b = './bloodpressure3.txt'
	c = './pulse3.txt'
	t3 = threading.Thread(target=generate(a,b,c))
	t3.start()
