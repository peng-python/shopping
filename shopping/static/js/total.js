
$(function () {

    total1=0;//总金额
    total_count=0;//总件数
    $('.col07').each(function () {
        //获取数量
        count=$(this).prev().text();
        //获取单价
        price=$(this).prev().prev().text();
        //计算小计
        total0=parseFloat(count)*parseFloat(price);
        $(this).text(total0.toFixed(2)+'元');
        total1+=total0;
        alert('123');
        total_count++;
    });
    //显示总计
    // $('.total').text(total1.toFixed(2));
    $('#total1').text(total1.toFixed(2));//总金额
    $('#total_count').text(total_count);//总件数
    $('#total3').text((total1+10).toFixed(2));//计算运费
    $('#total4').val((total1+10).toFixed(2));//显示总金额
});