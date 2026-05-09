module x7seg_top(
    input clk_top,
    input rst_top,
    output [7:0] segments_top,  
    output[3:0] digits_top
    );
    
    wire [15:0] x;
    assign x=32'h1234;
    x7seg X1(
        .x(x),
        .clk(clk_top),
        .rst(rst_top),
        .segments(segments_top),
        .digits(digits_top)
    );
endmodule