module top (
    input clk,      // 时钟信号 (频率为 100MHz)
    input rst,      // 复位信号 (按下为高电平)
    input key,      // 按键输入 (按下为高电平)
    output led      // LED输出
);
    wire toggle;
    
    debounce db (
        .clk(clk),
        .rst(rst),
        .key_in(key),
        .key_up(toggle) // 使用按键松开信号
    );

    led x (
        .clk(clk),
        .rst(rst),
        .key(toggle),
        .led(led)
    );
endmodule