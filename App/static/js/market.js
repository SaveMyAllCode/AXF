//页面加载完成以后，才执行的ｊｓ
$(function () {

    $.ajax({
        url: '/market/',
        type: 'GET',
        success:function (data) {
            alert(data.foodtypes.length);
            alert(data.goodslist.length);
            for(var i = 0;i<data.foodtypes.length;i++){
                // alert(data.foodtypes[i].typeid);

                if(data.typeid==data.foodtypes[i].typeid){
                    var pat = '<li><a class="id" typeid="'+data.foodtypes[i].typeid+'">'+'<span class="yellowSlide"></span>'+data.foodtypes[i].typename+'</a>'
                }
                else{
                    pat = '<li><a class="id" typeid="'+data.foodtypes[i].typeid+'">'+data.foodtypes[i].typename+'</a>'
                }
                $('aside ul ').append(pat);
            }
            for(var j=0;j<data.goodslist.length;j++){
                alert(data.goodslist[j].productimg)

                var img = '<img src="'+ data.goodslist[j].productimg +'" alt="'+data.goodslist[j].productname+' ">';
                var h6 = '<h6>'+ data.goodslist[j].productlongname +'</h6>';
                var p1 = '<p class="detailTag"><span>精选</span><span></span></p>';
                var span = '<span class="unit">'+ data.goodslist[j].specifics +'</span>';
                var p2 = '<p class="price"><span>'+ data.goodslist[j].price +'</span><s>'+ data.goodslist[j].marketprice +'</s></p>';

                var article = '<article class="shoppingInfo">'+h6+p1+span+p2+'</article>';

                var button1 = '<button class="subShopping" goodsid="'+data.goodslist[j].id +'">-</button>';
                var span1 = '<span id="'+data.goodslist[j].id +'" style="font-size: 0.3rem;">0</span>';
                var button2 = '<button class="addShopping" goodsid="'+data.goodslist[j].id +'">+</button>';
                var section = '<section >'+button1+span1+button2+'</section>';
                var gd ='<li><a href="#">'+img+article+'</a>'+section+'</li>'
                $('menu ul').append(gd);
            }
            for(var n=0;n<data.types.length;n++){
                var a = '<a id="'+data.types[n][1]+'" childtype="'+data.types[n][1]+'">'+'<span>'+data.types[n][0]+'</span><a>';
                $('#alltypes div').append(a)
            }
        }
    });

    $('#alltypes').hide();
    $('#zhsort').hide();


    $('base ul').on('click','li .id',function () {
        var typeid = $(this).attr('typeid');
        $.ajax({
            url:'/market/',
            type: 'PUT',
            data:{
                'typeid':typeid
            },
            success:function (data) {
                if(data.code==200){
                    window.location.href='market.html';
                }
                else{
                    alert('出错')
                }

            }
        });
    });
    $('.sort').click(function () {
        var sortid = $(this).attr('sortid')
        $.ajax({
            url:'/market/',
            type:'POST',
            data:{
                'sort':sortid,
                'log':0,
            },
            success:function (data) {
                if(data.code==200){
                    window.location.href='market.html'
                }
                else{
                    alert('报错')
                }
            }
        })
    })


    //点击全部类型的展示全部类型的ｄｉｖ
    $('#alltypespan').click(function(){

        $('#alltypes').show();

        //修改一下本身的样式图表
        $(this).removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up');
    });

    //点击综合排序就展示综合排序的ｄｉｖ
    $('#zhsortspan').click(function(){
        $('#zhsort').show();
        $(this).removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up');
    });

    //点击ｄｉｖ本身就隐藏
    $('#alltypes').click(function(){
        $(this).hide();
        $('#alltypespan').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    });

    //点击ｄｉｖ本身就隐藏
    $('#zhsort').click(function(){
        $(this).hide();
        $('#zhsortspan').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    });
    //添加点击事件
    $('.addShopping').onclick(function () {
        // alert($(this).attr('goodsid'));
        goodsid = $(this).attr('goodsid')
        //获取按钮上面的标签
        objects = $(this).prev()
        $.ajax({
            url:'/addshopcar/',
            type:'post',
            data:{
                'goodsid':goodsid,
                'log': 1,
            },
            success:function (result) {
                if(result.code == '0009'){
                    window.location.href='login.html';
                }else {
                    objects.html(result.num)
                }

            }

        });
    });
    $('.subShopping').onclick(function () {
        // alert($(this).attr('goodsid'));
        goodsid = $(this).attr('goodsid')

        $.ajax({
            url:'/subshopcar/',
            type:'post',
            data:{
                'goodsid':goodsid,
                'log': -1,
            },
            success:function (result) {
                if(result.code == '0009'){
                    window.location.href='login.html';
                }else{
                    gid = '#' + goodsid
                    $(gid).html(result.num)
                }

            }

        });
    });
});