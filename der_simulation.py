import pandapower as pp
import numpy as np

# -----------------------
# 5 BUS DER SYSTEM
# -----------------------
net = pp.create_empty_network()

# BUS
b1 = pp.create_bus(net, vn_kv=110)
b2 = pp.create_bus(net, vn_kv=110)
b3 = pp.create_bus(net, vn_kv=110)
b4 = pp.create_bus(net, vn_kv=110)
b5 = pp.create_bus(net, vn_kv=110)

# LINES (GRAPH)
pp.create_line_from_parameters(net, b1, b2, 1, 0.01, 0.05, 0, 1)
pp.create_line_from_parameters(net, b2, b3, 1, 0.01, 0.05, 0, 1)
pp.create_line_from_parameters(net, b3, b4, 1, 0.01, 0.05, 0, 1)
pp.create_line_from_parameters(net, b4, b5, 1, 0.01, 0.05, 0, 1)
pp.create_line_from_parameters(net, b1, b5, 1, 0.01, 0.05, 0, 1)

# LOADS
pp.create_load(net, b2, p_mw=100)
pp.create_load(net, b3, p_mw=120)
pp.create_load(net, b4, p_mw=150)

# DER (Distributed Generation)
pp.create_sgen(net, b2, p_mw=50)   # PV
pp.create_sgen(net, b4, p_mw=80)   # PV

# SLACK
pp.create_ext_grid(net, b1)

# RUN POWER FLOW
pp.runpp(net)

# -----------------------
# RESULTS
# -----------------------
print("\n--- BUS VOLTAGES (pu) ---")
print(net.res_bus.vm_pu)

print("\n--- LINE LOADING (%) ---")
print(net.res_line.loading_percent)

# -----------------------
# SIMPLE GRAPH METRIC
# -----------------------
Ybus = net._ppc["internal"]["Ybus"]

degree = np.abs(Ybus).sum(axis=1)
print("\n--- NODE ELECTRICAL CENTRALITY ---")
print(degree)
