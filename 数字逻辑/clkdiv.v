// 时钟分频器
// N 为二分次数: 输出时钟频率为输入时钟频率的1/2^N

module clkdiv #(N = 2)
(
    input  clk_in,
    output clk_out
);
    reg [N-1:0] cnt = 0;
    always @ (posedge clk_in)
        cnt <= cnt + 1;

    assign clk_out = cnt[N-1];
endmodule


// 如果输入 100MHz 的时钟信号(周期为 10ns)
// 则输出时钟频率为 100MHz / 2^N, 周期为 10ns * 2^N;

// N = 19 时, 输出时钟频率约为 190Hz, 周期约为 5ms;
// N = 20 时, 输出时钟频率约为 95Hz, 周期约为 10ms;