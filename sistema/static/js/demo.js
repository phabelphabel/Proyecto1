// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla = "#tabla_personal"; // id
var nombre_boton_eliminar = ".delete"; // Clase
var nombre_formulario_modal = "#frmEliminar"; //id
var nombre_ventana_modal = "#myModal"; // id
// Fin de configuraciones


    $(document).ready(function(){
        $(nombre_boton_eliminar).click(function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idPersonal').val(Pid);
            $('#modal_name').text(name);
        });
        /*var options = {
                        success:function(msn)
                        {
                            if(response.status=="True"){
                                alert("Eliminado!");
                                var idProd = response.personal_id;
                                var elementos= $(nombre_tabla+' >tbody >tr').length;
                                if(elementos==1){
                                        location.reload();
                                }else{
                                    $('#tr'+idProd).remove();
                                    $(nombre_ventana_modal).modal('hide');
                                }
                                
                            }else{
                                alert("Hubo un error al eliminar!");
                                $(nombre_ventana_modal).modal('hide');
                            };
                        }
                     };

        $(nombre_formulario_modal).ajaxForm(options);*/
    });
