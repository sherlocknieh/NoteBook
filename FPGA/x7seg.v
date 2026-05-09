// BCD十进制数显示器

module x7seg(
    input [15:0] x,             // 输入数据
    input clk,                  // 时钟信号
    input rst,                  // 复位信号
    output reg [7:0] segments,  // 段选信号
    output reg [3:0] digits     // 位选信号 (位表示)
);

    reg [3:0] hex;              // 十六进制数
    wire [1:0] d;           // 位选信号 (数字表示)
    reg [19:0] clkdiv;          // 时钟计数器
    assign d = clkdiv[19:18];   // 18分频，每 5.2ms 计数+1，依次点亮4个数码管 (仿真测试时可以改为clkdiv[4:3])


    // 时钟计数器逻辑
    always @ ( posedge clk or negedge rst ) begin
        if ( rst == 1 )
            clkdiv <= 0;                 // clkdiv 清零；
        else  
            clkdiv <= clkdiv+1;          // clkdiv + 1;
    end


    // 依次点亮4个数码管
    always @ ( * ) begin
        digits = 4'b0000;   
        if(rst == 0)
            digits[d] = 1'b1;
    end


    // 把 16 位二进制分为四个BCD
    always @ ( * ) case ( d )
        0:hex = x[3:0];
        1:hex = x[7:4];
        2:hex = x[11:8];
        3:hex = x[15:12];
        default: hex = x[3:0];
    endcase


    //段译码器
    always @ ( * ) case ( hex )
        4'b0000: segments = 8'b11111100; // 0
        4'b0001: segments = 8'b01100000; // 1
        4'b0010: segments = 8'b11011010; // 2
        4'b0011: segments = 8'b11110010; // 3
        4'b0100: segments = 8'b01100110; // 4
        4'b0101: segments = 8'b10110110; // 5
        4'b0110: segments = 8'b10111110; // 6
        4'b0111: segments = 8'b11100000; // 7
        4'b1000: segments = 8'b11111110; // 8
        4'b1001: segments = 8'b11110110; // 9
        4'b1010: segments = 8'b11101110; // A
        4'b1011: segments = 8'b00111110; // B
        4'b1100: segments = 8'b10011100; // C
        4'b1101: segments = 8'b01111010; // D
        4'b1110: segments = 8'b10011110; // E
        4'b1111: segments = 8'b10001110; // F
        default: segments = 8'b00000000; // 默认显示空白
    endcase  
endmodule