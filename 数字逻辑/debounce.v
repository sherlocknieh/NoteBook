// 按键消抖模块
// 消抖逻辑：只有持续 20ms 保持不变的信号才被认为是稳定信号;
//   输出信号会比输入信号落后 20ms 左右, 但一般不影响体验;

module debounce (
    input      clk,      // 系统时钟 (频率为100MHz)
    input      rst_n,    // 复位信号 (按下产生低电平)
    input      key_in,   // 按键信号 (按下产生高电平)
    output reg key_out,  // 消抖后的干净信号
    output reg key_down, // 按键按下脉冲信号
    output reg key_up    // 按键松开脉冲信号
);
    parameter [20:0] DEBOUNCE_MAX = 21'd2_000_000; // 20ms @100MHz

    reg [20:0] cnt;         // 消抖延迟计数器
    reg key_stable;         // 用于记录稳定信号
    reg [1:0]  key_sample;  // 按键信号两级采样
        // 按键信号是异步的, 当信号边沿与时钟边沿过于接近时会产生亚稳定状态
        // 故直接采样得到的 key_sample[0] 可能是亚稳定的, 故用 key_sample[1] 进行二次采样
        // key_sample[1] 会比 key_sample[0] 落后一个时钟周期, 但能有效避免亚稳定问题

    // 信号消抖逻辑
    always @(posedge clk or negedge rst_n) begin
        // 异步复位逻辑
        // 复位就是初始化, 不需要单独写 initial 块
        if (!rst_n) begin
            cnt <= 21'd0;           // 计数器清零
            key_stable <= 1'b0;     // 稳定值清零
            key_sample <= 2'b00;    // 采样值清零
            key_out <= 1'b0;        // 输出信号清零
            key_down <= 1'b0;       // 按下信号清零
            key_up <= 1'b0;         // 松开信号清零
        end
        // 时钟同步逻辑
        else begin
            // 在 always 块中, 同一信号的多次赋值以最后一次为准
            // 脉冲信号可在开头复位, 避免忘记复位产生阶跃信号
            key_down <= 1'b0;
            key_up <= 1'b0;

            // 按键信号采样
            key_sample <= {key_sample[0], key_in};

            // 如果按键状态与上次稳定值相反, 进入计数状态
            if (key_sample[1] != key_stable) begin
                // 未达消抖阈值, 继续计数
                if (cnt < DEBOUNCE_MAX) begin
                    cnt <= cnt + 1'b1;
                end
                // 达到消抖阈值, 更新记录并输出
                else begin
                    key_stable <= key_sample[1]; // 更新稳定值
                    key_out <= key_sample[1];    // 输出稳定信号
                    // 产生按下/松开脉冲
                    if (key_sample[1]) begin
                        key_down <= 1'b1; // 按下脉冲
                    end
                    else begin
                        key_up <= 1'b1;   // 松开脉冲
                    end
                    cnt <= 21'd0; // 计数器清零, 等待下次状态变化
                end
            end
            // 按键抖动回了上次的稳定值, 重置计数器
            if (key_sample[1] == key_stable)  begin
                cnt <= 21'd0;
            end
        end
    end
endmodule