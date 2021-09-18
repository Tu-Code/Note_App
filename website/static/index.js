
function deleteNote(noteId){
    //this will take the noteId, send post request to del note endpoint
    fetch('/delete-note',{
        method: 'POST',
        body: JSON.stringify({ noteId: noteId})
    }).then((_res) =>{
        //and then reload window nd redirect to home page
        window.location.href = '/';
    })
}