

const deleteNote = id=> fetch(`/delete-note`,{
    method: 'DELETE',
    body: JSON.stringify({ noteId: id})
}).then((_res) =>{
    //and then reload window nd redirect to home page
    // let x = activity_id +  1;
    $(`.${id}`).remove();
    // document.getElementById('{{note.id}}').style.display = 'none';  
    
    $(`#app-${id}`).remove();
    alert("deleted " + id)
})

let onAddNote = () =>{
    document.getElementById('onAddNote').style.display = 'block';  
    document.getElementById('notes').style.display = 'none';  
}