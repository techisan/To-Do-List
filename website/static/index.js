function completeItem(todoId) {
    var formData = new FormData();
    formData.append('todoId', todoId);
    formData.append('completeBtn', document.getElementById('btnCompleted_'+todoId).value);
    fetch('/complete-item', {
        method:'POST',
        body: formData,
    }).then((_res) => {
        window.location.href = "/";
    });
};

function EnableDisable(txtEdit, noteId) {

    //Reference the Button.
    var btnSubmit = document.getElementById("btnChanges_"+noteId);

    //Verify the TextBox value.
    if (txtEdit.value.trim() != "") {
        //Enable the TextBox when TextBox has value.
        btnSubmit.disabled = false;
    } else {
        //Disable the TextBox when TextBox is empty.
        btnSubmit.disabled = true;
    }
};

function editItem(noteId){
    var formData = new FormData();
    formData.append('noteId', noteId);
    formData.append('txtEdit', document.getElementById('txtEdit_'+noteId).value);

    fetch('/edit-item', {
        method:'POST',
        body: formData,
    }).then((_res) => {
        window.location.href = "/";
    });
}

function deleteItem(itemId){
    fetch('/delete-item', {
        method:'POST',
        body:JSON.stringify( { itemId: itemId } )
    }).then((_res) => {
        window.location.href = "/";
    });
}