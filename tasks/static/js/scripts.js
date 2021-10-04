(function (win, doc){
    'use strict';

    //Verificar se o usuário realmente quer deletar o dado...
    if(doc.querySelector('.delete-btn')){
        let btnDel = doc.querySelectorAll('.delete-btn');
        for (let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Deseja mesmo apagar este dado?')){
                    return true;

                }else{
                    event.preventDefault();
                } 
            })
        }
    }
}) (window, document)