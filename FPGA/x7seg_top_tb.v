module x7seg_top_tb ( );
    reg CLK;
    reg RST;
    wire [7:0] SEGMENTS;
    wire [3:0] DIGITS;
    
    x7seg_top tb(
        .clk(CLK),
        .rst(RST),
        .segments(SEGMENTS),
        .digits(DIGITS)
    );

    // 生成占空比50%的时钟波形
    parameter period = 10;
    always #(period/2) CLK = ~CLK;
   
    initial begin
        CLK = 0;
        RST = 0;
        #10 RST = 1;
        #10 RST = 0;           
    end
endmodule