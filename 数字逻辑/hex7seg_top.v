// 4位十六进制数显示器

module hex7seg_top(
    input clk,                  // 时钟信号
    input rst_n,                // 复位信号
    input [15:0] data,          // 输入数据
    output [3:0] digits,        // 位选信号
    output [7:0] segs           // 段选信号
);

    // 分频计数器
    reg [19:0] clkdiv = 0;
    always @ (posedge clk or negedge rst_n)
    begin
        if (!rst_n)   clkdiv <= 0;          // clkdiv 清零;
        else clkdiv <= clkdiv + 1;          // clkdiv + 1;
    end

    // 提取分频计数器高两位;
    wire [1:0] i = clkdiv[19:18];           // 对 100MHz 的时钟进行 2^19 分频; i = 0, 1, 2, 3 循环变化, 周期约 5ms;

    // 按计数频率切换数码管;
    assign digits = 4'b0001 << i;           // 位选信号依次为: 0001, 0010, 0100, 1000;
    
    // 按计数频率切换数据;
    reg [3:0] hex = 0;
    always @ ( * )
    case ( i )
        0: hex = data[3:0];
        1: hex = data[7:4];
        2: hex = data[11:8];
        3: hex = data[15:12];
        default: hex = data[3:0];
    endcase

    // 接入数码管显示模块
    hex7seg R(hex, 0, segs);
endmodule