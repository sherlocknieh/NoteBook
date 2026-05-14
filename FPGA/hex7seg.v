// 4位数码管显示模块

module hex7seg(
    input [3:0] hex,        // 4位二进制输入，表示要显示的十六进制数
    input point,            // 小数点控制信号，1表示点亮小数点，0表示不点亮
    input [1:0] digit,      // 位选输入信号，表示当前要点亮的数码管（0-3）
    output [3:0] digits,    // 位选输出信号，1表示当前数码管被选中，0表示未被选中
    output reg [7:0] segs   // 段选输出信号，7位控制a-g段，1表示点亮，0表示不点亮
);
    // 位选控制
    assign digits = (1 << digit);
    // 段译码器
    always @(*) begin
        case (hex)
            4'b0000: segs = 8'b11111100; // 0
            4'b0001: segs = 8'b01100000; // 1
            4'b0010: segs = 8'b11011010; // 2
            4'b0011: segs = 8'b11110010; // 3
            4'b0100: segs = 8'b01100110; // 4
            4'b0101: segs = 8'b10110110; // 5
            4'b0110: segs = 8'b10111110; // 6
            4'b0111: segs = 8'b11100000; // 7
            4'b1000: segs = 8'b11111110; // 8
            4'b1001: segs = 8'b11110110; // 9
            4'b1010: segs = 8'b11101110; // A
            4'b1011: segs = 8'b00111110; // b
            4'b1100: segs = 8'b10011100; // C
            4'b1101: segs = 8'b01111010; // d
            4'b1110: segs = 8'b10011110; // E
            4'b1111: segs = 8'b10001110; // F
            default: segs = 8'b00000000; // 默认空白
        endcase
        segs[0] = point;        // 小数点控制
    end
endmodule