module top (
    input clk,      // 时钟信号，频率为100MHz
    input rst,      // 复位键, 按下产生高电平
    input btn,      // 按键输入, 按下产生高电平
    output led      // LED输出
);
    wire toggle;
    
    debounce db (
        .clk(clk),
        .rst(rst),
        .key_in(btn),
        .key_out(toggle)
    );

    led x (
        .clk(clk),
        .rst(rst),
        .toggle(toggle),
        .led(led)
    );
endmodule