document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".delete-task").forEach(button => {
        button.addEventListener("click", () => {
            fetch(`/delete_task/${button.dataset.task}`, { method: "POST" })
                .then(() => location.reload());
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Todo form handling
    const todoForm = document.getElementById('todoForm');
    if (todoForm) {
        todoForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            try {
                const response = await fetch(this.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                });

                if (response.ok) {
                    const data = await response.json();
                    showNotification('Todo added successfully!', 'success');
                    if (data.redirect) {
                        window.location.href = data.redirect;
                    }
                } else {
                    showNotification('Error adding todo. Please try again.', 'danger');
                }
            } catch (error) {
                showNotification('An error occurred. Please try again.', 'danger');
            }
        });
    }

    // Child form handling
    const addChildForm = document.getElementById('addChildForm');
    if (addChildForm) {
        addChildForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            try {
                const response = await fetch(this.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                });

                if (response.ok) {
                    const data = await response.json();
                    showNotification('Child added successfully!', 'success');
                    if (data.redirect) {
                        window.location.href = data.redirect;
                    }
                } else {
                    showNotification('Error adding child. Please try again.', 'danger');
                }
            } catch (error) {
                showNotification('An error occurred. Please try again.', 'danger');
            }
        });
    }

    // Todo completion toggle
    document.querySelectorAll('.todo-complete-checkbox').forEach(checkbox => {
        checkbox.addEventListener('change', async function() {
            const todoId = this.dataset.todoId;
            try {
                const response = await fetch(`/todo/${todoId}/complete/`, {
                    method: 'POST',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                });

                if (response.ok) {
                    const parentElement = this.closest('.list-item');
                    if (this.checked) {
                        parentElement.classList.add('completed');
                    } else {
                        parentElement.classList.remove('completed');
                    }
                    showNotification('Todo status updated!', 'success');
                }
            } catch (error) {
                showNotification('Error updating todo status.', 'danger');
                this.checked = !this.checked; // Revert checkbox state
            }
        });
    });

    // Delete confirmation handling
    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });

    // Notification system
    function showNotification(message, type = 'info') {
        const notification = document.getElementById('notification');
        if (notification) {
            notification.className = `notification alert alert-${type} show`;
            notification.textContent = message;
            notification.style.display = 'block';

            setTimeout(() => {
                notification.style.display = 'none';
            }, 3000);
        }
    }

    // Helper function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Dynamic form validation
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Search functionality
    const searchInput = document.getElementById('searchTodo');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            document.querySelectorAll('.list-item').forEach(item => {
                const text = item.textContent.toLowerCase();
                item.style.display = text.includes(searchTerm) ? 'block' : 'none';
            });
        });
    }

    // Filter todos by status
    const filterSelect = document.getElementById('filterTodos');
    if (filterSelect) {
        filterSelect.addEventListener('change', function() {
            const status = this.value;
            document.querySelectorAll('.list-item').forEach(item => {
                switch(status) {
                    case 'completed':
                        item.style.display = item.classList.contains('completed') ? 'block' : 'none';
                        break;
                    case 'active':
                        item.style.display = !item.classList.contains('completed') ? 'block' : 'none';
                        break;
                    default:
                        item.style.display = 'block';
                }
            });
        });
    }
});