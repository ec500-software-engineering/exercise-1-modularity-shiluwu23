import Input_Module_lkn
import storage
import AiModule
import Alert_Module_Xinsha
import UserInterface_module
bloodoxy = Input_Module_lkn.read_data('./bloodoxy.txt')
bloodpressure = Input_Module_lkn.read_data('./bloodpressure.txt')
pulse = Input_Module_lkn.read_data('./pulse.txt')
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