document.addEventListener('DOMContentLoaded', function() {
  const addButton = document.querySelector('.add-button');
  const taskList = document.querySelector('.inbox');
  const task_detail = document.querySelector(".tasks")
  

  addButton.addEventListener('click', function() {
    const taskText = prompt('Enter the task:');
  
    if (taskText != null) {
      const formData = new FormData();
      formData.append('task_text', taskText);
  
      fetch('/create_task/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrfToken,
        },
        body: formData,
      })
      .then(response => response.json())
      .then(data => {
        if (data.status === 'success') {
          // const newTaskDiv = document.createElement('div');
          // newTaskDiv.className = 'msg selected-bg anim-y';
          // newTaskDiv.innerHTML = `
          //   <input type="checkbox" name="msg" class="mail-choice" checked>
          //   <label></label>
          //   <div class="msg-content">
          //     <div class="msg-title">${taskText}</div>
          //     <div class="msg-date">${getCurrentDate()}</div>
          //   </div>
          //   <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-1.2.1&auto=format&fit=crop&w=998&q=80" alt="" class="members mail-members">
          // `;
          // taskList.appendChild(newTaskDiv);

          
          location.reload()
        } else {
          alert('Error creating task');
        }
      })
      .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while creating the task');
      });
    }
  });

  function getCurrentDate() {
    const now = new Date();
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return now.toLocaleDateString('en-US', options);
  }
});