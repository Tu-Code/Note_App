
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
let i = 0;
let onAddNote = () =>{
    document.getElementById('onAddNote').style.display = 'block';  
    document.getElementById('notes').style.display = 'none';  
}
let arrayOfNotes = []

// 'clickedNote({{ note.title, note.data }})
// document.getElementById("app").addEventListener("click", function() {
//     document.getElementById("noteData").innerHTML = this.data;
//     // document.getElementById('notes').style.display = 'block';
//   });