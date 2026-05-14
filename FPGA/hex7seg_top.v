// BCD十进制数显示器

module hex7seg_top(
    input [15:0] bcd,           // 输入数据

    input clk,                  // 时钟信号
    input rst,                  // 复位信号
    
    output reg [3:0] digits,    // 位选输出信号，1表示当前数码管被选中，0表示未被选中
    output [7:0] segs           // 段选输出信号，7位控制a-g段，1表示点亮，0表示不点亮
);

    reg [19:0] counter;             // 时钟计数器
    wire [1:0] digit;               // 位选控制信号

    // 把位选控制信号连接到计数器
    assign digit = counter[19:18];
    // 对 100MHz 的时钟进行 18 分频，得到约 381Hz 的刷新频率

    // 时钟计数器逻辑
    always @ ( posedge clk or negedge rst ) begin
        if ( rst == 1 )
            counter <= 0;                 // counter 清零；
        else  
            counter <= counter+1;          // counter + 1;
    end


    // 依次切换4个数码管
    always @ ( * ) begin
        digits = 4'b0000;   
        if(rst == 0)
            digits[digit] = 1'b1;
    end


    // 把 16 位输入分为四个BCD, 依次读取到 hex;
    reg [3:0] hex;
    always @ ( * ) case ( digit )
        '00: hex = bcd[3:0];
        '01: hex = bcd[7:4];
        '10: hex = bcd[11:8];
        '11: hex = bcd[15:12];
        default: hex = bcd[3:0];
    endcase

    // 接入数码管显示模块
    hex7seg R( 
        .hex(hex), 
        .digit(digit),
        .point(1'b0),
        .digits(digits),
        .segs(segs)
    );
endmodule