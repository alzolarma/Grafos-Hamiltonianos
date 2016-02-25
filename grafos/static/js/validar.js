var letras="abcdefghyjklmnñopqrstuvwxyz";
function tiene_letras(texto){
   texto = texto.toLowerCase();
   for(i=0; i<texto.length; i++){
      if (letras.indexOf(texto.charAt(i),0)!=-1){
         return 1;
      }
   }
   return 0;
}
window.onload = (function(){
try{
    $("#input_node").on('keyup', function(){
        var value = $(this).val().length;
        var may = $(this).val().toUpperCase();
        $("#input_node").val(may);
    }).keyup();
}catch(e){}});

function validar(){
	var may = $("#input_node").val();
        mayr = may.replace(/,/g,' ');
        $("#input_edges").val(may);
        alert("hola");
}