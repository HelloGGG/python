$(function(){
    $('#submit').bind('click', function(){
        if($('input[name="project"]').val() && $('input[name="ids"]').val() && $('input[name="back_img"]').val() ){
            $('#myModal').modal('show')
            $('#mainForm').ajaxSubmit({
                type: "POST",
                url: "http://localhost:5000/get_image",
                beforeSubmit: function(){
                    $('#result').attr('src', '')
                    $('#submit').attr('disabled', 'true')
                },
                error: function(){
                    alert('生成图片失败。。。')
                },
                success: function(data){
                    console.log(data)
                    $('#myModal').modal('hide')
                    $('#submit').removeAttr('disabled')
                    $('#result').attr('src', 'static/imgs/' + data.result_src+ '?' + Math.random())
                    return data
                }
            })
        }else{
            alert('错误输入')
            return false
        }
    })
})