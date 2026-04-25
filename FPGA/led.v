module led (
    input clk,      // 时钟信号，频率为100MHz
    input rst,      // 复位键, 按下产生高电平
    input toggle,   // 已经消抖的输入
    output reg led  // LED输出
);
    // 时序逻辑
    always @ (posedge clk) begin
        if (rst) begin
            led <= 1'b1; // 复位时LED亮
        end
        else if (toggle) begin
            led <= ~led; // 每次按键切换LED状态
        end
    end
endmodule