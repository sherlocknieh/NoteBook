# 时钟和复位
set_property -dict {PACKAGE_PIN P17 IOSTANDARD LVCMOS33} [get_ports {clk}]
set_property -dict {PACKAGE_PIN P15 IOSTANDARD LVCMOS33} [get_ports {rst_n}]

# LED
set_property -dict {PACKAGE_PIN J2 IOSTANDARD LVCMOS33} [get_ports {q}]
set_property -dict {PACKAGE_PIN K2 IOSTANDARD LVCMOS33} [get_ports {clk_out}]