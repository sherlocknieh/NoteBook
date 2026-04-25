module led (
    input clk,      // 时钟信号 (频率为 100MHz)
    input rst,      // 复位信号 (按下为高电平)
    input key,      // 按键信号 (高电平脉冲信号)
    output reg led  // LED输出
);
    // 时序逻辑
    always @ (posedge clk) begin
        if (rst) begin
            led <= 1'b0; // 复位时LED熄灭
        end
        else if (key) begin
            led <= ~led; // 按下按键切换LED状态
        end
    end
endmodule