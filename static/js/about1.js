document.addEventListener("DOMContentLoaded",function(){
    const imagebox=document.querySelector('.img');
    const imagepath = ["../../../static/image/pexels-craytive-1464624.jpg","../../../static/image/pexels-mnzoutfits-1639729.jpg","../../../static/image/pexels-nyaraaquino-8159427.jpg"];
    let cindex=0;
    function change() {
        cindex = (cindex + 1) % imagepath.length;
        imagebox.src=imagepath[cindex];
    }
    setInterval(change,5000);
});

