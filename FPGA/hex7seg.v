module hex7seg(
    input [3:0] hex,
    output reg [7:0] segments,
    output enable // 使能信号，控制数码管的显示
);
    assign enable = 1; // 始终使能数码管显示

    always @(*) begin
        case (hex)
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
    end
    
endmodule