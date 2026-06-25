// 4位十进制数转BCD码


module bin2bcd(
    input wire [13:0] bin,  // 十进制数据范围 0-9999, 需要14个二进制位 (2^13=8192 < 9999 < 2^14=16384)
    output reg [15:0] bcd   // 0-9999的BCD码需要16位
);
    integer i;              // 循环变量
    always @(*) begin
        bcd = 0;            // 初始化为0，防止锁存器生成
        for (i = 13; i >= 0; i = i - 1) begin
            // 1. 加三 (如果BCD位大于等于5)
            if(bcd[15:12] >= 5) bcd[15:12] = bcd[15:12] + 3;
            if(bcd[11:8]  >= 5) bcd[11:8]  = bcd[11:8]  + 3;
            if(bcd[7:4]   >= 5) bcd[7:4]   = bcd[7:4]   + 3;
            if(bcd[3:0]   >= 5) bcd[3:0]   = bcd[3:0]   + 3;
            // 2. 左移 (并移入一位bin数据)
            bcd = {bcd[14:0], bin[i]};
        end
    end
endmodule
