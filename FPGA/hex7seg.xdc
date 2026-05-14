
# 拨码开关
set_property -dict {PACKAGE_PIN P4 IOSTANDARD LVCMOS33} [get_ports {digit[1]}]
set_property -dict {PACKAGE_PIN P3 IOSTANDARD LVCMOS33} [get_ports {digit[0]}]

set_property -dict {PACKAGE_PIN P2 IOSTANDARD LVCMOS33} [get_ports {point}]

set_property -dict {PACKAGE_PIN R2 IOSTANDARD LVCMOS33} [get_ports {hex[3]}]
set_property -dict {PACKAGE_PIN M4 IOSTANDARD LVCMOS33} [get_ports {hex[2]}]
set_property -dict {PACKAGE_PIN N4 IOSTANDARD LVCMOS33} [get_ports {hex[1]}]
set_property -dict {PACKAGE_PIN R1 IOSTANDARD LVCMOS33} [get_ports {hex[0]}]


# 数码管位选信号
set_property -dict {PACKAGE_PIN G1 IOSTANDARD LVCMOS33} [get_ports {digits[3]}]
set_property -dict {PACKAGE_PIN F1 IOSTANDARD LVCMOS33} [get_ports {digits[2]}]
set_property -dict {PACKAGE_PIN E1 IOSTANDARD LVCMOS33} [get_ports {digits[1]}]
set_property -dict {PACKAGE_PIN G6 IOSTANDARD LVCMOS33} [get_ports {digits[0]}]

# 数码管段选信号
# 右4位数码管(共8段,依次为: 上、右上、右下、下、左下、左上、中横杠、小数点)
set_property -dict {PACKAGE_PIN D4 IOSTANDARD LVCMOS33} [get_ports {segs[7]}]
set_property -dict {PACKAGE_PIN E3 IOSTANDARD LVCMOS33} [get_ports {segs[6]}]
set_property -dict {PACKAGE_PIN D3 IOSTANDARD LVCMOS33} [get_ports {segs[5]}]
set_property -dict {PACKAGE_PIN F4 IOSTANDARD LVCMOS33} [get_ports {segs[4]}]
set_property -dict {PACKAGE_PIN F3 IOSTANDARD LVCMOS33} [get_ports {segs[3]}]
set_property -dict {PACKAGE_PIN E2 IOSTANDARD LVCMOS33} [get_ports {segs[2]}]
set_property -dict {PACKAGE_PIN D2 IOSTANDARD LVCMOS33} [get_ports {segs[1]}]
set_property -dict {PACKAGE_PIN H2 IOSTANDARD LVCMOS33} [get_ports {segs[0]}]
