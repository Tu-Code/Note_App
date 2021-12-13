// $(document).ready(function(){
//     $('#body').slideDown();
// })function end post request to del note endpoint
const deleteNote = id => fetch(`/delete-note/${id}`,{
    method: 'DELETE',
    body: JSON.stringify({ activity_id: id})
}).then((_res) =>{
    //and then reload window nd redirect to home page
    // let x = activity_id +  1;
    $(`#act-${id}`).remove();
    alert("deleted " + id)
})

// $(document).ready(function(){
//     $('.data_content').on('click', function(){
//         var data_id = $(this).data('rep');
//         $.ajax({
//             url: '/saved',
//             type: 'get'
//             data: {data_id: data_id},
//             success: function(response){
//                 var new_html = response.html
//             }
//         })
//     })
// })
