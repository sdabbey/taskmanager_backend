
  var checkboxes = document.querySelectorAll('.mail-choice');
  checkboxes.forEach(checkbox => {
    checkbox.addEventListener("click", () =>{
      checkbox.checked = true;
    }) 
   
    
  });


const delete_btns = document.querySelectorAll(".bx-trash")
delete_btns.forEach(btn => {
    btn.addEventListener("click", () => {
        
        fetch('/delete_task/'+ btn.id + '/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrfToken,
        },
        
      })
      .then(response => response.json())
      .then(data => {
        if (data.status === 'success') {
          const task_details = document.querySelectorAll('.task-detail');
          task_details.forEach(task_detail => {
            var itemId = task_detail.getAttribute('data-task-id');
            if (itemId == btn.id){
              task_detail.innerHTML = ''
            }
          })
          
          const sidetasks = document.querySelectorAll('.msg.anim-y');
          sidetasks.forEach(task => {
            var itemId = task.getAttribute('data-task-id');
            if (itemId == btn.id){
              task.remove()
            }
          })
        }
    })
})
})