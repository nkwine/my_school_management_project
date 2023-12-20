$(".nav").click(function () {
		$("#mysidenave").css('width','10%');
		$(".main").css('margin-left','10%');
		$(".logo").css('visibility','hidden');
		$(".logo span").css('visibility','visible');
		$(".logo span").css('margin-left','-10px');
		$(".anc").css('visibility','visible');
		$(".icon").css('visibility','visible');
		$(".icon").css('margin-left','-8px');
		$(".nav").css('display','none');
		$(".nav2").css('display','block');
		// body...
	})
	$(".nav2").click(function () {
		$("#mysidenave").css('width','18%');
		$(".main").css('margin-left','18%');
		$(".logo").css('visibility','visible');
		$(".logo span").css('visibility','visible');	
		$(".anc").css('visibility','visible');
		$(".icon").css('visibility','visible');
		$(".nav").css('display','block');
		$(".nav2").css('display','none');
		// body...
	})
	var x =0;
    $('#drop').click(function () {
      if (x==0) {
        x+=1
        $('#drop1').css('display','block');
        
      }else{
        x=0
        $('#drop1').css('display','none');

      }
    })