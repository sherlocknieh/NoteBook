`timescale 1ns / 1ps
module flowing_light(
    input clk,              // 时钟信号，频率为100MHz
    input rst,              // 复位键, 按下产生高电平
    input btn_up,               // 上按键, 按下产生高电平
    input btn_down,             // 下按键, 按下产生高电平
    input btn_left,             // 左按键, 按下产生高电平
    input btn_right,            // 右按键, 按下产生高电平
    output [15:0] led       // 16个LED灯
	);
	
    reg [15 : 0] led_reg;   // LED状态寄存器
    assign led = led_reg;   // 连接到LED引脚

    reg [28 : 0] cnt_reg;   // 29位计数器, 计数范围 0~536870911, 能实现最高 5 秒的计数
	reg [28 : 0] cnt_max;   // 计数器阈值, 用于控制计数周期
    parameter PERIOD = 29'd100000000;   // 默认周期: 1 秒
    localparam MAX_PERIOD = PERIOD * 5; // 最大周期: 5 秒
    localparam MIN_PERIOD = PERIOD / 8; // 最小周期: 1/8 秒

	// 方向寄存器: 0表示向左移动，1表示向右移动
    reg direction_reg;

    // 时序逻辑
    always @ (posedge clk) begin
        // 复位逻辑
        if (rst) begin
            led_reg <= 16'h0001;    // LED 初始状态: 0000 0000 0000 0001
            direction_reg <= 1'b0;  // 默认向左移动
            cnt_reg <= 0;           // 计数器清零
            cnt_max <= PERIOD;      // 默认周期为 1 秒
        end
        // 正常逻辑
        else begin

            // 方向控制
            if (btn_left)
                direction_reg <= 1'b0;
            else if (btn_right)
                direction_reg <= 1'b1;

            // 频率控制
            if (btn_up) begin
                if (cnt_max > PERIOD)
                    cnt_max <= cnt_max - PERIOD;
                else if (cnt_max > MIN_PERIOD)
                    cnt_max <= cnt_max >> 1;
            end
            
            else if (btn_down) begin
                if (cnt_max < PERIOD)
                    cnt_max <= cnt_max << 1;
                else if (cnt_max < MAX_PERIOD)
                    cnt_max <= cnt_max + PERIOD;
            end

            // 计数与LED更新
            if (cnt_reg >= cnt_max) begin
                cnt_reg <= 0;
                if (direction_reg == 1'b0)
                    led_reg <= {led_reg[14:0], led_reg[15]};
                else
                    led_reg <= {led_reg[0], led_reg[15:1]};
            end
            
            else begin
                cnt_reg <= cnt_reg + 1;
            end
        end
    end
endmodule