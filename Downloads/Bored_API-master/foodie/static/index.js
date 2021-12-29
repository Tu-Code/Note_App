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

const deleteNotes = id => fetch(`/delete-notes/`,{
    method: 'GET'
}).then((_res) =>{
    $(`#act-`).remove();
    console.log('work')
    window.location.href = '/saved';
})
