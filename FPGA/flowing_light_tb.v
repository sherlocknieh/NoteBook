module flowing_light_tb(    );		
    reg CLK;
    reg RST;
    wire [15:0] LED;

    // 接入流水灯模块
    flowing_light F(CLK,RST,LED);

    // 定义时钟周期
    parameter PERIOD = 10;

    // 实现占空比位50%的周期时钟信号
    // 每延迟（PERIOD/2）CLK信号取反一次
    always #(PERIOD/2) CLK <= ~CLK;


    //初始化CLK，RST_N
    initial         
    begin
        CLK = 1'b0;
        RST = 1'b1;
        #10 RST = 1'b0;
        #10 RST = 1'b1;
        #10 RST = 1'b0;
    end

    //评测代码
    initial
    begin
        #0 $display("time\tRST\tLED");
    end
    
    initial
    begin
        $dumpfile("test.vcd");
        $dumpvars;
        $monitor("%g\t%b\t%b",$time,RST,LED);
        #2000 $finish;
    end
endmodule
