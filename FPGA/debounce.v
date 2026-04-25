module debounce (
    input      clk,      // 系统时钟(频率为100MHz)
    input      rst,      // 复位信号(按下产生高电平)
    input      key_in,   // 硬件按键输入(按下产生高电平)
    output reg key_out   // 消抖后的信号
);

    localparam [20:0] DEBOUNCE_MAX = 21'd2_000_000; // 20ms @100MHz

    reg [20:0] cnt;      // 稳定计数器
    reg [1:0] key_sync;  // 按键两级同步
    reg key_state;       // 上一次稳定电平

    always @(posedge clk or posedge rst) begin
        // 复位
        if (rst) begin
            cnt <= 20'd0;
            key_sync <= 2'b00;
            key_state <= 1'b0;
            key_out <= 1'b0;
        end else begin
            // 默认输出低电平，仅在稳定按下瞬间拉高1个时钟周期
            key_out <= 1'b0;

            // 按键同步到clk域
            key_sync <= {key_sync[0], key_in};

            // 同步值与稳定值不同，开始计时确认稳定性
            if (key_sync[1] != key_state) begin
                if (cnt < DEBOUNCE_MAX - 1'b1) begin
                    cnt <= cnt + 1'b1;
                end else begin
                    cnt <= 21'd0;
                    key_state <= key_sync[1]; // 更新稳定值
                    // 只有从未按下到按下的瞬间才输出高电平
                    // 只在稳定上升沿输出一个脉冲
                    if (key_sync[1] == 1'b1)
                        key_out <= 1'b1;
                end
            end else begin
                cnt <= 21'd0;
            end
        end
    end
endmodule