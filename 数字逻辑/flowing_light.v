// 流水灯模块

// 默认从右向左移动, 每秒移动一次
// 按上键加速, 下键减速
// 按左/右键改变方向

module flowing_light(
    input clk,              // 时钟信号 (频率为100MHz)
    input rst,              // 复位键 (按下产生高电平)
    input btn_up,           // 上按键 (高电平脉冲)
    input btn_down,         // 下按键 (高电平脉冲)
    input btn_left,         // 左按键 (高电平脉冲)
    input btn_right,        // 右按键 (高电平脉冲)
    output reg [15:0] led   // 16个LED灯
	);
	
    reg [28 : 0] cnt_reg;   // 29位计数器, 计数范围 0~536870911, 能实现最高 5 秒计数
	reg [28 : 0] cnt_max;   // 计数器阈值, 用于控制计数周期
    localparam PERIOD = 29'd100000000;   // 默认周期: 1 秒
    localparam MAX_PERIOD = PERIOD * 4;  // 最大周期: 4 秒
    localparam MIN_PERIOD = PERIOD / 16;  // 最小周期: 1/16 秒

	// 方向寄存器: 0表示向左移动，1表示向右移动
    reg direction_reg;

    // 时序逻辑
    always @ (posedge clk or posedge rst) begin
        // 复位逻辑
        if (rst) begin
            led <= 16'h0001;    // 初始状态: 最右边的LED亮
            direction_reg <= 1'b0;  // 默认向左移动
            cnt_reg <= 0;           // 计数器清零
            cnt_max <= PERIOD;      // 默认周期为 1 秒
        end
        // 时钟同步逻辑
        else begin
            // 计数逻辑
            if (cnt_reg < cnt_max-1) begin
                cnt_reg <= cnt_reg + 1;
            end
            else begin
                cnt_reg <= 0;
                if (direction_reg == 1'b0) begin
                    led <= {led[14:0], led[15]};  // 向左移动
                end
                else begin
                    led <= {led[0], led[15:1]};   // 向右移动
                end
            end

            // 按键控制方向
            if (btn_left) begin
                direction_reg <= 1'b0;  // 设置方向为向左移动
            end
            if (btn_right) begin
                direction_reg <= 1'b1;  // 设置方向为向右移动
            end

            // 上按键加速 (减小周期)
            if (btn_up) begin
                // 周期大于 PERIOD, 使用减法减少周期
                if (cnt_max > PERIOD) begin
                    cnt_max <= cnt_max - PERIOD;  // 减少周期
                end
                // 周期小于 PERIOD, 使用除法减少周期
                else if (cnt_max > MIN_PERIOD) begin
                    cnt_max <= cnt_max / 2;  // 减少周期
                end
            end
            // 下按键减速 (增大周期)
            if (btn_down) begin
                // 周期小于 PERIOD 时, 使用乘法增加周期
                if (cnt_max < PERIOD) begin
                    cnt_max <= cnt_max * 2;  // 增加周期
                end
                // 周期大于 PERIOD 时, 使用加法增加周期
                else if (cnt_max < MAX_PERIOD) begin
                    cnt_max <= cnt_max + PERIOD;  // 增加周期
                end
            end
        end
    end
endmodule