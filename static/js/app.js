document.addEventListener("DOMContentLoaded", () => {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));

    // Helper function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Show notifications
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

    // Handle task deletion with DELETE method
    document.querySelectorAll(".delete-task").forEach(button => {
        button.addEventListener("click", async () => {
            if (!confirm("Are you sure you want to delete this task?")) return;
            
            try {
                const response = await fetch(`/delete_task/${button.dataset.task}/`, {
                    method: "DELETE",
                    headers: { "X-CSRFToken": getCookie("csrftoken") }
                });

                if (response.ok) {
                    location.reload();
                } else {
                    showNotification("Error deleting task", "danger");
                }
            } catch (error) {
                showNotification("An error occurred while deleting the task.", "danger");
            }
        });
    });

    // Handle todo form submission
    const todoForm = document.getElementById('todoForm');
    if (todoForm) {
        todoForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            if (!todoForm.checkValidity()) {
                todoForm.classList.add("was-validated");
                return;
            }

            const formData = new FormData(this);
            try {
                const response = await fetch(this.action, {
                    method: "POST",
                    body: formData,
                    headers: { "X-CSRFToken": getCookie("csrftoken") }
                });

                if (!response.ok) throw new Error("Submission failed");

                const data = await response.json();
                showNotification("Todo added successfully!", "success");

                if (data.redirect) window.location.href = data.redirect;
            } catch (error) {
                showNotification("Error adding todo. Please try again.", "danger");
            }
        });
    }

    // Handle adding a child
    const addChildForm = document.getElementById("addChildForm");
    if (addChildForm) {
        addChildForm.addEventListener("submit", async function (e) {
            e.preventDefault();
            if (!addChildForm.checkValidity()) {
                addChildForm.classList.add("was-validated");
                return;
            }

            const formData = new FormData(this);
            try {
                const response = await fetch(this.action, {
                    method: "POST",
                    body: formData,
                    headers: { "X-CSRFToken": getCookie("csrftoken") }
                });

                if (!response.ok) throw new Error("Submission failed");

                const data = await response.json();
                showNotification("Child added successfully!", "success");

                if (data.redirect) window.location.href = data.redirect;
            } catch (error) {
                showNotification("Error adding child. Please try again.", "danger");
            }
        });
    }

    // Handle todo completion toggle
    document.querySelectorAll('.todo-complete-checkbox').forEach(checkbox => {
        checkbox.addEventListener('change', async function () {
            const todoId = this.dataset.todoId;
            try {
                const response = await fetch(`/todo/${todoId}/complete/`, {
                    method: "POST",
                    headers: { "X-CSRFToken": getCookie("csrftoken") }
                });

                if (!response.ok) throw new Error("Failed to update");

                this.closest(".list-item").classList.toggle("completed", this.checked);
                showNotification("Todo status updated!", "success");

            } catch (error) {
                showNotification("Error updating todo status.", "danger");
                this.checked = !this.checked; // Revert checkbox state
            }
        });
    });

    // Search functionality
    const searchInput = document.getElementById("searchTodo");
    if (searchInput) {
        searchInput.addEventListener("input", function () {
            const searchTerm = this.value.toLowerCase();
            document.querySelectorAll(".list-item").forEach(item => {
                const text = item.textContent.toLowerCase();
                item.style.display = text.includes(searchTerm) ? "block" : "none";
            });
        });
    }

    // Filter todos by status
    const filterSelect = document.getElementById("filterTodos");
    if (filterSelect) {
        filterSelect.addEventListener("change", function () {
            const status = this.value;
            document.querySelectorAll(".list-item").forEach(item => {
                switch (status) {
                    case "completed":
                        item.style.display = item.classList.contains("completed") ? "block" : "none";
                        break;
                    case "active":
                        item.style.display = !item.classList.contains("completed") ? "block" : "none";
                        break;
                    default:
                        item.style.display = "block";
                }
            });
        });
    }
});

/* Styles & Animations */
document.head.insertAdjacentHTML("beforeend", `
<style>
    .list-item {
        transition: all 0.3s ease;
    }
    .list-item.completed {
        opacity: 0.7;
        background: rgba(255, 255, 255, 0.1);
    }
    .list-item.completed .todo-title {
        text-decoration: line-through;
    }
    .notification {
        animation: slideIn 0.3s ease-out;
    }
    @keyframes slideIn {
        from { transform: translateY(-100%); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    .was-validated .form-control:invalid {
        border-color: #dc3545;
    }
    .was-validated .form-control:valid {
        border-color: #198754;
    }
    .btn-action {
        transition: all 0.2s ease;
    }
    .btn-action:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    #searchTodo {
        transition: all 0.3s ease;
    }
    #searchTodo:focus {
        box-shadow: 0 0 15px rgba(70, 130, 180, 0.3);
    }
</style>
`);
