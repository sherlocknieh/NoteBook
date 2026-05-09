
################################### 拨码开关 #############################
set_property -dict {PACKAGE_PIN R2 IOSTANDARD LVCMOS33} [get_ports {hex[3]}]
set_property -dict {PACKAGE_PIN M4 IOSTANDARD LVCMOS33} [get_ports {hex[2]}]
set_property -dict {PACKAGE_PIN N4 IOSTANDARD LVCMOS33} [get_ports {hex[1]}]
set_property -dict {PACKAGE_PIN R1 IOSTANDARD LVCMOS33} [get_ports {hex[0]}]


############################### 数码管位选信号 #################################
set_property -dict {PACKAGE_PIN G6 IOSTANDARD LVCMOS33} [get_ports {enable}]

################################### 数码管段选信号 ##################################

set_property -dict {PACKAGE_PIN D4 IOSTANDARD LVCMOS33} [get_ports {segments[7]}]
set_property -dict {PACKAGE_PIN E3 IOSTANDARD LVCMOS33} [get_ports {segments[6]}]
set_property -dict {PACKAGE_PIN D3 IOSTANDARD LVCMOS33} [get_ports {segments[5]}]
set_property -dict {PACKAGE_PIN F4 IOSTANDARD LVCMOS33} [get_ports {segments[4]}]
set_property -dict {PACKAGE_PIN F3 IOSTANDARD LVCMOS33} [get_ports {segments[3]}]
set_property -dict {PACKAGE_PIN E2 IOSTANDARD LVCMOS33} [get_ports {segments[2]}]
set_property -dict {PACKAGE_PIN D2 IOSTANDARD LVCMOS33} [get_ports {segments[1]}]
set_property -dict {PACKAGE_PIN H2 IOSTANDARD LVCMOS33} [get_ports {segments[0]}]