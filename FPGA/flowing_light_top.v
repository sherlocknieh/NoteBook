module flowing_light_top(		
    input clk,
    input rst,
    input btn_up,
    input btn_down,
    input btn_left,
    input btn_right,
    output [15:0] led
);

    wire debounced_btn_up;
    wire debounced_btn_down;
    wire debounced_btn_left;
    wire debounced_btn_right;
    
    // 接入消抖模块
    debounce left_btn(
        .clk(clk),
        .rst(rst),
        .key_in(btn_left),
        .key_down(debounced_btn_left)
    );

    debounce right_btn(
        .clk(clk),
        .rst(rst),
        .key_in(btn_right),
        .key_down(debounced_btn_right)
    );

    debounce up_btn(
        .clk(clk),
        .rst(rst),
        .key_in(btn_up),
        .key_down(debounced_btn_up)
    );

    debounce down_btn(
        .clk(clk),
        .rst(rst),
        .key_in(btn_down),
        .key_down(debounced_btn_down)
    );

    // 接入流水灯模块
    flowing_light F(
        .clk(clk),
        .rst(rst),
        .btn_up(debounced_btn_up),
        .btn_down(debounced_btn_down),
        .btn_left(debounced_btn_left),
        .btn_right(debounced_btn_right),
        .led(led)
    );

endmodule
