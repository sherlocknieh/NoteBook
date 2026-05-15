module reg_N # ( parameter N = 8 ) (
	input clk,
    input rst_n,
	input load,
	input [N-1:0] in_data,
	output reg [N-1:0] out_data
	);

    always @ (posedge clk, negedge rst_n) begin
        if(!rst_n)    out_data <= 0;
        else if(load) out_data <= in_data;
    end
 endmodule