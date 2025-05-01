document.addEventListener('DOMContentLoaded', function() {
    const usernameInput = document.getElementById('id_username');  // ссылки на элементы формы
    const emailInput = document.getElementById('id_email');
    const passwordInput = document.getElementById('id_password1');

    const usernameFeedback = document.getElementById('username-feedback');
    const emailFeedback = document.getElementById('email-feedback');
    const passwordFeedback = document.getElementById('password-feedback');

    // Проверка логина на лету
    if (usernameInput) {
        usernameInput.addEventListener('keyup', function() {
            const username = usernameInput.value.trim();

            if (!usernameFeedback) return; // Если элемента нет, выходим

            if (username === "") {
                usernameFeedback.textContent = "Логин не может быть пустым.";
                return;
            }

            usernameFeedback.textContent = "Проверка логина...";

            // Отправляем AJAX-запрос на сервер для проверки уникальности логина
            fetch(`/books/ajax/check_username/?username=${encodeURIComponent(username)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.exists) {
                        usernameFeedback.textContent = "Этот логин уже занят.";
                        usernameFeedback.style.color = "red";
                    } else {
                        usernameFeedback.textContent = "Логин свободен.";
                        usernameFeedback.style.color = "green";
                    }
                })
                .catch(error => {
                    console.error('Ошибка проверки логина:', error);
                    usernameFeedback.textContent = "Ошибка при проверке.";
                });
        });
    }

    // Валидация email
    if (emailInput) {
        emailInput.addEventListener('keyup', function() {
            const email = emailInput.value.trim();
            const emailRegex = /^[a-zA-Z0-9!#$%&*+\-\/=?^_`{|}~.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;

            if (!emailRegex.test(email)) {
                emailFeedback.textContent = "Введите корректный email.";
                return;
            }

            emailFeedback.textContent = "Проверка email...";

            fetch(`/books/ajax/check_email/?email=${encodeURIComponent(email)}`)
                .then(response => response.json())
                .then(data => {
                    emailFeedback.textContent = data.exists ? "Этот email уже используется." : "Email доступен.";
                    emailFeedback.style.color = data.exists ? "red" : "green";
                })
                .catch(error => {
                    console.error('Ошибка проверки email:', error);
                    emailFeedback.textContent = "Ошибка при проверке.";
                });
        });
    }

    // Проверка пароля
if (passwordInput) {
        passwordInput.addEventListener('keyup', function() {
            const password = passwordInput.value.trim();

            if (password.length < 6) {
                passwordFeedback.textContent = "Пароль должен содержать не менее 6 символов.";
                passwordFeedback.style.color = "red";
            } else if (password.length < 8) {
                passwordFeedback.textContent = "Пароль должен содержать не менее 8 символов.";
                passwordFeedback.style.color = "orange"; // Предупреждение, но не ошибка
            } else if (/^\d+$/.test(password)) {
                passwordFeedback.textContent = "Пароль не может состоять только из цифр.";
                passwordFeedback.style.color = "red";
            } else {
                passwordFeedback.textContent = "";
            }
        });
    }
});
