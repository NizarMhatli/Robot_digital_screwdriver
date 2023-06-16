from PRO_FUSE_SOFT import PRO_SCREW_in_RE,PRO_SCREW_pik_RE,PRO_SCREW_in,PRO_SCREW_pik,PRO_PARA_IN,PRO_DATA_IN
import time
data = PRO_SCREW_in_RE()
cycle_start_time = time.time()
print(int(cycle_start_time))
data1 = PRO_SCREW_pik_RE()
print(data1)
PRO_SCREW_in()
PRO_SCREW_pik()
data2 = PRO_PARA_IN()
data2 = PRO_DATA_IN()
print(data2)