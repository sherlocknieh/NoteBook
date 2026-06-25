// PWM信号发生器
module pwm #(N = 8)
(
    input          clk,          // 时钟信号
    input          rst_n,        // 复位信号
    input  [N-1:0] duty,         // 占空比，范围为0到255
    output reg pwm_out           // PWM输出信号
);
    
    reg [N-1:0] counter;         // 计数器, 256个时钟周期为一个PWM周期
    
    always @(posedge clk) begin
        if (!rst_n) begin
            pwm_out <= 0;
            counter <= 0;
        end else if (counter < duty) begin
            pwm_out <= 1; // 输出高电平
        end else begin
            pwm_out <= 0; // 输出低电平
        end
        
        counter <= counter + 1; // 计数器递增
    end
endmodule