// 16进制数码管显示模块
// 输入一个4位二进制数，输出对应的7段显示信号

module hex7seg(
    input [3:0] hex,            // 4位二进制输入
    input point,                // 小数点控制信号
    output reg [7:0] segs       // 段选输出信号
);
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
            default: segs = 8'b10001110; // 默认显示 F
        endcase
        // 小数点
        segs[0] = point;
    end
endmodule