# 时钟
set_property -dict {PACKAGE_PIN P17 IOSTANDARD LVCMOS33} [get_ports clk]

# 使用 LED[0]
set_property -dict {PACKAGE_PIN K3  IOSTANDARD LVCMOS33} [get_ports led]

# 用下键作为复位键
set_property -dict {PACKAGE_PIN R17 IOSTANDARD LVCMOS33} [get_ports rst]

# 用中键作为控制键
set_property -dict {PACKAGE_PIN R15 IOSTANDARD LVCMOS33} [get_ports key]
