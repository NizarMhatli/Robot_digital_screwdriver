from aphyt import omron
import time
eip_instance = omron.n_series.NSeriesEIP()
eip_instance.connect_explicit('192.168.251.1')
eip_instance.register_session()
eip_instance.update_variable_dictionary()

time.sleep(10)
reply = eip_instance.write_variable('tol', False)
reply = eip_instance.write_variable('toolu', False)
reply = eip_instance.write_variable('tol', True)