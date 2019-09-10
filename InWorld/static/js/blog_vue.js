function initBlogVM(data){
    var blogvm = new Vue({
        el:'#postlist',
        data:{
            data:data,
        },
        methods:{}
    })
};

$(function(){
    $.getJSON("/api/blog/postlist",function(data){
        console.log(data);
        initBlogVM(data);
    });
});