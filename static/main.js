
function desativaSelect() {
    var select1 = document.getElementById('select1');
    var text = select1.value;
    
   

    if (text === 'Benfica' || text == 'Santo Amaro' || text == 'Camaragibe') {
        var select2 = document.getElementById('select2');
        select2.removeAttribute("disabled");
        op1 = document.getElementById('op1')

        function load(text){
            $.ajax({
                url: "/getUnidadesByCampus",
                type: "POST",
                data: {'select1_value': text},
                dataType: "json",
                success: function(data){
                    $(select2).replaceWith(data)
                }
            })
        }
        load(text)
    }   

        
    else {
        var select2 = document.getElementById('select2');
        select2.setAttribute("disabled", "disabled");
        
    }

    
    
        }



